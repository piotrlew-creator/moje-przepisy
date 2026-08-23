---
hide:
  - toc
---

<a class="p-back" href="../../">&larr; Wszystkie przepisy</a>

# Mozzarella, pomidor, grahamka i orzechy

<div class="p-hero" data-slot="1">
<div class="p-hero__top">
<span>Śniadanie</span><span class="p-num">7:00-10:00</span>
</div>
<div class="p-macros">
<div class="p-macro"><span class="p-macro__v">469</span><span class="p-macro__l">kcal</span></div>
<div class="p-macro"><span class="p-macro__v">22 g</span><span class="p-macro__l">białko</span></div>
<div class="p-macro"><span class="p-macro__v">51 g</span><span class="p-macro__l">węgl.</span></div>
<div class="p-macro"><span class="p-macro__v">19 g</span><span class="p-macro__l">tłuszcz</span></div>
</div>
<p style="margin:0;font-size:.66rem;color:var(--p-ink-3);font-weight:600">Wartości dla jednej porcji, tak jak w planie diety.</p>
</div>

<div class="p-servings">
<span class="p-eyebrow">Dla ilu osób gotujesz?</span>
<div class="p-stepper">
<button type="button" class="p-stepper__btn" id="srv-minus" aria-label="Mniej osób">&minus;</button>
<span class="p-stepper__value"><span class="p-stepper__num" id="srv-num" aria-live="polite">1</span><span class="p-stepper__word" id="srv-word">osoba</span></span>
<button type="button" class="p-stepper__btn" id="srv-plus" aria-label="Więcej osób">+</button>
</div>
<p class="p-note" id="srv-note" style="margin:0" hidden></p>
</div>

<div class="p-ings__head">
<h2 id="ing-heading" style="margin:0">Składniki na 1 osobę</h2>
<button type="button" class="p-btn p-btn--ghost" id="swap-reset" style="min-height:auto;padding:6px 8px" hidden>Przywróć oryginał</button>
</div>
<ul class="p-ings" id="ing-list">
<li><div class="p-ing__row"><span class="p-ing__q">1 sztuka</span><span class="p-ing__n">bułki grahamki</span><span class="p-ing__g">80 g</span></div>
<div class="p-ing__swap">
<label class="p-swaplabel" for="swap-0">Zamień na</label>
<select class="p-select" id="swap-0" data-ing="0">
<option value="chleb-zytni-razowy">Chleb żytni razowy</option>
<option value="chleb-zytni">Chleb żytni</option>
<option value="chleb-orkiszowy">Chleb orkiszowy</option>
<option value="chleb-pelnoziarnisty">Chleb pełnoziarnisty</option>
<option value="chleb-na-zakwasie">Chleb żytni na zakwasie</option>
<option value="bulka-grahamka" selected>Bułka grahamka · oryginał</option>
<option value="bulka-owsiana">Bułka owsiana</option>
</select>
</div>
</li>
<li><div class="p-ing__row"><span class="p-ing__q">0.5 plastra</span><span class="p-ing__n">sera mozzarella</span><span class="p-ing__g">60 g</span></div>
</li>
<li><div class="p-ing__row"><span class="p-ing__q">3 sztuki</span><span class="p-ing__n">orzechów włoskich</span><span class="p-ing__g">12 g</span></div>
<div class="p-ing__swap">
<label class="p-swaplabel" for="swap-2">Zamień na</label>
<select class="p-select" id="swap-2" data-ing="2">
<option value="orzechy-wloskie" selected>Orzechy włoskie · oryginał</option>
<option value="orzechy-nerkowca">Orzechy nerkowca</option>
<option value="orzechy-laskowe">Orzechy laskowe</option>
<option value="orzechy-pistacjowe">Orzechy pistacjowe</option>
<option value="orzechy-arachidowe">Orzechy arachidowe</option>
<option value="pestki-dyni">Pestki dyni</option>
<option value="pestki-slonecznika">Pestki słonecznika</option>
</select>
</div>
</li>
<li><div class="p-ing__row"><span class="p-ing__q">1 sztuka</span><span class="p-ing__n">małego pomidora</span><span class="p-ing__g">60 g</span></div>
</li>
</ul>

