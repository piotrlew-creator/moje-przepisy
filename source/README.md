# source/

Tu leżą PDF-y z planami diety — źródło wszystkich danych w `recipes.json`.

Nazewnictwo ma znaczenie:

* **`dieta.pdf`** — pierwszy plan. To on ustala slugi (adresy stron przepisów),
  które są zachowywane przy każdej przebudowie, żeby nie posypały się zakładki
  i zapisane w przeglądarce listy zakupów. Nie zmieniaj tej nazwy.
* `dieta_2.pdf`, `dieta_3.pdf`, … — kolejne plany. Cyfra z nazwy trafia do
  pola `plan` przy przepisie.

Do czego są potrzebne:

```bash
python verify_against_pdf.py source   # kontrola: czy dane zgadzają się ze źródłem
python tools/build.py                 # przebudowa recipes.json po dodaniu planu
```

Same PDF-y nie są potrzebne do zbudowania strony — wystarczy `recipes.json`.
Trzymamy je tu po to, żeby dało się odtworzyć każdą liczbę i sprawdzić, że nic
się nie rozjechało.

**Do repozytorium nie wchodzą** — `.gitignore` ma wpis `source/*.pdf`. Powody
są dwa: to ~42 MB, których strona do niczego nie potrzebuje, a raz wysłane
zostałyby w historii gita na zawsze; poza tym to Twoje osobiste plany od
dietetyka. Ten `README.md` jest jedynym plikiem z tego katalogu w repo — po to,
żeby po świeżym klonie było wiadomo, co tu wrzucić.
