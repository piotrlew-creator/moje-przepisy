---
hide:
  - toc
---

<a class="p-back" href="../../">&larr; Wszystkie przepisy</a>

# Ryżowa sałatka z ananasem, ogórkiem, selerem i kukurydzą + shake białkowy

<div class="p-hero" data-slot="4">
<div class="p-hero__top">
<span>Kolacja</span><span class="p-num">18:00-21:00</span><span class="p-num">Dzień 9</span>
</div>
<div class="p-macros">
<div class="p-macro"><span class="p-macro__v">458</span><span class="p-macro__l">kcal</span></div>
<div class="p-macro"><span class="p-macro__v">26 g</span><span class="p-macro__l">białko</span></div>
<div class="p-macro"><span class="p-macro__v">55 g</span><span class="p-macro__l">węgl.</span></div>
<div class="p-macro"><span class="p-macro__v">17 g</span><span class="p-macro__l">tłuszcz</span></div>
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

<h2 id="ing-heading">Składniki na 1 osobę</h2>
<ul class="p-ings" id="ing-list">
<li><span class="p-ing__q">2 łyżki</span><span>ryżu basmati</span><span class="p-ing__g">30 g</span></li>
<li><span class="p-ing__q">3 łyżki</span><span>kukurydzy konserwowej</span><span class="p-ing__g">60 g</span></li>
<li><span class="p-ing__q">1 plaster</span><span>ananasa świeżego</span><span class="p-ing__g">80 g</span></li>
<li><span class="p-ing__q">1 sztuka</span><span>małego ogórka</span><span class="p-ing__g">70 g</span></li>
<li><span class="p-ing__q">1 sztuka</span><span>selera naciowego</span><span class="p-ing__g">45 g</span></li>
<li data-pantry="1"><span class="p-ing__q">0.5 garści</span><span>świeżej kolendry</span><span class="p-ing__g">2 g</span></li>
<li><span class="p-ing__q">1 łyżka</span><span>majonezu wegańskiego</span><span class="p-ing__g">25 g</span></li>
<li><span class="p-ing__q">1 łyżka</span><span>soku z cytryny</span><span class="p-ing__g">6 g</span></li>
<li data-pantry="1"><span class="p-ing__q">1 szczypta</span><span>soli i pieprzu</span><span class="p-ing__g">0.25 g</span></li>
<li><span class="p-ing__q">3 łyżki</span><span>wegańskiej odżywki białkowej</span><span class="p-ing__g">24 g</span></li>
</ul>

<div class="p-actions">
<button type="button" class="p-btn p-btn--block" id="open-shopping">&#128722; Lista zakupów</button>
<button type="button" class="p-btn p-btn--primary p-btn--block" id="cook-start">Gotujmy &rarr;</button>
</div>

<h2>Sposób przygotowania</h2>
<ol class="p-steps">
<li>Ryż gotujemy według instrukcji na opakowaniu.</li>
<li>Do ugotowanego, ostudzonego ryżu dodajemy odcedzoną kukurydzę, posiekaną kolendrę i sok z cytryny.</li>
<li>Ananasa, ogórka, seler naciowy kroimy w drobną kostkę i dodajemy do ryżu.</li>
<li>Doprawiamy solą, pieprzem, dodajemy majonez wegański. Dokładnie mieszamy. Odżywkę mieszamy z wodą i wypijamy shake białkowy. Smacznego!</li>
</ol>

<div class="p-cook" id="cook" data-open="0" role="dialog" aria-modal="true" aria-label="Gotowanie: Ryżowa sałatka z ananasem, ogórkiem, selerem i kukurydzą + shake białkowy">
<div class="p-cook__bar">
<span class="p-cook__title">Ryżowa sałatka z ananasem, ogórkiem, selerem i kukurydzą + shake białkowy</span>
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
</div>
</div>
<div class="p-sheet" id="shopping" data-open="0" role="dialog" aria-modal="true" aria-label="Lista zakupów">
<button type="button" class="p-sheet__scrim" id="shopping-scrim" aria-label="Zamknij listę zakupów"></button>
<div class="p-sheet__panel">
<div class="p-sheet__head"><h2>Lista zakupów</h2><button type="button" class="p-iconbtn" id="close-shopping" aria-label="Zamknij">&times;</button></div>
<div class="p-sheet__body" id="shopping-body"></div>
<div class="p-sheet__foot">
<button type="button" class="p-btn" id="reset-shopping">Odznacz wszystko</button>
<button type="button" class="p-btn p-btn--primary" id="pdf-btn">Wygeneruj PDF</button>
</div>
</div></div>
<div class="p-toast" id="toast" role="status" data-on="0"></div>

