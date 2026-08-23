# -*- coding: utf-8 -*-
"""Wyciąga przepisy z sekcji „Plan diety” planów żywieniowych.

Wszystkie plany mają ten sam układ dwukolumnowy: po lewej nazwa dania
i składniki, po prawej ponumerowane kroki. Różnią się zapisem składnika:

  starszy:  „2 łyżki ryżu basmati (30 g)”          — ilość, potem nazwa
  nowszy:   „Papryka czerwona – 0.5 sztuki (85 g)” — nazwa, potem ilość
            „Kasza kuskus – 50 g”                  — sama gramatura

Nowsze plany dzielą też składniki na sekcje („sos:”, „Przekąska”,
„Panierka:”), co zachowujemy.

Liczby w nagłówku posiłku są w PDF-ie rysowane dwukrotnie (imitacja
pogrubienia), więc pdfplumber czyta je jako „446644”. Dlatego metadane
bierzemy z pdftotext, a treść z pdfplumber, który jako jedyny wie,
w której kolumnie stoi dany wyraz.
"""
import re
import subprocess

import pdfplumber

PODZIAL_KOLUMN = 340

RE_POSILEK_META = re.compile(
    r"Posiłek\s+(\d)\s*/\s*(\d{1,2}:\d{2})-(\d{1,2}:\d{2})\s+"
    r"(\d+)\s+(\d+)\s*g\s+(\d+)\s*g\s+(\d+)\s*g")
RE_PRZEKASKA_META = re.compile(
    r"^\s*Przekąska\s+(\d+)\s+(\d+)\s*g\s+(\d+)\s*g\s+(\d+)\s*g\s*$")
RE_DZIEN_META = re.compile(r"^\s*Dzień\s+(\d+)\b")
# Przekąska to osobny posiłek dnia (własne kcal, własny przepis), tyle że
# bez godzin — dlatego jest własną granicą bloku, a nie sekcją składników.
RE_POSILEK_NAGLOWEK = re.compile(r"^Posiłek\s+\d\s*/|^Przekąska$")
RE_KROK = re.compile(r"(?<!\d)(\d{1,2})\.\s")

RE_ILOSC_PIERWSZA = re.compile(r"^([\d.]+)\s+(\S+)\s+(.+?)\s+\(([\d.]+)\s*g\)$")
RE_NAZWA_PIERWSZA = re.compile(r"^(.+?)\s+[–—]\s+([\d.]+)\s+(\S+)\s+\(([\d.]+)\s*g\)$")
RE_NAZWA_WAGA = re.compile(r"^(.+?)\s+[–—]\s+([\d.]+)\s*g$")

RE_SEKCJA = re.compile(r"^([^–—]{1,40}):$")
RE_SMIECI = re.compile(
    r"^\(\d+\s*g błonnika"
    r"|^\(\d+$"
    r"|^\d+\s*g błonnika"
    r"|^Plan diety$"
    r"|^Lista wymienników$"
    r"|^Kcal(\s+[BWT])*$"
    r"|^(?=.*gg)[\dg\s]+$"
    r"|^Dzień\s+\d+\s*\(?\d*$")

RE_PORCJE = re.compile(r"\(liczba porcji:\s*(\d+)\)|przepis na (\d+) porcje")


def _pelny_skladnik(l):
    return (RE_ILOSC_PIERWSZA.match(l) or RE_NAZWA_PIERWSZA.match(l)
            or RE_NAZWA_WAGA.match(l))


def metadane(path):
    """Dzień, numer posiłku, godziny, kcal i makro — w kolejności występowania."""
    txt = subprocess.run(["pdftotext", "-layout", path, "-"],
                         capture_output=True, text=True, check=True).stdout
    lines = txt.split("\n")
    start = next(i for i, l in enumerate(lines) if l.strip() == "Plan diety")
    out, dzien = [], None
    for l in lines[start:]:
        d = RE_DZIEN_META.match(l)
        if d and "kcal" not in l:
            dzien = int(d.group(1))
        m = RE_POSILEK_META.search(l)
        if m:
            slot, t1, t2, kcal, b, w, t = m.groups()
            out.append({"day": dzien, "mealNo": int(slot), "time": f"{t1}-{t2}",
                        "kcal": int(kcal), "protein": int(b),
                        "carbs": int(w), "fat": int(t)})
            continue
        m = RE_PRZEKASKA_META.match(l)
        if m:
            kcal, b, w, t = m.groups()
            # przekąska zamyka dzień w planach trzyposiłkowych i nie ma godzin
            out.append({"day": dzien, "mealNo": 4, "time": None,
                        "kcal": int(kcal), "protein": int(b),
                        "carbs": int(w), "fat": int(t)})
    return out


def _linie(page, lewa):
    """Linie tekstu jednej kolumny: [(y, tekst)] posortowane od góry."""
    words = [x for x in page.extract_words()
             if (x["x0"] < PODZIAL_KOLUMN) == lewa]
    grupy = {}
    for x in words:
        grupy.setdefault(round(x["top"] / 3), []).append(x)
    return [(k, " ".join(w["text"] for w in sorted(g, key=lambda w: w["x0"])).strip())
            for k, g in sorted(grupy.items())]


