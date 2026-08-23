# -*- coding: utf-8 -*-
"""Etap 2: zamienniki składników.

W krokach przygotowania nazwy zamienianych składników są podmieniane na
znaczniki «indeks|PRZYPADEK|przymiotnik|wtrącenie|U». Strona wstawia w nie
formę wybranego wariantu, dzięki czemu „Jabłko pokrój w kostkę” po zamianie
czyta się „Gruszkę pokrój w kostkę”, a nie „Gruszka pokrój w kostkę”.

Znacznik wskazuje konkretny SKŁADNIK, nie grupę — inaczej w sałatce greckiej
„paprykę, pomidor, ogórek” zamieniłyby się wszystkie na to samo warzywo.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import swaps

# Biernik rodzaju męskiego dla rzeczowników odmienianych jak żywotne.
_MZ = {"umyty": "umytego", "świeży": "świeżego", "odsączony": "odsączonego",
       "pokrojony": "pokrojonego", "ugotowany": "ugotowanego",
       "podsmażony": "podsmażonego", "przyprawiony": "przyprawionego",
       "starty": "startego", "przygotowany": "przygotowanego"}
for _k, _v in swaps.PRZYMIOTNIKI.items():
    _v["mz"] = _MZ.get(_v["m"], _v["m"]) if _k.endswith("_B") else _v["m"]

RODZAJ_B = {"banan": "mz", "pomidor": "mz", "ogorek": "mz",
            "brokul": "mz", "kalafior": "mz", "baklazan": "mz"}

# Biernik przed mianownikiem: w przepisach składnik jest prawie zawsze
# dopełnieniem („Jabłko pokrój”), a dla rodzaju nijakiego obie formy brzmią
# tak samo, więc bez tej kolejności wychodziłoby „Gruszka pokrój”.
PRIORYTET = ["B", "Bpl", "Bpot", "D", "Dpl", "N", "Npl", "Ms", "Mspl", "M", "Mpl"]

# Słowa, po których następny rzeczownik stoi w dopełniaczu („plastry ogórka”,
# „wstążki z marchewki”). Bez tego biernik wygrywałby z dopełniaczem i po
# zamianie wychodziłoby „plastry paprykę”.
DOPELNIACZ_PO = re.compile(
    r"(plastry|plasterki|wstążki|różyczki|masy|resztę|reszta|trochę|linii|"
    r"kilka|garść|garści|kawałki|kawałek|szklanka|szklanki|łyżka|łyżki|porcja|porcje)"
    r"\s+(?:(?:z|ze|do|od)\s+)?$", re.I)
def do_dopelniacza(forms, dopasowanie):
    """Wybiera tę formę dopełniacza, która brzmi tak jak dopasowany tekst.
    „z marchewki” to dopełniacz liczby pojedynczej, choć wygląda jak mnoga."""
    for case in ("D", "Dpl"):
        if forms.get(case, "").lower() == dopasowanie.lower():
            return case
    return "D"

# Przymiotnik stojący PO rzeczowniku („ogórek zielony”) — wtedy nie
# podmieniamy, bo zamiennik zostałby z cudzym określeniem.
PO_RZECZOWNIKU = r"\s+(zielony|zielona|czerwony|czerwona|żółty|żółta|biały|biała|" \
                 r"wędzony|wędzona|słodki|słodka|naturalny|naturalna|konserwowy|konserwowa)\b"

import unicodedata


def _n(t):
    t = t.lower()
    t = "".join(c for c in unicodedata.normalize("NFD", t)
                if unicodedata.category(c) != "Mn")
    return t.replace("ł", "l").strip()


def dopasuj_po_nazwie(nazwa, grupy):
    """Nowsze plany zapisują składnik w mianowniku („Chleb żytni razowy”),
    więc poza słownikiem ręcznym próbujemy trafić wprost w formę wariantu."""
    n = _n(nazwa)
    for gid, g in grupy.items():
        for o in g["opcje"]:
            for forma in o["formy"].values():
                if n == _n(forma):
                    return gid, o["id"], "M"
    return None


PATH = os.environ.get("WYNIK", "recipes.json")
data = json.load(open(PATH, encoding="utf-8"))

opt_by_id = {}
for gid, g in swaps.GRUPY.items():
    for o in g["opcje"]:
        o["rodzajB"] = RODZAJ_B.get(o["id"], o["rodzaj"])
        opt_by_id[(gid, o["id"])] = o


def wzorce(self_opt):
    """Lista (regex, przypadek, przymiotnik) — od najdłuższego dopasowania."""
    forms = self_opt["formy"]
    kolejnosc = [c for c in PRIORYTET if c in forms] + \
                [c for c in forms if c not in PRIORYTET]
    out = []
    for adj_key, adj_forms in swaps.PRZYMIOTNIKI.items():
        for case in kolejnosc:
            # „pokrojony pomidor” (biernik poprawny) vs „pokrojonego pomidora”
            # (biernik potoczny) — przymiotnik idzie za formą rzeczownika.
            rodz = self_opt["rodzajB"] if (adj_key.endswith("_B") and case == "Bpot") \
                else self_opt["rodzaj"]
            adj = adj_forms[rodz]
            # przymiotnik może być oddzielony od rzeczownika krótkim wtrąceniem
            # („startą NA DROBNYCH OCZKACH marchewkę”)
            rx = (r"(?<![\w])(" + re.escape(adj) + r")\s+"
                  r"((?:[a-ząćęłńóśźżA-ZĄĆĘŁŃÓŚŹŻ]+\s+){0,3})"
                  + re.escape(forms[case]) + r"(?![\w])")
            out.append((rx, case, adj_key, 100 + len(adj) + len(forms[case])))
    for case in kolejnosc:
        out.append((r"(?<![\w])" + re.escape(forms[case]) + r"(?![\w])",
                    case, None, len(forms[case])))
    # dłuższe dopasowania najpierw, przy równej długości — priorytet przypadka
    out.sort(key=lambda p: (-p[3], PRIORYTET.index(p[1]) if p[1] in PRIORYTET else 99))
    return [(a, b, c) for a, b, c, _ in out]


def tokenize(step, idx, self_opt):
    hits = 0
    out = step
    for rx, case, adj_key in wzorce(self_opt):
        pat = re.compile(rx, re.I)

        def rep(m):
            nonlocal hits
            if re.match(PO_RZECZOWNIKU, out[m.end():m.end() + 24]):
                return m.group(0)
            for weto in swaps.WETO.get(self_opt["id"], []):
                if re.search(weto, out[m.end():m.end() + 24]) or \
                   re.search(weto, out[max(0, m.start() - 24):m.start()]):
                    return m.group(0)
            wybrany = case
            if not adj_key and case not in ("D", "Dpl") and \
                    DOPELNIACZ_PO.search(out[max(0, m.start() - 30):m.start()]):
                wybrany = do_dopelniacza(self_opt["formy"], m.group(0))
            infix = (m.group(2).strip() if adj_key else "")
            up = "U" if m.group(0)[0].isupper() else ""
            hits += 1
            return f"«{idx}|{wybrany}|{adj_key or ''}|{infix}|{up}»"

        out = pat.sub(rep, out)
    return out, hits


total = 0
with_swap = 0
for r in data["recipes"]:
    steps = list(r["steps"])
    for idx, ing in enumerate(r["ingredients"]):
        entry = swaps.SKLADNIK_DO_WARIANTU.get(ing["name"])
        if not entry:
            entry = dopasuj_po_nazwie(ing["name"], swaps.GRUPY)
        if not entry:
            ing.pop("swap", None)
            continue
        gid, self_id, name_case = entry
        self_opt = opt_by_id[(gid, self_id)]
        ing["swap"] = {"group": gid, "self": self_id, "nameCase": name_case}
        with_swap += 1
        for i, s in enumerate(steps):
            steps[i], n = tokenize(s, idx, self_opt)
            total += n
    r["steps"] = steps

used = {i["swap"]["group"] for r in data["recipes"] for i in r["ingredients"] if "swap" in i}
data["swapAdjectives"] = swaps.PRZYMIOTNIKI
data["swapGroups"] = {gid: {"label": g["label"], "options": g["opcje"]}
                      for gid, g in swaps.GRUPY.items() if gid in used}

json.dump(data, open(PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"składników z zamiennikami: {with_swap}")
print(f"znaczników w krokach: {total}")
print(f"grup: {len(data['swapGroups'])}")
