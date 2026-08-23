#!/usr/bin/env python3
"""Generuje całą zawartość docs/ z jednego pliku recipes.json.

Powstają:
  docs/index.md           — wyszukiwarka + lista wszystkich przepisów
  docs/przepisy/<slug>.md — pojedynczy przepis
  docs/zamienniki.md      — lista wymienników z PDF-u

Nic w docs/ nie jest pisane ręcznie, więc lista przepisów i lista składników
nie mogą się rozjechać z przepisami. Skrypt jest też uruchamiany w GitHub
Actions przed `mkdocs build`.

Użycie:  python generate_site.py
"""
import html
import json
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, "recipes.json")
DOCS = os.path.join(ROOT, "docs")
RECIPE_DIR = os.path.join(DOCS, "przepisy")

# Pliki po usuniętej funkcji „Plan 10 dni” — kasowane, gdyby zostały po
# wcześniejszej wersji.
PRZESTARZALE = ["plan.md"]

SEARCH_ICON = (
    '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" '
    'stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true">'
    '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>'
)

TOKEN = re.compile(r"«(\d+)\|([A-Za-z]+)\|([A-Za-z_]*)\|([^|]*)\|(U?)»")


def e(s):
    return html.escape(str(s), quote=True)


def plural(n, one, few, many):
    if n == 1:
        return one
    if 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14:
        return few
    return many


# Skróty jednostek — tylko przy wyświetlaniu. W recipes.json zostaje pełny
# zapis z PDF-u, żeby verify_against_pdf.py dalej porównywał dane ze źródłem
# znak w znak. Ta sama tabela jest w docs/javascripts/app.js (SKROTY), bo
# tam ilości są przeliczane na żywo — zmieniasz jedno, zmień drugie.
SKROTY = {
    "sztuka": "szt.", "sztuki": "szt.", "sztuk": "szt.",
    "opakowanie": "op.", "opakowania": "op.", "opakowań": "op.",
    "szczypta": "szcz.", "szczypty": "szcz.", "szczypt": "szcz.",
}


def skrot(u):
    return SKROTY.get(u, u)


def num(x):
    return str(int(x)) if float(x).is_integer() else str(x)


def render_step(step, ingredients, groups, adjectives):
    """Podstawia znaczniki formami składników z przepisu (wersja bez zamian).

    Ta sama logika działa w przeglądarce; tutaj potrzebna jest po to, żeby
    kroki były czytelne także bez JavaScriptu i dla wyszukiwarki.
    """
    def rep(m):
        idx, case, adj, infix, up = m.groups()
        ing = ingredients[int(idx)]
        opt = next(o for o in groups[ing["swap"]["group"]]["options"]
                   if o["id"] == ing["swap"]["self"])
        word = opt["formy"].get(case) or opt["formy"]["M"]
        if adj:
            rodz = opt.get("rodzajB", opt["rodzaj"]) \
                if (adj.endswith("_B") and case == "Bpot") else opt["rodzaj"]
            word = adjectives[adj][rodz] + " " + (infix + " " if infix else "") + word
        return word[0].upper() + word[1:] if up else word

    return TOKEN.sub(rep, step)


# --------------------------------------------------------------- index.md ---

