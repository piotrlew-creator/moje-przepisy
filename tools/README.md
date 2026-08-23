# tools/ — przebudowa `recipes.json` z PDF-ów

Te skrypty są potrzebne tylko wtedy, gdy dochodzi nowy plan diety. Do
zbudowania samej strony wystarczy `recipes.json` i `generate_site.py`
w katalogu głównym.

## Dodanie nowego planu

1. Wrzuć PDF do `source/`. Pierwszy plan **musi** nazywać się `dieta.pdf` —
   to on ustala slugi (adresy stron), które są potem zachowywane przy każdej
   przebudowie, żeby nie posypały się zakładki i zapisane listy zakupów.
   Kolejne plany nazywaj `dieta_2.pdf`, `dieta_3.pdf` … — cyfra z nazwy
   trafia do pola `plan`.

2. Uruchom z katalogu głównego projektu:

   ```bash
   pip install pdfplumber          # plus poppler-utils dla `pdftotext`
   python tools/build.py           # PDF-y  ──▶ recipes.json
   python tools/migrate2.py        # znaczniki zamienników w krokach
   python generate_site.py         # recipes.json ──▶ docs/
   python verify_against_pdf.py source
   ```

3. `verify_against_pdf.py` musi wypisać zero niezgodności. Dopiero wtedy
   commituj `recipes.json` razem z `docs/`.

## Co robi który plik

| plik | rola |
|---|---|
| `extract.py` | czyta rozdział „Plan diety”: dzieli stronę na kolumny, skleja zawinięte składniki, rozpoznaje oba zapisy składnika, wydziela przekąski |
| `tagi.py` | przypisuje składnikom identyfikatory do filtra i oznacza produkty spiżarniane (sól, pieprz, oliwa) |
| `imperative2.py` | słownik czasowników: „kroimy” → „pokrój”, z zachowaniem form niedokonanych tam, gdzie czynność trwa („gotuj”, nie „ugotuj”) |
| `swaps.py` | grupy wymienne z „Listy wymienników” wraz z pełną odmianą przez przypadki |
| `build.py` | spina powyższe i zapisuje `recipes.json`; odsiewa dania powtarzające się między planami |
| `migrate2.py` | zamienia nazwy składników w krokach na znaczniki `«indeks\|PRZYPADEK\|…»` |

## Uwaga o powtórzeniach

Dania powtarzają się między planami — z 358 posiłków w dziesięciu PDF-ach
zostaje 280 unikalnych przepisów. Odsiewanie idzie po znormalizowanej nazwie
dania (bez „(liczba porcji: N)”), zawsze zostaje wersja z planu wcześniejszego
na liście.
