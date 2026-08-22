---
hide:
  - toc
---

<a class="p-back" href="../../">&larr; Wszystkie przepisy</a>

# Sałatka grecka z serem sałatkowym i pieczywem

<div class="p-hero" data-slot="4">
<div class="p-hero__top">
<span>Kolacja</span><span class="p-num">18:00-21:00</span><span class="p-num">Dzień 5</span>
</div>
<div class="p-macros">
<div class="p-macro"><span class="p-macro__v">464</span><span class="p-macro__l">kcal</span></div>
<div class="p-macro"><span class="p-macro__v">24 g</span><span class="p-macro__l">białko</span></div>
<div class="p-macro"><span class="p-macro__v">41 g</span><span class="p-macro__l">węgl.</span></div>
<div class="p-macro"><span class="p-macro__v">25 g</span><span class="p-macro__l">tłuszcz</span></div>
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
<li><span class="p-ing__q">2 garści</span><span>miksu sałat</span><span class="p-ing__g">50 g</span></li>
<li><span class="p-ing__q">0.5 sztuki</span><span>sera feta</span><span class="p-ing__g">100 g</span></li>
<li><span class="p-ing__q">0.5 garści</span><span>oliwek zielonych</span><span class="p-ing__g">20 g</span></li>
<li data-pantry="1"><span class="p-ing__q">1 łyżeczka</span><span>suszonego oregano</span><span class="p-ing__g">3 g</span></li>
<li><span class="p-ing__q">0.5 sztuki</span><span>papryki żółtej</span><span class="p-ing__g">85 g</span></li>
<li><span class="p-ing__q">0.5 sztuki</span><span>cebuli</span><span class="p-ing__g">55 g</span></li>
<li><span class="p-ing__q">1 łyżeczka</span><span>oliwy z oliwek</span><span class="p-ing__g">5 g</span></li>
<li><span class="p-ing__q">0.5 łyżki</span><span>soku z cytryny</span><span class="p-ing__g">3 g</span></li>
<li><span class="p-ing__q">1 sztuka</span><span>pomidora</span><span class="p-ing__g">160 g</span></li>
<li><span class="p-ing__q">1 sztuka</span><span>ogórka zielonego</span><span class="p-ing__g">150 g</span></li>
<li><span class="p-ing__q">1 kromka</span><span>chleba żytniego razowego</span><span class="p-ing__g">30 g</span></li>
</ul>

<div class="p-actions">
<button type="button" class="p-btn p-btn--block" id="open-shopping">&#128722; Lista zakupów</button>
<button type="button" class="p-btn p-btn--primary p-btn--block" id="cook-start">Gotujmy &rarr;</button>
</div>

<h2>Sposób przygotowania</h2>
<ol class="p-steps">
<li>Kroimy paprykę, cebulę, pomidor, ogórek, oliwki i ser feta/sałatkowy.</li>
<li>Mieszamy oliwę, oregano, sól, pieprz, sok z cytryny.</li>
<li>Na talerz nakładamy sałatę, pokrojone warzywa, oliwki, ser sałatkowy, polewamy sosem, dokładnie mieszamy i podajemy z pieczywem. Smacznego!</li>
</ol>

<div class="p-cook" id="cook" data-open="0" role="dialog" aria-modal="true" aria-label="Gotowanie: Sałatka grecka z serem sałatkowym i pieczywem">
<div class="p-cook__bar">
<span class="p-cook__title">Sałatka grecka z serem sałatkowym i pieczywem</span>
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

<script>window.RECIPE = {"slug": "salatka-grecka", "title": "Sałatka grecka z serem sałatkowym i pieczywem", "day": 5, "slotLabel": "Kolacja", "time": "18:00-21:00", "baseServings": 1, "ingredients": [{"qty": 2.0, "unit": "garści", "unitLemma": "garść", "name": "miksu sałat", "grams": 50.0, "pantry": false, "tag": "salata"}, {"qty": 0.5, "unit": "sztuki", "unitLemma": "sztuka", "name": "sera feta", "grams": 100.0, "pantry": false, "tag": "feta"}, {"qty": 0.5, "unit": "garści", "unitLemma": "garść", "name": "oliwek zielonych", "grams": 20.0, "pantry": false, "tag": "oliwki"}, {"qty": 1.0, "unit": "łyżeczka", "unitLemma": "łyżeczka", "name": "suszonego oregano", "grams": 3.0, "pantry": true, "tag": null}, {"qty": 0.5, "unit": "sztuki", "unitLemma": "sztuka", "name": "papryki żółtej", "grams": 85.0, "pantry": false, "tag": "papryka"}, {"qty": 0.5, "unit": "sztuki", "unitLemma": "sztuka", "name": "cebuli", "grams": 55.0, "pantry": false, "tag": "cebula"}, {"qty": 1.0, "unit": "łyżeczka", "unitLemma": "łyżeczka", "name": "oliwy z oliwek", "grams": 5.0, "pantry": false, "tag": "oliwa"}, {"qty": 0.5, "unit": "łyżki", "unitLemma": "łyżka", "name": "soku z cytryny", "grams": 3.0, "pantry": false, "tag": "cytryna"}, {"qty": 1.0, "unit": "sztuka", "unitLemma": "sztuka", "name": "pomidora", "grams": 160.0, "pantry": false, "tag": "pomidor"}, {"qty": 1.0, "unit": "sztuka", "unitLemma": "sztuka", "name": "ogórka zielonego", "grams": 150.0, "pantry": false, "tag": "ogorek"}, {"qty": 1.0, "unit": "kromka", "unitLemma": "kromka", "name": "chleba żytniego razowego", "grams": 30.0, "pantry": false, "tag": "chleb"}], "steps": ["Kroimy paprykę, cebulę, pomidor, ogórek, oliwki i ser feta/sałatkowy.", "Mieszamy oliwę, oregano, sól, pieprz, sok z cytryny.", "Na talerz nakładamy sałatę, pokrojone warzywa, oliwki, ser sałatkowy, polewamy sosem, dokładnie mieszamy i podajemy z pieczywem. Smacznego!"]};
window.UNITS = {"łyżka": ["łyżka", "łyżki", "łyżek", "łyżki"], "łyżeczka": ["łyżeczka", "łyżeczki", "łyżeczek", "łyżeczki"], "sztuka": ["sztuka", "sztuki", "sztuk", "sztuki"], "garść": ["garść", "garście", "garści", "garści"], "kromka": ["kromka", "kromki", "kromek", "kromki"], "plaster": ["plaster", "plastry", "plastrów", "plastra"], "szklanka": ["szklanka", "szklanki", "szklanek", "szklanki"], "opakowanie": ["opakowanie", "opakowania", "opakowań", "opakowania"], "ząbek": ["ząbek", "ząbki", "ząbków", "ząbka"], "szczypta": ["szczypta", "szczypty", "szczypt", "szczypty"], "porcja": ["porcja", "porcje", "porcji", "porcji"], "puszka": ["puszka", "puszki", "puszek", "puszki"]};</script>
