---
hide:
  - toc
---

<a class="p-back" href="../../">&larr; Wszystkie przepisy</a>

# Kanapka z pastą z ciecierzycy

<div class="p-hero" data-slot="2">
<div class="p-hero__top">
<span>II śniadanie</span><span class="p-num">10:00-13:00</span><span class="p-num">Dzień 5</span>
</div>
<div class="p-macros">
<div class="p-macro"><span class="p-macro__v">465</span><span class="p-macro__l">kcal</span></div>
<div class="p-macro"><span class="p-macro__v">14 g</span><span class="p-macro__l">białko</span></div>
<div class="p-macro"><span class="p-macro__v">60 g</span><span class="p-macro__l">węgl.</span></div>
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

<h2 id="ing-heading">Składniki na 1 osobę</h2>
<ul class="p-ings" id="ing-list">
<li><span class="p-ing__q">4 łyżki</span><span>ciecierzycy konserwowej</span><span class="p-ing__g">80 g</span></li>
<li><span class="p-ing__q">1 ząbek</span><span>czosnku</span><span class="p-ing__g">6 g</span></li>
<li><span class="p-ing__q">3 łyżeczki</span><span>oliwy</span><span class="p-ing__g">15 g</span></li>
<li data-pantry="1"><span class="p-ing__q">1 szczypta</span><span>kuminu</span><span class="p-ing__g">1 g</span></li>
<li data-pantry="1"><span class="p-ing__q">1 łyżeczka</span><span>kolendry</span><span class="p-ing__g">1 g</span></li>
<li data-pantry="1"><span class="p-ing__q">1 łyżeczka</span><span>papryki słodkiej</span><span class="p-ing__g">3 g</span></li>
<li><span class="p-ing__q">2 łyżki</span><span>soku z cytryny</span><span class="p-ing__g">12 g</span></li>
<li><span class="p-ing__q">2 kromki</span><span>chleba żytniego</span><span class="p-ing__g">60 g</span></li>
<li><span class="p-ing__q">3 łyżki</span><span>kiełków rzodkiewki</span><span class="p-ing__g">24 g</span></li>
<li><span class="p-ing__q">0.5 sztuki</span><span>ogórka</span><span class="p-ing__g">75 g</span></li>
<li><span class="p-ing__q">1 sztuka</span><span>marchewki</span><span class="p-ing__g">45 g</span></li>
</ul>

<div class="p-actions">
<button type="button" class="p-btn p-btn--block" id="open-shopping">&#128722; Lista zakupów</button>
<button type="button" class="p-btn p-btn--primary p-btn--block" id="cook-start">Gotujmy &rarr;</button>
</div>

<h2>Sposób przygotowania</h2>
<ol class="p-steps">
<li>Do blendera wkładamy składniki na pastę, blendujemy do momentu uzyskania jednolitej masy, doprawiamy solą i znowu mieszamy.</li>
<li>Kromki pieczywa smarujemy pastą i układamy kiełki, plastry ogórka i wstążki z marchewki.</li>
</ol>

<div class="p-cook" id="cook" data-open="0" role="dialog" aria-modal="true" aria-label="Gotowanie: Kanapka z pastą z ciecierzycy">
<div class="p-cook__bar">
<span class="p-cook__title">Kanapka z pastą z ciecierzycy</span>
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

<script>window.RECIPE = {"slug": "kanapka-z-pasta-z-ciecierzycy", "title": "Kanapka z pastą z ciecierzycy", "day": 5, "slotLabel": "II śniadanie", "time": "10:00-13:00", "baseServings": 1, "ingredients": [{"qty": 4.0, "unit": "łyżki", "unitLemma": "łyżka", "name": "ciecierzycy konserwowej", "grams": 80.0, "pantry": false, "tag": "ciecierzyca"}, {"qty": 1.0, "unit": "ząbek", "unitLemma": "ząbek", "name": "czosnku", "grams": 6.0, "pantry": false, "tag": "czosnek"}, {"qty": 3.0, "unit": "łyżeczki", "unitLemma": "łyżeczka", "name": "oliwy", "grams": 15.0, "pantry": false, "tag": "oliwa"}, {"qty": 1.0, "unit": "szczypta", "unitLemma": "szczypta", "name": "kuminu", "grams": 1.0, "pantry": true, "tag": null}, {"qty": 1.0, "unit": "łyżeczka", "unitLemma": "łyżeczka", "name": "kolendry", "grams": 1.0, "pantry": true, "tag": null}, {"qty": 1.0, "unit": "łyżeczka", "unitLemma": "łyżeczka", "name": "papryki słodkiej", "grams": 3.0, "pantry": true, "tag": null}, {"qty": 2.0, "unit": "łyżki", "unitLemma": "łyżka", "name": "soku z cytryny", "grams": 12.0, "pantry": false, "tag": "cytryna"}, {"qty": 2.0, "unit": "kromki", "unitLemma": "kromka", "name": "chleba żytniego", "grams": 60.0, "pantry": false, "tag": "chleb"}, {"qty": 3.0, "unit": "łyżki", "unitLemma": "łyżka", "name": "kiełków rzodkiewki", "grams": 24.0, "pantry": false, "tag": "kielki"}, {"qty": 0.5, "unit": "sztuki", "unitLemma": "sztuka", "name": "ogórka", "grams": 75.0, "pantry": false, "tag": "ogorek"}, {"qty": 1.0, "unit": "sztuka", "unitLemma": "sztuka", "name": "marchewki", "grams": 45.0, "pantry": false, "tag": "marchewka"}], "steps": ["Do blendera wkładamy składniki na pastę, blendujemy do momentu uzyskania jednolitej masy, doprawiamy solą i znowu mieszamy.", "Kromki pieczywa smarujemy pastą i układamy kiełki, plastry ogórka i wstążki z marchewki."]};
window.UNITS = {"łyżka": ["łyżka", "łyżki", "łyżek", "łyżki"], "łyżeczka": ["łyżeczka", "łyżeczki", "łyżeczek", "łyżeczki"], "sztuka": ["sztuka", "sztuki", "sztuk", "sztuki"], "garść": ["garść", "garście", "garści", "garści"], "kromka": ["kromka", "kromki", "kromek", "kromki"], "plaster": ["plaster", "plastry", "plastrów", "plastra"], "szklanka": ["szklanka", "szklanki", "szklanek", "szklanki"], "opakowanie": ["opakowanie", "opakowania", "opakowań", "opakowania"], "ząbek": ["ząbek", "ząbki", "ząbków", "ząbka"], "szczypta": ["szczypta", "szczypty", "szczypt", "szczypty"], "porcja": ["porcja", "porcje", "porcji", "porcji"], "puszka": ["puszka", "puszki", "puszek", "puszki"]};</script>
