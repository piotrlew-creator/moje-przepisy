---
hide:
  - toc
---

<a class="p-back" href="../../">&larr; Wszystkie przepisy</a>

# Krem paprykowo-pomidorowy

<div class="p-hero" data-slot="3">
<div class="p-hero__top">
<span>Obiad</span><span class="p-num">14:00-17:00</span><span class="p-num">Dzień 2</span>
</div>
<div class="p-macros">
<div class="p-macro"><span class="p-macro__v">385</span><span class="p-macro__l">kcal</span></div>
<div class="p-macro"><span class="p-macro__v">18 g</span><span class="p-macro__l">białko</span></div>
<div class="p-macro"><span class="p-macro__v">45 g</span><span class="p-macro__l">węgl.</span></div>
<div class="p-macro"><span class="p-macro__v">15 g</span><span class="p-macro__l">tłuszcz</span></div>
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
<li><span class="p-ing__q">0.5 opakowania</span><span>pomidorów w puszce</span><span class="p-ing__g">200 g</span></li>
<li data-pantry="1"><span class="p-ing__q">1 szczypta</span><span>papryki wędzonej</span><span class="p-ing__g">0.5 g</span></li>
<li data-pantry="1"><span class="p-ing__q">1 garść</span><span>świeżej bazylii</span><span class="p-ing__g">3 g</span></li>
<li data-pantry="1"><span class="p-ing__q">1 szczypta</span><span>soli i pieprzu</span><span class="p-ing__g">0.25 g</span></li>
<li><span class="p-ing__q">7 łyżek</span><span>makaronu razowego</span><span class="p-ing__g">35 g</span></li>
<li><span class="p-ing__q">1 łyżeczka</span><span>oliwy z oliwek</span><span class="p-ing__g">5 g</span></li>
<li><span class="p-ing__q">3 plastry</span><span>mozzarelli</span><span class="p-ing__g">45 g</span></li>
<li><span class="p-ing__q">1 sztuka</span><span>selera naciowego</span><span class="p-ing__g">45 g</span></li>
<li><span class="p-ing__q">1 sztuka</span><span>małej cebuli</span><span class="p-ing__g">30 g</span></li>
<li><span class="p-ing__q">1 ząbek</span><span>czosnku</span><span class="p-ing__g">6 g</span></li>
<li><span class="p-ing__q">1 sztuka</span><span>marchewki</span><span class="p-ing__g">45 g</span></li>
<li data-pantry="1"><span class="p-ing__q">1 szklanka</span><span>wody</span><span class="p-ing__g">250 g</span></li>
<li><span class="p-ing__q">0.5 sztuki</span><span>papryki czerwonej</span><span class="p-ing__g">85 g</span></li>
</ul>

<div class="p-actions">
<button type="button" class="p-btn p-btn--block" id="open-shopping">&#128722; Lista zakupów</button>
<button type="button" class="p-btn p-btn--primary p-btn--block" id="cook-start">Gotujmy &rarr;</button>
</div>

<h2>Sposób przygotowania</h2>
<ol class="p-steps">
<li>Paprykę, seler, cebulę i marchewkę kroimy w kostkę, czosnek siekamy.</li>
<li>Na rozgrzanej oliwie w rondelku podsmażamy warzywa, dodajemy paprykę wędzoną. Po 7 minutach dodajemy pomidory, wodę i bazylię. Gotujemy przez 10 minut.</li>
<li>Całość blendujemy i doprawiamy solą i pieprzem. Gotujemy jeszcze przez 5 minut.</li>
<li>Makaron gotujemy według instrukcji na opakowaniu</li>
<li>Mozzarellę kroimy w drobną kostkę.</li>
<li>Zupę podajemy z makaronem i mozzarellą.</li>
</ol>

<div class="p-cook" id="cook" data-open="0" role="dialog" aria-modal="true" aria-label="Gotowanie: Krem paprykowo-pomidorowy">
<div class="p-cook__bar">
<span class="p-cook__title">Krem paprykowo-pomidorowy</span>
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

