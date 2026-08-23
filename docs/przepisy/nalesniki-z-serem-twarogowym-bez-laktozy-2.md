---
hide:
  - toc
---

<a class="p-back" href="../../">&larr; Wszystkie przepisy</a>

# Naleśniki z serem twarogowym bez laktozy i owocami

<div class="p-hero" data-slot="2">
<div class="p-hero__top">
<span>Obiad</span><span class="p-num">13:00-16:00</span>
</div>
<div class="p-macros">
<div class="p-macro"><span class="p-macro__v">504</span><span class="p-macro__l">kcal</span></div>
<div class="p-macro"><span class="p-macro__v">30 g</span><span class="p-macro__l">białko</span></div>
<div class="p-macro"><span class="p-macro__v">58 g</span><span class="p-macro__l">węgl.</span></div>
<div class="p-macro"><span class="p-macro__v">16 g</span><span class="p-macro__l">tłuszcz</span></div>
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
<li data-order="name"><div class="p-ing__row"><span class="p-ing__q">2 sztuki</span><span class="p-ing__n">Ciasto do naleśników low fodmap</span><span class="p-ing__g">192 g</span></div>
</li>
<li data-order="name"><div class="p-ing__row"><span class="p-ing__q">3 plastry</span><span class="p-ing__n">Ser twarogowy półtłusty bez laktozy</span><span class="p-ing__g">90 g</span></div>
</li>
<li data-order="name"><div class="p-ing__row"><span class="p-ing__q">3 łyżki</span><span class="p-ing__n">Jogurt naturalny bez laktozy</span><span class="p-ing__g">60 g</span></div>
</li>
<li data-pantry="1" data-order="name"><div class="p-ing__row"><span class="p-ing__q">0.5 łyżeczki</span><span class="p-ing__n">Cynamon</span><span class="p-ing__g">2 g</span></div>
</li>
<li data-order="name"><div class="p-ing__row"><span class="p-ing__q"></span><span class="p-ing__n">Truskawki, świeże lub mrożone</span><span class="p-ing__g">100 g</span></div>
</li>
</ul>

<div class="p-actions">
<button type="button" class="p-btn p-btn--block" id="open-shopping">&#128722; Lista zakupów</button>
<button type="button" class="p-btn p-btn--primary p-btn--block" id="cook-start">Gotujmy &rarr;</button>
</div>

<h2>Sposób przygotowania</h2>
<ol class="p-steps" id="steps-list">
<li>Przygotuj naleśniki wg przepisu https://centrumrespo.pl/przepisy/ciasto- do-nalesnikow-bez-glutenu/</li>
<li>Ser twarogowy bez laktozy wymieszaj z jogurtem bez laktozy oraz cynamonem</li>
<li>Gotową masą serową przełóż naleśniki.</li>
<li>Owoce możesz włożyć zarówno do środka jak i położyć na wierzch. Smacznego!</li>
</ol>

<div class="p-cook" id="cook" data-open="0" role="dialog" aria-modal="true" aria-label="Gotowanie: Naleśniki z serem twarogowym bez laktozy i owocami">
<div class="p-cook__bar">
<span class="p-cook__title">Naleśniki z serem twarogowym bez laktozy i owocami</span>
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