<div class="p-actions">
<button type="button" class="p-btn p-btn--block" id="open-shopping">&#128722; Lista zakupów</button>
<button type="button" class="p-btn p-btn--primary p-btn--block" id="cook-start">Gotujmy &rarr;</button>
</div>

<h2>Sposób przygotowania</h2>
<ol class="p-steps" id="steps-list">
<li>Bułkę pokrój na pół, na niej ułóż ser pokrojony ser mozzarella, pokrojonego pomidora i na wierzch posyp orzechy włoskie. Smacznego!</li>
</ol>

<div class="p-cook" id="cook" data-open="0" role="dialog" aria-modal="true" aria-label="Gotowanie: Mozzarella, pomidor, grahamka i orzechy">
<div class="p-cook__bar">
<span class="p-cook__title">Mozzarella, pomidor, grahamka i orzechy</span>
<button type="button" class="p-iconbtn" id="cook-close" aria-label="Zamknij tryb gotowania">&times;</button>
</div>
<div class="p-progress" id="cook-progress"></div>
<div class="p-cook__body">
<span class="p-cook__step" id="cook-label"></span>
<p class="p-cook__text" id="cook-text"></p>
</div>
<div class="p-cook__nav">
<button type="button" class="p-btn" id="cook-prev">Wstecz</button>
<button type="button" class="p-btn p-btn--primary" id="cook-next">Następny krok</button>
</div></div>
<div class="p-sheet" id="shopping" data-open="0" role="dialog" aria-modal="true" aria-label="Lista zakupów">
<button type="button" class="p-sheet__scrim" id="shopping-scrim" aria-label="Zamknij listę zakupów"></button>
<div class="p-sheet__panel">
<div class="p-sheet__head"><h2>Lista zakupów</h2><button type="button" class="p-iconbtn" id="close-shopping" aria-label="Zamknij">&times;</button></div>
<div class="p-sheet__body" id="shopping-body"></div>
<div class="p-sheet__foot">
<button type="button" class="p-btn" id="reset-shopping">Odznacz wszystko</button>
<button type="button" class="p-btn p-btn--primary" id="pdf-btn">Wygeneruj PDF</button>
</div></div></div>
<div class="p-toast" id="toast" role="status" data-on="0"></div>

