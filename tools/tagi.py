# -*- coding: utf-8 -*-
"""Przypisanie nazw składników do kategorii wyszukiwarki.

Nazwy w planach zapisane są różnie („Papryka czerwona”, „papryki zielonej”,
„małego pomidora”), więc dopasowujemy je wzorcami do nazwy pozbawionej
znaków diakrytycznych. Wygrywa pierwsza pasująca reguła, dlatego kolejność
ma znaczenie: nazwy handlowe i złożenia stoją nad kategoriami ogólnymi —
inaczej „Roślinna kaszanka” trafiłaby do kaszy, a „masło orzechowe”
do masła.

SPIZARNIA to pozycje, które nie trafiają do listy wyboru składników
(nikt nie szuka przepisu „na sól”) i na liście zakupów lądują osobno.
"""
import re
import unicodedata


def norm(s):
    s = s.lower()
    s = "".join(c for c in unicodedata.normalize("NFD", s)
                if unicodedata.category(c) != "Mn")
    return s.replace("ł", "l")


SPIZARNIA = [
    r"\bsol\b", r"\bsoli\b", r"kala namak", r"pieprz",
    r"cynamon", r"kumin", r"\bkmink", r"\bkminek", r"kurkum", r"\bcurry\b",
    r"oregano", r"bazyli", r"tymian", r"rozmaryn", r"majeran",
    r"lisc laurow", r"liscia laurow", r"lisci laurow",
    r"ziele angielsk", r"ziela angielsk", r"galka muszkat", r"galki muszkat",
    r"kardamon", r"czarnuszk", r"platk\w* chilli", r"platk\w* chili",
    r"papryka slodka", r"papryki slodkiej", r"slodkiej papryki",
    r"papryka wedzona", r"papryki wedzonej",
    r"kolendr", r"koper", r"szczypiorek", r"szczypiorku",
    r"natki pietruszki", r"natka pietruszki", r"natki piertuszki",
    r"\bmiet", r"wanili", r"proszek do pieczenia", r"proszku do pieczenia",
    r"sody oczyszczonej", r"drozdz(?!owych|owe)", r"\bwoda\b", r"\bwody\b",
    r"\blodu\b", r"bulion", r"ksylitol", r"erytrol", r"\bocet\b", r"\boctu\b",
    r"czosnku granulowanego", r"czosnek granulowany",
]

# Nazwy handlowe, w których słowo-przyprawa jest tylko częścią nazwy produktu
# („Zupy krem z pomidorów z bazylią Chef select” to danie, nie bazylia).
NIE_SPIZARNIA = [
    r"chef select", r"dobra kaloria", r"go active", r"go vege", r"solevita",
    r"crownfield", r"tarczynski", r"valio", r"vitanella", r"alesto",
    r"fruvit", r"pudding", r"baton", r"protein bar", r"zupy krem",
    r"smoothie", r"serek", r"jogurt", r"platki", r"owsiank", r"ciasto do",
]