<script>window.RECIPE = {"slug": "nalesniki-z-serem-twarogowym-bez-laktozy-2", "title": "Naleśniki z serem twarogowym bez laktozy i owocami", "slotLabel": "Obiad", "time": "13:00-16:00", "baseServings": 1, "ingredients": [{"qty": 2.0, "unit": "sztuki", "unitLemma": "sztuka", "name": "Ciasto do naleśników low fodmap", "grams": 192.0, "pantry": false, "tag": "ciasto-nalesniki", "nameFirst": true}, {"qty": 3.0, "unit": "plastry", "unitLemma": "plaster", "name": "Ser twarogowy półtłusty bez laktozy", "grams": 90.0, "pantry": false, "tag": "twarog", "nameFirst": true}, {"qty": 3.0, "unit": "łyżki", "unitLemma": "łyżka", "name": "Jogurt naturalny bez laktozy", "grams": 60.0, "pantry": false, "tag": "jogurt", "nameFirst": true}, {"qty": 0.5, "unit": "łyżeczki", "unitLemma": "łyżeczka", "name": "Cynamon", "grams": 2.0, "pantry": true, "tag": null, "nameFirst": true}, {"qty": 100.0, "unit": "g", "unitLemma": null, "name": "Truskawki, świeże lub mrożone", "grams": 100.0, "pantry": false, "tag": "truskawki", "nameFirst": true, "weightOnly": true}], "steps": ["Przygotuj naleśniki wg przepisu https://centrumrespo.pl/przepisy/ciasto- do-nalesnikow-bez-glutenu/", "Ser twarogowy bez laktozy wymieszaj z jogurtem bez laktozy oraz cynamonem", "Gotową masą serową przełóż naleśniki.", "Owoce możesz włożyć zarówno do środka jak i położyć na wierzch. Smacznego!"]};
window.UNITS = {"łyżka": ["łyżka", "łyżki", "łyżek", "łyżki"], "łyżeczka": ["łyżeczka", "łyżeczki", "łyżeczek", "łyżeczki"], "sztuka": ["sztuka", "sztuki", "sztuk", "sztuki"], "garść": ["garść", "garście", "garści", "garści"], "kromka": ["kromka", "kromki", "kromek", "kromki"], "plaster": ["plaster", "plastry", "plastrów", "plastra"], "szklanka": ["szklanka", "szklanki", "szklanek", "szklanki"], "opakowanie": ["opakowanie", "opakowania", "opakowań", "opakowania"], "ząbek": ["ząbek", "ząbki", "ząbków", "ząbka"], "szczypta": ["szczypta", "szczypty", "szczypt", "szczypty"], "porcja": ["porcja", "porcje", "porcji", "porcji"], "puszka": ["puszka", "puszki", "puszek", "puszki"], "kostka": ["kostka", "kostki", "kostek", "kostki"], "listek": ["listek", "listki", "listków", "listka"], "łodyga": ["łodyga", "łodygi", "łodyg", "łodygi"]};
window.SWAPS = {};
window.SWAP_ADJ = {"umyty_B": {"m": "umyty", "f": "umytą", "n": "umyte", "pl": "umyte", "mz": "umytego"}, "swiezy_B": {"m": "świeży", "f": "świeżą", "n": "świeże", "pl": "świeże", "mz": "świeżego"}, "odsaczony_B": {"m": "odsączony", "f": "odsączoną", "n": "odsączone", "pl": "odsączone", "mz": "odsączonego"}, "pieczony_N": {"m": "pieczonym", "f": "pieczoną", "n": "pieczonym", "pl": "pieczonymi", "mz": "pieczonym"}, "pokrojony_B": {"m": "pokrojony", "f": "pokrojoną", "n": "pokrojone", "pl": "pokrojone", "mz": "pokrojonego"}, "ugotowany_B": {"m": "ugotowany", "f": "ugotowaną", "n": "ugotowane", "pl": "ugotowane", "mz": "ugotowanego"}, "podsmazony_B": {"m": "podsmażony", "f": "podsmażoną", "n": "podsmażone", "pl": "podsmażone", "mz": "podsmażonego"}, "przyprawiony_B": {"m": "przyprawiony", "f": "przyprawioną", "n": "przyprawione", "pl": "przyprawione", "mz": "przyprawionego"}, "prazony_N": {"m": "prażonym", "f": "prażoną", "n": "prażonym", "pl": "prażonymi", "mz": "prażonym"}, "pokrojony_N": {"m": "pokrojonym", "f": "pokrojoną", "n": "pokrojonym", "pl": "pokrojonymi", "mz": "pokrojonym"}, "starty_B": {"m": "starty", "f": "startą", "n": "starte", "pl": "starte", "mz": "startego"}, "ugotowany_N": {"m": "ugotowanym", "f": "ugotowaną", "n": "ugotowanym", "pl": "ugotowanymi", "mz": "ugotowanym"}, "przygotowany_B": {"m": "przygotowany", "f": "przygotowaną", "n": "przygotowane", "pl": "przygotowane", "mz": "przygotowanego"}};</script>
