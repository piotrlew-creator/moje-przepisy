# Przepisy Dietetyczne

Statyczna strona z przepisami z planu diety: wyszukiwarka według pory posiłku
i składników, przelicznik porcji, zamienniki składników, interaktywna lista
zakupów z eksportem do PDF oraz tryb gotowania krok po kroku. Zbudowana na
MkDocs Material, hostowana na GitHub Pages.

**Strona:** https://piotrlew-creator.github.io/moje-przepisy/

## Jak to działa

Wszystko pochodzi z jednego pliku — **`recipes.json`**. To jedyne miejsce, w
którym trzymamy dane: nazwy dań, składniki (ilość domowa + gramatura),
kroki przygotowania, kaloryczność, makroskładniki, dzień i numer posiłku.

`generate_site.py` zamienia ten plik w całą zawartość `docs/`:

```
recipes.json ──▶ generate_site.py ──▶ docs/index.md          (wyszukiwarka + lista dań)
                                      docs/przepisy/*.md     (40 przepisów)
                                      docs/zamienniki.md     (lista wymienników)
                                             │
                                             ▼
                                      mkdocs build ──▶ GitHub Pages
```

## Dwie wersje kroków przygotowania

Każdy przepis trzyma kroki dwa razy:

* **`stepsSource`** — dosłowny zapis z PDF-u („Jabłko kroimy w kostkę”).
  To wersja odniesienia; `verify_against_pdf.py` porównuje właśnie ją.
* **`steps`** — ta sama treść w trybie rozkazującym („Jabłko pokrój w kostkę”)
  ze znacznikami zamienników.

Znacznik wygląda tak: `«2|B|przyprawiony_B||U»` i znaczy „składnik nr 2,
biernik, z przymiotnikiem »przyprawiony«, wielką literą”. Strona podstawia
w niego formę wybranego wariantu, dzięki czemu po zamianie jabłka na gruszkę
krok czyta się „Gruszkę pokrój w kostkę”, a nie „Gruszka pokrój w kostkę”.
Znacznik wskazuje konkretny składnik, nie grupę — inaczej w sałatce greckiej
„paprykę, pomidor, ogórek” zamieniłyby się wszystkie na to samo warzywo.

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
| `mealNo` | numer posiłku z PDF-u (1–4), do kontroli kompletności |
| `slotId`, `slotLabel`, `time` | pora dnia — musi zgadzać się z `slots` |
| `kcal`, `protein`, `carbs`, `fat` | wartości z planu diety, na porcję |
| `baseServings` | ile porcji daje przepis w źródle (domyślnie 1) |
| `ingredients[]` | `qty` + `unit` (miara domowa), `grams`, `name`, `pantry`, `tag`, opcjonalnie `swap` |
| `stepsSource[]` | kroki dosłownie ze źródła |
| `steps[]` | kroki w trybie rozkazującym, ze znacznikami zamienników |
| `tags[]` | identyfikatory składników używane przez filtr |

Nowy składnik w filtrze wymaga też wpisu w `ingredientIndex`
(`id`, `label`, `count`). Lista `featuredIngredients` decyduje, których 20
składników widać bez wyszukiwania — reszta jest dostępna przez pole „Szukaj
składnika”, które toleruje literówki.

## Kategorie posiłków

PDF ma cztery posiłki dziennie; na stronie Posiłek 1 i 2 są scalone w jedno
„Śniadanie”:

| Strona | Posiłki z PDF-u | Godziny |
|---|---|---|
| Śniadanie | 1 i 2 | 7:00–10:00 |
| Obiad | 3 | 13:00–16:00 |
| Kolacja | 4 | 18:00–20:00 |

## Zamienniki składników

`swapGroups` w `recipes.json` opisuje grupy wymienne z „Listy wymienników”
w PDF-ie (płatki, ryż i kasze, makaron, pieczywo, mleko, twarogowe,
strączkowe, orzechy, zielone liściaste, ziemniaki, tłuszcze, warzywa, owoce,
słodziki, pasty). Każdy wariant ma pełną odmianę przez przypadki, bo bez tego
podmiana w krokach dawałaby „Do rondelka po gruszka”.

W grupie „owoce” warianty mają dodatkowo `equiv` — wagę jednej sztuki z tabeli
zamienników w PDF-ie. Dzięki temu zamiana jabłka (150 g, 1 sztuka) na banana
daje 106 g, a nie 150 g.

## Skąd pochodzą dane

Sekcja „Plan diety” z PDF-a z planem żywieniowym: 10 dni × 4 posiłki.
Nazwy dań, składniki i kroki są przepisane dosłownie, łącznie z literówkami
oryginału. Trzymaj plik źródłowy w `source/`, żeby dało się odtworzyć każdą
liczbę.
