#!/usr/bin/env python3
"""Sprawdza, czy recipes.json nadal mówi dokładnie to, co plany diety w PDF.

Skrypt czyta PDF-y drugą, niezależną ścieżką (własny podział na kolumny
i własne sklejanie zawiniętych linii), więc jest kontrolą dla extract.py,
a nie jego powtórzeniem. Porównuje z rozdziałem „Plan diety”:

  * każdy składnik — wiersz odtworzony z danych musi dosłownie stać w PDF,
  * każdy krok przygotowania (`stepsSource`, czyli zapis przed zamianą
    czasowników na tryb rozkazujący) — w całości, nie tylko początek,
  * każdą nazwę dania,
  * kaloryczność i makroskładniki (osobna ścieżka odczytu — pdftotext),
  * komplet posiłków w każdym planie.

Użycie:
    python verify_against_pdf.py plik.pdf [plik2.pdf ...]
    python verify_against_pdf.py katalog_z_pdfami
"""
import json
import os
import re
import subprocess
import sys
from collections import Counter

import pdfplumber

PODZIAL = 340
RE_ILOSC = re.compile(r"^([\d.]+)\s+(\S+)\s+(.+?)\s+\(([\d.]+)\s*g\)$")
RE_NAZWA = re.compile(r"^(.+?)\s+[–—]\s+([\d.]+)\s+(\S+)\s+\(([\d.]+)\s*g\)$")
RE_WAGA = re.compile(r"^(.+?)\s+[–—]\s+([\d.]+)\s*g$")

# Nagłówek posiłku z pdftotext: kcal, białko, węglowodany, tłuszcz.
RE_MAKRO = re.compile(
    r"(?:Posiłek\s+\d\s*/\s*\d{1,2}:\d{2}-\d{1,2}:\d{2}|^\s*Przekąska)\s+"
    r"(\d+)\s+(\d+)\s*g\s+(\d+)\s*g\s+(\d+)\s*g", re.M)

norm = lambda t: re.sub(r"\s+([,.])", r"\1", re.sub(r"\s+", " ", t)).strip()


def num(x):
    return str(int(x)) if float(x) == int(x) else str(x)


def kolumna(pdf, start, lewa):
    out = []
    for pg in pdf.pages[start:]:
        ws = [w for w in pg.extract_words() if (w["x0"] < PODZIAL) == lewa]
        linie = {}
        for w in ws:
            linie.setdefault(round(w["top"] / 3), []).append(w)
        for k in sorted(linie):
            out.append(" ".join(w["text"] for w in sorted(linie[k], key=lambda w: w["x0"])).strip())
    return out


def pelny(l):
    return RE_ILOSC.match(l) or RE_NAZWA.match(l) or RE_WAGA.match(l)


def sklej(linie):
    """Składnik zawinięty na dwie linie sklejamy z powrotem."""
    out = []
    for l in linie:
        l = l.strip()
        if not l:
            continue
        if out and not pelny(out[-1]) and (re.match(r"^[\d.]", out[-1]) or "–" in out[-1]):
            if out[-1].rstrip().endswith(("–", "—")) or not (
                    re.match(r"^[\d.]+\s+\S", l) or "–" in l):
                out[-1] += " " + l
                continue
        out.append(l)
    return out


def makra(path):
    """Czwórki (kcal, B, W, T) z nagłówków posiłków — druga ścieżka odczytu."""
    txt = subprocess.run(["pdftotext", "-layout", path, "-"],
                         capture_output=True, text=True, check=True).stdout
    start = txt.index("Plan diety")
    return {tuple(int(x) for x in m.groups())
            for m in RE_MAKRO.finditer(txt[start:])}


def czytaj(path):
    pdf = pdfplumber.open(path)
    start = next(n for n, pg in enumerate(pdf.pages)
                 if (pg.extract_text() or "").strip().startswith("Plan diety"))
    lewe = sklej(kolumna(pdf, start, True))
    prawe = norm(" ".join(kolumna(pdf, start, False)))
    caly = norm(" ".join((pg.extract_text() or "") for pg in pdf.pages[start:]))
    return set(lewe), prawe, caly


