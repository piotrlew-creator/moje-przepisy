# Przepisy Dietetyczne

Statyczna strona z przepisami z planów diety: wyszukiwarka według pory posiłku
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
                                      docs/przepisy/*.md     (263 przepisy)
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

Generator sprawdza dane **przed** zapisem — dzięki temu błąd daje czytelny
komunikat, a nie ślad stosu z połowy renderowania, i nie zostawia po sobie na
wpół wygenerowanego `docs/`. Kontrolowane jest:

* slugi są unikalne (inaczej dwa przepisy nadpisałyby ten sam plik),
* każdy składnik w filtrze ma co najmniej jeden pasujący przepis,
* każdy składnik z `featuredIngredients` istnieje w `ingredientIndex`,
* każdy znacznik zamiennika wskazuje składnik, który zamiennik ma,
* **każdy wariant grupy zamienników umie każdy przypadek i przymiotnik**,
  jakiego używa krok — inaczej po zamianie w przeglądarce cicho wychodziłby
  zły przypadek („Papryka pokrój” zamiast „Paprykę pokrój”),
* skróty jednostek w `generate_site.py` i `app.js` mówią to samo,
* każda jednostka użyta w danych ma skrót we wszystkich swoich formach.

Po zapisie sprawdzany jest jeszcze komplet linków na stronie głównej.

## Zawartość docs/

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
| `plan` | z którego planu pochodzi przepis (1–11) |
| `title` | nazwa dania; trafia też do `title:` we front matterze strony, bo bez tego MkDocs wziąłby tytuł z nazwy pliku („Klejacy ryz”) |
| `day`, `slot` | dzień planu (1–10) i numer posiłku (1–4) |
| `mealNo` | numer posiłku z PDF-u (1–4), do kontroli kompletności |
| `sourceTime` | godziny posiłku z PDF-u; `null` dla przekąski, która ich nie ma |
| `slotId`, `slotLabel`, `time` | pora dnia — musi zgadzać się z `slots` |
| `kcal`, `protein`, `carbs`, `fat` | wartości z planu diety, na porcję |
| `baseServings` | ile porcji daje przepis w źródle (domyślnie 1) |
| `ingredients[]` | `qty` + `unit` (miara domowa), `grams`, `name`, `pantry`, `tag`, opcjonalnie `swap`, `nameFirst`, `weightOnly`, `section` |
| `stepsSource[]` | kroki dosłownie ze źródła |
| `steps[]` | kroki w trybie rozkazującym, ze znacznikami zamienników |
| `tags[]` | identyfikatory składników używane przez filtr |

Nowy składnik w filtrze wymaga też wpisu w `ingredientIndex`
(`id`, `label`, `count`). Lista `featuredIngredients` decyduje, których 20
składników widać bez wyszukiwania — reszta jest dostępna przez pole „Szukaj
składnika”, które toleruje literówki.

## Dwa zapisy składnika

Plany różnią się tym, co stoi w wierszu pierwsze, a strona zachowuje zapis
źródłowy — stąd trzy flagi przy składniku:

| zapis w PDF | flagi | jak wygląda na stronie |
|---|---|---|
| `2 łyżki ryżu basmati (30 g)` | brak | `2 łyżki ryżu basmati` |
| `Papryka czerwona – 0.5 sztuki (85 g)` | `nameFirst` | `Papryka czerwona — 0.5 sztuki` |
| `Kasza kuskus – 50 g` | `nameFirst`, `weightOnly` | `Kasza kuskus 50 g` |

`section` przechowuje nagłówek, którym nowsze plany dzielą listę składników
(`łosoś:`, `sos:`, `Panierka:`). Sekcje widać i na stronie przepisu, i na
liście zakupów.

## Kategorie posiłków

Plany mają trzy albo cztery posiłki dziennie, a niektóre dokładają przekąskę
bez godzin. Na stronie wszystko sprowadza się do trzech pór, po godzinie
rozpoczęcia z PDF-u:

| Strona | Godzina startu w PDF | Godziny na stronie |
|---|---|---|
| Śniadanie | do 10:00 (Posiłek 1 i 2) | 7:00–10:00 |
| Obiad | 12:00–16:00 | 13:00–16:00 |
| Kolacja | od 17:00 | 18:00–20:00 |

Przekąski (batonik, jogurt, garść orzechów — pozycje bez godzin w PDF-ie) są
**pomijane w całości**. Nie ma w nich czego gotować, a w wyszukiwarce zaśmiecały
kolację pozycjami na 180 kcal obok obiadów na 600. Odsiewa je `tools/build.py`.

## Zamienniki składników

`swapGroups` w `recipes.json` opisuje grupy wymienne z „Listy wymienników”
w PDF-ie (płatki, ryż i kasze, makaron, pieczywo, mleko, twarogowe,
strączkowe, orzechy, zielone liściaste, ziemniaki, tłuszcze, warzywa, owoce,
słodziki, pasty). Każdy wariant ma pełną odmianę przez przypadki, bo bez tego
podmiana w krokach dawałaby „Do rondelka po gruszka”.

W grupie „owoce” warianty mają dodatkowo `equiv` — wagę jednej sztuki z tabeli
zamienników w PDF-ie. Przy jednostce sztukowej gramatura liczona jest wprost:
`liczba sztuk × waga sztuki wariantu`, więc 1 sztuka jabłka po zamianie na kaki
daje 250 g — dokładnie tyle, ile mówi tabela na stronie „Zamienniki”.

Warzywa takiej tabeli w PDF-ie nie mają, a jedna sztuka dyni to nie to samo co
jedna sztuka pomidora. Dlatego po zamianie warzywa mierzonego w sztukach
zostaje sama gramatura z planu („160 g dyni”) — dietetyk podaje właśnie wagę,
a mylącej liczby sztuk nie wymyślamy.

Formy gramatyczne mają rozsądne cofnięcie: biernik potoczny („pokrój pomidora”)
mają tylko rzeczowniki męskie odmieniane jak żywotne, więc dla żeńskich
i nijakich wariant dostaje zwykły biernik („Paprykę pokrój”).

## Skąd pochodzą dane

Rozdział „Plan diety” z dziesięciu planów żywieniowych — razem 358 posiłków,
z czego **263 unikalne przepisy**; powtórzenia (to samo danie w kilku planach)
są odsiewane po nazwie, a przekąski pomijane. Nazwy dań, składniki i kroki są przepisane
dosłownie, łącznie z literówkami oryginału. Trzymaj pliki źródłowe w `source/`, żeby dało się
odtworzyć każdą liczbę — ale **nie commituj ich**: `.gitignore` ma wpis
`source/*.pdf`, bo to ~42 MB, których strona nie potrzebuje (buduje się
z `recipes.json`), a w historii gita zostałyby na zawsze.

Kontrola zgodności ze źródłem:

```bash
python verify_against_pdf.py source        # albo: source/plan1.pdf source/plan2.pdf ...
```

Skrypt czyta PDF-y drugą, niezależną ścieżką i sprawdza, czy każdy składnik,
każdy krok z `stepsSource` i każda nazwa dania stoją w źródle dosłownie.
