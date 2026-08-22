---
hide:
  - toc
---

<a class="p-back" href="../../">&larr; Wszystkie przepisy</a>

# Kanapka z pastą pomidorową

<div class="p-hero" data-slot="4">
<div class="p-hero__top">
<span>Kolacja</span><span class="p-num">18:00-21:00</span><span class="p-num">Dzień 10</span>
</div>
<div class="p-macros">
<div class="p-macro"><span class="p-macro__v">443</span><span class="p-macro__l">kcal</span></div>
<div class="p-macro"><span class="p-macro__v">19 g</span><span class="p-macro__l">białko</span></div>
<div class="p-macro"><span class="p-macro__v">66 g</span><span class="p-macro__l">węgl.</span></div>
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
<li><span class="p-ing__q">4 łyżki</span><span>soczewicy czerwonej</span><span class="p-ing__g">40 g</span></li>
<li><span class="p-ing__q">2 kromki</span><span>chleba żytniego razowego</span><span class="p-ing__g">60 g</span></li>
<li><span class="p-ing__q">3 łyżeczki</span><span>pasty tahini</span><span class="p-ing__g">18 g</span></li>
<li><span class="p-ing__q">1 sztuka</span><span>pomidorów suszonych</span><span class="p-ing__g">20 g</span></li>
<li><span class="p-ing__q">1 ząbek</span><span>czosnku</span><span class="p-ing__g">6 g</span></li>
<li data-pantry="1"><span class="p-ing__q">1 łyżeczka</span><span>tymianku</span><span class="p-ing__g">3 g</span></li>
<li data-pantry="1"><span class="p-ing__q">1 szczypta</span><span>kuminu</span><span class="p-ing__g">1 g</span></li>
</ul>

<div class="p-actions">
<button type="button" class="p-btn p-btn--block" id="open-shopping">&#128722; Lista zakupów</button>
<button type="button" class="p-btn p-btn--primary p-btn--block" id="cook-start">Gotujmy &rarr;</button>
</div>

<h2>Sposób przygotowania</h2>
<ol class="p-steps">
<li>Soczewicę gotujemy zgodnie z instrukcją na opakowaniu</li>
<li>Po ugotowaniu soczewicę studzimy</li>
<li>Przekładamy do blendera wszystkie składniki pasty i blendujemy na gładką masę.</li>
<li>Podajemy z pieczywem.</li>
</ol>

<div class="p-cook" id="cook" data-open="0" role="dialog" aria-modal="true" aria-label="Gotowanie: Kanapka z pastą pomidorową">
<div class="p-cook__bar">
<span class="p-cook__title">Kanapka z pastą pomidorową</span>
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

<script>window.RECIPE = {"slug": "kanapka-z-pasta-pomidorowa", "title": "Kanapka z pastą pomidorową", "day": 10, "slotLabel": "Kolacja", "time": "18:00-21:00", "baseServings": 1, "ingredients": [{"qty": 4.0, "unit": "łyżki", "unitLemma": "łyżka", "name": "soczewicy czerwonej", "grams": 40.0, "pantry": false, "tag": "soczewica"}, {"qty": 2.0, "unit": "kromki", "unitLemma": "kromka", "name": "chleba żytniego razowego", "grams": 60.0, "pantry": false, "tag": "chleb"}, {"qty": 3.0, "unit": "łyżeczki", "unitLemma": "łyżeczka", "name": "pasty tahini", "grams": 18.0, "pantry": false, "tag": "tahini"}, {"qty": 1.0, "unit": "sztuka", "unitLemma": "sztuka", "name": "pomidorów suszonych", "grams": 20.0, "pantry": false, "tag": "pomidory-suszone"}, {"qty": 1.0, "unit": "ząbek", "unitLemma": "ząbek", "name": "czosnku", "grams": 6.0, "pantry": false, "tag": "czosnek"}, {"qty": 1.0, "unit": "łyżeczka", "unitLemma": "łyżeczka", "name": "tymianku", "grams": 3.0, "pantry": true, "tag": null}, {"qty": 1.0, "unit": "szczypta", "unitLemma": "szczypta", "name": "kuminu", "grams": 1.0, "pantry": true, "tag": null}], "steps": ["Soczewicę gotujemy zgodnie z instrukcją na opakowaniu", "Po ugotowaniu soczewicę studzimy", "Przekładamy do blendera wszystkie składniki pasty i blendujemy na gładką masę.", "Podajemy z pieczywem."]};
window.UNITS = {"łyżka": ["łyżka", "łyżki", "łyżek", "łyżki"], "łyżeczka": ["łyżeczka", "łyżeczki", "łyżeczek", "łyżeczki"], "sztuka": ["sztuka", "sztuki", "sztuk", "sztuki"], "garść": ["garść", "garście", "garści", "garści"], "kromka": ["kromka", "kromki", "kromek", "kromki"], "plaster": ["plaster", "plastry", "plastrów", "plastra"], "szklanka": ["szklanka", "szklanki", "szklanek", "szklanki"], "opakowanie": ["opakowanie", "opakowania", "opakowań", "opakowania"], "ząbek": ["ząbek", "ząbki", "ząbków", "ząbka"], "szczypta": ["szczypta", "szczypty", "szczypt", "szczypty"], "porcja": ["porcja", "porcje", "porcji", "porcji"], "puszka": ["puszka", "puszki", "puszek", "puszki"]};</script>