<script>window.RECIPE = {"slug": "ryzowa-salatka-z-ananasem", "title": "Ryżowa sałatka z ananasem, ogórkiem, selerem i kukurydzą + shake białkowy", "day": 9, "slotLabel": "Kolacja", "time": "18:00-21:00", "baseServings": 1, "ingredients": [{"qty": 2.0, "unit": "łyżki", "unitLemma": "łyżka", "name": "ryżu basmati", "grams": 30.0, "pantry": false, "tag": "ryz"}, {"qty": 3.0, "unit": "łyżki", "unitLemma": "łyżka", "name": "kukurydzy konserwowej", "grams": 60.0, "pantry": false, "tag": "kukurydza"}, {"qty": 1.0, "unit": "plaster", "unitLemma": "plaster", "name": "ananasa świeżego", "grams": 80.0, "pantry": false, "tag": "ananas"}, {"qty": 1.0, "unit": "sztuka", "unitLemma": "sztuka", "name": "małego ogórka", "grams": 70.0, "pantry": false, "tag": "ogorek"}, {"qty": 1.0, "unit": "sztuka", "unitLemma": "sztuka", "name": "selera naciowego", "grams": 45.0, "pantry": false, "tag": "seler"}, {"qty": 0.5, "unit": "garści", "unitLemma": "garść", "name": "świeżej kolendry", "grams": 2.0, "pantry": true, "tag": null}, {"qty": 1.0, "unit": "łyżka", "unitLemma": "łyżka", "name": "majonezu wegańskiego", "grams": 25.0, "pantry": false, "tag": "majonez"}, {"qty": 1.0, "unit": "łyżka", "unitLemma": "łyżka", "name": "soku z cytryny", "grams": 6.0, "pantry": false, "tag": "cytryna"}, {"qty": 1.0, "unit": "szczypta", "unitLemma": "szczypta", "name": "soli i pieprzu", "grams": 0.25, "pantry": true, "tag": null}, {"qty": 3.0, "unit": "łyżki", "unitLemma": "łyżka", "name": "wegańskiej odżywki białkowej", "grams": 24.0, "pantry": false, "tag": "odzywka"}], "steps": ["Ryż gotujemy według instrukcji na opakowaniu.", "Do ugotowanego, ostudzonego ryżu dodajemy odcedzoną kukurydzę, posiekaną kolendrę i sok z cytryny.", "Ananasa, ogórka, seler naciowy kroimy w drobną kostkę i dodajemy do ryżu.", "Doprawiamy solą, pieprzem, dodajemy majonez wegański. Dokładnie mieszamy. Odżywkę mieszamy z wodą i wypijamy shake białkowy. Smacznego!"]};
window.UNITS = {"łyżka": ["łyżka", "łyżki", "łyżek", "łyżki"], "łyżeczka": ["łyżeczka", "łyżeczki", "łyżeczek", "łyżeczki"], "sztuka": ["sztuka", "sztuki", "sztuk", "sztuki"], "garść": ["garść", "garście", "garści", "garści"], "kromka": ["kromka", "kromki", "kromek", "kromki"], "plaster": ["plaster", "plastry", "plastrów", "plastra"], "szklanka": ["szklanka", "szklanki", "szklanek", "szklanki"], "opakowanie": ["opakowanie", "opakowania", "opakowań", "opakowania"], "ząbek": ["ząbek", "ząbki", "ząbków", "ząbka"], "szczypta": ["szczypta", "szczypty", "szczypt", "szczypty"], "porcja": ["porcja", "porcje", "porcji", "porcji"], "puszka": ["puszka", "puszki", "puszek", "puszki"]};</script>