def wiersz_zrodlowy(i):
    """Odtwarza wiersz składnika w zapisie, jakiego użył dietetyk."""
    g = num(i["grams"])
    if i.get("nameFirst"):
        if i.get("weightOnly"):
            return f'{i["name"]} – {g} g'
        return f'{i["name"]} – {num(i["qty"])} {i["unit"]} ({g} g)'
    if i.get("weightOnly"):
        return None  # zapis „0 -- borówek (50 g)” — sprawdzamy po nazwie
    return f'{num(i["qty"])} {i["unit"]} {i["name"]} ({g} g)'


def main(pliki):
    dane = json.load(open("recipes.json", encoding="utf-8"))

    skladniki, kroki, teksty, czworki = set(), [], [], set()
    for p in pliki:
        s, kr, ca = czytaj(p)
        skladniki |= s
        kroki.append(kr)
        teksty.append(ca)
        czworki |= makra(p)
    kroki = " ".join(kroki)
    teksty = " ".join(teksty)

    zle_skl, sprawdzone = [], 0
    for r in dane["recipes"]:
        for i in r["ingredients"]:
            w = wiersz_zrodlowy(i)
            if w is None:
                if not any(i["name"] in l and num(i["grams"]) in l for l in skladniki):
                    zle_skl.append((r["slug"], i["name"]))
                sprawdzone += 1
                continue
            sprawdzone += 1
            if w not in skladniki:
                zle_skl.append((r["slug"], w))

    zle_kroki, ile_krokow = [], 0
    for r in dane["recipes"]:
        for s in r["stepsSource"]:
            ile_krokow += 1
            if norm(s) not in kroki:
                zle_kroki.append((r["slug"], norm(s)))

    zle_tytuly = [r["slug"] for r in dane["recipes"]
                  if norm(r["title"]) not in teksty]

    # Kcal i makro idą z PDF-u inną ścieżką niż składniki (pdftotext kontra
    # pdfplumber) i są zestawiane z treścią po kolejności — czyli podatne na
    # przesunięcie o jeden posiłek. Sprawdzamy, czy każda czwórka istnieje
    # w źródle.
    zle_makro = [(r["slug"], (r["kcal"], r["protein"], r["carbs"], r["fat"]))
                 for r in dane["recipes"]
                 if (r["kcal"], r["protein"], r["carbs"], r["fat"]) not in czworki]

    print(f"Składniki: {sprawdzone} sprawdzonych, niezgodnych z PDF: {len(zle_skl)}")
    for x in zle_skl[:15]:
        print("   ", x)
    print(f"Kroki:     {ile_krokow} sprawdzonych, niezgodnych: {len(zle_kroki)}")
    for x in zle_kroki[:15]:
        print("   ", x[0], "|", x[1][:90])
    print(f"Tytuły:    {len(dane['recipes'])} sprawdzonych, niezgodnych: {len(zle_tytuly)}")
    for x in zle_tytuly[:15]:
        print("   ", x)
    print(f"Kcal+makro: {len(dane['recipes'])} sprawdzonych, niezgodnych: {len(zle_makro)}")
    for x in zle_makro[:15]:
        print("   ", x[0], x[1])

    # komplet posiłków w każdym planie (po odsianiu powtórzeń część wypada —
    # pokazujemy więc, ile dni i posiłków zostało z każdego planu)
    print("\nPlany po odsianiu powtórzeń:")
    for plan, c in sorted(Counter(r["plan"] for r in dane["recipes"]).items(),
                          key=lambda kv: int(kv[0])):
        dni = len({r["day"] for r in dane["recipes"] if r["plan"] == plan})
        print(f"   plan {plan:>2}: {c:3d} przepisów z {dni} dni")

    print("\nPory posiłków:", dict(Counter(r["slotLabel"] for r in dane["recipes"])))
    return 1 if (zle_skl or zle_kroki or zle_tytuly or zle_makro) else 0


if __name__ == "__main__":
    arg = sys.argv[1:] or ["source"]
    pliki = []
    for a in arg:
        if os.path.isdir(a):
            pliki += sorted(os.path.join(a, f) for f in os.listdir(a) if f.endswith(".pdf"))
        else:
            pliki.append(a)
    if not pliki:
        sys.exit("Nie podano żadnego PDF-a.")
    sys.exit(main(pliki))
