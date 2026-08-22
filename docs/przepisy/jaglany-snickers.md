---
hide:
  - toc
---

<a class="p-back" href="../../">&larr; Wszystkie przepisy</a>

# Jaglany snickers

<div class="p-hero" data-slot="1">
<div class="p-hero__top">
<span>Śniadanie</span><span class="p-num">6:00-9:00</span><span class="p-num">Dzień 9</span>
</div>
<div class="p-macros">
<div class="p-macro"><span class="p-macro__v">466</span><span class="p-macro__l">kcal</span></div>
<div class="p-macro"><span class="p-macro__v">27 g</span><span class="p-macro__l">białko</span></div>
<div class="p-macro"><span class="p-macro__v">52 g</span><span class="p-macro__l">węgl.</span></div>
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

<h2 id="ing-heading">Składniki na 1 osobę</h2>
<ul class="p-ings" id="ing-list">
<li><span class="p-ing__q">1 porcja</span><span>gorzkiej czekolady</span><span class="p-ing__g">10 g</span></li>
<li><span class="p-ing__q">2 łyżki</span><span>kaszy jaglanej</span><span class="p-ing__g">30 g</span></li>
<li><span class="p-ing__q">0.5 opakowania</span><span>jogurtu roślinnego</span><span class="p-ing__g">80 g</span></li>
<li><span class="p-ing__q">9 łyżek</span><span>napoju sojowego</span><span class="p-ing__g">105 g</span></li>
<li><span class="p-ing__q">1 łyżeczka</span><span>masła orzechowego</span><span class="p-ing__g">10 g</span></li>
<li><span class="p-ing__q">2 sztuki</span><span>świeżych daktyli</span><span class="p-ing__g">10 g</span></li>
<li><span class="p-ing__q">2 sztuki</span><span>posiekanych orzechów włoskich</span><span class="p-ing__g">8 g</span></li>
<li><span class="p-ing__q">0.5 łyżki</span><span>syropu z agawy</span><span class="p-ing__g">7 g</span></li>
<li><span class="p-ing__q">2 łyżki</span><span>wegańskiej odżywki białkowej</span><span class="p-ing__g">16 g</span></li>
</ul>

<div class="p-actions">
<button type="button" class="p-btn p-btn--block" id="open-shopping">&#128722; Lista zakupów</button>
<button type="button" class="p-btn p-btn--primary p-btn--block" id="cook-start">Gotujmy &rarr;</button>
</div>

<h2>Sposób przygotowania</h2>
<ol class="p-steps">
<li>Kaszę gotujemy w osolonej wodzie według instrukcji na opakowaniu.</li>
<li>Daktyle jeśli mamy suszone, zalewamy gorącą wodą na 10 minut. W przypadku daktyli świeżych pomijamy ten krok.</li>
<li>Do blendera przekładamy czekoladę, daktyle, masło orzechowe, napój roślinny, jogurt, odżywkę wegańską oraz ugotowaną kaszę.</li>
<li>Całość blendujemy, przekładamy do szklanek oblanych syropem z agawy i posypanych posiekanymi orzechami. Jeśli jest za gęste, dolewamy wody. Na wierzchu układamy pozostałą posiekaną czekoladę. Smacznego!</li>
</ol>

<div class="p-cook" id="cook" data-open="0" role="dialog" aria-modal="true" aria-label="Gotowanie: Jaglany snickers">
<div class="p-cook__bar">
<span class="p-cook__title">Jaglany snickers</span>
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

<script>window.RECIPE = {"slug": "jaglany-snickers", "title": "Jaglany snickers", "day": 9, "slotLabel": "Śniadanie", "time": "6:00-9:00", "baseServings": 1, "ingredients": [{"qty": 1.0, "unit": "porcja", "unitLemma": "porcja", "name": "gorzkiej czekolady", "grams": 10.0, "pantry": false, "tag": "czekolada"}, {"qty": 2.0, "unit": "łyżki", "unitLemma": "łyżka", "name": "kaszy jaglanej", "grams": 30.0, "pantry": false, "tag": "kasza"}, {"qty": 0.5, "unit": "opakowania", "unitLemma": "opakowanie", "name": "jogurtu roślinnego", "grams": 80.0, "pantry": false, "tag": "jogurt"}, {"qty": 9.0, "unit": "łyżek", "unitLemma": "łyżka", "name": "napoju sojowego", "grams": 105.0, "pantry": false, "tag": "mleko"}, {"qty": 1.0, "unit": "łyżeczka", "unitLemma": "łyżeczka", "name": "masła orzechowego", "grams": 10.0, "pantry": false, "tag": "maslo-orzechowe"}, {"qty": 2.0, "unit": "sztuki", "unitLemma": "sztuka", "name": "świeżych daktyli", "grams": 10.0, "pantry": false, "tag": "daktyle"}, {"qty": 2.0, "unit": "sztuki", "unitLemma": "sztuka", "name": "posiekanych orzechów włoskich", "grams": 8.0, "pantry": false, "tag": "orzechy"}, {"qty": 0.5, "unit": "łyżki", "unitLemma": "łyżka", "name": "syropu z agawy", "grams": 7.0, "pantry": false, "tag": "syrop-agawa"}, {"qty": 2.0, "unit": "łyżki", "unitLemma": "łyżka", "name": "wegańskiej odżywki białkowej", "grams": 16.0, "pantry": false, "tag": "odzywka"}], "steps": ["Kaszę gotujemy w osolonej wodzie według instrukcji na opakowaniu.", "Daktyle jeśli mamy suszone, zalewamy gorącą wodą na 10 minut. W przypadku daktyli świeżych pomijamy ten krok.", "Do blendera przekładamy czekoladę, daktyle, masło orzechowe, napój roślinny, jogurt, odżywkę wegańską oraz ugotowaną kaszę.", "Całość blendujemy, przekładamy do szklanek oblanych syropem z agawy i posypanych posiekanymi orzechami. Jeśli jest za gęste, dolewamy wody. Na wierzchu układamy pozostałą posiekaną czekoladę. Smacznego!"]};
window.UNITS = {"łyżka": ["łyżka", "łyżki", "łyżek", "łyżki"], "łyżeczka": ["łyżeczka", "łyżeczki", "łyżeczek", "łyżeczki"], "sztuka": ["sztuka", "sztuki", "sztuk", "sztuki"], "garść": ["garść", "garście", "garści", "garści"], "kromka": ["kromka", "kromki", "kromek", "kromki"], "plaster": ["plaster", "plastry", "plastrów", "plastra"], "szklanka": ["szklanka", "szklanki", "szklanek", "szklanki"], "opakowanie": ["opakowanie", "opakowania", "opakowań", "opakowania"], "ząbek": ["ząbek", "ząbki", "ząbków", "ząbka"], "szczypta": ["szczypta", "szczypty", "szczypt", "szczypty"], "porcja": ["porcja", "porcje", "porcji", "porcji"], "puszka": ["puszka", "puszki", "puszek", "puszki"]};</script>
