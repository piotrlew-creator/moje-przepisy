---
hide:
  - toc
---

<a class="p-back" href="../../">&larr; Wszystkie przepisy</a>

# Koktajl bananowo-orzechowy

<div class="p-hero" data-slot="4">
<div class="p-hero__top">
<span>Kolacja</span><span class="p-num">18:00-21:00</span><span class="p-num">Dzień 3</span>
</div>
<div class="p-macros">
<div class="p-macro"><span class="p-macro__v">468</span><span class="p-macro__l">kcal</span></div>
<div class="p-macro"><span class="p-macro__v">18 g</span><span class="p-macro__l">białko</span></div>
<div class="p-macro"><span class="p-macro__v">52 g</span><span class="p-macro__l">węgl.</span></div>
<div class="p-macro"><span class="p-macro__v">24 g</span><span class="p-macro__l">tłuszcz</span></div>
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
<li><span class="p-ing__q">1 sztuka</span><span>banana</span><span class="p-ing__g">120 g</span></li>
<li><span class="p-ing__q">1 szklanka</span><span>napoju sojowego</span><span class="p-ing__g">250 g</span></li>
<li data-pantry="1"><span class="p-ing__q">2 łyżeczki</span><span>erytrolu</span><span class="p-ing__g">10 g</span></li>
<li><span class="p-ing__q">3 łyżeczki</span><span>masła orzechowego</span><span class="p-ing__g">30 g</span></li>
<li><span class="p-ing__q">3 łyżeczki</span><span>nasion chia</span><span class="p-ing__g">15 g</span></li>
</ul>

<div class="p-actions">
<button type="button" class="p-btn p-btn--block" id="open-shopping">&#128722; Lista zakupów</button>
<button type="button" class="p-btn p-btn--primary p-btn--block" id="cook-start">Gotujmy &rarr;</button>
</div>

<h2>Sposób przygotowania</h2>
<ol class="p-steps">
<li>Zblenduj wszystkie składniki. W razie potrzeby dodaj wody.</li>
</ol>

<div class="p-cook" id="cook" data-open="0" role="dialog" aria-modal="true" aria-label="Gotowanie: Koktajl bananowo-orzechowy">
<div class="p-cook__bar">
<span class="p-cook__title">Koktajl bananowo-orzechowy</span>
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

<script>window.RECIPE = {"slug": "koktajl-bananowy", "title": "Koktajl bananowo-orzechowy", "day": 3, "slotLabel": "Kolacja", "time": "18:00-21:00", "baseServings": 1, "ingredients": [{"qty": 1.0, "unit": "sztuka", "unitLemma": "sztuka", "name": "banana", "grams": 120.0, "pantry": false, "tag": "banan"}, {"qty": 1.0, "unit": "szklanka", "unitLemma": "szklanka", "name": "napoju sojowego", "grams": 250.0, "pantry": false, "tag": "mleko"}, {"qty": 2.0, "unit": "łyżeczki", "unitLemma": "łyżeczka", "name": "erytrolu", "grams": 10.0, "pantry": true, "tag": null}, {"qty": 3.0, "unit": "łyżeczki", "unitLemma": "łyżeczka", "name": "masła orzechowego", "grams": 30.0, "pantry": false, "tag": "maslo-orzechowe"}, {"qty": 3.0, "unit": "łyżeczki", "unitLemma": "łyżeczka", "name": "nasion chia", "grams": 15.0, "pantry": false, "tag": "chia"}], "steps": ["Zblenduj wszystkie składniki. W razie potrzeby dodaj wody."]};
window.UNITS = {"łyżka": ["łyżka", "łyżki", "łyżek", "łyżki"], "łyżeczka": ["łyżeczka", "łyżeczki", "łyżeczek", "łyżeczki"], "sztuka": ["sztuka", "sztuki", "sztuk", "sztuki"], "garść": ["garść", "garście", "garści", "garści"], "kromka": ["kromka", "kromki", "kromek", "kromki"], "plaster": ["plaster", "plastry", "plastrów", "plastra"], "szklanka": ["szklanka", "szklanki", "szklanek", "szklanki"], "opakowanie": ["opakowanie", "opakowania", "opakowań", "opakowania"], "ząbek": ["ząbek", "ząbki", "ząbków", "ząbka"], "szczypta": ["szczypta", "szczypty", "szczypt", "szczypty"], "porcja": ["porcja", "porcje", "porcji", "porcji"], "puszka": ["puszka", "puszki", "puszek", "puszki"]};</script>
