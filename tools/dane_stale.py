# -*- coding: utf-8 -*-
"""Dane, których nie da się wyciągnąć z rozdziału „Plan diety”.

Wcześniej siedziały wyłącznie w recipes.json i nic ich nie odtwarzało —
skasowanie tego pliku znaczyło bezpowrotną utratę strony „Zamienniki”
i dwudziestu widocznych chipów na stronie głównej. Teraz są w repozytorium
jako źródło, a build.py tylko je przepisuje.
"""

# Przepisany fragment „Listy wymienników” z PDF-u. Dosłownie, ze znakiem „=”.
WYMIENNIKI = [
    {
        "title": "Źródła węglowodanów",
        "items": [
            "Pomidor = ogórek = papryka = cukinia = brokuł = marchew = rzodkiewka = kapusta = seler naciowy = kalafior = szparagi = bakłażan = dynia = pieczarki = inne warzywa (poza nasiona roślin strączkowych i ziemniakami)",
            "Szpinak = rukola = roszponka = sałata rzymska = miks sałat = jarmuż = sałata lodowa = inne zielone warzywa liściaste",
            "Owoce świeże, zawsze możesz zamieniać na suszone i na odwrót: 150 g owoców świeżych = 20 g suszonych",
            "Mąka jaglana = mąka gryczana = mąka żytnia typ 2000 = mąka ryżowa = mąka z tapioki = mąka amarantusowa = mąka orkiszowa = mąka pełnoziarnista = mąka owsiana",
            "Płatki owsiane = płatki jaglane = płatki gryczane = płatki ryżowe = płatki orkiszowe",
            "Ryż biały = ryż basmati = ryż brązowy = ryż dziki = komosa ryżowa = kasza gryczana = kasza jaglana = kasza pęczak = kasza bulgur = kasza owsiana = kasza jęczmienna = amarantus = makaron gryczany = makaron jaglany = makaron żytni = makaron ryżowy = makaron pełnoziarnisty = makaron orkiszowy = makaron bezglutenowy",
            "Ziemniaki = bataty = topinambur",
            "100 g ryżu / kaszy = 450-500 g ziemniaków",
            "Chleb żytni razowy = chleb żytni na zakwasie = chleb orkiszowy = chleb pełnoziarnisty = chleb bezglutenowy = bułka owsiana = bułka grahamka = bułka pełnoziarnista",
            "Hummus = pasty warzywne",
            "Miód = syrop klonowy = syrop z agawy"
        ]
    },
    {
        "title": "Źródła białka",
        "items": [
            "Mięso z piersi z kurczaka = mięso z piersi indyka = mielone mięso drobiowe = schab wieprzowy = polędwiczka wieprzowa = polędwica wołowa = rostbef wołowy = inne chude mięso = tofu naturalne = krewetki tygrysie",
            "Dorsz = mintaj = pstrąg = morszczuk = sandacz = tuńczyk = krewetki tygrysie = inna chuda ryba lub owoce morza",
            "Halibut = łosoś = śledź = makrela = pstrąg tęczowy = inna tłusta ryba",
            "Ciecierzyca = soczewica = fasola = groch = soja",
            "Serek wiejski = ser twarogowy chudy = tofu naturalne",
            "Mleko 2% = mleko bezlaktozowe 2% = napój sojowy niesłodzony = napój migdałowy niesłodzony = napój owsiany niesłodzony = inne napoje roślinne niesłodzone"
        ]
    },
    {
        "title": "Źródła tłuszczu",
        "items": [
            "Orzechy włoskie = orzechy nerkowca = orzechy laskowe = orzechy pistacjowe = orzechy piniowe = orzechy pekan = orzechy arachidowe = siemię lniane = sezam = pestki słonecznika = pestki dyni = wiórki kokosowe = masło orzechowe = nasiona chia",
            "Oliwa z oliwek = olej rzepakowy = olej z awokado = olej kokosowy = inny olej roślinny = masło"
        ]
    },
    {
        "title": "Napoje",
        "items": [
            "Woda = herbata = kawa = napary ziołowe (np. mięta, pokrzywa, melisa)"
        ]
    },
    {
        "title": "Zamienniki owoców",
        "items": [
            "1 sztuka (120 g) banana = 1 sztuka (170 g) dużego jabłka = 1 sztuka (240 g) pomarańczy = 1⁄2 sztuki (125 g) kaki = 3 sztuki (195 g) mandarynek = 2 sztuki (180 g) brzoskwiń = 1 sztuka (170 g) gruszki = 2 sztuki (160 g) kiwi = 3 garści (210 g) malin = 4 garści (280 g) truskawek = 2 garści (140 g) winogron = 1 sztuka (220 g) grejpfruta = 1⁄2 sztuki (140 g) mango = 7 sztuk (210 g) śliwek = 200 g ananasa = 4 garści (175 g) borówek = 2 garści (160 g) czereśni"
        ]
    }
]

# Dwadzieścia składników widocznych bez wyszukiwania. Dobrane pod „na co masz
# ochotę”, a nie po częstości — dlatego nie ma tu soli, oliwy i przypraw.
WYROZNIONE = [
    "jajka",
    "makaron",
    "ryz",
    "kasza",
    "platki-owsiane",
    "chleb",
    "tortilla",
    "banan",
    "jablko",
    "pomidor",
    "ogorek",
    "papryka",
    "szpinak",
    "cukinia",
    "mozzarella",
    "jogurt",
    "tofu",
    "losos",
    "orzechy",
    "maslo-orzechowe"
]

# Opis źródła, pokazywany w README i w metadanych.
ZRODLO = "Rozdział „Plan diety” z dziesięciu planów żywieniowych"
