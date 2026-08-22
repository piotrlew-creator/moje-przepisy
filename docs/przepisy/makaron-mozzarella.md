---
hide:
  - toc
---

<a class="p-back" href="../../">&larr; Wszystkie przepisy</a>

# Makaron z mozzarellą, szpinakiem, ogórkiem i pomidorkami koktajlowymi

<div class="p-hero" data-slot="3">
<div class="p-hero__top">
<span>Obiad</span><span class="p-num">14:00-17:00</span><span class="p-num">Dzień 1</span>
</div>
<div class="p-macros">
<div class="p-macro"><span class="p-macro__v">381</span><span class="p-macro__l">kcal</span></div>
<div class="p-macro"><span class="p-macro__v">23 g</span><span class="p-macro__l">białko</span></div>
<div class="p-macro"><span class="p-macro__v">40 g</span><span class="p-macro__l">węgl.</span></div>
<div class="p-macro"><span class="p-macro__v">13 g</span><span class="p-macro__l">tłuszcz</span></div>
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
<li><span class="p-ing__q">1 porcja</span><span>makaronu pełnoziarnistego</span><span class="p-ing__g">50 g</span></li>
<li><span class="p-ing__q">2 łyżeczki</span><span>zielonego pesto</span><span class="p-ing__g">10 g</span></li>
<li><span class="p-ing__q">7 sztuk</span><span>pomidorków koktajlowych</span><span class="p-ing__g">140 g</span></li>
<li data-pantry="1"><span class="p-ing__q">0.5 garści</span><span>bazylii świeżej</span><span class="p-ing__g">1.5 g</span></li>
<li><span class="p-ing__q">2 garści</span><span>szpinaku</span><span class="p-ing__g">50 g</span></li>
<li><span class="p-ing__q">0.5 sztuki</span><span>ogórka</span><span class="p-ing__g">75 g</span></li>
<li><span class="p-ing__q">3 plastry</span><span>mozzarelli light</span><span class="p-ing__g">45 g</span></li>
<li><span class="p-ing__q">1 łyżka</span><span>sera grana padano</span><span class="p-ing__g">10 g</span></li>
<li data-pantry="1"><span class="p-ing__q">1 szczypta</span><span>soli</span><span class="p-ing__g">0.25 g</span></li>
<li data-pantry="1"><span class="p-ing__q">1 szczypta</span><span>pieprzu</span><span class="p-ing__g">0.25 g</span></li>
</ul>

<div class="p-actions">
<button type="button" class="p-btn p-btn--block" id="open-shopping">&#128722; Lista zakupów</button>
<button type="button" class="p-btn p-btn--primary p-btn--block" id="cook-start">Gotujmy &rarr;</button>
</div>

<h2>Sposób przygotowania</h2>
<ol class="p-steps">
<li>Makaron gotujemy według instrukcji umieszczonej na opakowaniu.</li>
<li>Kroimy pomidorki, ogórek zielony, siekamy bazylię.</li>
<li>Do miski dodajemy makaron, pokrojone warzywa, posiekaną bazylię, umyty szpinak, czerwone pesto i całość dokładnie mieszamy, w razie potrzeby przyprawiamy solą i pieprzem.</li>
<li>Gotowy makaron z warzywami wykładamy na talerz. Posypujmy tartym serem grana padano i układamy mozzarellę. Smacznego!</li>
</ol>

<div class="p-cook" id="cook" data-open="0" role="dialog" aria-modal="true" aria-label="Gotowanie: Makaron z mozzarellą, szpinakiem, ogórkiem i pomidorkami koktajlowymi">
<div class="p-cook__bar">
<span class="p-cook__title">Makaron z mozzarellą, szpinakiem, ogórkiem i pomidorkami koktajlowymi</span>
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

<script>window.RECIPE = {"slug": "makaron-mozzarella", "title": "Makaron z mozzarellą, szpinakiem, ogórkiem i pomidorkami koktajlowymi", "day": 1, "slotLabel": "Obiad", "time": "14:00-17:00", "baseServings": 1, "ingredients": [{"qty": 1.0, "unit": "porcja", "unitLemma": "porcja", "name": "makaronu pełnoziarnistego", "grams": 50.0, "pantry": false, "tag": "makaron"}, {"qty": 2.0, "unit": "łyżeczki", "unitLemma": "łyżeczka", "name": "zielonego pesto", "grams": 10.0, "pantry": false, "tag": "pesto"}, {"qty": 7.0, "unit": "sztuk", "unitLemma": "sztuka", "name": "pomidorków koktajlowych", "grams": 140.0, "pantry": false, "tag": "pomidor"}, {"qty": 0.5, "unit": "garści", "unitLemma": "garść", "name": "bazylii świeżej", "grams": 1.5, "pantry": true, "tag": null}, {"qty": 2.0, "unit": "garści", "unitLemma": "garść", "name": "szpinaku", "grams": 50.0, "pantry": false, "tag": "szpinak"}, {"qty": 0.5, "unit": "sztuki", "unitLemma": "sztuka", "name": "ogórka", "grams": 75.0, "pantry": false, "tag": "ogorek"}, {"qty": 3.0, "unit": "plastry", "unitLemma": "plaster", "name": "mozzarelli light", "grams": 45.0, "pantry": false, "tag": "mozzarella"}, {"qty": 1.0, "unit": "łyżka", "unitLemma": "łyżka", "name": "sera grana padano", "grams": 10.0, "pantry": false, "tag": "grana-padano"}, {"qty": 1.0, "unit": "szczypta", "unitLemma": "szczypta", "name": "soli", "grams": 0.25, "pantry": true, "tag": null}, {"qty": 1.0, "unit": "szczypta", "unitLemma": "szczypta", "name": "pieprzu", "grams": 0.25, "pantry": true, "tag": null}], "steps": ["Makaron gotujemy według instrukcji umieszczonej na opakowaniu.", "Kroimy pomidorki, ogórek zielony, siekamy bazylię.", "Do miski dodajemy makaron, pokrojone warzywa, posiekaną bazylię, umyty szpinak, czerwone pesto i całość dokładnie mieszamy, w razie potrzeby przyprawiamy solą i pieprzem.", "Gotowy makaron z warzywami wykładamy na talerz. Posypujmy tartym serem grana padano i układamy mozzarellę. Smacznego!"]};
window.UNITS = {"łyżka": ["łyżka", "łyżki", "łyżek", "łyżki"], "łyżeczka": ["łyżeczka", "łyżeczki", "łyżeczek", "łyżeczki"], "sztuka": ["sztuka", "sztuki", "sztuk", "sztuki"], "garść": ["garść", "garście", "garści", "garści"], "kromka": ["kromka", "kromki", "kromek", "kromki"], "plaster": ["plaster", "plastry", "plastrów", "plastra"], "szklanka": ["szklanka", "szklanki", "szklanek", "szklanki"], "opakowanie": ["opakowanie", "opakowania", "opakowań", "opakowania"], "ząbek": ["ząbek", "ząbki", "ząbków", "ząbka"], "szczypta": ["szczypta", "szczypty", "szczypt", "szczypty"], "porcja": ["porcja", "porcje", "porcji", "porcji"], "puszka": ["puszka", "puszki", "puszek", "puszki"]};</script>
