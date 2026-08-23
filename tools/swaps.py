# -*- coding: utf-8 -*-
"""Zamienniki składników — wyłącznie z „Listy wymienników” w PDF-ie.

Każdy wariant ma pełną odmianę, bo składniki pojawiają się w krokach w różnych
przypadkach („Jabłko pokrój”, „Do rondelka po jabłkach”, „ryż z jabłkami”).
Bez tego podmiana dawałaby „Do rondelka po gruszka”.

Klucze przypadków:
  M  mianownik   (kto? co?)        B  biernik     (kogo? co?)
  D  dopełniacz  (kogo? czego?)    N  narzędnik   (kim? czym?)
  Ms miejscownik (o kim? o czym?)
  *pl — te same przypadki w liczbie mnogiej.

`rodzaj` steruje odmianą przymiotników w krokach (patrz PRZYMIOTNIKI).
`equiv` to gramatura jednej sztuki z tabeli zamienników owoców w PDF-ie —
używana tylko w grupie „owoce”, żeby podmiana nie zmieniała wielkości porcji.
"""

# Przymiotniki, które w krokach stoją przy zamienianym składniku.
# Klucze: rodzaj męski / żeński / nijaki / mnogi.
PRZYMIOTNIKI = {
    "umyty_B":       {"m": "umyty",       "f": "umytą",       "n": "umyte",       "pl": "umyte"},
    "swiezy_B":      {"m": "świeży",      "f": "świeżą",      "n": "świeże",      "pl": "świeże"},
    "odsaczony_B":   {"m": "odsączony",   "f": "odsączoną",   "n": "odsączone",   "pl": "odsączone"},
    "pieczony_N":    {"m": "pieczonym",   "f": "pieczoną",    "n": "pieczonym",   "pl": "pieczonymi"},
    "pokrojony_B":   {"m": "pokrojony",   "f": "pokrojoną",   "n": "pokrojone",   "pl": "pokrojone"},
    "ugotowany_B":   {"m": "ugotowany",   "f": "ugotowaną",   "n": "ugotowane",   "pl": "ugotowane"},
    "podsmazony_B":  {"m": "podsmażony",  "f": "podsmażoną",  "n": "podsmażone",  "pl": "podsmażone"},
    "przyprawiony_B": {"m": "przyprawiony", "f": "przyprawioną", "n": "przyprawione", "pl": "przyprawione"},
    "prazony_N":     {"m": "prażonym",    "f": "prażoną",     "n": "prażonym",    "pl": "prażonymi"},
    "pokrojony_N":   {"m": "pokrojonym",  "f": "pokrojoną",   "n": "pokrojonym",  "pl": "pokrojonymi"},
    "starty_B":      {"m": "starty",      "f": "startą",      "n": "starte",      "pl": "starte"},
    "ugotowany_N":   {"m": "ugotowanym",  "f": "ugotowaną",   "n": "ugotowanym",  "pl": "ugotowanymi"},
    "przygotowany_B": {"m": "przygotowany", "f": "przygotowaną", "n": "przygotowane", "pl": "przygotowane"},
}


def _o(id, label, rodzaj, M, D, B, N, Ms, **extra):
    d = {"id": id, "label": label, "rodzaj": rodzaj,
         "formy": {"M": M, "D": D, "B": B, "N": N, "Ms": Ms}}
    for k, v in extra.items():
        if k == "equiv":
            d["equiv"] = v
        else:
            d["formy"][k] = v
    return d


