# -*- coding: utf-8 -*-
"""Przypisanie składników do działów sklepowych.

Lista zakupów posortowana alfabetycznie zmusza do biegania po sklepie w tę
i z powrotem. Tutaj każdy składnik dostaje dział, a działy idą w kolejności
typowego obchodu sklepu (układ zbliżony do Lidla): najpierw warzywa i owoce
przy wejściu, potem pieczywo, chłodnia, mrożonki, dalej alejki suche,
konserwy, sosy i przyprawy, na końcu bakalie, słodycze i napoje.

Źródłem prawdy jest `tagi.py`: składnik ma już kategorię wyszukiwarki
(„mozzarella”, „platki-owsiane”), więc dział wystarczy przypisać kategorii,
a nie każdej odmianie nazwy z osobna. Pozycje spiżarniowe (sól, pieprz,
świeże zioła) kategorii nie mają — dla nich jest osobny zestaw wzorców.

Kompletność pilnuje `sprawdz_pokrycie()`, wywoływane przy budowaniu strony:
każdy identyfikator z `tagi.REGULY` musi tu mieć swój dział.
"""
import re

try:
    from . import tagi
except ImportError:  # uruchamiane jako zwykły skrypt
    import tagi


# Kolejność ma znaczenie — to jest trasa przez sklep, nie alfabet.
DZIALY = [
    ("warzywa",  "Warzywa i owoce"),
    ("pieczywo", "Pieczywo"),
    ("nabial",   "Nabiał i jaja"),
    ("chlodnia", "Wędliny i produkty roślinne"),
    ("mrozone",  "Ryby i mrożonki"),
    ("sypkie",   "Makarony, ryże, kasze i mąki"),
    ("konserwy", "Konserwy i strączki"),
    ("sosy",     "Sosy, oleje i przyprawy"),
    ("bakalie",  "Orzechy, bakalie i słodycze"),
    ("napoje",   "Napoje i produkty gotowe"),
    ("inne",     "Pozostałe"),
]

ETYKIETY = dict(DZIALY)
KOLEJNOSC = {d: n for n, (d, _) in enumerate(DZIALY)}


# --- kategoria wyszukiwarki -> dział ---------------------------------------
PO_TAGU = {
    # warzywa i owoce (świeże)
    "ananas": "warzywa", "awokado": "warzywa", "baklazan": "warzywa",
    "banan": "warzywa", "batat": "warzywa", "borowki": "warzywa",
    "brokul": "warzywa", "burak": "warzywa", "cebula": "warzywa",
    "cukinia": "warzywa", "cytryna": "warzywa", "czosnek": "warzywa",
    "dynia": "warzywa", "grejpfrut": "warzywa", "gruszka": "warzywa",
    "imbir": "warzywa", "jablko": "warzywa", "jagody": "warzywa",
    "kaki": "warzywa", "kalafior": "warzywa", "kapusta": "warzywa",
    "kielki": "warzywa", "kiwi": "warzywa", "limonka": "warzywa",
    "maliny": "warzywa", "mandarynka": "warzywa", "mango": "warzywa",
    "marchewka": "warzywa", "melon": "warzywa", "ogorek": "warzywa",
    "papryczka-chili": "warzywa", "papryka": "warzywa",
    "pieczarki": "warzywa", "pietruszka-korzen": "warzywa",
    "pomarancza": "warzywa", "pomidor": "warzywa", "por": "warzywa",
    "porzeczki": "warzywa", "rzodkiewka": "warzywa", "salata": "warzywa",
    "seler": "warzywa", "szpinak": "warzywa", "truskawki": "warzywa",
    "wisnie": "warzywa", "ziemniaki": "warzywa",

    # pieczywo
    "bagietka": "pieczywo", "bajgiel": "pieczywo", "bulka": "pieczywo",
    "bulka-tarta": "pieczywo", "chleb": "pieczywo", "tortilla": "pieczywo",
    "wafle": "pieczywo",

    # nabiał i jaja
    "camembert": "nabial", "cheddar": "nabial", "feta": "nabial",
    "gouda": "nabial", "grana-padano": "nabial", "halloumi": "nabial",
    "jajka": "nabial", "jogurt": "nabial", "maslanka": "nabial",
    "maslo": "nabial", "mleko": "nabial", "mozzarella": "nabial",
    "ser-plesniowy": "nabial", "ser-zolty": "nabial",
    "serek-proteinowy": "nabial", "serek-smietankowy": "nabial",
    "serek-wiejski": "nabial", "smietanka": "nabial", "twarog": "nabial",

    # chłodnia: wędliny roślinne, tofu, gotowe pasty
    "gyoza": "chlodnia", "hummus": "chlodnia", "kabanosy": "chlodnia",
    "kaszanka": "chlodnia", "kielbaski": "chlodnia",
    "mieso-wegan": "chlodnia", "parowki": "chlodnia",
    "pasta-warzywna": "chlodnia", "plastry-wegan": "chlodnia",
    "tofu": "chlodnia",

    # ryby i mrożonki
    "dorsz": "mrozone", "losos": "mrozone", "makrela": "mrozone",
    "mintaj": "mrozone", "owoce-mrozone": "mrozone", "pstrag": "mrozone",

    # produkty sypkie i śniadaniowe
    "chia": "sypkie", "ciasto-nalesniki": "sypkie", "kasza": "sypkie",
    "komosa": "sypkie", "kuskus": "sypkie", "maka": "sypkie",
    "makaron": "sypkie", "odzywka": "sypkie", "papier-ryzowy": "sypkie",
    "platki-drozdzowe": "sypkie", "platki-inne": "sypkie",
    "platki-jaglane": "sypkie", "platki-owsiane": "sypkie",
    "ryz": "sypkie", "siemie-lniane": "sypkie",

    # konserwy i strączki
    "bob": "konserwy", "ciecierzyca": "konserwy", "fasola": "konserwy",
    "groch": "konserwy", "groszek": "konserwy", "kukurydza": "konserwy",
    "mleczko-kokosowe": "konserwy", "ogorki-kiszone": "konserwy",
    "oliwki": "konserwy", "papryka-konserwowa": "konserwy",
    "pomidory-puszka": "konserwy", "pomidory-suszone": "konserwy",
    "soczewica": "konserwy",

    # sosy, oleje, przyprawy
    "chrzan": "sosy", "ketchup": "sosy", "majonez": "sosy", "miso": "sosy",
    "musztarda": "sosy", "olej-kokosowy": "sosy", "olej-sezamowy": "sosy",
    "oliwa": "sosy", "pesto": "sosy", "sos-ostry": "sosy",
    "sos-sojowy": "sosy", "tahini": "sosy",

    # orzechy, bakalie, słodycze
    "baton": "bakalie", "biszkopty": "bakalie", "budyn": "bakalie",
    "czekolada": "bakalie", "daktyle": "bakalie", "dzem": "bakalie",
    "kakao": "bakalie", "maslo-orzechowe": "bakalie", "migdaly": "bakalie",
    "miod": "bakalie", "orzechy": "bakalie", "pestki-dyni": "bakalie",
    "pistacje": "bakalie", "sezam": "bakalie", "slonecznik": "bakalie",
    "syrop-agawa": "bakalie", "syrop-klonowy": "bakalie",
    "wiorki": "bakalie", "zurawina": "bakalie",

    # napoje i produkty gotowe
    "kawa": "napoje", "owsianka-instant": "napoje", "pudding": "napoje",
    "smoothie": "napoje", "sok": "napoje", "zupa-gotowa": "napoje",
}