def _scal_zawiniete(linie):
    """Skleja składnik zawinięty na dwie linie.

    Doklejamy kolejną linię, gdy poprzednia wygląda na urwany składnik:
    zaczyna się od liczby (starszy układ) albo zawiera myślnik (nowszy),
    a mimo to nie pasuje do żadnego pełnego wzorca.
    """
    out = []
    for l in linie:
        l = l.strip()
        if not l:
            continue
        if out:
            poprz = out[-1]
            urwany = (not _pelny_skladnik(poprz)
                      and (re.match(r"^[\d.]", poprz) or "–" in poprz or "—" in poprz)
                      and not RE_SEKCJA.match(poprz))
            nowy_start = bool(re.match(r"^[\d.]+\s+\S", l)) or "–" in l
            # linia urwana na samym myślniku zawsze bierze następną
            if poprz.rstrip().endswith(("–", "—")):
                nowy_start = False
            if urwany and not nowy_start:
                out[-1] = poprz + " " + l
                continue
        out.append(l)
    return out


def _parsuj_skladniki(linie):
    """Zwraca (nazwa dania, składniki, linie nierozpoznane)."""
    nazwa, skladniki, reszta = [], [], []
    sekcja = None
    widziane = set()
    zaczely_sie = False

    for l in _scal_zawiniete(linie):
        if RE_SMIECI.match(l):
            continue

        wpis = None
        m = RE_ILOSC_PIERWSZA.match(l)
        if m:
            q, u, n, g = m.groups()
            if float(q) == 0 or set(u) <= set("-–—"):
                # zapis „0 -- borówek (50 g)” znaczy: bez miary domowej
                wpis = {"qty": float(g), "unit": "g", "name": n.strip(),
                        "grams": float(g), "nameFirst": False, "weightOnly": True}
            else:
                wpis = {"qty": float(q), "unit": u, "name": n.strip(),
                        "grams": float(g), "nameFirst": False, "weightOnly": False}
        else:
            m = RE_NAZWA_PIERWSZA.match(l)
            if m:
                n, q, u, g = m.groups()
                wpis = {"qty": float(q), "unit": u, "name": n.strip(),
                        "grams": float(g), "nameFirst": True, "weightOnly": False}
            else:
                m = RE_NAZWA_WAGA.match(l)
                if m:
                    n, g = m.groups()
                    wpis = {"qty": float(g), "unit": "g", "name": n.strip(),
                            "grams": float(g), "nameFirst": True, "weightOnly": True}

        if wpis is None:
            s = RE_SEKCJA.match(l)
            if s:
                # nagłówek sekcji („łosoś:”, „sos:”) kończy nazwę dania —
                # bez tego tytuł brzmiałby „Bowl z łososiem teriyaki łosoś:”
                sekcja = s.group(1).strip()
                zaczely_sie = True
            elif not zaczely_sie:
                nazwa.append(l)
            else:
                reszta.append(l)
            continue

        zaczely_sie = True
        if sekcja:
            wpis["section"] = sekcja
        klucz = (wpis["qty"], wpis["unit"], wpis["name"], wpis["grams"],
                 wpis.get("section"))
        if klucz in widziane:
            continue  # w źródle zdarza się ta sama pozycja dwa razy
        widziane.add(klucz)
        skladniki.append(wpis)

    return " ".join(nazwa).strip(), skladniki, reszta


def surowe_posilki(path):
    """Nazwa, składniki i kroki każdego posiłku — w kolejności występowania."""
    pdf = pdfplumber.open(path)
    start = next(n for n, pg in enumerate(pdf.pages)
                 if (pg.extract_text() or "").strip().startswith("Plan diety"))

    lewe, prawe = [], []
    for nr, pg in enumerate(pdf.pages[start:]):
        for y, txt in _linie(pg, True):
            lewe.append((nr, y, txt))
        for y, txt in _linie(pg, False):
            if RE_SMIECI.match(txt):
                continue
            prawe.append((nr, y, txt))

    granice = [i for i, (_, _, t) in enumerate(lewe)
               if RE_POSILEK_NAGLOWEK.match(t)]

    posilki = []
    for n, i in enumerate(granice):
        koniec = granice[n + 1] if n + 1 < len(granice) else len(lewe)
        blok = lewe[i:koniec]
        poz_od = (blok[0][0], blok[0][1])
        poz_do = (lewe[koniec][0], lewe[koniec][1]) if koniec < len(lewe) else (10 ** 6, 0)

        teksty = [t for _, _, t in blok]
        try:
            po_kcal = next(j for j, t in enumerate(teksty) if t.startswith("Kcal")) + 1
        except StopIteration:
            po_kcal = 1

        tytul, skladniki, reszta = _parsuj_skladniki(teksty[po_kcal:])

        prawy = " ".join(t for p, y, t in prawe if poz_od <= (p, y) < poz_do)
        prawy = re.sub(r"\s+", " ", prawy).strip()
        czesci = RE_KROK.split(prawy)
        kroki = [re.sub(r"\s+([,.])", r"\1", czesci[j + 1]).strip()
                 for j in range(1, len(czesci), 2)]

        porcje = RE_PORCJE.search(tytul)
        posilki.append({
            "title": tytul,
            "baseServings": int(porcje.group(1) or porcje.group(2)) if porcje else 1,
            "ingredients": skladniki,
            "steps": kroki,
            "unparsed": reszta,
        })
    return posilki


def przepisy(path):
    """Metadane sklejone z treścią. Zwraca listę pełnych przepisów."""
    meta = metadane(path)
    tresc = surowe_posilki(path)
    if len(meta) != len(tresc):
        raise SystemExit(f"{path}: {len(meta)} nagłówków, {len(tresc)} bloków treści")
    return [dict(m, **t) for m, t in zip(meta, tresc)]