# (wzorzec, id kategorii, etykieta)
REGULY = [
    # --- produkty z nazwy własnej
    (r"baton|protein bar|przekaski na 2 sniadanie", "baton", "Baton / przekąska"),
    (r"pudding proteinowy", "pudding", "Pudding proteinowy"),
    (r"smoothie|fruvit", "smoothie", "Smoothie / sok"),
    (r"zupy krem", "zupa-gotowa", "Zupa gotowa"),
    (r"owsianki malinowej|owsianka malinowa", "owsianka-instant", "Owsianka instant"),
    (r"gyoza", "gyoza", "Pierożki gyoza"),
    (r"kaszank", "kaszanka", "Kaszanka roślinna"),
    (r"kabanos", "kabanosy", "Kabanosy roślinne"),
    (r"parowek|parowki", "parowki", "Parówki roślinne"),
    (r"kielbask", "kielbaski", "Kiełbaski roślinne"),
    (r"plastry wegansk", "plastry-wegan", "Plastry wegańskie"),
    (r"mieso wegansk", "mieso-wegan", "Mięso wegańskie"),
    (r"wafli ryzowych|wafle ryzowe", "wafle", "Wafle ryżowe"),
    (r"odzywk", "odzywka", "Odżywka białkowa"),
    (r"ciasto do nalesnikow", "ciasto-nalesniki", "Ciasto na naleśniki"),
    (r"serek proteinowy|serka proteinowego", "serek-proteinowy", "Serek proteinowy"),
    (r"platkow drozdzowych|platki drozdzowe", "platki-drozdzowe", "Płatki drożdżowe"),
    (r"napar z kawy", "kawa", "Kawa"),
    (r"sok jablkowy", "sok", "Sok"),

    # --- złożenia, które muszą wyprzedzić składnik prostszy
    (r"maslo orzechowe|masla orzechowego", "maslo-orzechowe", "Masło orzechowe"),
    (r"mleczk\w* kokosow", "mleczko-kokosowe", "Mleczko kokosowe"),
    (r"olej\w* kokosow", "olej-kokosowy", "Olej kokosowy"),
    (r"olej\w* sezamow", "olej-sezamowy", "Olej sezamowy"),
    (r"oliw\w* z oliwek|\boliwy\b|\boliwa\b|\bolej|\boleju\b", "oliwa", "Oliwa / olej"),
    (r"pomidor\w* suszon|suszonych pomidorow|pomidora suszonego",
     "pomidory-suszone", "Pomidory suszone"),
    (r"pomidor\w* (z puszki|w puszce|konserwow|krojonych)|passat"
     r"|przecieru pomidorowego|koncentratu pomidorowego",
     "pomidory-puszka", "Pomidory z puszki / passata"),
    (r"ogork\w* (kiszon|konserwow)|ogorka kiszonego|kiszonego ogorka|soku z ogorkow",
     "ogorki-kiszone", "Ogórki kiszone"),
    (r"kielk", "kielki", "Kiełki"),
    (r"platk\w* owsian", "platki-owsiane", "Płatki owsiane"),
    (r"platk\w* jaglan", "platki-jaglane", "Płatki jaglane"),
    (r"platk\w* migdal", "migdaly", "Migdały"),
    (r"platk\w* (ryzow|zytni|lion)|ryz preparowany", "platki-inne", "Płatki inne"),
    (r"bulki tartej", "bulka-tarta", "Bułka tarta"),
    (r"mak\w* (pszenn|orkiszow|zytni|jaglan|ziemniaczan|z ciecierzycy|owsian)"
     r"|\bmaki\b|\bmaka\b", "maka", "Mąka"),
    (r"pietruszka korzen|korzenia pietruszki|pietruszki korzen|\bpietruszki\b",
     "pietruszka-korzen", "Pietruszka korzeń"),

    # --- zboża i pieczywo
    (r"makaron|lazank", "makaron", "Makaron"),
    (r"kuskus", "kuskus", "Kasza kuskus"),
    (r"komosa|komosy", "komosa", "Komosa ryżowa"),
    (r"kasz", "kasza", "Kasza"),
    (r"\bryz\b|\bryzu\b", "ryz", "Ryż"),
    (r"bajgiel|bajgla", "bajgiel", "Bajgiel"),
    (r"tortill|tortili", "tortilla", "Tortilla"),
    (r"bulk", "bulka", "Bułka"),
    (r"bagietk", "bagietka", "Bagietka"),
    (r"chleb|pieczyw|grahamk", "chleb", "Chleb"),
    (r"papieru ryzowego", "papier-ryzowy", "Papier ryżowy"),
    (r"biszkopt", "biszkopty", "Biszkopty"),

    # --- owoce
    (r"banan", "banan", "Banan"),
    (r"jablk|jablek", "jablko", "Jabłko"),
    (r"grusz", "gruszka", "Gruszka"),
    (r"pomarancz", "pomarancza", "Pomarańcza"),
    (r"mandaryn", "mandarynka", "Mandarynka"),
    (r"grejpfrut", "grejpfrut", "Grejpfrut"),
    (r"\bkiwi\b", "kiwi", "Kiwi"),
    (r"mango", "mango", "Mango"),
    (r"ananas", "ananas", "Ananas"),
    (r"melon", "melon", "Melon"),
    (r"\bkaki\b", "kaki", "Kaki"),
    (r"truskaw", "truskawki", "Truskawki"),
    (r"malin", "maliny", "Maliny"),
    (r"borow", "borowki", "Borówki"),
    (r"\bjagod", "jagody", "Jagody"),
    (r"wisni", "wisnie", "Wiśnie"),
    (r"porzecz", "porzeczki", "Porzeczki"),
    (r"zurawin", "zurawina", "Żurawina"),
    (r"daktyl", "daktyle", "Daktyle"),
    (r"cytryn", "cytryna", "Cytryna"),
    (r"limonk", "limonka", "Limonka"),
    (r"swiezych lub mrozonych owocow", "owoce-mrozone", "Owoce mrożone"),

    # --- warzywa
    (r"pomidor", "pomidor", "Pomidor"),
    (r"ogor", "ogorek", "Ogórek"),
    (r"papryczk|papryki ostrej", "papryczka-chili", "Papryczka chili"),
    (r"papryki konserwowej|papryki pieczona", "papryka-konserwowa", "Papryka konserwowa"),
    (r"papryk", "papryka", "Papryka"),
    (r"\bpor\b|\bpora\b", "por", "Por"),
    (r"cebul", "cebula", "Cebula"),
    (r"czosnek|czosnku", "czosnek", "Czosnek"),
    (r"marchew|marchwi", "marchewka", "Marchewka"),
    (r"seler", "seler", "Seler"),
    (r"burak|buraczk", "burak", "Burak"),
    (r"ziemniak", "ziemniaki", "Ziemniaki"),
    (r"batat", "batat", "Batat"),
    (r"dyni", "dynia", "Dynia"),
    (r"cukini", "cukinia", "Cukinia"),
    (r"baklazan", "baklazan", "Bakłażan"),
    (r"brokul", "brokul", "Brokuł"),
    (r"kalafior", "kalafior", "Kalafior"),
    (r"kapust", "kapusta", "Kapusta"),
    (r"szpinak", "szpinak", "Szpinak"),
    (r"jarmuz|rukol|roszpon|miks salat|mix salat|mieszanych salat|salat",
     "salata", "Sałata / rukola / roszponka"),
    (r"rzodkiew", "rzodkiewka", "Rzodkiewka"),
    (r"groszek|groszku", "groszek", "Groszek"),
    (r"kukurydz", "kukurydza", "Kukurydza"),
    (r"oliwk|oliwek", "oliwki", "Oliwki"),
    (r"awokado", "awokado", "Awokado"),
    (r"pieczar|boczniak", "pieczarki", "Pieczarki"),
    (r"imbir", "imbir", "Imbir"),
    (r"chrzan", "chrzan", "Chrzan"),

    # --- białko roślinne
    (r"\btofu", "tofu", "Tofu"),
    (r"ciecierzyc", "ciecierzyca", "Ciecierzyca"),
    (r"soczewic", "soczewica", "Soczewica"),
    (r"fasol", "fasola", "Fasola"),
    (r"\bbobu\b|\bbob\b", "bob", "Bób"),
    (r"groch", "groch", "Groch"),

    # --- nabiał i sery
    (r"mozzarell", "mozzarella", "Mozzarella"),
    (r"\bfeta\b|typu feta|sera feta", "feta", "Feta"),
    (r"gouda", "gouda", "Gouda"),
    (r"cheddar", "cheddar", "Cheddar"),
    (r"halloumi", "halloumi", "Halloumi"),
    (r"camembert", "camembert", "Camembert"),
    (r"niebiesk\w* plesni|lazur", "ser-plesniowy", "Ser pleśniowy"),
    (r"grana padano", "grana-padano", "Grana padano"),
    (r"sera zoltego|ser zolty|sera salatkowego", "ser-zolty", "Ser żółty"),
    (r"serek wiejski|serka wiejskiego", "serek-wiejski", "Serek wiejski"),
    (r"serek smietankowy|serka smietankowego|serka kanapkowego|twarozk",
     "serek-smietankowy", "Serek śmietankowy"),
    (r"twarog", "twarog", "Twaróg"),
    (r"maslank", "maslanka", "Maślanka"),
    (r"smietan", "smietanka", "Śmietanka"),
    (r"jogurt", "jogurt", "Jogurt / skyr"),
    (r"mleko roslinne|mleka roslinnego|napoj\w* (roslinn|sojow|migdalow|owsian)"
     r"|mleko 2", "mleko", "Mleko roślinne"),
    (r"\bmaslo extra\b|\bmasla\b|margaryn", "maslo", "Masło / margaryna"),

    # --- ryby
    (r"losos", "losos", "Łosoś"),
    (r"dorsz", "dorsz", "Dorsz"),
    (r"mintaj", "mintaj", "Mintaj"),
    (r"pstrag", "pstrag", "Pstrąg"),
    (r"makrel", "makrela", "Makrela"),

    # --- orzechy i nasiona
    (r"migdal", "migdaly", "Migdały"),
    (r"pistacj", "pistacje", "Pistacje"),
    (r"orzech|orzeszk|nerkowc", "orzechy", "Orzechy"),
    (r"slonecznik", "slonecznik", "Słonecznik"),
    (r"pestek dyni|pestki dyni", "pestki-dyni", "Pestki dyni"),
    (r"sezam", "sezam", "Sezam"),
    (r"\bchia\b", "chia", "Nasiona chia"),
    (r"siemien|siemie", "siemie-lniane", "Siemię lniane"),
    (r"wiork\w* kokosow|wiorek kokosowych", "wiorki", "Wiórki kokosowe"),

    # --- pasty, sosy, dodatki
    (r"tahini", "tahini", "Tahini"),
    (r"hummus", "hummus", "Hummus"),
    (r"pasty warzywnej|pasta warzywna", "pasta-warzywna", "Pasta warzywna"),
    (r"pasty miso", "miso", "Miso"),
    (r"pesto", "pesto", "Pesto"),
    (r"majonez", "majonez", "Majonez"),
    (r"musztard", "musztarda", "Musztarda"),
    (r"ketchup", "ketchup", "Ketchup"),
    (r"sos\w* sojow|sosu sojowego", "sos-sojowy", "Sos sojowy"),
    (r"sriracha|sosu rybnego", "sos-ostry", "Sos ostry / rybny"),

    # --- słodkie
    (r"\bmiod|miodu", "miod", "Miód"),
    (r"syrop\w* klonow", "syrop-klonowy", "Syrop klonowy"),
    (r"syrop\w* z agawy", "syrop-agawa", "Syrop z agawy"),
    (r"dzem", "dzem", "Dżem"),
    (r"czekolad", "czekolada", "Czekolada"),
    (r"kakao", "kakao", "Kakao"),
    (r"budyn", "budyn", "Budyń"),

    # --- jajka na końcu, żeby „jajecznica” nie zjadła reguły
    (r"\bjaj", "jajka", "Jajka"),
]

_SPIZ = [re.compile(p) for p in SPIZARNIA]
_NIE_SPIZ = [re.compile(p) for p in NIE_SPIZARNIA]
_REG = [(re.compile(p), i, l) for p, i, l in REGULY]


def spizarnia(nazwa):
    n = norm(nazwa)
    if any(p.search(n) for p in _NIE_SPIZ):
        return False
    return any(p.search(n) for p in _SPIZ)


def tag(nazwa):
    """(id kategorii, etykieta) albo None, jeśli nic nie pasuje."""
    n = norm(nazwa)
    for p, i, l in _REG:
        if p.search(n):
            return i, l
    return None
