---
hide:
  - toc
---

<a class="p-back" href="../../">&larr; Wszystkie przepisy</a>

# Pasta z wędzonego pstrąga i twarogu ze szczypiorkiem, warzywami i pieczywem

<div class="p-hero" data-slot="2">
<div class="p-hero__top">
<span>II śniadanie</span><span class="p-num">10:00-13:00</span><span class="p-num">Dzień 9</span>
</div>
<div class="p-macros">
<div class="p-macro"><span class="p-macro__v">446</span><span class="p-macro__l">kcal</span></div>
<div class="p-macro"><span class="p-macro__v">31 g</span><span class="p-macro__l">białko</span></div>
<div class="p-macro"><span class="p-macro__v">41 g</span><span class="p-macro__l">węgl.</span></div>
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
<li><span class="p-ing__q">2 kromki</span><span>chleba żytniego razowego</span><span class="p-ing__g">60 g</span></li>
<li><span class="p-ing__q">2 opakowania</span><span>twarogu tłustego</span><span class="p-ing__g">60 g</span></li>
<li><span class="p-ing__q">2 porcje</span><span>pstrąga wędzonego</span><span class="p-ing__g">60 g</span></li>
<li><span class="p-ing__q">0.5 sztuki</span><span>ogórka zielonego</span><span class="p-ing__g">75 g</span></li>
<li><span class="p-ing__q">6 sztuk</span><span>rzodkiewek</span><span class="p-ing__g">90 g</span></li>
<li><span class="p-ing__q">1 garść</span><span>rukoli</span><span class="p-ing__g">20 g</span></li>
<li data-pantry="1"><span class="p-ing__q">3 łyżeczki</span><span>koperku</span><span class="p-ing__g">12 g</span></li>
<li data-pantry="1"><span class="p-ing__q">2 łyżeczki</span><span>szczypiorku</span><span class="p-ing__g">10 g</span></li>
<li data-pantry="1"><span class="p-ing__q">1 szczypta</span><span>soli i pieprzu</span><span class="p-ing__g">0.25 g</span></li>
<li><span class="p-ing__q">2 łyżeczki</span><span>masła</span><span class="p-ing__g">10 g</span></li>
</ul>

<div class="p-actions">
<button type="button" class="p-btn p-btn--block" id="open-shopping">&#128722; Lista zakupów</button>
<button type="button" class="p-btn p-btn--primary p-btn--block" id="cook-start">Gotujmy &rarr;</button>
</div>

<h2>Sposób przygotowania</h2>
<ol class="p-steps">
<li>Pstrąga obieramy z ości i dzielimy na mniejsze kawałki.</li>
<li>Siekamy szczypiorek i przekładamy do miski.</li>
<li>Dodajemy twaróg, dokładnie mieszamy. Doprawiamy solą i pieprzem.</li>
<li>Gotową pastę podajemy z pokrojonymi warzywami: rzodkiewką, ogórkiem, rukolą i pieczywem posmarowanym masłem. Smacznego!</li>
</ol>

<div class="p-cook" id="cook" data-open="0" role="dialog" aria-modal="true" aria-label="Gotowanie: Pasta z wędzonego pstrąga i twarogu ze szczypiorkiem, warzywami i pieczywem">
<div class="p-cook__bar">
<span class="p-cook__title">Pasta z wędzonego pstrąga i twarogu ze szczypiorkiem, warzywami i pieczywem</span>
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

<script>window.RECIPE = {"slug": "pasta-z-pstroga", "title": "Pasta z wędzonego pstrąga i twarogu ze szczypiorkiem, warzywami i pieczywem", "day": 9, "slotLabel": "II śniadanie", "time": "10:00-13:00", "baseServings": 1, "ingredients": [{"qty": 2.0, "unit": "kromki", "unitLemma": "kromka", "name": "chleba żytniego razowego", "grams": 60.0, "pantry": false, "tag": "chleb"}, {"qty": 2.0, "unit": "opakowania", "unitLemma": "opakowanie", "name": "twarogu tłustego", "grams": 60.0, "pantry": false, "tag": "twarog"}, {"qty": 2.0, "unit": "porcje", "unitLemma": "porcja", "name": "pstrąga wędzonego", "grams": 60.0, "pantry": false, "tag": "pstrag"}, {"qty": 0.5, "unit": "sztuki", "unitLemma": "sztuka", "name": "ogórka zielonego", "grams": 75.0, "pantry": false, "tag": "ogorek"}, {"qty": 6.0, "unit": "sztuk", "unitLemma": "sztuka", "name": "rzodkiewek", "grams": 90.0, "pantry": false, "tag": "rzodkiewka"}, {"qty": 1.0, "unit": "garść", "unitLemma": "garść", "name": "rukoli", "grams": 20.0, "pantry": false, "tag": "salata"}, {"qty": 3.0, "unit": "łyżeczki", "unitLemma": "łyżeczka", "name": "koperku", "grams": 12.0, "pantry": true, "tag": null}, {"qty": 2.0, "unit": "łyżeczki", "unitLemma": "łyżeczka", "name": "szczypiorku", "grams": 10.0, "pantry": true, "tag": null}, {"qty": 1.0, "unit": "szczypta", "unitLemma": "szczypta", "name": "soli i pieprzu", "grams": 0.25, "pantry": true, "tag": null}, {"qty": 2.0, "unit": "łyżeczki", "unitLemma": "łyżeczka", "name": "masła", "grams": 10.0, "pantry": false, "tag": "maslo"}], "steps": ["Pstrąga obieramy z ości i dzielimy na mniejsze kawałki.", "Siekamy szczypiorek i przekładamy do miski.", "Dodajemy twaróg, dokładnie mieszamy. Doprawiamy solą i pieprzem.", "Gotową pastę podajemy z pokrojonymi warzywami: rzodkiewką, ogórkiem, rukolą i pieczywem posmarowanym masłem. Smacznego!"]};
window.UNITS = {"łyżka": ["łyżka", "łyżki", "łyżek", "łyżki"], "łyżeczka": ["łyżeczka", "łyżeczki", "łyżeczek", "łyżeczki"], "sztuka": ["sztuka", "sztuki", "sztuk", "sztuki"], "garść": ["garść", "garście", "garści", "garści"], "kromka": ["kromka", "kromki", "kromek", "kromki"], "plaster": ["plaster", "plastry", "plastrów", "plastra"], "szklanka": ["szklanka", "szklanki", "szklanek", "szklanki"], "opakowanie": ["opakowanie", "opakowania", "opakowań", "opakowania"], "ząbek": ["ząbek", "ząbki", "ząbków", "ząbka"], "szczypta": ["szczypta", "szczypty", "szczypt", "szczypty"], "porcja": ["porcja", "porcje", "porcji", "porcji"], "puszka": ["puszka", "puszki", "puszek", "puszki"]};</script>