GRUPY = {
    # ---------------------------------------------------------------- płatki
    # PDF: Płatki owsiane = jaglane = gryczane = ryżowe = orkiszowe
    "platki": {
        "label": "Płatki",
        "opcje": [
            _o("platki-owsiane", "Płatki owsiane", "pl",
               "płatki owsiane", "płatków owsianych", "płatki owsiane",
               "płatkami owsianymi", "płatkach owsianych"),
            _o("platki-jaglane", "Płatki jaglane", "pl",
               "płatki jaglane", "płatków jaglanych", "płatki jaglane",
               "płatkami jaglanymi", "płatkach jaglanych"),
            _o("platki-gryczane", "Płatki gryczane", "pl",
               "płatki gryczane", "płatków gryczanych", "płatki gryczane",
               "płatkami gryczanymi", "płatkach gryczanych"),
            _o("platki-ryzowe", "Płatki ryżowe", "pl",
               "płatki ryżowe", "płatków ryżowych", "płatki ryżowe",
               "płatkami ryżowymi", "płatkach ryżowych"),
            _o("platki-orkiszowe", "Płatki orkiszowe", "pl",
               "płatki orkiszowe", "płatków orkiszowych", "płatki orkiszowe",
               "płatkami orkiszowymi", "płatkach orkiszowych"),
        ],
    },
    # ------------------------------------------------------------ ryż i kasze
    # PDF: Ryż biały = basmati = brązowy = dziki = komosa = kasza gryczana =
    #      jaglana = pęczak = bulgur = ...
    "zboza": {
        "label": "Ryż i kasze",
        "opcje": [
            _o("ryz-basmati", "Ryż basmati", "m",
               "ryż basmati", "ryżu basmati", "ryż basmati",
               "ryżem basmati", "ryżu basmati"),
            _o("ryz-brazowy", "Ryż brązowy", "m",
               "ryż brązowy", "ryżu brązowego", "ryż brązowy",
               "ryżem brązowym", "ryżu brązowym"),
            _o("kasza-jaglana", "Kasza jaglana", "f",
               "kasza jaglana", "kaszy jaglanej", "kaszę jaglaną",
               "kaszą jaglaną", "kaszy jaglanej"),
            _o("kasza-gryczana", "Kasza gryczana", "f",
               "kasza gryczana", "kaszy gryczanej", "kaszę gryczaną",
               "kaszą gryczaną", "kaszy gryczanej"),
            _o("kasza-bulgur", "Kasza bulgur", "f",
               "kasza bulgur", "kaszy bulgur", "kaszę bulgur",
               "kaszą bulgur", "kaszy bulgur"),
            _o("komosa", "Komosa ryżowa", "f",
               "komosa ryżowa", "komosy ryżowej", "komosę ryżową",
               "komosą ryżową", "komosie ryżowej"),
        ],
    },
    # --------------------------------------------------------------- makaron
    "makaron": {
        "label": "Makaron",
        "opcje": [
            _o("makaron-pelnoziarnisty", "Makaron pełnoziarnisty", "m",
               "makaron pełnoziarnisty", "makaronu pełnoziarnistego",
               "makaron pełnoziarnisty", "makaronem pełnoziarnistym",
               "makaronie pełnoziarnistym"),
            _o("makaron-razowy", "Makaron razowy", "m",
               "makaron razowy", "makaronu razowego", "makaron razowy",
               "makaronem razowym", "makaronie razowym"),
            _o("makaron-penne", "Makaron penne", "m",
               "makaron penne", "makaronu penne", "makaron penne",
               "makaronem penne", "makaronie penne"),
            _o("makaron-gryczany", "Makaron gryczany", "m",
               "makaron gryczany", "makaronu gryczanego", "makaron gryczany",
               "makaronem gryczanym", "makaronie gryczanym"),
            _o("makaron-zytni", "Makaron żytni", "m",
               "makaron żytni", "makaronu żytniego", "makaron żytni",
               "makaronem żytnim", "makaronie żytnim"),
            _o("makaron-ryzowy", "Makaron ryżowy", "m",
               "makaron ryżowy", "makaronu ryżowego", "makaron ryżowy",
               "makaronem ryżowym", "makaronie ryżowym"),
            _o("makaron-orkiszowy", "Makaron orkiszowy", "m",
               "makaron orkiszowy", "makaronu orkiszowego", "makaron orkiszowy",
               "makaronem orkiszowym", "makaronie orkiszowym"),
        ],
    },
    # -------------------------------------------------------------- pieczywo
    # PDF: Chleb żytni razowy = na zakwasie = orkiszowy = pełnoziarnisty =
    #      bezglutenowy = bułka owsiana = grahamka = pełnoziarnista
    "pieczywo": {
        "label": "Pieczywo",
        "opcje": [
            _o("chleb-zytni-razowy", "Chleb żytni razowy", "m",
               "chleb żytni razowy", "chleba żytniego razowego",
               "chleb żytni razowy", "chlebem żytnim razowym",
               "chlebie żytnim razowym"),
            _o("chleb-zytni", "Chleb żytni", "m",
               "chleb żytni", "chleba żytniego", "chleb żytni",
               "chlebem żytnim", "chlebie żytnim"),
            _o("chleb-orkiszowy", "Chleb orkiszowy", "m",
               "chleb orkiszowy", "chleba orkiszowego", "chleb orkiszowy",
               "chlebem orkiszowym", "chlebie orkiszowym"),
            _o("chleb-pelnoziarnisty", "Chleb pełnoziarnisty", "m",
               "chleb pełnoziarnisty", "chleba pełnoziarnistego",
               "chleb pełnoziarnisty", "chlebem pełnoziarnistym",
               "chlebie pełnoziarnistym"),
            _o("chleb-na-zakwasie", "Chleb żytni na zakwasie", "m",
               "chleb żytni na zakwasie", "chleba żytniego na zakwasie",
               "chleb żytni na zakwasie", "chlebem żytnim na zakwasie",
               "chlebie żytnim na zakwasie"),
            _o("bulka-grahamka", "Bułka grahamka", "f",
               "bułka grahamka", "bułki grahamki", "bułkę grahamkę",
               "bułką grahamką", "bułce grahamce"),
            _o("bulka-owsiana", "Bułka owsiana", "f",
               "bułka owsiana", "bułki owsianej", "bułkę owsianą",
               "bułką owsianą", "bułce owsianej"),
        ],
    },
    # ---------------------------------------------------------- napoje mleczne
    # PDF: Mleko 2% = bezlaktozowe = napój sojowy = migdałowy = owsiany
    "mleko": {
        "label": "Mleko i napoje roślinne",
        "opcje": [
            _o("mleko-roslinne", "Mleko roślinne", "n",
               "mleko roślinne", "mleka roślinnego", "mleko roślinne",
               "mlekiem roślinnym", "mleku roślinnym"),
            _o("napoj-roslinny", "Napój roślinny", "m",
               "napój roślinny", "napoju roślinnego", "napój roślinny",
               "napojem roślinnym", "napoju roślinnym"),
            _o("napoj-sojowy", "Napój sojowy", "m",
               "napój sojowy", "napoju sojowego", "napój sojowy",
               "napojem sojowym", "napoju sojowym"),
            _o("napoj-migdalowy", "Napój migdałowy", "m",
               "napój migdałowy", "napoju migdałowego", "napój migdałowy",
               "napojem migdałowym", "napoju migdałowym"),
            _o("napoj-owsiany", "Napój owsiany", "m",
               "napój owsiany", "napoju owsianego", "napój owsiany",
               "napojem owsianym", "napoju owsianym"),
            _o("mleko-2", "Mleko 2%", "n",
               "mleko 2%", "mleka 2%", "mleko 2%", "mlekiem 2%", "mleku 2%"),
        ],
    },
    # ------------------------------------------------------- twaróg i zamienniki
    # PDF: Serek wiejski = ser twarogowy chudy = tofu naturalne
    "twarogowe": {
        "label": "Serek wiejski i zamienniki",
        "opcje": [
            _o("serek-wiejski", "Serek wiejski", "m",
               "serek wiejski", "serka wiejskiego", "serek wiejski",
               "serkiem wiejskim", "serku wiejskim"),
            _o("twarog-chudy", "Twaróg chudy", "m",
               "twaróg chudy", "twarogu chudego", "twaróg chudy",
               "twarogiem chudym", "twarogu chudym"),
            _o("tofu-naturalne", "Tofu naturalne", "n",
               "tofu naturalne", "tofu naturalnego", "tofu naturalne",
               "tofu naturalnym", "tofu naturalnym"),
        ],
    },
    # ------------------------------------------------------------- strączkowe
    # PDF: Ciecierzyca = soczewica = fasola = groch = soja
    "straczkowe": {
        "label": "Nasiona roślin strączkowych",
        "opcje": [
            _o("ciecierzyca", "Ciecierzyca", "f",
               "ciecierzyca", "ciecierzycy", "ciecierzycę",
               "ciecierzycą", "ciecierzycy"),
            _o("soczewica", "Soczewica", "f",
               "soczewica", "soczewicy", "soczewicę", "soczewicą", "soczewicy"),
            _o("fasola", "Fasola", "f",
               "fasola", "fasoli", "fasolę", "fasolą", "fasoli"),
            _o("groch", "Groch", "m",
               "groch", "grochu", "groch", "grochem", "grochu"),
            _o("soja", "Soja", "f",
               "soja", "soi", "soję", "soją", "soi"),
        ],
    },
    # ---------------------------------------------------------------- orzechy
    "orzechy": {
        "label": "Orzechy i pestki",
        "opcje": [
            _o("orzechy-wloskie", "Orzechy włoskie", "pl",
               "orzechy włoskie", "orzechów włoskich", "orzechy włoskie",
               "orzechami włoskimi", "orzechach włoskich"),
            _o("orzechy-nerkowca", "Orzechy nerkowca", "pl",
               "orzechy nerkowca", "orzechów nerkowca", "orzechy nerkowca",
               "orzechami nerkowca", "orzechach nerkowca"),
            _o("orzechy-laskowe", "Orzechy laskowe", "pl",
               "orzechy laskowe", "orzechów laskowych", "orzechy laskowe",
               "orzechami laskowymi", "orzechach laskowych"),
            _o("orzechy-pistacjowe", "Orzechy pistacjowe", "pl",
               "orzechy pistacjowe", "orzechów pistacjowych", "orzechy pistacjowe",
               "orzechami pistacjowymi", "orzechach pistacjowych"),
            _o("orzechy-arachidowe", "Orzechy arachidowe", "pl",
               "orzechy arachidowe", "orzechów arachidowych", "orzechy arachidowe",
               "orzechami arachidowymi", "orzechach arachidowych"),
            _o("pestki-dyni", "Pestki dyni", "pl",
               "pestki dyni", "pestek dyni", "pestki dyni",
               "pestkami dyni", "pestkach dyni"),
            _o("pestki-slonecznika", "Pestki słonecznika", "pl",
               "pestki słonecznika", "pestek słonecznika", "pestki słonecznika",
               "pestkami słonecznika", "pestkach słonecznika"),
        ],
    },
    # ----------------------------------------------------- zielone liściaste
    # PDF: Szpinak = rukola = roszponka = sałata rzymska = miks sałat = jarmuż
    "liscizielone": {
        "label": "Zielone warzywa liściaste",
        "opcje": [
            _o("szpinak", "Szpinak", "m",
               "szpinak", "szpinaku", "szpinak", "szpinakiem", "szpinaku"),
            _o("rukola", "Rukola", "f",
               "rukola", "rukoli", "rukolę", "rukolą", "rukoli"),
            _o("roszponka", "Roszponka", "f",
               "roszponka", "roszponki", "roszponkę", "roszponką", "roszponce"),
            _o("jarmuz", "Jarmuż", "m",
               "jarmuż", "jarmużu", "jarmuż", "jarmużem", "jarmużu"),
            _o("salata-rzymska", "Sałata rzymska", "f",
               "sałata rzymska", "sałaty rzymskiej", "sałatę rzymską",
               "sałatą rzymską", "sałacie rzymskiej"),
            _o("miks-salat", "Miks sałat", "m",
               "miks sałat", "miksu sałat", "miks sałat",
               "miksem sałat", "miksie sałat"),
        ],
    },
    # -------------------------------------------------------------- ziemniaki
    # PDF: Ziemniaki = bataty = topinambur
    "ziemniaki": {
        "label": "Ziemniaki",
        "opcje": [
            _o("ziemniaki", "Ziemniaki", "pl",
               "ziemniaki", "ziemniaków", "ziemniaki", "ziemniakami", "ziemniakach"),
            _o("bataty", "Bataty", "pl",
               "bataty", "batatów", "bataty", "batatami", "batatach"),
            _o("topinambur", "Topinambur", "m",
               "topinambur", "topinamburu", "topinambur",
               "topinamburem", "topinamburze"),
        ],
    },
    # ------------------------------------------------------------------ tłuszcz
    # PDF: Oliwa z oliwek = olej rzepakowy = z awokado = kokosowy = masło
    "tluszcz": {
        "label": "Oliwa i oleje",
        "opcje": [
            _o("oliwa", "Oliwa z oliwek", "f",
               "oliwa z oliwek", "oliwy z oliwek", "oliwę z oliwek",
               "oliwą z oliwek", "oliwie z oliwek"),
            _o("olej-rzepakowy", "Olej rzepakowy", "m",
               "olej rzepakowy", "oleju rzepakowego", "olej rzepakowy",
               "olejem rzepakowym", "oleju rzepakowym"),
            _o("olej-kokosowy", "Olej kokosowy", "m",
               "olej kokosowy", "oleju kokosowego", "olej kokosowy",
               "olejem kokosowym", "oleju kokosowym"),
            _o("olej-z-awokado", "Olej z awokado", "m",
               "olej z awokado", "oleju z awokado", "olej z awokado",
               "olejem z awokado", "oleju z awokado"),
        ],
    },
    # -------------------------------------------------------------------- owoce
    # PDF podaje równoważność wagową jednej sztuki — `equiv` trzyma te gramatury,
    # żeby podmiana nie zmieniała wielkości porcji.
    "owoce": {
        "label": "Owoce",
        "opcje": [
            _o("jablko", "Jabłko", "n",
               "jabłko", "jabłka", "jabłko", "jabłkiem", "jabłku",
               Mpl="jabłka", Dpl="jabłek", Bpl="jabłka",
               Npl="jabłkami", Mspl="jabłkach", equiv=170),
            _o("gruszka", "Gruszka", "f",
               "gruszka", "gruszki", "gruszkę", "gruszką", "gruszce",
               Mpl="gruszki", Dpl="gruszek", Bpl="gruszki",
               Npl="gruszkami", Mspl="gruszkach", equiv=170),
            _o("banan", "Banan", "m",
               "banan", "banana", "banan", "bananem", "bananie",
               Bpot="banana",
               Mpl="banany", Dpl="bananów", Bpl="banany",
               Npl="bananami", Mspl="bananach", equiv=120),
            _o("mandarynka", "Mandarynka", "f",
               "mandarynka", "mandarynki", "mandarynkę", "mandarynką", "mandarynce",
               Mpl="mandarynki", Dpl="mandarynek", Bpl="mandarynki",
               Npl="mandarynkami", Mspl="mandarynkach", equiv=65),
            _o("brzoskwinia", "Brzoskwinia", "f",
               "brzoskwinia", "brzoskwini", "brzoskwinię", "brzoskwinią", "brzoskwini",
               Mpl="brzoskwinie", Dpl="brzoskwiń", Bpl="brzoskwinie",
               Npl="brzoskwiniami", Mspl="brzoskwiniach", equiv=90),
            _o("kiwi", "Kiwi", "n",
               "kiwi", "kiwi", "kiwi", "kiwi", "kiwi",
               Mpl="kiwi", Dpl="kiwi", Bpl="kiwi",
               Npl="kiwi", Mspl="kiwi", equiv=80),
            _o("kaki", "Kaki", "n",
               "kaki", "kaki", "kaki", "kaki", "kaki",
               Mpl="kaki", Dpl="kaki", Bpl="kaki",
               Npl="kaki", Mspl="kaki", equiv=250),
        ],
    },

    # ---------------------------------------------------------------- warzywa
    # PDF: Pomidor = ogórek = papryka = cukinia = brokuł = marchew =
    #      rzodkiewka = kapusta = seler naciowy = kalafior = szparagi =
    #      bakłażan = dynia = pieczarki = inne warzywa
    "warzywa": {
        "label": "Warzywa",
        "opcje": [
            _o("pomidor", "Pomidor", "m",
               "pomidor", "pomidora", "pomidor", "pomidorem", "pomidorze",
               Bpot="pomidora",
               Mpl="pomidory", Dpl="pomidorów", Bpl="pomidory",
               Npl="pomidorami", Mspl="pomidorach"),
            _o("ogorek", "Ogórek", "m",
               "ogórek", "ogórka", "ogórek", "ogórkiem", "ogórku",
               Bpot="ogórka",
               Mpl="ogórki", Dpl="ogórków", Bpl="ogórki",
               Npl="ogórkami", Mspl="ogórkach"),
            _o("papryka", "Papryka", "f",
               "papryka", "papryki", "paprykę", "papryką", "papryce",
               Mpl="papryki", Dpl="papryk", Bpl="papryki",
               Npl="paprykami", Mspl="paprykach"),
            _o("cukinia", "Cukinia", "f",
               "cukinia", "cukinii", "cukinię", "cukinią", "cukinii",
               Mpl="cukinie", Dpl="cukinii", Bpl="cukinie",
               Npl="cukiniami", Mspl="cukiniach"),
            _o("brokul", "Brokuł", "m",
               "brokuł", "brokuła", "brokuł", "brokułem", "brokule",
               Bpot="brokuła",
               Mpl="brokuły", Dpl="brokułów", Bpl="brokuły",
               Npl="brokułami", Mspl="brokułach"),
            _o("marchewka", "Marchewka", "f",
               "marchewka", "marchewki", "marchewkę", "marchewką", "marchewce",
               Mpl="marchewki", Dpl="marchewek", Bpl="marchewki",
               Npl="marchewkami", Mspl="marchewkach"),
            _o("marchew", "Marchew", "f",
               "marchew", "marchwi", "marchew", "marchwią", "marchwi",
               Mpl="marchwie", Dpl="marchwi", Bpl="marchwie",
               Npl="marchwiami", Mspl="marchwiach"),
            _o("rzodkiewka", "Rzodkiewka", "f",
               "rzodkiewka", "rzodkiewki", "rzodkiewkę", "rzodkiewką", "rzodkiewce",
               Mpl="rzodkiewki", Dpl="rzodkiewek", Bpl="rzodkiewki",
               Npl="rzodkiewkami", Mspl="rzodkiewkach"),
            _o("seler-naciowy", "Seler naciowy", "m",
               "seler naciowy", "selera naciowego", "seler naciowy",
               "selerem naciowym", "selerze naciowym",
               Mpl="selery naciowe", Dpl="selerów naciowych", Bpl="selery naciowe",
               Npl="selerami naciowymi", Mspl="selerach naciowych"),
            _o("dynia", "Dynia", "f",
               "dynia", "dyni", "dynię", "dynią", "dyni",
               Mpl="dynie", Dpl="dyń", Bpl="dynie",
               Npl="dyniami", Mspl="dyniach"),
            _o("pieczarki", "Pieczarki", "pl",
               "pieczarki", "pieczarek", "pieczarki", "pieczarkami", "pieczarkach",
               Mpl="pieczarki", Dpl="pieczarek", Bpl="pieczarki",
               Npl="pieczarkami", Mspl="pieczarkach"),
            _o("kalafior", "Kalafior", "m",
               "kalafior", "kalafiora", "kalafior", "kalafiorem", "kalafiorze",
               Bpot="kalafiora",
               Mpl="kalafiory", Dpl="kalafiorów", Bpl="kalafiory",
               Npl="kalafiorami", Mspl="kalafiorach"),
            _o("baklazan", "Bakłażan", "m",
               "bakłażan", "bakłażana", "bakłażan", "bakłażanem", "bakłażanie",
               Bpot="bakłażana",
               Mpl="bakłażany", Dpl="bakłażanów", Bpl="bakłażany",
               Npl="bakłażanami", Mspl="bakłażanach"),
        ],
    },
    # -------------------------------------------------------------- słodziki
    # PDF: Miód = syrop klonowy = syrop z agawy
    "slodziki": {
        "label": "Miód i syropy",
        "opcje": [
            _o("miod", "Miód", "m",
               "miód", "miodu", "miód", "miodem", "miodzie"),
            _o("syrop-klonowy", "Syrop klonowy", "m",
               "syrop klonowy", "syropu klonowego", "syrop klonowy",
               "syropem klonowym", "syropie klonowym"),
            _o("syrop-z-agawy", "Syrop z agawy", "m",
               "syrop z agawy", "syropu z agawy", "syrop z agawy",
               "syropem z agawy", "syropie z agawy"),
        ],
    },
    # ----------------------------------------------------------- pasty do pieczywa
    # PDF: Hummus = pasty warzywne
    "pasty": {
        "label": "Hummus i pasty warzywne",
        "opcje": [
            _o("hummus", "Hummus", "m",
               "hummus", "hummusu", "hummus", "hummusem", "hummusie"),
            _o("pasta-warzywna", "Pasta warzywna", "f",
               "pasta warzywna", "pasty warzywnej", "pastę warzywną",
               "pastą warzywną", "paście warzywnej"),
        ],
    },
}