<script>window.RECIPE = {"slug": "mozzarella-pomidor-grahamka-i-orzechy", "title": "Mozzarella, pomidor, grahamka i orzechy", "slotLabel": "Śniadanie", "time": "7:00-10:00", "baseServings": 1, "ingredients": [{"qty": 1.0, "unit": "sztuka", "unitLemma": "sztuka", "name": "bułki grahamki", "grams": 80.0, "pantry": false, "tag": "bulka", "swap": {"group": "pieczywo", "self": "bulka-grahamka", "nameCase": "D"}}, {"qty": 0.5, "unit": "plastra", "unitLemma": "plaster", "name": "sera mozzarella", "grams": 60.0, "pantry": false, "tag": "mozzarella"}, {"qty": 3.0, "unit": "sztuki", "unitLemma": "sztuka", "name": "orzechów włoskich", "grams": 12.0, "pantry": false, "tag": "orzechy", "swap": {"group": "orzechy", "self": "orzechy-wloskie", "nameCase": "D"}}, {"qty": 1.0, "unit": "sztuka", "unitLemma": "sztuka", "name": "małego pomidora", "grams": 60.0, "pantry": false, "tag": "pomidor"}], "steps": ["Bułkę pokrój na pół, na niej ułóż ser pokrojony ser mozzarella, pokrojonego pomidora i na wierzch posyp «2|B|||». Smacznego!"]};
window.UNITS = {"łyżka": ["łyżka", "łyżki", "łyżek", "łyżki"], "łyżeczka": ["łyżeczka", "łyżeczki", "łyżeczek", "łyżeczki"], "sztuka": ["sztuka", "sztuki", "sztuk", "sztuki"], "garść": ["garść", "garście", "garści", "garści"], "kromka": ["kromka", "kromki", "kromek", "kromki"], "plaster": ["plaster", "plastry", "plastrów", "plastra"], "szklanka": ["szklanka", "szklanki", "szklanek", "szklanki"], "opakowanie": ["opakowanie", "opakowania", "opakowań", "opakowania"], "ząbek": ["ząbek", "ząbki", "ząbków", "ząbka"], "szczypta": ["szczypta", "szczypty", "szczypt", "szczypty"], "porcja": ["porcja", "porcje", "porcji", "porcji"], "puszka": ["puszka", "puszki", "puszek", "puszki"], "kostka": ["kostka", "kostki", "kostek", "kostki"], "listek": ["listek", "listki", "listków", "listka"], "łodyga": ["łodyga", "łodygi", "łodyg", "łodygi"]};
window.SWAPS = {"orzechy": {"label": "Orzechy i pestki", "options": [{"id": "orzechy-wloskie", "label": "Orzechy włoskie", "rodzaj": "pl", "formy": {"M": "orzechy włoskie", "D": "orzechów włoskich", "B": "orzechy włoskie", "N": "orzechami włoskimi", "Ms": "orzechach włoskich"}, "rodzajB": "pl"}, {"id": "orzechy-nerkowca", "label": "Orzechy nerkowca", "rodzaj": "pl", "formy": {"M": "orzechy nerkowca", "D": "orzechów nerkowca", "B": "orzechy nerkowca", "N": "orzechami nerkowca", "Ms": "orzechach nerkowca"}, "rodzajB": "pl"}, {"id": "orzechy-laskowe", "label": "Orzechy laskowe", "rodzaj": "pl", "formy": {"M": "orzechy laskowe", "D": "orzechów laskowych", "B": "orzechy laskowe", "N": "orzechami laskowymi", "Ms": "orzechach laskowych"}, "rodzajB": "pl"}, {"id": "orzechy-pistacjowe", "label": "Orzechy pistacjowe", "rodzaj": "pl", "formy": {"M": "orzechy pistacjowe", "D": "orzechów pistacjowych", "B": "orzechy pistacjowe", "N": "orzechami pistacjowymi", "Ms": "orzechach pistacjowych"}, "rodzajB": "pl"}, {"id": "orzechy-arachidowe", "label": "Orzechy arachidowe", "rodzaj": "pl", "formy": {"M": "orzechy arachidowe", "D": "orzechów arachidowych", "B": "orzechy arachidowe", "N": "orzechami arachidowymi", "Ms": "orzechach arachidowych"}, "rodzajB": "pl"}, {"id": "pestki-dyni", "label": "Pestki dyni", "rodzaj": "pl", "formy": {"M": "pestki dyni", "D": "pestek dyni", "B": "pestki dyni", "N": "pestkami dyni", "Ms": "pestkach dyni"}, "rodzajB": "pl"}, {"id": "pestki-slonecznika", "label": "Pestki słonecznika", "rodzaj": "pl", "formy": {"M": "pestki słonecznika", "D": "pestek słonecznika", "B": "pestki słonecznika", "N": "pestkami słonecznika", "Ms": "pestkach słonecznika"}, "rodzajB": "pl"}]}, "pieczywo": {"label": "Pieczywo", "options": [{"id": "chleb-zytni-razowy", "label": "Chleb żytni razowy", "rodzaj": "m", "formy": {"M": "chleb żytni razowy", "D": "chleba żytniego razowego", "B": "chleb żytni razowy", "N": "chlebem żytnim razowym", "Ms": "chlebie żytnim razowym"}, "rodzajB": "m"}, {"id": "chleb-zytni", "label": "Chleb żytni", "rodzaj": "m", "formy": {"M": "chleb żytni", "D": "chleba żytniego", "B": "chleb żytni", "N": "chlebem żytnim", "Ms": "chlebie żytnim"}, "rodzajB": "m"}, {"id": "chleb-orkiszowy", "label": "Chleb orkiszowy", "rodzaj": "m", "formy": {"M": "chleb orkiszowy", "D": "chleba orkiszowego", "B": "chleb orkiszowy", "N": "chlebem orkiszowym", "Ms": "chlebie orkiszowym"}, "rodzajB": "m"}, {"id": "chleb-pelnoziarnisty", "label": "Chleb pełnoziarnisty", "rodzaj": "m", "formy": {"M": "chleb pełnoziarnisty", "D": "chleba pełnoziarnistego", "B": "chleb pełnoziarnisty", "N": "chlebem pełnoziarnistym", "Ms": "chlebie pełnoziarnistym"}, "rodzajB": "m"}, {"id": "chleb-na-zakwasie", "label": "Chleb żytni na zakwasie", "rodzaj": "m", "formy": {"M": "chleb żytni na zakwasie", "D": "chleba żytniego na zakwasie", "B": "chleb żytni na zakwasie", "N": "chlebem żytnim na zakwasie", "Ms": "chlebie żytnim na zakwasie"}, "rodzajB": "m"}, {"id": "bulka-grahamka", "label": "Bułka grahamka", "rodzaj": "f", "formy": {"M": "bułka grahamka", "D": "bułki grahamki", "B": "bułkę grahamkę", "N": "bułką grahamką", "Ms": "bułce grahamce"}, "rodzajB": "f"}, {"id": "bulka-owsiana", "label": "Bułka owsiana", "rodzaj": "f", "formy": {"M": "bułka owsiana", "D": "bułki owsianej", "B": "bułkę owsianą", "N": "bułką owsianą", "Ms": "bułce owsianej"}, "rodzajB": "f"}]}};
window.SWAP_ADJ = {"umyty_B": {"m": "umyty", "f": "umytą", "n": "umyte", "pl": "umyte", "mz": "umytego"}, "swiezy_B": {"m": "świeży", "f": "świeżą", "n": "świeże", "pl": "świeże", "mz": "świeżego"}, "odsaczony_B": {"m": "odsączony", "f": "odsączoną", "n": "odsączone", "pl": "odsączone", "mz": "odsączonego"}, "pieczony_N": {"m": "pieczonym", "f": "pieczoną", "n": "pieczonym", "pl": "pieczonymi", "mz": "pieczonym"}, "pokrojony_B": {"m": "pokrojony", "f": "pokrojoną", "n": "pokrojone", "pl": "pokrojone", "mz": "pokrojonego"}, "ugotowany_B": {"m": "ugotowany", "f": "ugotowaną", "n": "ugotowane", "pl": "ugotowane", "mz": "ugotowanego"}, "podsmazony_B": {"m": "podsmażony", "f": "podsmażoną", "n": "podsmażone", "pl": "podsmażone", "mz": "podsmażonego"}, "przyprawiony_B": {"m": "przyprawiony", "f": "przyprawioną", "n": "przyprawione", "pl": "przyprawione", "mz": "przyprawionego"}, "prazony_N": {"m": "prażonym", "f": "prażoną", "n": "prażonym", "pl": "prażonymi", "mz": "prażonym"}, "pokrojony_N": {"m": "pokrojonym", "f": "pokrojoną", "n": "pokrojonym", "pl": "pokrojonymi", "mz": "pokrojonym"}, "starty_B": {"m": "starty", "f": "startą", "n": "starte", "pl": "starte", "mz": "startego"}, "ugotowany_N": {"m": "ugotowanym", "f": "ugotowaną", "n": "ugotowanym", "pl": "ugotowanymi", "mz": "ugotowanym"}, "przygotowany_B": {"m": "przygotowany", "f": "przygotowaną", "n": "przygotowane", "pl": "przygotowane", "mz": "przygotowanego"}};</script>
