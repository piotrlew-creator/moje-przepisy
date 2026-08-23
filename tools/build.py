# -*- coding: utf-8 -*-
"""Buduje recipes.json ze wszystkich planów diety.

Kolejność działań:
  1. wyciągnięcie przepisów z każdego PDF-u (extract.py),
  2. odsianie powtórzeń — najpierw względem planu pierwszego, potem
     wewnątrz nowych planów,
  3. przypisanie pory posiłku po godzinie z PDF-u,
  4. tagi składników i flagi spiżarniane (tagi.py),
  5. przepisanie kroków na tryb rozkazujący (imperative2.py),
  6. znaczniki zamienników w krokach (migrate2 uruchamiany osobno).

Slugi przepisów, które już były na stronie, zostają nietknięte — inaczej
posypałyby się zapisane w przeglądarce listy zakupów i adresy stron.
"""
import json
import os
import re
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import extract
import tagi
from imperative2 import VERBS, NIEDOKONANE, TRWANIE, ZAIMKI

# PDF-y z planami leżą w source/. Pierwszy plan (ten, z którego powstała
# strona) musi iść na początku, bo to on ustala slugi zachowywane potem
# przy każdej przebudowie.
KATALOG = os.environ.get("PLANY", "source")
PIERWSZY_WZORZEC = "dieta.pdf"
WYNIK = os.environ.get("WYNIK", "recipes.json")

SLOTS = [
    {"id": "sniadanie", "label": "Śniadanie", "time": "7:00-10:00", "slot": 1},
    {"id": "obiad", "label": "Obiad", "time": "13:00-16:00", "slot": 2},
    {"id": "kolacja", "label": "Kolacja", "time": "18:00-20:00", "slot": 3},
]

# Odmiana jednostek miary: mianownik, forma po 2–4, forma po 5+, dopełniacz.
# Potrzebna przy przeliczaniu porcji („6 łyżek”, nie „6 łyżki”).
JEDNOSTKI = {
    "łyżka": ["łyżka", "łyżki", "łyżek", "łyżki"],
    "łyżeczka": ["łyżeczka", "łyżeczki", "łyżeczek", "łyżeczki"],
    "sztuka": ["sztuka", "sztuki", "sztuk", "sztuki"],
    "garść": ["garść", "garście", "garści", "garści"],
    "kromka": ["kromka", "kromki", "kromek", "kromki"],
    "plaster": ["plaster", "plastry", "plastrów", "plastra"],
    "szklanka": ["szklanka", "szklanki", "szklanek", "szklanki"],
    "opakowanie": ["opakowanie", "opakowania", "opakowań", "opakowania"],
    "ząbek": ["ząbek", "ząbki", "ząbków", "ząbka"],
    "szczypta": ["szczypta", "szczypty", "szczypt", "szczypty"],
    "porcja": ["porcja", "porcje", "porcji", "porcji"],
    "puszka": ["puszka", "puszki", "puszek", "puszki"],
    "kostka": ["kostka", "kostki", "kostek", "kostki"],
    "listek": ["listek", "listki", "listków", "listka"],
    "łodyga": ["łodyga", "łodygi", "łodyg", "łodygi"],
}
LEMAT = {f: lem for lem, formy in JEDNOSTKI.items() for f in formy}
LEMAT.update({"ząbku": "ząbek", "kromek": "kromka"})

_PAT = re.compile(r"\b(" + "|".join(sorted(VERBS, key=len, reverse=True)) + r")\b", re.I)
_TRWA = re.compile(TRWANIE, re.I)


def rozkaz(zdanie):
    """1. os. l.mn. → 2. os. l.poj. trybu rozkazującego."""
    def rep(m):
        w = m.group(0)
        nowy = VERBS[w.lower()]
        return nowy[0].upper() + nowy[1:] if w[0].isupper() else nowy
    out = _PAT.sub(rep, zdanie)

    # czynność, która trwa, zostaje niedokonana
    for dok, niedok in NIEDOKONANE.items():
        for m in reversed(list(re.finditer(r"\b" + dok + r"\b", out, re.I))):
            if _TRWA.search(out[m.end():m.end() + 60]):
                slowo = niedok[0].upper() + niedok[1:] if out[m.start()].isupper() else niedok
                out = out[:m.start()] + slowo + out[m.end():]

    for a, b in ZAIMKI:
        out = out.replace(a, b)
    return out


def slug(tytul, zajete):
    s = tytul.lower()
    s = re.sub(r"\(.*?\)", "", s)
    s = "".join(c for c in unicodedata.normalize("NFD", s)
                if unicodedata.category(c) != "Mn")
    s = s.replace("ł", "l")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    s = "-".join(s.split("-")[:6])[:60].strip("-")
    baza, n = s, 2
    while s in zajete:
        s = f"{baza}-{n}"
        n += 1
    zajete.add(s)
    return s


