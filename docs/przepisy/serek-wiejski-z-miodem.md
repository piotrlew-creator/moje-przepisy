---
hide:
  - toc
---

<a class="p-back" href="../../">&larr; Wszystkie przepisy</a>

# Serek wiejski z miodem, orzechami i gruszką

<div class="p-hero" data-slot="1">
<div class="p-hero__top">
<span>Śniadanie</span><span class="p-num">6:00-9:00</span><span class="p-num">Dzień 5</span>
</div>
<div class="p-macros">
<div class="p-macro"><span class="p-macro__v">467</span><span class="p-macro__l">kcal</span></div>
<div class="p-macro"><span class="p-macro__v">30 g</span><span class="p-macro__l">białko</span></div>
<div class="p-macro"><span class="p-macro__v">42 g</span><span class="p-macro__l">węgl.</span></div>
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
<li><span class="p-ing__q">1 opakowanie</span><span>serka wiejskiego</span><span class="p-ing__g">200 g</span></li>
<li><span class="p-ing__q">0.5 łyżeczki</span><span>miodu</span><span class="p-ing__g">6 g</span></li>
<li><span class="p-ing__q">5 sztuk</span><span>orzechów włoskich</span><span class="p-ing__g">20 g</span></li>
<li><span class="p-ing__q">1 sztuka</span><span>gruszki</span><span class="p-ing__g">130 g</span></li>
<li><span class="p-ing__q">1 sztuka</span><span>wafli ryżowych</span><span class="p-ing__g">10 g</span></li>
</ul>

<div class="p-actions">
<button type="button" class="p-btn p-btn--block" id="open-shopping">&#128722; Lista zakupów</button>
<button type="button" class="p-btn p-btn--primary p-btn--block" id="cook-start">Gotujmy &rarr;</button>
</div>

<h2>Sposób przygotowania</h2>
<ol class="p-steps">
<li>Gruszkę myjemy i kroimy w kostkę, orzechy siekamy.</li>
<li>Pokrojoną gruszkę wraz z orzechami dodajemy do serka wiejskiego, polewamy miodem i mieszamy. Zjadamy z waflami ryżowymi.</li>
</ol>

<div class="p-cook" id="cook" data-open="0" role="dialog" aria-modal="true" aria-label="Gotowanie: Serek wiejski z miodem, orzechami i gruszką">
<div class="p-cook__bar">
<span class="p-cook__title">Serek wiejski z miodem, orzechami i gruszką</span>
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

<script>window.RECIPE = {"slug": "serek-wiejski-z-miodem", "title": "Serek wiejski z miodem, orzechami i gruszką", "day": 5, "slotLabel": "Śniadanie", "time": "6:00-9:00", "baseServings": 1, "ingredients": [{"qty": 1.0, "unit": "opakowanie", "unitLemma": "opakowanie", "name": "serka wiejskiego", "grams": 200.0, "pantry": false, "tag": "serek-wiejski"}, {"qty": 0.5, "unit": "łyżeczki", "unitLemma": "łyżeczka", "name": "miodu", "grams": 6.0, "pantry": false, "tag": "miod"}, {"qty": 5.0, "unit": "sztuk", "unitLemma": "sztuka", "name": "orzechów włoskich", "grams": 20.0, "pantry": false, "tag": "orzechy"}, {"qty": 1.0, "unit": "sztuka", "unitLemma": "sztuka", "name": "gruszki", "grams": 130.0, "pantry": false, "tag": "gruszka"}, {"qty": 1.0, "unit": "sztuka", "unitLemma": "sztuka", "name": "wafli ryżowych", "grams": 10.0, "pantry": false, "tag": "wafle"}], "steps": ["Gruszkę myjemy i kroimy w kostkę, orzechy siekamy.", "Pokrojoną gruszkę wraz z orzechami dodajemy do serka wiejskiego, polewamy miodem i mieszamy. Zjadamy z waflami ryżowymi."]};
window.UNITS = {"łyżka": ["łyżka", "łyżki", "łyżek", "łyżki"], "łyżeczka": ["łyżeczka", "łyżeczki", "łyżeczek", "łyżeczki"], "sztuka": ["sztuka", "sztuki", "sztuk", "sztuki"], "garść": ["garść", "garście", "garści", "garści"], "kromka": ["kromka", "kromki", "kromek", "kromki"], "plaster": ["plaster", "plastry", "plastrów", "plastra"], "szklanka": ["szklanka", "szklanki", "szklanek", "szklanki"], "opakowanie": ["opakowanie", "opakowania", "opakowań", "opakowania"], "ząbek": ["ząbek", "ząbki", "ząbków", "ząbka"], "szczypta": ["szczypta", "szczypty", "szczypt", "szczypty"], "porcja": ["porcja", "porcje", "porcji", "porcji"], "puszka": ["puszka", "puszki", "puszek", "puszki"]};</script>