<script>window.RECIPE = {"slug": "krem-paprykowo-pomidorowy", "title": "Krem paprykowo-pomidorowy", "day": 2, "slotLabel": "Obiad", "time": "14:00-17:00", "baseServings": 1, "ingredients": [{"qty": 0.5, "unit": "opakowania", "unitLemma": "opakowanie", "name": "pomidorów w puszce", "grams": 200.0, "pantry": false, "tag": "pomidory-puszka"}, {"qty": 1.0, "unit": "szczypta", "unitLemma": "szczypta", "name": "papryki wędzonej", "grams": 0.5, "pantry": true, "tag": null}, {"qty": 1.0, "unit": "garść", "unitLemma": "garść", "name": "świeżej bazylii", "grams": 3.0, "pantry": true, "tag": null}, {"qty": 1.0, "unit": "szczypta", "unitLemma": "szczypta", "name": "soli i pieprzu", "grams": 0.25, "pantry": true, "tag": null}, {"qty": 7.0, "unit": "łyżek", "unitLemma": "łyżka", "name": "makaronu razowego", "grams": 35.0, "pantry": false, "tag": "makaron"}, {"qty": 1.0, "unit": "łyżeczka", "unitLemma": "łyżeczka", "name": "oliwy z oliwek", "grams": 5.0, "pantry": false, "tag": "oliwa"}, {"qty": 3.0, "unit": "plastry", "unitLemma": "plaster", "name": "mozzarelli", "grams": 45.0, "pantry": false, "tag": "mozzarella"}, {"qty": 1.0, "unit": "sztuka", "unitLemma": "sztuka", "name": "selera naciowego", "grams": 45.0, "pantry": false, "tag": "seler"}, {"qty": 1.0, "unit": "sztuka", "unitLemma": "sztuka", "name": "małej cebuli", "grams": 30.0, "pantry": false, "tag": "cebula"}, {"qty": 1.0, "unit": "ząbek", "unitLemma": "ząbek", "name": "czosnku", "grams": 6.0, "pantry": false, "tag": "czosnek"}, {"qty": 1.0, "unit": "sztuka", "unitLemma": "sztuka", "name": "marchewki", "grams": 45.0, "pantry": false, "tag": "marchewka"}, {"qty": 1.0, "unit": "szklanka", "unitLemma": "szklanka", "name": "wody", "grams": 250.0, "pantry": true, "tag": null}, {"qty": 0.5, "unit": "sztuki", "unitLemma": "sztuka", "name": "papryki czerwonej", "grams": 85.0, "pantry": false, "tag": "papryka"}], "steps": ["Paprykę, seler, cebulę i marchewkę kroimy w kostkę, czosnek siekamy.", "Na rozgrzanej oliwie w rondelku podsmażamy warzywa, dodajemy paprykę wędzoną. Po 7 minutach dodajemy pomidory, wodę i bazylię. Gotujemy przez 10 minut.", "Całość blendujemy i doprawiamy solą i pieprzem. Gotujemy jeszcze przez 5 minut.", "Makaron gotujemy według instrukcji na opakowaniu", "Mozzarellę kroimy w drobną kostkę.", "Zupę podajemy z makaronem i mozzarellą."]};
window.UNITS = {"łyżka": ["łyżka", "łyżki", "łyżek", "łyżki"], "łyżeczka": ["łyżeczka", "łyżeczki", "łyżeczek", "łyżeczki"], "sztuka": ["sztuka", "sztuki", "sztuk", "sztuki"], "garść": ["garść", "garście", "garści", "garści"], "kromka": ["kromka", "kromki", "kromek", "kromki"], "plaster": ["plaster", "plastry", "plastrów", "plastra"], "szklanka": ["szklanka", "szklanki", "szklanek", "szklanki"], "opakowanie": ["opakowanie", "opakowania", "opakowań", "opakowania"], "ząbek": ["ząbek", "ząbki", "ząbków", "ząbka"], "szczypta": ["szczypta", "szczypty", "szczypt", "szczypty"], "porcja": ["porcja", "porcje", "porcji", "porcji"], "puszka": ["puszka", "puszki", "puszek", "puszki"]};</script>