def slot_po_godzinie(czas):
    """Pora posiłku wg godziny rozpoczęcia z PDF-u.

    Przekąska nie ma w PDF-ie godzin — w planach, w których występuje, jest
    ostatnim posiłkiem dnia (te plany nie mają osobnej kolacji), więc trafia
    do kolacji.
    """
    if not czas:
        return SLOTS[2]
    godz = int(czas.split(":")[0])
    if godz <= 10:
        return SLOTS[0]
    if godz <= 16:
        return SLOTS[1]
    return SLOTS[2]


def klucz_tytulu(t):
    t = t.lower().strip()
    t = re.sub(r"\s*\(liczba porcji:\s*\d+\)", "", t)
    t = re.sub(r"\s*-\s*przepis na \d+ porcje", "", t)
    return re.sub(r"\s+", " ", t)


def main():
    stara = json.load(open(WYNIK, encoding="utf-8"))
    slug_po_tytule = {klucz_tytulu(r["title"]): r["slug"] for r in stara["recipes"]}
    baza_porcji = {klucz_tytulu(r["title"]): r["baseServings"] for r in stara["recipes"]}

    wszystkie_pdf = sorted(os.path.join(KATALOG, f) for f in os.listdir(KATALOG)
                           if f.lower().endswith(".pdf"))
    pierwszy = [p for p in wszystkie_pdf if p.endswith(PIERWSZY_WZORZEC)]
    pliki = pierwszy + [p for p in wszystkie_pdf if p not in pierwszy]

    wszystkie, widziane = [], set()
    for path in pliki:
        plan = "1" if path in pierwszy else re.sub(r"\D", "", os.path.basename(path)) or "?"
        for r in extract.przepisy(path):
            k = klucz_tytulu(r["title"])
            if k in widziane:
                continue
            widziane.add(k)
            r["plan"] = plan
            wszystkie.append(r)
        print(f"  plan {plan}: łącznie unikalnych {len(wszystkie)}", flush=True)

    zajete = set()
    przepisy = []
    for r in wszystkie:
        k = klucz_tytulu(r["title"])
        s = slug_po_tytule.get(k)
        if s:
            zajete.add(s)
        else:
            s = slug(r["title"], zajete)

        skl = []
        for i in r["ingredients"]:
            pantry = tagi.spizarnia(i["name"])
            t = None if pantry else tagi.tag(i["name"])
            wpis = {
                "qty": i["qty"], "unit": i["unit"],
                "unitLemma": LEMAT.get(i["unit"]),
                "name": i["name"], "grams": i["grams"],
                "pantry": pantry, "tag": t[0] if t else None,
            }
            if i.get("nameFirst"):
                wpis["nameFirst"] = True
            if i.get("weightOnly"):
                wpis["weightOnly"] = True
            if i.get("section"):
                wpis["section"] = i["section"]
            skl.append(wpis)

        sl = slot_po_godzinie(r["time"])
        przepisy.append({
            "slug": s,
            "title": r["title"],
            "plan": r["plan"],
            "day": r["day"],
            "mealNo": r["mealNo"],
            "sourceTime": r["time"],
            "slot": sl["slot"], "slotId": sl["id"], "slotLabel": sl["label"],
            "time": sl["time"],
            "kcal": r["kcal"], "protein": r["protein"],
            "carbs": r["carbs"], "fat": r["fat"],
            "baseServings": baza_porcji.get(k, r.get("baseServings", 1)),
            "tags": sorted({i["tag"] for i in skl if i["tag"]}),
            "ingredients": skl,
            "stepsSource": list(r["steps"]),
            "steps": [rozkaz(s) for s in r["steps"]],
        })

    # jednostki miary — odmiana przy przeliczaniu porcji
    dane = dict(stara)
    dane["slots"] = SLOTS
    dane["units"] = JEDNOSTKI
    dane["recipes"] = przepisy

    etykiety = {}
    for _, i, l in tagi.REGULY:
        etykiety.setdefault(i, l)
    from collections import Counter
    licz = Counter(t for r in przepisy for t in r["tags"])
    dane["ingredientIndex"] = [
        {"id": t, "label": etykiety.get(t, t), "count": c}
        for t, c in sorted(licz.items(), key=lambda kv: (-kv[1], etykiety.get(kv[0], kv[0])))
    ]

    json.dump(dane, open(WYNIK, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"\nprzepisów: {len(przepisy)}")
    print(f"składników (wierszy): {sum(len(r['ingredients']) for r in przepisy)}")
    print(f"kategorii składników: {len(dane['ingredientIndex'])}")
    from collections import Counter as C
    print("pory posiłków:", dict(C(r["slotLabel"] for r in przepisy)))


if __name__ == "__main__":
    main()