def render_index(data):
    slots = data["slots"]
    idx = data["ingredientIndex"]
    featured = data["featuredIngredients"]
    recipes = data["recipes"]
    by_id = {i["id"]: i for i in idx}

    out = ["---", "hide:", "  - toc", "---", "", "# Co dziś jesz?", ""]
    out.append(
        "Wybierz porę posiłku, zaznacz produkty, na które masz ochotę — "
        f"albo po prostu przewiń wszystkie {len(recipes)} "
        f"{plural(len(recipes), 'przepis', 'przepisy', 'przepisów')} z Twoich planów."
    )
    out.append("")

    out.append('<div class="p-finder" id="finder">')

    # --- pora posiłku
    out.append('<div class="p-slotbar" role="group" aria-label="Pora posiłku">')
    out.append('<button type="button" class="p-chip" data-slot-filter="all" '
               'data-on="1" aria-pressed="true">Wszystkie</button>')
    for s in slots:
        out.append(
            f'<button type="button" class="p-chip p-chip--slot{s["slot"]}" '
            f'data-slot-filter="{e(s["id"])}" data-slot-label="{e(s["label"])}" '
            f'aria-pressed="false">'
            f'<span class="p-dot"></span>{e(s["label"])} '
            f'<span class="p-num" style="opacity:.7">{e(s["time"])}</span></button>'
        )
    out.append("</div>")

    # --- składniki
    out.append('<details class="p-panel" id="ing-panel">')
    out.append('<summary class="p-panel__summary">')
    out.append('<span class="p-eyebrow">Mam ochotę na…</span>')
    out.append('<span class="p-panel__state" id="ing-state">wybierz składniki</span>')
    out.append("</summary>")
    out.append('<div class="p-panel__inner">')

    # Pole wyszukiwania i „Wyczyść” stoją obok siebie — odznaczenie wszystkiego
    # ma być pod ręką, a nie schowane pod listą wyników.
    out.append('<div class="p-searchrow">')
    out.append('<div class="p-search">' + SEARCH_ICON +
               '<input type="search" id="ing-search" inputmode="search" '
               'placeholder="Szukaj składnika…" aria-label="Szukaj składnika">'
               '<button type="button" class="p-search__x" id="search-clear" '
               'aria-label="Wyczyść wyszukiwanie" hidden>&times;</button></div>')
    out.append('<button type="button" class="p-btn p-btn--clear" id="clear-filters" '
               'hidden>Wyczyść <span class="p-num" id="clear-count"></span></button>')
    out.append("</div>")

    out.append('<div class="p-chips" id="ing-chips">')
    for iid in featured:
        ing = by_id[iid]
        out.append(
            f'<label class="p-chip" data-rank="top" data-label="{e(ing["label"])}">'
            f'<input type="checkbox" value="{e(ing["id"])}">'
            f'{e(ing["label"])} <span class="p-num" style="opacity:.55">{ing["count"]}</span></label>'
        )
    for ing in idx:
        if ing["id"] in featured:
            continue
        out.append(
            f'<label class="p-chip" data-rank="rest" data-label="{e(ing["label"])}" hidden>'
            f'<input type="checkbox" value="{e(ing["id"])}">'
            f'{e(ing["label"])} <span class="p-num" style="opacity:.55">{ing["count"]}</span></label>'
        )
    out.append("</div>")
    out.append(f'<p class="p-hint" id="ing-hint">Widzisz {len(featured)} '
               f"najczęstszych składników. Pozostałe {len(idx) - len(featured)} "
               "znajdziesz przez wyszukiwanie.</p>")
    out.append("</div>")
    out.append("</details>")
    out.append("</div>")

    out.append('<div class="p-count"><span id="result-count" class="p-num"></span></div>')
    out.append("")
    out.append('<p class="p-empty" id="empty-state" hidden>Żaden przepis nie pasuje do tego '
               "wyboru. Odznacz część składników albo wróć do wszystkich pór dnia.</p>")
    out.append("")

    out.append('<ul class="p-cards" id="recipes">')
    for r in recipes:
        tags = " ".join(r["tags"])
        top = ", ".join(i["name"] for i in r["ingredients"] if not i["pantry"]).strip()
        if len(top) > 78:
            top = top[:75].rsplit(",", 1)[0] + "…"
        out.append("<li>")
        out.append(f'<article class="p-card" data-slot="{r["slot"]}" '
                   f'data-slot-id="{e(r["slotId"])}" data-tags="{e(tags)}">')
        out.append('<div class="p-card__band"></div>')
        out.append('<div class="p-card__body">')
        out.append(f'<a class="p-card__title" href="przepisy/{e(r["slug"])}/">{e(r["title"])}</a>')
        out.append('<div class="p-card__meta">')
        out.append(f'<span class="p-card__slot"><span class="p-dot"></span>{e(r["slotLabel"])}</span>')
        out.append(f'<span class="p-num">{e(r["time"])}</span>')
        out.append(f'<span class="p-num">{r["kcal"]} kcal</span>')
        out.append("</div>")
        if top:
            out.append(f'<div class="p-card__tags">{e(top)}</div>')
        out.append("</div></article></li>")
    out.append("</ul>")
    out.append("")

    payload = {"count": len(recipes),
               "ingredients": [{"id": i["id"], "label": i["label"]} for i in idx]}
    out.append("<script>window.RECIPES = " + json.dumps(payload, ensure_ascii=False) + ";</script>")
    out.append("")
    return "\n".join(out)


# ------------------------------------------------------------- przepis.md ---

