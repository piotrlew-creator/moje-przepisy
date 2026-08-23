---
hide:
  - toc
---

<a class="p-back" href="../../">&larr; Wszystkie przepisy</a>

# Płatki z malinami oraz orzechami włoskimi

<div class="p-hero" data-slot="1">
<div class="p-hero__top">
<span>Śniadanie</span><span class="p-num">7:00-10:00</span>
</div>
<div class="p-macros">
<div class="p-macro"><span class="p-macro__v">588</span><span class="p-macro__l">kcal</span></div>
<div class="p-macro"><span class="p-macro__v">28 g</span><span class="p-macro__l">białko</span></div>
<div class="p-macro"><span class="p-macro__v">77 g</span><span class="p-macro__l">węgl.</span></div>
<div class="p-macro"><span class="p-macro__v">20 g</span><span class="p-macro__l">tłuszcz</span></div>
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
<li data-order="name"><div class="p-ing__row"><span class="p-ing__q">1 opakowanie</span><span class="p-ing__n">Jogurt skyr bez laktozy</span><span class="p-ing__g">140 g</span></div>
</li>
<li data-order="name"><div class="p-ing__row"><span class="p-ing__q">6.5 łyżki</span><span class="p-ing__n">Płatki jaglane</span><span class="p-ing__g">65 g</span></div>
<div class="p-ing__swap">
<label class="p-swaplabel" for="swap-1">Zamień na</label>
<select class="p-select" id="swap-1" data-ing="1">
<option value="platki-owsiane">Płatki owsiane</option>
<option value="platki-jaglane" selected>Płatki jaglane · oryginał</option>
<option value="platki-gryczane">Płatki gryczane</option>
<option value="platki-ryzowe">Płatki ryżowe</option>
<option value="platki-orkiszowe">Płatki orkiszowe</option>
</select>
</div>
</li>
<li data-order="name"><div class="p-ing__row"><span class="p-ing__q"></span><span class="p-ing__n">Orzechy włoskie</span><span class="p-ing__g">30 g</span></div>
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
<li data-order="name"><div class="p-ing__row"><span class="p-ing__q"></span><span class="p-ing__n">Maliny świeże lub mrożone</span><span class="p-ing__g">100 g</span></div>
</li>
</ul>

<div class="p-actions">
<button type="button" class="p-btn p-btn--block" id="open-shopping">&#128722; Lista zakupów</button>
<button type="button" class="p-btn p-btn--primary p-btn--block" id="cook-start">Gotujmy &rarr;</button>
</div>

<h2>Sposób przygotowania</h2>
<ol class="p-steps" id="steps-list">
<li>Płatki jaglane ugotuj w wodzie do miękkości. Do gotowania dodaj 2 razy więcej wody niż objętość płatków.</li>
<li>Miękkie płatki wymieszaj z jogurtem skyr bez laktozy.</li>
<li>Podaj z malinami oraz orzechami włoskimi. Smacznego!</li>
</ol>

<div class="p-cook" id="cook" data-open="0" role="dialog" aria-modal="true" aria-label="Gotowanie: Płatki z malinami oraz orzechami włoskimi">
<div class="p-cook__bar">
<span class="p-cook__title">Płatki z malinami oraz orzechami włoskimi</span>
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

