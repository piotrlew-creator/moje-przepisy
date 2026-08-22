#!/usr/bin/env python3
"""Generuje całą zawartość docs/ z jednego pliku recipes.json.

Powstają:
  docs/index.md          — wyszukiwarka + lista wszystkich przepisów
  docs/przepisy/<slug>.md — pojedynczy przepis
  docs/plan.md           — plan 10 dni
  docs/zamienniki.md     — lista wymienników z PDF-u

Nic w docs/ nie jest pisane ręcznie, więc lista przepisów i lista składników
nie mogą się rozjechać z przepisami. Skrypt jest też uruchamiany w GitHub
Actions przed `mkdocs build`.

Użycie:  python generate_site.py
"""
import html
import json
import os
import shutil
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, "recipes.json")
DOCS = os.path.join(ROOT, "docs")
RECIPE_DIR = os.path.join(DOCS, "przepisy")

TOP_INGREDIENTS = 18  # ile chipów widać przed „Pokaż wszystkie”

SEARCH_ICON = (
    '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" '
    'stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true">'
    '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>'
)


def e(s):
    return html.escape(str(s), quote=True)


def plural(n, one, few, many):
    if n == 1:
        return one
    if 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14:
        return few
    return many


# --------------------------------------------------------------- index.md ---

def render_index(data):
    slots = data["slots"]
    idx = data["ingredientIndex"]
    recipes = data["recipes"]

    out = []
    out.append("---")
    out.append("hide:")
    out.append("  - toc")
    out.append("---")
    out.append("")
    out.append("# Co dziś jesz?")
    out.append("")
    out.append(
        "Wybierz porę posiłku, zaznacz produkty, na które masz ochotę — "
        f"albo po prostu przewiń wszystkie {len(recipes)} przepisów z Twojego planu."
    )
    out.append("")

    out.append('<div class="p-finder" id="finder">')

    # --- pory dnia
    out.append('<div class="p-slotbar" role="group" aria-label="Pora posiłku">')
    out.append(
        '<button type="button" class="p-chip" data-slot-filter="all" '
        'data-on="1" aria-pressed="true">Wszystkie</button>'
    )
    for s in slots:
        out.append(
            f'<button type="button" class="p-chip p-chip--slot{s["slot"]}" '
            f'data-slot-filter="{e(s["id"])}" aria-pressed="false">'
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
    out.append('<div class="p-search">' + SEARCH_ICON +
               '<input type="search" id="ing-search" inputmode="search" '
               'placeholder="Szukaj składnika…" aria-label="Szukaj składnika"></div>')
    out.append('<div class="p-chips" id="ing-chips" data-collapsed="1">')
    for i, ing in enumerate(idx):
        rank = "top" if i < TOP_INGREDIENTS else "rest"
        out.append(
            f'<label class="p-chip" data-rank="{rank}" data-label="{e(ing["label"])}">'
            f'<input type="checkbox" value="{e(ing["id"])}">'
            f'{e(ing["label"])} <span class="p-num" style="opacity:.55">{ing["count"]}</span></label>'
        )
    out.append("</div>")
    out.append('<button type="button" class="p-btn p-btn--ghost" id="ing-toggle" '
               'style="align-self:flex-start"></button>')
    out.append("</div>")
    out.append("</details>")
    out.append("</div>")

    # --- licznik
    out.append('<div class="p-count">')
    out.append('<span id="result-count" class="p-num"></span>')
    out.append('<button type="button" class="p-btn p-btn--ghost" id="clear-filters" '
               'style="min-height:auto;padding:6px 8px" hidden>Wyczyść filtry</button>')
    out.append("</div>")
    out.append("")

    out.append('<p class="p-empty" id="empty-state" hidden>Żaden przepis nie pasuje do tego '
               "wyboru. Odznacz część składników albo wróć do wszystkich pór dnia.</p>")
    out.append("")

    # --- karty
    out.append('<ul class="p-cards" id="recipes">')
    for r in recipes:
        tags = " ".join(r["tags"])
        top = ", ".join(
            i["name"] for i in r["ingredients"] if not i["pantry"]
        ).strip()
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
        out.append(f'<span class="p-num">Dzień {r["day"]}</span>')
        out.append("</div>")
        if top:
            out.append(f'<div class="p-card__tags">{e(top)}</div>')
        out.append("</div>")
        out.append("</article>")
        out.append("</li>")
    out.append("</ul>")
    out.append("")

    payload = {"count": len(recipes)}
    out.append("<script>window.RECIPES = " + json.dumps(payload, ensure_ascii=False) + ";</script>")
    out.append("")
    return "\n".join(out)


# ------------------------------------------------------------- przepis.md ---

def render_recipe(r, units):
    out = []
    out.append("---")
    out.append("hide:")
    out.append("  - toc")
    out.append("---")
    out.append("")
    out.append('<a class="p-back" href="../../">&larr; Wszystkie przepisy</a>')
    out.append("")
    out.append(f'# {r["title"]}')
    out.append("")

    out.append(f'<div class="p-hero" data-slot="{r["slot"]}">')
    out.append('<div class="p-hero__top">')
    out.append(f'<span>{e(r["slotLabel"])}</span><span class="p-num">{e(r["time"])}</span>'
               f'<span class="p-num">Dzień {r["day"]}</span>')
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

    # --- liczba osób
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

    out.append(f'<h2 id="ing-heading">Składniki na 1 osobę</h2>')
    out.append('<ul class="p-ings" id="ing-list">')
    for ing in r["ingredients"]:
        qty = ing["qty"]
        qty_s = str(int(qty)) if float(qty).is_integer() else str(qty)
        grams = ing["grams"]
        grams_s = str(int(grams)) if float(grams).is_integer() else str(grams)
        pantry = ' data-pantry="1"' if ing["pantry"] else ""
        out.append(
            f'<li{pantry}><span class="p-ing__q">{e(qty_s)} {e(ing["unit"])}</span>'
            f'<span>{e(ing["name"])}</span>'
            f'<span class="p-ing__g">{e(grams_s)} g</span></li>'
        )
    out.append("</ul>")
    out.append("")

    out.append('<div class="p-actions">')
    out.append('<button type="button" class="p-btn p-btn--block" id="open-shopping">'
               "&#128722; Lista zakupów</button>")
    out.append('<button type="button" class="p-btn p-btn--primary p-btn--block" id="cook-start">'
               "Gotujmy &rarr;</button>")
    out.append("</div>")
    out.append("")

    # --- kroki (widoczne też bez JS, tryb gotowania czyta je z window.RECIPE)
    out.append("<h2>Sposób przygotowania</h2>")
    out.append('<ol class="p-steps">')
    for s in r["steps"]:
        out.append(f"<li>{e(s)}</li>")
    out.append("</ol>")
    out.append("")

    # --- tryb gotowania
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
    out.append("</div>")
    out.append("</div>")

    # --- lista zakupów
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
    out.append("</div>")
    out.append("</div></div>")
    out.append('<div class="p-toast" id="toast" role="status" data-on="0"></div>')
    out.append("")

    payload = {
        "slug": r["slug"], "title": r["title"], "day": r["day"],
        "slotLabel": r["slotLabel"], "time": r["time"],
        "baseServings": r["baseServings"],
        "ingredients": r["ingredients"], "steps": r["steps"],
    }
    out.append("<script>window.RECIPE = " + json.dumps(payload, ensure_ascii=False) + ";")
    out.append("window.UNITS = " + json.dumps(units, ensure_ascii=False) + ";</script>")
    out.append("")
    return "\n".join(out)


# ---------------------------------------------------------------- plan.md ---

def render_plan(data):
    recipes = data["recipes"]
    days = {}
    for r in recipes:
        days.setdefault(r["day"], []).append(r)

    out = ["---", "hide:", "  - toc", "---", "", "# Plan 10 dni", "",
           "Dokładnie tak, jak w Twoim PDF-ie: cztery posiłki dziennie, "
           "od śniadania o 6:00 do kolacji o 21:00.", ""]
    for day in sorted(days):
        meals = sorted(days[day], key=lambda m: m["slot"])
        total = sum(m["kcal"] for m in meals)
        out.append('<div class="p-day">')
        out.append('<div class="p-day__head">')
        out.append(f"<h2>Dzień {day}</h2>")
        out.append(f'<span class="p-day__kcal">{total} kcal</span>')
        out.append("</div>")
        out.append('<ul class="p-day__meals">')
        for m in meals:
            out.append("<li>")
            out.append(f'<a class="p-day__meal" data-slot="{m["slot"]}" '
                       f'href="../przepisy/{e(m["slug"])}/">')
            out.append('<span class="p-day__bar"></span>')
            out.append(f'<span><span class="p-day__slot">{e(m["slotLabel"])} · {e(m["time"])}</span>'
                       f'<br><span class="p-day__name">{e(m["title"])}</span></span>')
            out.append(f'<span class="p-day__kcal p-num">{m["kcal"]} kcal</span>')
            out.append("</a>")
            out.append("</li>")
        out.append("</ul>")
        out.append("</div>")
    out.append("")
    return "\n".join(out)


# ---------------------------------------------------------- zamienniki.md ---

def render_substitutions(data):
    out = ["---", "hide:", "  - toc", "---", "", "# Zamienniki", "",
           "Przepisany fragment „Listy wymienników” z Twojego planu diety. "
           "Znak `=` znaczy: możesz wymienić jedno na drugie.", ""]
    for group in data.get("substitutions", []):
        out.append('<div class="p-swap">')
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

    write(os.path.join(DOCS, "index.md"), render_index(data))
    write(os.path.join(DOCS, "plan.md"), render_plan(data))
    write(os.path.join(DOCS, "zamienniki.md"), render_substitutions(data))
    for r in data["recipes"]:
        write(os.path.join(RECIPE_DIR, r["slug"] + ".md"), render_recipe(r, data["units"]))

    n = len(data["recipes"])
    print(f"Wygenerowano: index.md, plan.md, zamienniki.md oraz {n} "
          f"{plural(n, 'przepis', 'przepisy', 'przepisów')}.")
    print(f"Składniki w wyszukiwarce: {len(data['ingredientIndex'])}.")

    # Zabezpieczenie: każdy przepis musi być osiągalny ze strony głównej.
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
    print("Kontrola spójności: OK — każdy przepis ma link, każdy filtr ma wyniki.")


if __name__ == "__main__":
    main()