def render_recipe(r, data):
    groups = data["swapGroups"]
    adjectives = data["swapAdjectives"]
    out = ["---", "hide:", "  - toc", "---", "",
           '<a class="p-back" href="../../">&larr; Wszystkie przepisy</a>', "",
           f'# {r["title"]}', ""]

    out.append(f'<div class="p-hero" data-slot="{r["slot"]}">')
    out.append('<div class="p-hero__top">')
    out.append(f'<span>{e(r["slotLabel"])}</span><span class="p-num">{e(r["time"])}</span>')
    out.append("</div>")
    out.append('<div class="p-macros">')
    for value, label in [(f'{r["kcal"]}', "kcal"), (f'{r["protein"]} g', "białko"),
                         (f'{r["carbs"]} g', "węgl."), (f'{r["fat"]} g', "tłuszcz")]:
        out.append(f'<div class="p-macro"><span class="p-macro__v">{e(value)}</span>'
                   f'<span class="p-macro__l">{e(label)}</span></div>')
    out.append("</div>")
    out.append('<p style="margin:0;font-size:.66rem;color:var(--p-ink-3);font-weight:600">'
               "Wartości dla jednej porcji, tak jak w planie diety.</p>")
    out.append("</div>")
    out.append("")

    out.append('<div class="p-servings">')
    out.append('<span class="p-eyebrow">Dla ilu osób gotujesz?</span>')
    out.append('<div class="p-stepper">')
    out.append('<button type="button" class="p-stepper__btn" id="srv-minus" '
               'aria-label="Mniej osób">&minus;</button>')
    out.append('<span class="p-stepper__value">'
               '<span class="p-stepper__num" id="srv-num" aria-live="polite">1</span>'
               '<span class="p-stepper__word" id="srv-word">osoba</span></span>')
    out.append('<button type="button" class="p-stepper__btn" id="srv-plus" '
               'aria-label="Więcej osób">+</button>')
    out.append("</div>")
    out.append('<p class="p-note" id="srv-note" style="margin:0" hidden></p>')
    out.append("</div>")
    out.append("")

    out.append('<div class="p-ings__head">')
    out.append('<h2 id="ing-heading" style="margin:0">Składniki na 1 osobę</h2>')
    out.append('<button type="button" class="p-btn p-btn--ghost" id="swap-reset" '
               'style="min-height:auto;padding:6px 8px" hidden>Przywróć oryginał</button>')
    out.append("</div>")

    out.append('<ul class="p-ings" id="ing-list">')
    sekcja = None
    for i, ing in enumerate(r["ingredients"]):
        # Nowsze plany dzielą składniki na sekcje („sos:”, „Przekąska: …”).
        if ing.get("section") != sekcja:
            sekcja = ing.get("section")
            if sekcja:
                out.append(f'<li class="p-ings__sec">{e(sekcja)}</li>')
        pantry = ' data-pantry="1"' if ing["pantry"] else ""
        order = ' data-order="name"' if ing.get("nameFirst") else ""
        # „Kasza kuskus – 50 g” nie ma miary domowej, więc gramatura jest
        # jedyną liczbą i nie powtarzamy jej po prawej stronie.
        ilosc = "" if ing.get("weightOnly") else f'{num(ing["qty"])} {skrot(ing["unit"])}'
        out.append(f'<li{pantry}{order}><div class="p-ing__row">'
                   f'<span class="p-ing__q">{e(ilosc)}</span>'
                   f'<span class="p-ing__n">{e(ing["name"])}</span>'
                   f'<span class="p-ing__g">{e(num(ing["grams"]))} g</span></div>')
        if "swap" in ing:
            g = groups[ing["swap"]["group"]]
            out.append('<div class="p-ing__swap">')
            out.append(f'<label class="p-swaplabel" for="swap-{i}">Zamień na</label>')
            out.append(f'<select class="p-select" id="swap-{i}" data-ing="{i}">')
            for o in g["options"]:
                sel = " selected" if o["id"] == ing["swap"]["self"] else ""
                mark = " · oryginał" if o["id"] == ing["swap"]["self"] else ""
                out.append(f'<option value="{e(o["id"])}"{sel}>{e(o["label"])}{mark}</option>')
            out.append("</select>")
            out.append("</div>")
        out.append("</li>")
    out.append("</ul>")
    out.append("")

    out.append('<div class="p-actions">')
    out.append('<button type="button" class="p-btn p-btn--block" id="open-shopping">'
               "&#128722; Lista zakupów</button>")
    out.append('<button type="button" class="p-btn p-btn--primary p-btn--block" id="cook-start">'
               "Gotujmy &rarr;</button>")
    out.append("</div>")
    out.append("")

    out.append("<h2>Sposób przygotowania</h2>")
    out.append('<ol class="p-steps" id="steps-list">')
    for s in r["steps"]:
        out.append(f"<li>{e(render_step(s, r['ingredients'], groups, adjectives))}</li>")
    out.append("</ol>")
    out.append("")

    out.append('<div class="p-cook" id="cook" data-open="0" role="dialog" aria-modal="true" '
               f'aria-label="Gotowanie: {e(r["title"])}">')
    out.append('<div class="p-cook__bar">')
    out.append(f'<span class="p-cook__title">{e(r["title"])}</span>')
    out.append('<button type="button" class="p-iconbtn" id="cook-close" '
               'aria-label="Zamknij tryb gotowania">&times;</button>')
    out.append("</div>")
    out.append('<div class="p-progress" id="cook-progress"></div>')
    out.append('<div class="p-cook__body">')
    out.append('<span class="p-cook__step" id="cook-label"></span>')
    out.append('<p class="p-cook__text" id="cook-text"></p>')
    out.append("</div>")
    out.append('<div class="p-cook__nav">')
    out.append('<button type="button" class="p-btn" id="cook-prev">Wstecz</button>')
    out.append('<button type="button" class="p-btn p-btn--primary" id="cook-next">Następny krok</button>')
    out.append("</div></div>")

    out.append('<div class="p-sheet" id="shopping" data-open="0" role="dialog" aria-modal="true" '
               'aria-label="Lista zakupów">')
    out.append('<button type="button" class="p-sheet__scrim" id="shopping-scrim" '
               'aria-label="Zamknij listę zakupów"></button>')
    out.append('<div class="p-sheet__panel">')
    out.append('<div class="p-sheet__head"><h2>Lista zakupów</h2>'
               '<button type="button" class="p-iconbtn" id="close-shopping" '
               'aria-label="Zamknij">&times;</button></div>')
    out.append('<div class="p-sheet__body" id="shopping-body"></div>')
    out.append('<div class="p-sheet__foot">')
    out.append('<button type="button" class="p-btn" id="reset-shopping">Odznacz wszystko</button>')
    out.append('<button type="button" class="p-btn p-btn--primary" id="pdf-btn">Wygeneruj PDF</button>')
    out.append("</div></div></div>")
    out.append('<div class="p-toast" id="toast" role="status" data-on="0"></div>')
    out.append("")

    used = sorted({i["swap"]["group"] for i in r["ingredients"] if "swap" in i})
    payload = {
        "slug": r["slug"], "title": r["title"],
        "slotLabel": r["slotLabel"], "time": r["time"],
        "baseServings": r["baseServings"],
        "ingredients": r["ingredients"], "steps": r["steps"],
    }
    out.append("<script>window.RECIPE = " + json.dumps(payload, ensure_ascii=False) + ";")
    out.append("window.UNITS = " + json.dumps(data["units"], ensure_ascii=False) + ";")
    out.append("window.SWAPS = " + json.dumps(
        {g: groups[g] for g in used}, ensure_ascii=False) + ";")
    out.append("window.SWAP_ADJ = " + json.dumps(data["swapAdjectives"], ensure_ascii=False) + ";</script>")
    out.append("")
    return "\n".join(out)


