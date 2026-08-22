---
hide:
  - toc
---

<a class="p-back" href="../../">&larr; Wszystkie przepisy</a>

# Wegańskie spaghetti bolognese

<div class="p-hero" data-slot="3">
<div class="p-hero__top">
<span>Obiad</span><span class="p-num">14:00-17:00</span><span class="p-num">Dzień 5</span>
</div>
<div class="p-macros">
<div class="p-macro"><span class="p-macro__v">385</span><span class="p-macro__l">kcal</span></div>
<div class="p-macro"><span class="p-macro__v">25 g</span><span class="p-macro__l">białko</span></div>
<div class="p-macro"><span class="p-macro__v">49 g</span><span class="p-macro__l">węgl.</span></div>
<div class="p-macro"><span class="p-macro__v">11 g</span><span class="p-macro__l">tłuszcz</span></div>
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
<li><span class="p-ing__q">1 opakowanie</span><span>tofu naturalnego</span><span class="p-ing__g">180 g</span></li>
<li><span class="p-ing__q">1 porcja</span><span>makaronu spaghetti pełnoziarnistego</span><span class="p-ing__g">50 g</span></li>
<li><span class="p-ing__q">1 sztuka</span><span>marchewki</span><span class="p-ing__g">45 g</span></li>
<li><span class="p-ing__q">1 sztuka</span><span>cebuli</span><span class="p-ing__g">20 g</span></li>
<li><span class="p-ing__q">1 ząbek</span><span>czosnku</span><span class="p-ing__g">6 g</span></li>
<li><span class="p-ing__q">0.5 opakowania</span><span>pomidorów w puszce</span><span class="p-ing__g">200 g</span></li>
<li><span class="p-ing__q">0.5 łyżki</span><span>sosu sojowego</span><span class="p-ing__g">5 g</span></li>
<li data-pantry="1"><span class="p-ing__q">1 szczypta</span><span>papryki wędzonej słodkiej</span><span class="p-ing__g">0.5 g</span></li>
<li data-pantry="1"><span class="p-ing__q">1 szczypta</span><span>soli</span><span class="p-ing__g">0.25 g</span></li>
<li data-pantry="1"><span class="p-ing__q">1 szczypta</span><span>pieprzu</span><span class="p-ing__g">0.25 g</span></li>
</ul>

<div class="p-actions">
<button type="button" class="p-btn p-btn--block" id="open-shopping">&#128722; Lista zakupów</button>
<button type="button" class="p-btn p-btn--primary p-btn--block" id="cook-start">Gotujmy &rarr;</button>
</div>

<h2>Sposób przygotowania</h2>
<ol class="p-steps">
<li>Tofu odsączamy i rozdrabniamy, dodajemy do niego sos sojowy i paprykę wędzoną. Smażymy na rozgrzanej patelni przez 7-8 minut, następnie odstawiamy na bok.</li>
<li>Na tej samej patelni podsmażamy pokrojoną cebulę, czosnek oraz startą marchewkę przez około 8 minut.</li>
<li>Dodajemy podsmażone tofu i puszkę pomidorów oraz 100 ml wody</li>
<li>Dusimy przez 25 minut, następnie dodajemy listki bazylii oraz doprawiamy solą i pieprzem.</li>
<li>Makaron gotujemy według instrukcji na opakowaniu</li>
</ol>

<div class="p-cook" id="cook" data-open="0" role="dialog" aria-modal="true" aria-label="Gotowanie: Wegańskie spaghetti bolognese">
<div class="p-cook__bar">
<span class="p-cook__title">Wegańskie spaghetti bolognese</span>
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

<script>window.RECIPE = {"slug": "spaghetti-bolognese", "title": "Wegańskie spaghetti bolognese", "day": 5, "slotLabel": "Obiad", "time": "14:00-17:00", "baseServings": 1, "ingredients": [{"qty": 1.0, "unit": "opakowanie", "unitLemma": "opakowanie", "name": "tofu naturalnego", "grams": 180.0, "pantry": false, "tag": "tofu"}, {"qty": 1.0, "unit": "porcja", "unitLemma": "porcja", "name": "makaronu spaghetti pełnoziarnistego", "grams": 50.0, "pantry": false, "tag": "makaron"}, {"qty": 1.0, "unit": "sztuka", "unitLemma": "sztuka", "name": "marchewki", "grams": 45.0, "pantry": false, "tag": "marchewka"}, {"qty": 1.0, "unit": "sztuka", "unitLemma": "sztuka", "name": "cebuli", "grams": 20.0, "pantry": false, "tag": "cebula"}, {"qty": 1.0, "unit": "ząbek", "unitLemma": "ząbek", "name": "czosnku", "grams": 6.0, "pantry": false, "tag": "czosnek"}, {"qty": 0.5, "unit": "opakowania", "unitLemma": "opakowanie", "name": "pomidorów w puszce", "grams": 200.0, "pantry": false, "tag": "pomidory-puszka"}, {"qty": 0.5, "unit": "łyżki", "unitLemma": "łyżka", "name": "sosu sojowego", "grams": 5.0, "pantry": false, "tag": "sos-sojowy"}, {"qty": 1.0, "unit": "szczypta", "unitLemma": "szczypta", "name": "papryki wędzonej słodkiej", "grams": 0.5, "pantry": true, "tag": null}, {"qty": 1.0, "unit": "szczypta", "unitLemma": "szczypta", "name": "soli", "grams": 0.25, "pantry": true, "tag": null}, {"qty": 1.0, "unit": "szczypta", "unitLemma": "szczypta", "name": "pieprzu", "grams": 0.25, "pantry": true, "tag": null}], "steps": ["Tofu odsączamy i rozdrabniamy, dodajemy do niego sos sojowy i paprykę wędzoną. Smażymy na rozgrzanej patelni przez 7-8 minut, następnie odstawiamy na bok.", "Na tej samej patelni podsmażamy pokrojoną cebulę, czosnek oraz startą marchewkę przez około 8 minut.", "Dodajemy podsmażone tofu i puszkę pomidorów oraz 100 ml wody", "Dusimy przez 25 minut, następnie dodajemy listki bazylii oraz doprawiamy solą i pieprzem.", "Makaron gotujemy według instrukcji na opakowaniu"]};
window.UNITS = {"łyżka": ["łyżka", "łyżki", "łyżek", "łyżki"], "łyżeczka": ["łyżeczka", "łyżeczki", "łyżeczek", "łyżeczki"], "sztuka": ["sztuka", "sztuki", "sztuk", "sztuki"], "garść": ["garść", "garście", "garści", "garści"], "kromka": ["kromka", "kromki", "kromek", "kromki"], "plaster": ["plaster", "plastry", "plastrów", "plastra"], "szklanka": ["szklanka", "szklanki", "szklanek", "szklanki"], "opakowanie": ["opakowanie", "opakowania", "opakowań", "opakowania"], "ząbek": ["ząbek", "ząbki", "ząbków", "ząbka"], "szczypta": ["szczypta", "szczypty", "szczypt", "szczypty"], "porcja": ["porcja", "porcje", "porcji", "porcji"], "puszka": ["puszka", "puszki", "puszek", "puszki"]};</script>
