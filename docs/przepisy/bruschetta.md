---
hide:
  - toc
---

<a class="p-back" href="../../">&larr; Wszystkie przepisy</a>

# Bruschetta z pomidorami, świeżymi ziołami i serem grana padano

<div class="p-hero" data-slot="4">
<div class="p-hero__top">
<span>Kolacja</span><span class="p-num">18:00-21:00</span><span class="p-num">Dzień 7</span>
</div>
<div class="p-macros">
<div class="p-macro"><span class="p-macro__v">480</span><span class="p-macro__l">kcal</span></div>
<div class="p-macro"><span class="p-macro__v">24 g</span><span class="p-macro__l">białko</span></div>
<div class="p-macro"><span class="p-macro__v">49 g</span><span class="p-macro__l">węgl.</span></div>
<div class="p-macro"><span class="p-macro__v">21 g</span><span class="p-macro__l">tłuszcz</span></div>
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
<li><span class="p-ing__q">0.5 sztuki</span><span>bagietki</span><span class="p-ing__g">70 g</span></li>
<li><span class="p-ing__q">1 sztuka</span><span>pomidora</span><span class="p-ing__g">100 g</span></li>
<li><span class="p-ing__q">1 sztuka</span><span>małej cebuli czerwonej</span><span class="p-ing__g">20 g</span></li>
<li><span class="p-ing__q">1 ząbek</span><span>czosnku</span><span class="p-ing__g">6 g</span></li>
<li data-pantry="1"><span class="p-ing__q">1 garść</span><span>bazylii świeżej</span><span class="p-ing__g">3 g</span></li>
<li><span class="p-ing__q">2 porcje</span><span>sera grana padano</span><span class="p-ing__g">50 g</span></li>
<li data-pantry="1"><span class="p-ing__q">0.5 łyżki</span><span>octu balsamicznego</span><span class="p-ing__g">3 g</span></li>
<li><span class="p-ing__q">1 łyżeczka</span><span>oliwy z oliwek</span><span class="p-ing__g">5 g</span></li>
<li data-pantry="1"><span class="p-ing__q">1 szczypta</span><span>soli i pieprzu</span><span class="p-ing__g">0.25 g</span></li>
</ul>

<div class="p-actions">
<button type="button" class="p-btn p-btn--block" id="open-shopping">&#128722; Lista zakupów</button>
<button type="button" class="p-btn p-btn--primary p-btn--block" id="cook-start">Gotujmy &rarr;</button>
</div>

<h2>Sposób przygotowania</h2>
<ol class="p-steps">
<li>Pomidory myjemy, cebulę i czosnek obieramy. Warzywa kroimy w kostkę.</li>
<li>Pokrojone warzywa mieszamy ze sobą, dodajemy posiekaną bazylię. Całość doprawiamy solą, pieprzem, octem i oliwą z oliwek.</li>
<li>Bagietkę kroimy na kromki i pieczemy w piekarniku rozgrzanym do 180 stopni przez około 5 minut, aż będą chrupkie.</li>
<li>Na grzanki nakładamy pomidory z cebulką i czosnkiem, posypujemy startym serem grana padano.</li>
</ol>

<div class="p-cook" id="cook" data-open="0" role="dialog" aria-modal="true" aria-label="Gotowanie: Bruschetta z pomidorami, świeżymi ziołami i serem grana padano">
<div class="p-cook__bar">
<span class="p-cook__title">Bruschetta z pomidorami, świeżymi ziołami i serem grana padano</span>
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

<script>window.RECIPE = {"slug": "bruschetta", "title": "Bruschetta z pomidorami, świeżymi ziołami i serem grana padano", "day": 7, "slotLabel": "Kolacja", "time": "18:00-21:00", "baseServings": 1, "ingredients": [{"qty": 0.5, "unit": "sztuki", "unitLemma": "sztuka", "name": "bagietki", "grams": 70.0, "pantry": false, "tag": "bagietka"}, {"qty": 1.0, "unit": "sztuka", "unitLemma": "sztuka", "name": "pomidora", "grams": 100.0, "pantry": false, "tag": "pomidor"}, {"qty": 1.0, "unit": "sztuka", "unitLemma": "sztuka", "name": "małej cebuli czerwonej", "grams": 20.0, "pantry": false, "tag": "cebula"}, {"qty": 1.0, "unit": "ząbek", "unitLemma": "ząbek", "name": "czosnku", "grams": 6.0, "pantry": false, "tag": "czosnek"}, {"qty": 1.0, "unit": "garść", "unitLemma": "garść", "name": "bazylii świeżej", "grams": 3.0, "pantry": true, "tag": null}, {"qty": 2.0, "unit": "porcje", "unitLemma": "porcja", "name": "sera grana padano", "grams": 50.0, "pantry": false, "tag": "grana-padano"}, {"qty": 0.5, "unit": "łyżki", "unitLemma": "łyżka", "name": "octu balsamicznego", "grams": 3.0, "pantry": true, "tag": null}, {"qty": 1.0, "unit": "łyżeczka", "unitLemma": "łyżeczka", "name": "oliwy z oliwek", "grams": 5.0, "pantry": false, "tag": "oliwa"}, {"qty": 1.0, "unit": "szczypta", "unitLemma": "szczypta", "name": "soli i pieprzu", "grams": 0.25, "pantry": true, "tag": null}], "steps": ["Pomidory myjemy, cebulę i czosnek obieramy. Warzywa kroimy w kostkę.", "Pokrojone warzywa mieszamy ze sobą, dodajemy posiekaną bazylię. Całość doprawiamy solą, pieprzem, octem i oliwą z oliwek.", "Bagietkę kroimy na kromki i pieczemy w piekarniku rozgrzanym do 180 stopni przez około 5 minut, aż będą chrupkie.", "Na grzanki nakładamy pomidory z cebulką i czosnkiem, posypujemy startym serem grana padano."]};
window.UNITS = {"łyżka": ["łyżka", "łyżki", "łyżek", "łyżki"], "łyżeczka": ["łyżeczka", "łyżeczki", "łyżeczek", "łyżeczki"], "sztuka": ["sztuka", "sztuki", "sztuk", "sztuki"], "garść": ["garść", "garście", "garści", "garści"], "kromka": ["kromka", "kromki", "kromek", "kromki"], "plaster": ["plaster", "plastry", "plastrów", "plastra"], "szklanka": ["szklanka", "szklanki", "szklanek", "szklanki"], "opakowanie": ["opakowanie", "opakowania", "opakowań", "opakowania"], "ząbek": ["ząbek", "ząbki", "ząbków", "ząbka"], "szczypta": ["szczypta", "szczypty", "szczypt", "szczypty"], "porcja": ["porcja", "porcje", "porcji", "porcji"], "puszka": ["puszka", "puszki", "puszek", "puszki"]};</script>