# ---------------------------------------------------------- zamienniki.md ---

def render_substitutions(data):
    out = ["---", "hide:", "  - toc", "---", "", "# Zamienniki", "",
           "Przepisany fragment „Listy wymienników” z Twojego planu diety. "
           "Znak `=` znaczy: możesz wymienić jedno na drugie. Przy składnikach "
           "w przepisach znajdziesz te same zamienniki pod przyciskiem "
           "**Zamień na**.", ""]
    for group in data.get("substitutions", []):
        out.append('<div class="p-swap-card">')
        out.append(f'<h3>{e(group["title"])}</h3>')
        for item in group["items"]:
            out.append(f"<p>{e(item)}</p>")
        out.append("</div>")
    out.append("")
    return "\n".join(out)


# -------------------------------------------------------------------- main --

def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    with open(DATA, encoding="utf-8") as f:
        data = json.load(f)

    if os.path.isdir(RECIPE_DIR):
        shutil.rmtree(RECIPE_DIR)
    os.makedirs(RECIPE_DIR)
    for stale in PRZESTARZALE:
        p = os.path.join(DOCS, stale)
        if os.path.exists(p):
            os.remove(p)
            print(f"Usunięto nieużywany plik: docs/{stale}")

    write(os.path.join(DOCS, "index.md"), render_index(data))
    write(os.path.join(DOCS, "zamienniki.md"), render_substitutions(data))
    for r in data["recipes"]:
        write(os.path.join(RECIPE_DIR, r["slug"] + ".md"), render_recipe(r, data))

    n = len(data["recipes"])
    print(f"Wygenerowano: index.md, zamienniki.md oraz {n} "
          f"{plural(n, 'przepis', 'przepisy', 'przepisów')}.")
    print(f"Kategorie: " + ", ".join(f"{s['label']} {s['time']}" for s in data["slots"]))
    print(f"Składniki: {len(data['featuredIngredients'])} widocznych, "
          f"{len(data['ingredientIndex'])} dostępnych przez wyszukiwanie.")
    swaps = sum(1 for r in data["recipes"] for i in r["ingredients"] if "swap" in i)
    print(f"Składników z zamiennikami: {swaps}.")

    # --- kontrole spójności; przy błędzie build ma się wywalić, nie milczeć
    index_text = open(os.path.join(DOCS, "index.md"), encoding="utf-8").read()
    missing = [r["slug"] for r in data["recipes"]
               if f'przepisy/{r["slug"]}/' not in index_text]
    if missing:
        print("BŁĄD: brak linków na stronie głównej:", missing, file=sys.stderr)
        sys.exit(1)

    tags_used = {t for r in data["recipes"] for t in r["tags"]}
    dead = [i["id"] for i in data["ingredientIndex"] if i["id"] not in tags_used]
    if dead:
        print("BŁĄD: filtry bez pokrycia:", dead, file=sys.stderr)
        sys.exit(1)

    known = {i["id"] for i in data["ingredientIndex"]}
    bad = [f for f in data["featuredIngredients"] if f not in known]
    if bad:
        print("BŁĄD: wyróżnione składniki spoza indeksu:", bad, file=sys.stderr)
        sys.exit(1)

    for r in data["recipes"]:
        for s in r["steps"]:
            for m in TOKEN.finditer(s):
                idx = int(m.group(1))
                if idx >= len(r["ingredients"]) or "swap" not in r["ingredients"][idx]:
                    print(f"BŁĄD: {r['slug']} — znacznik wskazuje na składnik "
                          f"bez zamiennika ({m.group(0)})", file=sys.stderr)
                    sys.exit(1)

    # Skróty jednostek są w dwóch miejscach — tu i w app.js. Gdyby się
    # rozjechały, strona przepisu pokazywałaby „1 szt.”, a po zmianie liczby
    # osób „2 sztuki”. Pilnujemy, żeby obie tabele mówiły to samo.
    js = open(os.path.join(DOCS, "javascripts", "app.js"), encoding="utf-8").read()
    blok = re.search(r"var SKROTY = \{(.*?)\};", js, re.S)
    if not blok:
        print("BŁĄD: nie znalazłem tabeli SKROTY w app.js", file=sys.stderr)
        sys.exit(1)
    z_js = dict(re.findall(r'"([^"]+)":\s*"([^"]+)"', blok.group(1)))
    if z_js != SKROTY:
        print("BŁĄD: skróty jednostek rozjechały się między generate_site.py "
              f"a app.js.\n  tylko w app.js: {sorted(set(z_js) - set(SKROTY))}"
              f"\n  tylko w generate_site.py: {sorted(set(SKROTY) - set(z_js))}"
              f"\n  różne wartości: "
              f"{sorted(k for k in set(z_js) & set(SKROTY) if z_js[k] != SKROTY[k])}",
              file=sys.stderr)
        sys.exit(1)

    uzyte = {i["unit"] for r in data["recipes"] for i in r["ingredients"]}
    odmiany = {f for lem in SKROTY if lem in data["units"] for f in data["units"][lem]}
    nieobjete = sorted(f for f in odmiany | uzyte
                       if f in odmiany and f not in SKROTY)
    if nieobjete:
        print(f"BŁĄD: formy jednostek bez skrótu: {nieobjete}", file=sys.stderr)
        sys.exit(1)

    print("Kontrola spójności: OK.")


if __name__ == "__main__":
    main()
