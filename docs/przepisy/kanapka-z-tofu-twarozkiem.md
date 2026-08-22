---
hide:
  - toc
---

<a class="p-back" href="../../">&larr; Wszystkie przepisy</a>

# Kanapka z tofu twarożkiem

<div class="p-hero" data-slot="2">
<div class="p-hero__top">
<span>II śniadanie</span><span class="p-num">10:00-13:00</span><span class="p-num">Dzień 7</span>
</div>
<div class="p-macros">
<div class="p-macro"><span class="p-macro__v">457</span><span class="p-macro__l">kcal</span></div>
<div class="p-macro"><span class="p-macro__v">18 g</span><span class="p-macro__l">białko</span></div>
<div class="p-macro"><span class="p-macro__v">57 g</span><span class="p-macro__l">węgl.</span></div>
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
<li><span class="p-ing__q">1 sztuka</span><span>bułki grahamki</span><span class="p-ing__g">80 g</span></li>
<li><span class="p-ing__q">1 łyżka</span><span>serka śmietankowego</span><span class="p-ing__g">25 g</span></li>
<li><span class="p-ing__q">1 łyżeczka</span><span>majonezu wegańskiego</span><span class="p-ing__g">15 g</span></li>
<li><span class="p-ing__q">0.5 opakowania</span><span>tofu naturalnego</span><span class="p-ing__g">90 g</span></li>
<li><span class="p-ing__q">2 sztuki</span><span>ogórków kiszonych</span><span class="p-ing__g">100 g</span></li>
<li><span class="p-ing__q">1 sztuka</span><span>pomidora</span><span class="p-ing__g">160 g</span></li>
<li data-pantry="1"><span class="p-ing__q">3 łyżeczki</span><span>szczypiorku</span><span class="p-ing__g">15 g</span></li>
</ul>

<div class="p-actions">
<button type="button" class="p-btn p-btn--block" id="open-shopping">&#128722; Lista zakupów</button>
<button type="button" class="p-btn p-btn--primary p-btn--block" id="cook-start">Gotujmy &rarr;</button>
</div>

<h2>Sposób przygotowania</h2>
<ol class="p-steps">
<li>Bułkę kroimy na pół, smarujemy serkiem śmietankowym.</li>
<li>Tofu przekładamy do miseczki, dodajemy majonez i rozgniatamy widelcem.</li>
<li>Ogórki drobno siekamy. Dodajemy do twarożku, mieszamy.</li>
<li>Bułkę smarujemy twarożkiem, jemy z pomidorem i posiekanym szczypiorkiem.</li>
</ol>

<div class="p-cook" id="cook" data-open="0" role="dialog" aria-modal="true" aria-label="Gotowanie: Kanapka z tofu twarożkiem">
<div class="p-cook__bar">
<span class="p-cook__title">Kanapka z tofu twarożkiem</span>
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

<script>window.RECIPE = {"slug": "kanapka-z-tofu-twarozkiem", "title": "Kanapka z tofu twarożkiem", "day": 7, "slotLabel": "II śniadanie", "time": "10:00-13:00", "baseServings": 1, "ingredients": [{"qty": 1.0, "unit": "sztuka", "unitLemma": "sztuka", "name": "bułki grahamki", "grams": 80.0, "pantry": false, "tag": "bulka"}, {"qty": 1.0, "unit": "łyżka", "unitLemma": "łyżka", "name": "serka śmietankowego", "grams": 25.0, "pantry": false, "tag": "serek-smietankowy"}, {"qty": 1.0, "unit": "łyżeczka", "unitLemma": "łyżeczka", "name": "majonezu wegańskiego", "grams": 15.0, "pantry": false, "tag": "majonez"}, {"qty": 0.5, "unit": "opakowania", "unitLemma": "opakowanie", "name": "tofu naturalnego", "grams": 90.0, "pantry": false, "tag": "tofu"}, {"qty": 2.0, "unit": "sztuki", "unitLemma": "sztuka", "name": "ogórków kiszonych", "grams": 100.0, "pantry": false, "tag": "ogorki-kiszone"}, {"qty": 1.0, "unit": "sztuka", "unitLemma": "sztuka", "name": "pomidora", "grams": 160.0, "pantry": false, "tag": "pomidor"}, {"qty": 3.0, "unit": "łyżeczki", "unitLemma": "łyżeczka", "name": "szczypiorku", "grams": 15.0, "pantry": true, "tag": null}], "steps": ["Bułkę kroimy na pół, smarujemy serkiem śmietankowym.", "Tofu przekładamy do miseczki, dodajemy majonez i rozgniatamy widelcem.", "Ogórki drobno siekamy. Dodajemy do twarożku, mieszamy.", "Bułkę smarujemy twarożkiem, jemy z pomidorem i posiekanym szczypiorkiem."]};
window.UNITS = {"łyżka": ["łyżka", "łyżki", "łyżek", "łyżki"], "łyżeczka": ["łyżeczka", "łyżeczki", "łyżeczek", "łyżeczki"], "sztuka": ["sztuka", "sztuki", "sztuk", "sztuki"], "garść": ["garść", "garście", "garści", "garści"], "kromka": ["kromka", "kromki", "kromek", "kromki"], "plaster": ["plaster", "plastry", "plastrów", "plastra"], "szklanka": ["szklanka", "szklanki", "szklanek", "szklanki"], "opakowanie": ["opakowanie", "opakowania", "opakowań", "opakowania"], "ząbek": ["ząbek", "ząbki", "ząbków", "ząbka"], "szczypta": ["szczypta", "szczypty", "szczypt", "szczypty"], "porcja": ["porcja", "porcje", "porcji", "porcji"], "puszka": ["puszka", "puszki", "puszek", "puszki"]};</script>
