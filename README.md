# Przepisy Dietetyczne

Statyczna strona z przepisami z planu diety: wyszukiwarka według pory posiłku
i składników, przelicznik porcji, interaktywna lista zakupów z eksportem do PDF
oraz tryb gotowania krok po kroku. Zbudowana na MkDocs Material, hostowana na
GitHub Pages.

**Strona:** https://piotrlew-creator.github.io/moje-przepisy/

## Jak to działa

Wszystko pochodzi z jednego pliku — **`recipes.json`**. To jedyne miejsce, w
którym trzymamy dane: nazwy dań, składniki (ilość domowa + gramatura),
kroki przygotowania, kaloryczność, makroskładniki, dzień i numer posiłku.

`generate_site.py` zamienia ten plik w całą zawartość `docs/`:

```
recipes.json ──▶ generate_site.py ──▶ docs/index.md          (wyszukiwarka + lista dań)
                                      docs/przepisy/*.md     (40 przepisów)
                                      docs/plan.md           (plan 10 dni)
                                      docs/zamienniki.md     (lista wymienników)
                                             │
                                             ▼
                                      mkdocs build ──▶ GitHub Pages
```

**Nic w `docs/` nie jest pisane ręcznie.** Dzięki temu lista przepisów na
stronie głównej i lista składników w filtrze nie mogą się rozjechać z samymi
przepisami — wcześniej właśnie tak się stało i 25 z 40 dań było nieosiągalnych.

Generator na koniec sprawdza dwie rzeczy i przerywa build, jeśli któraś nie
wychodzi:

* każdy przepis ma link ze strony głównej,
* każdy składnik w filtrze ma co najmniej jeden pasujący przepis.

## Porządki po przebudowie

Dwa pliki nie są już do niczego potrzebne:

```bash
git rm generate_recipes.py docs/javascripts/main.js
git rm .github/workflows/jekyll-gh-pages.yml
```

Zawartość `docs/` jest generowana, ale trzymamy ją też w repozytorium — dzięki
temu strona zbuduje się nawet wtedy, gdy ktoś zapomni uruchomić generator.
Po każdej zmianie w `recipes.json` uruchom `python generate_site.py`
i zacommituj wynik razem z danymi.

## Praca lokalna

```bash
pip install -r requirements.txt
python generate_site.py     # wygeneruj docs/ z recipes.json
mkdocs serve                # podgląd na http://127.0.0.1:8000
```

## Publikacja

Push na `main` uruchamia `.github/workflows/deploy.yml`, który generuje strony
i publikuje je na GitHub Pages. **To jedyny workflow publikujący tę stronę** —
nie dodawaj drugiego, bo dwa pipeline'y ścigają się o Pages i wygrywa ten,
który akurat skończy później.

## Dodanie przepisu

Dopisz obiekt do tablicy `recipes` w `recipes.json` i uruchom
`python generate_site.py`. Pola:

| pole | znaczenie |
|---|---|
| `slug` | nazwa pliku i adres strony |
| `day`, `slot` | dzień planu (1–10) i numer posiłku (1–4) |
| `slotId`, `slotLabel`, `time` | pora dnia — musi zgadzać się z `slots` |
| `kcal`, `protein`, `carbs`, `fat` | wartości z planu diety, na porcję |
| `baseServings` | ile porcji daje przepis w źródle (domyślnie 1) |
| `ingredients[]` | `qty` + `unit` (miara domowa), `grams`, `name`, `pantry`, `tag` |
| `steps[]` | kroki przygotowania, dosłownie ze źródła |
| `tags[]` | identyfikatory składników używane przez filtr |

Nowy składnik w filtrze wymaga też wpisu w `ingredientIndex`
(`id`, `label`, `count`).

## Skąd pochodzą dane

Sekcja „Plan diety” z PDF-a z planem żywieniowym: 10 dni × 4 posiłki.
Nazwy dań, składniki i kroki są przepisane dosłownie, łącznie z literówkami
oryginału. Trzymaj plik źródłowy w `source/`, żeby dało się odtworzyć każdą
liczbę.
