# -*- coding: utf-8 -*-
"""Zamiana 1. os. l.mn. na 2. os. l.poj. trybu rozkazującego.

Domyślnie forma dokonana („kroimy” → „pokrój”). Czasowniki opisujące
czynność, która trwa, wracają do formy niedokonanej, gdy w zdaniu stoi
określenie czasu — „Usmaż, aż jajka się zetną” jest po polsku błędne,
„Smaż, aż jajka się zetną” nie.

Słownik jest listą dozwolonych słów, nie regułą ogólną: dzięki temu
rzeczowniki kończące się na „-my” (formy, kurkumy) zostają nietknięte.
"""
from imperative import VERBS as VERBS_BAZOWE

VERBS = dict(VERBS_BAZOWE)

VERBS.update({
    # --- czynności kuchenne
    "pozbywamy": "pozbądź",   # „pozbywamy się pestek” → „pozbądź się pestek”
    "miksujemy": "zmiksuj",
    "skrapiamy": "skrop",
    "ścieramy": "zetrzyj",
    "zawijamy": "zawiń",
    "umieszczamy": "umieść",
    "wylewamy": "wylej",
    "grillujemy": "grilluj",
    "grilujemy": "griluj",
    "solimy": "posól",
    "pieprzymy": "popieprz",
    "podpiekamy": "podpiecz",
    "wydrążamy": "wydrąż",
    "prażymy": "praż",
    "przelewamy": "przelej",
    "rozkładamy": "rozłóż",
    "ubijamy": "ubij",
    "zmniejszamy": "zmniejsz",
    "kruszymy": "pokrusz",
    "odparowujemy": "odparuj",
    "osuszamy": "osusz",
    "przecieramy": "przetrzyj",
    "przekrajamy": "przekrój",
    "przekręcamy": "przekręć",
    "przesmażamy": "przesmaż",
    "przewracamy": "przewróć",
    "rozpuszczamy": "rozpuść",
    "usuwamy": "usuń",
    "wrzucamy": "wrzuć",
    "wyciskamy": "wyciśnij",
    "wyjmujemy": "wyjmij",
    "dekorujemy": "udekoruj",
    "nasączamy": "nasącz",
    "odcinamy": "odetnij",
    "odkładamy": "odłóż",
    "odwracamy": "odwróć",
    "przecinamy": "przetnij",
    "płuczemy": "wypłucz",
    "opłukujemy": "opłucz",
    "robimy": "zrób",
    "roztrzepujemy": "roztrzep",
    "słodzimy": "posłódź",
    "wstawiamy": "wstaw",
    "wsuwamy": "wsuń",
    "zwijamy": "zwiń",
    "rolujemy": "zroluj",
    "doprowadzamy": "doprowadź",
    "miażdżymy": "zmiażdż",
    "moczymy": "namocz",
    "nalewamy": "nalej",
    "natłuszczamy": "natłuść",
    "oblewamy": "oblej",
    "obracamy": "obróć",
    "odciskamy": "odciśnij",
    "oddzielamy": "oddziel",
    "oprawiamy": "opraw",
    "oprószamy": "oprósz",
    "otwieramy": "otwórz",
    "podgotowujemy": "podgotuj",
    "przebieramy": "przebierz",
    "przesiewamy": "przesiej",
    "przyciskamy": "przyciśnij",
    "próbujemy": "spróbuj",
    "smakujemy": "skosztuj",
    "rozciągamy": "rozciągnij",
    "rozkłócamy": "rozkłóć",
    "rozprowadzamy": "rozprowadź",
    "rozrabiamy": "rozrób",
    "rozsmarowujemy": "rozsmaruj",
    "spłaszczamy": "spłaszcz",
    "szarpiemy": "poszarp",
    "szykujemy": "przyszykuj",
    "wybijamy": "wbij",
    "wycieramy": "wytrzyj",
    "wycinamy": "wytnij",
    "wyłączamy": "wyłącz",
    "zagniatamy": "zagnieć",
    "zagęszczamy": "zagęść",
    "zestawiamy": "zestaw",
    "marynujemy": "marynuj",
    "czekamy": "czekaj",
    "chłodzimy": "chłodź",
    "trzymamy": "trzymaj",
    "trzymajmy": "trzymaj",
    "potrząsamy": "potrząsaj",
    "powtarzamy": "powtarzaj",
    "używamy": "używaj",
    "delektujemy": "delektuj",
    "cieszymy": "ciesz",
    # --- literówki źródła zachowujemy w duchu oryginału
    "podjemy": "podaj",
    "posupujemy": "posyp",
    # --- formy, które nie są rozkazem, tylko zwrotem do czytelnika
    "możemy": "możesz",
    "będziemy": "będziesz",
    "uzyskamy": "uzyskasz",
    "otrzymamy": "otrzymasz",
    "dodajmy": "dodaj",
})

# Czasowniki, które przy określeniu czasu wracają do formy niedokonanej.
NIEDOKONANE = {
    "ugotuj": "gotuj",
    "usmaż": "smaż",
    "upiecz": "piecz",
    "wymieszaj": "mieszaj",
    "uduś": "duś",
}

# Konteksty świadczące o czynności trwającej.
TRWANIE = (r"aż\b|przez\s+(?:około\s+)?\d|co\s+chwil|na\s+wolnym\s+ogniu"
           r"|na\s+małym\s+ogniu|na\s+średnim\s+ogniu|\d\s*-\s*\d+\s*minut"
           r"|\d+\s*minut|\d+\s*godzin")

# Pozostałości pierwszej osoby liczby mnogiej poza czasownikami.
ZAIMKI = [
    ("które nam zostały", "które Ci zostały"),
    ("naszym omletem", "swoim omletem"),
    ("naszej", "swojej"),
    ("nasze ", "swoje "),
    ("naszą", "swoją"),
]