# Warianty, których nie wolno rozpoznawać w pewnym sąsiedztwie — „papryka
# słodka” i „papryka wędzona” to przyprawy, nie warzywo.
WETO = {
    "papryka": [r"\s+(wędzon\w+|słodk\w+)", r"(wędzon\w+|słodk\w+)\s+$"],
}

# Który wariant odpowiada danemu składnikowi w przepisie i w jakim przypadku
# zapisana jest jego nazwa na liście składników.
SKLADNIK_DO_WARIANTU = {
    "płatków owsianych":            ("platki", "platki-owsiane", "D"),
    "płatków owsianych górskich":   ("platki", "platki-owsiane", "D"),
    "płatków jaglanych":            ("platki", "platki-jaglane", "D"),
    "ryżu basmati":                 ("zboza", "ryz-basmati", "D"),
    "kaszy gryczanej":              ("zboza", "kasza-gryczana", "D"),
    "kaszy jaglanej":               ("zboza", "kasza-jaglana", "D"),
    "makaronu pełnoziarnistego":    ("makaron", "makaron-pelnoziarnisty", "D"),
    "makaronu razowego":            ("makaron", "makaron-razowy", "D"),
    "makaronu penne":               ("makaron", "makaron-penne", "D"),
    "makaronu spaghetti pełnoziarnistego": ("makaron", "makaron-pelnoziarnisty", "D"),
    "chleba żytniego razowego":     ("pieczywo", "chleb-zytni-razowy", "D"),
    "chleba żytniego":              ("pieczywo", "chleb-zytni", "D"),
    "chleba tostowego pełnoziarnistego": ("pieczywo", "chleb-pelnoziarnisty", "D"),
    "bułki grahamki":               ("pieczywo", "bulka-grahamka", "D"),
    "bułki":                        ("pieczywo", "bulka-grahamka", "D"),
    "mleka roślinnego":             ("mleko", "mleko-roslinne", "D"),
    "napoju roślinnego":            ("mleko", "napoj-roslinny", "D"),
    "napoju sojowego":              ("mleko", "napoj-sojowy", "D"),
    "serka wiejskiego":             ("twarogowe", "serek-wiejski", "D"),
    "twarogu chudego":              ("twarogowe", "twarog-chudy", "D"),
    "tofu naturalnego":             ("twarogowe", "tofu-naturalne", "D"),
    "ciecierzycy konserwowej":      ("straczkowe", "ciecierzyca", "D"),
    "soczewicy czerwonej":          ("straczkowe", "soczewica", "D"),
    "orzechów włoskich":            ("orzechy", "orzechy-wloskie", "D"),
    "posiekanych orzechów włoskich": ("orzechy", "orzechy-wloskie", "D"),
    "orzechów nerkowca":            ("orzechy", "orzechy-nerkowca", "D"),
    "szpinaku":                     ("liscizielone", "szpinak", "D"),
    "rukoli":                       ("liscizielone", "rukola", "D"),
    "roszponki":                    ("liscizielone", "roszponka", "D"),
    "miksu sałat":                  ("liscizielone", "miks-salat", "D"),
    "ziemniaków":                   ("ziemniaki", "ziemniaki", "D"),
    "oliwy z oliwek":               ("tluszcz", "oliwa", "D"),
    "oliwy":                        ("tluszcz", "oliwa", "D"),
    "oleju rzepakowego":            ("tluszcz", "olej-rzepakowy", "D"),
    "jabłka":                       ("owoce", "jablko", "D"),
    "małego jabłka":                ("owoce", "jablko", "D"),
    "gruszki":                      ("owoce", "gruszka", "D"),
    "banana":                       ("owoce", "banan", "D"),
    "małego banana":                ("owoce", "banan", "D"),
    "mandarynki":                   ("owoce", "mandarynka", "D"),
    "kaki":                         ("owoce", "kaki", "D"),
    "pomidora":                     ("warzywa", "pomidor", "D"),
    "pomidor":                      ("warzywa", "pomidor", "M"),
    "pomidorków":                   ("warzywa", "pomidor", "Dpl"),
    "pomidorków koktajlowych":      ("warzywa", "pomidor", "Dpl"),
    "ogórka":                       ("warzywa", "ogorek", "D"),
    "ogórka zielonego":             ("warzywa", "ogorek", "D"),
    "małego ogórka":                ("warzywa", "ogorek", "D"),
    "papryki czerwonej":            ("warzywa", "papryka", "D"),
    "papryki żółtej":               ("warzywa", "papryka", "D"),
    "brokuła":                      ("warzywa", "brokul", "D"),
    "marchewki":                    ("warzywa", "marchewka", "D"),
    "marchwi":                      ("warzywa", "marchew", "D"),
    "rzodkiewki":                   ("warzywa", "rzodkiewka", "D"),
    "rzodkiewek":                   ("warzywa", "rzodkiewka", "Dpl"),
    "selera naciowego":             ("warzywa", "seler-naciowy", "D"),
    "dyni":                         ("warzywa", "dynia", "D"),
    "pieczarek":                    ("warzywa", "pieczarki", "D"),
    "miodu":                        ("slodziki", "miod", "D"),
    "syropu z agawy":               ("slodziki", "syrop-z-agawy", "D"),
    "hummusu spicy salsa":          ("pasty", "hummus", "D"),
    "pasty warzywnej":              ("pasty", "pasta-warzywna", "D"),
}