# --- spiżarnia (składniki bez kategorii) -----------------------------------
# Kolejność ma znaczenie: „bazylia świeża” musi wyprzedzić „bazylia”,
# inaczej pęczek zieleniny trafiłby na półkę z suszonymi ziołami.
REGULY_SPIZ = [
    # świeże zioła — leżą przy warzywach, nie w alejce z przyprawami
    (r"szczypior", "warzywa"),
    (r"natk\w* (pietruszki|piertuszki)|natka pietruszki", "warzywa"),
    (r"\bkoper|kopereku|koperk", "warzywa"),
    (r"\bmiet", "warzywa"),
    (r"swiez\w* (bazyli|kolendr|koperk|tymianku)", "warzywa"),
    (r"(bazyli|kolendr|koperk|tymianek|tymianku)\w* swiez", "warzywa"),

    # pieczenie — obok mąki
    (r"proszek do pieczenia|proszku do pieczenia", "sypkie"),
    (r"sody oczyszczonej|soda oczyszczona", "sypkie"),
    (r"drozdz", "sypkie"),

    # słodziki — obok cukru i bakalii
    (r"ksylitol|erytrol", "bakalie"),

    # gotowa przekąska, którą `tagi.py` łapie jako cynamon — na liście zakupów
    # to jednak produkt z półki ze słodyczami, a nie przyprawa
    (r"przekaski na 2 sniadanie", "bakalie"),

    # napoje (nazwy są już bez znaków diakrytycznych: „wodę” -> „wode”)
    (r"\bwod[aey]\b|\blod[u]?\b", "napoje"),

    # reszta spiżarni to przyprawy, ocet i bulion
    (r"\bocet\b|\boctu\b", "sosy"),
    (r"bulion", "sosy"),
]

_SPIZ = [(re.compile(p), d) for p, d in REGULY_SPIZ]


def dzial(nazwa, tag=None, pantry=False):
    """Identyfikator działu dla składnika.

    `tag` to kategoria z `tagi.tag()`; jeśli jej nie ma (pozycja spiżarniowa),
    decydują wzorce nazwy. Domyślnie przyprawy — spiżarnia to w tych planach
    prawie wyłącznie sól, pieprz i zioła.
    """
    if tag and tag in PO_TAGU:
        return PO_TAGU[tag]
    n = tagi.norm(nazwa or "")
    for p, d in _SPIZ:
        if p.search(n):
            return d
    if pantry:
        return "sosy"
    # Nieznana nazwa bez kategorii — spróbujmy jeszcze raz przez tagi.
    t = tagi.tag(nazwa or "")
    if t and t[0] in PO_TAGU:
        return PO_TAGU[t[0]]
    return "inne"


def sprawdz_pokrycie():
    """Lista identyfikatorów z `tagi.REGULY` bez przypisanego działu."""
    return sorted({i for _, i, _ in tagi.REGULY if i not in PO_TAGU})