<script>window.RECIPE = {"slug": "platki-z-malinami-oraz-orzechami-wloskimi", "title": "Płatki z malinami oraz orzechami włoskimi", "slotLabel": "Śniadanie", "time": "7:00-10:00", "baseServings": 1, "ingredients": [{"qty": 1.0, "unit": "opakowanie", "unitLemma": "opakowanie", "name": "Jogurt skyr bez laktozy", "grams": 140.0, "pantry": false, "tag": "jogurt", "nameFirst": true}, {"qty": 6.5, "unit": "łyżki", "unitLemma": "łyżka", "name": "Płatki jaglane", "grams": 65.0, "pantry": false, "tag": "platki-jaglane", "nameFirst": true, "swap": {"group": "platki", "self": "platki-jaglane", "nameCase": "M"}}, {"qty": 30.0, "unit": "g", "unitLemma": null, "name": "Orzechy włoskie", "grams": 30.0, "pantry": false, "tag": "orzechy", "nameFirst": true, "weightOnly": true, "swap": {"group": "orzechy", "self": "orzechy-wloskie", "nameCase": "M"}}, {"qty": 100.0, "unit": "g", "unitLemma": null, "name": "Maliny świeże lub mrożone", "grams": 100.0, "pantry": false, "tag": "maliny", "nameFirst": true, "weightOnly": true}], "steps": ["«1|B|||U» ugotuj w wodzie do miękkości. Do gotowania dodaj 2 razy więcej wody niż objętość płatków.", "Miękkie płatki wymieszaj z jogurtem skyr bez laktozy.", "Podaj z malinami oraz «2|N|||». Smacznego!"]};
window.UNITS = {"łyżka": ["łyżka", "łyżki", "łyżek", "łyżki"], "łyżeczka": ["łyżeczka", "łyżeczki", "łyżeczek", "łyżeczki"], "sztuka": ["sztuka", "sztuki", "sztuk", "sztuki"], "garść": ["garść", "garście", "garści", "garści"], "kromka": ["kromka", "kromki", "kromek", "kromki"], "plaster": ["plaster", "plastry", "plastrów", "plastra"], "szklanka": ["szklanka", "szklanki", "szklanek", "szklanki"], "opakowanie": ["opakowanie", "opakowania", "opakowań", "opakowania"], "ząbek": ["ząbek", "ząbki", "ząbków", "ząbka"], "szczypta": ["szczypta", "szczypty", "szczypt", "szczypty"], "porcja": ["porcja", "porcje", "porcji", "porcji"], "puszka": ["puszka", "puszki", "puszek", "puszki"], "kostka": ["kostka", "kostki", "kostek", "kostki"], "listek": ["listek", "listki", "listków", "listka"], "łodyga": ["łodyga", "łodygi", "łodyg", "łodygi"]};
window.SWAPS = {"orzechy": {"label": "Orzechy i pestki", "options": [{"id": "orzechy-wloskie", "label": "Orzechy włoskie", "rodzaj": "pl", "formy": {"M": "orzechy włoskie", "D": "orzechów włoskich", "B": "orzechy włoskie", "N": "orzechami włoskimi", "Ms": "orzechach włoskich"}, "rodzajB": "pl"}, {"id": "orzechy-nerkowca", "label": "Orzechy nerkowca", "rodzaj": "pl", "formy": {"M": "orzechy nerkowca", "D": "orzechów nerkowca", "B": "orzechy nerkowca", "N": "orzechami nerkowca", "Ms": "orzechach nerkowca"}, "rodzajB": "pl"}, {"id": "orzechy-laskowe", "label": "Orzechy laskowe", "rodzaj": "pl", "formy": {"M": "orzechy laskowe", "D": "orzechów laskowych", "B": "orzechy laskowe", "N": "orzechami laskowymi", "Ms": "orzechach laskowych"}, "rodzajB": "pl"}, {"id": "orzechy-pistacjowe", "label": "Orzechy pistacjowe", "rodzaj": "pl", "formy": {"M": "orzechy pistacjowe", "D": "orzechów pistacjowych", "B": "orzechy pistacjowe", "N": "orzechami pistacjowymi", "Ms": "orzechach pistacjowych"}, "rodzajB": "pl"}, {"id": "orzechy-arachidowe", "label": "Orzechy arachidowe", "rodzaj": "pl", "formy": {"M": "orzechy arachidowe", "D": "orzechów arachidowych", "B": "orzechy arachidowe", "N": "orzechami arachidowymi", "Ms": "orzechach arachidowych"}, "rodzajB": "pl"}, {"id": "pestki-dyni", "label": "Pestki dyni", "rodzaj": "pl", "formy": {"M": "pestki dyni", "D": "pestek dyni", "B": "pestki dyni", "N": "pestkami dyni", "Ms": "pestkach dyni"}, "rodzajB": "pl"}, {"id": "pestki-slonecznika", "label": "Pestki słonecznika", "rodzaj": "pl", "formy": {"M": "pestki słonecznika", "D": "pestek słonecznika", "B": "pestki słonecznika", "N": "pestkami słonecznika", "Ms": "pestkach słonecznika"}, "rodzajB": "pl"}]}, "platki": {"label": "Płatki", "options": [{"id": "platki-owsiane", "label": "Płatki owsiane", "rodzaj": "pl", "formy": {"M": "płatki owsiane", "D": "płatków owsianych", "B": "płatki owsiane", "N": "płatkami owsianymi", "Ms": "płatkach owsianych"}, "rodzajB": "pl"}, {"id": "platki-jaglane", "label": "Płatki jaglane", "rodzaj": "pl", "formy": {"M": "płatki jaglane", "D": "płatków jaglanych", "B": "płatki jaglane", "N": "płatkami jaglanymi", "Ms": "płatkach jaglanych"}, "rodzajB": "pl"}, {"id": "platki-gryczane", "label": "Płatki gryczane", "rodzaj": "pl", "formy": {"M": "płatki gryczane", "D": "płatków gryczanych", "B": "płatki gryczane", "N": "płatkami gryczanymi", "Ms": "płatkach gryczanych"}, "rodzajB": "pl"}, {"id": "platki-ryzowe", "label": "Płatki ryżowe", "rodzaj": "pl", "formy": {"M": "płatki ryżowe", "D": "płatków ryżowych", "B": "płatki ryżowe", "N": "płatkami ryżowymi", "Ms": "płatkach ryżowych"}, "rodzajB": "pl"}, {"id": "platki-orkiszowe", "label": "Płatki orkiszowe", "rodzaj": "pl", "formy": {"M": "płatki orkiszowe", "D": "płatków orkiszowych", "B": "płatki orkiszowe", "N": "płatkami orkiszowymi", "Ms": "płatkach orkiszowych"}, "rodzajB": "pl"}]}};
window.SWAP_ADJ = {"umyty_B": {"m": "umyty", "f": "umytą", "n": "umyte", "pl": "umyte", "mz": "umytego"}, "swiezy_B": {"m": "świeży", "f": "świeżą", "n": "świeże", "pl": "świeże", "mz": "świeżego"}, "odsaczony_B": {"m": "odsączony", "f": "odsączoną", "n": "odsączone", "pl": "odsączone", "mz": "odsączonego"}, "pieczony_N": {"m": "pieczonym", "f": "pieczoną", "n": "pieczonym", "pl": "pieczonymi", "mz": "pieczonym"}, "pokrojony_B": {"m": "pokrojony", "f": "pokrojoną", "n": "pokrojone", "pl": "pokrojone", "mz": "pokrojonego"}, "ugotowany_B": {"m": "ugotowany", "f": "ugotowaną", "n": "ugotowane", "pl": "ugotowane", "mz": "ugotowanego"}, "podsmazony_B": {"m": "podsmażony", "f": "podsmażoną", "n": "podsmażone", "pl": "podsmażone", "mz": "podsmażonego"}, "przyprawiony_B": {"m": "przyprawiony", "f": "przyprawioną", "n": "przyprawione", "pl": "przyprawione", "mz": "przyprawionego"}, "prazony_N": {"m": "prażonym", "f": "prażoną", "n": "prażonym", "pl": "prażonymi", "mz": "prażonym"}, "pokrojony_N": {"m": "pokrojonym", "f": "pokrojoną", "n": "pokrojonym", "pl": "pokrojonymi", "mz": "pokrojonym"}, "starty_B": {"m": "starty", "f": "startą", "n": "starte", "pl": "starte", "mz": "startego"}, "ugotowany_N": {"m": "ugotowanym", "f": "ugotowaną", "n": "ugotowanym", "pl": "ugotowanymi", "mz": "ugotowanym"}, "przygotowany_B": {"m": "przygotowany", "f": "przygotowaną", "n": "przygotowane", "pl": "przygotowane", "mz": "przygotowanego"}};</script>
