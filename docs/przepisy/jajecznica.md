---
hide:
  - toc
---

<a class="p-back" href="../../">&larr; Wszystkie przepisy</a>

# Jajecznica z pieczarkami, cebulą i pieczywem

<div class="p-hero" data-slot="2">
<div class="p-hero__top">
<span>II śniadanie</span><span class="p-num">10:00-13:00</span><span class="p-num">Dzień 1</span>
</div>
<div class="p-macros">
<div class="p-macro"><span class="p-macro__v">470</span><span class="p-macro__l">kcal</span></div>
<div class="p-macro"><span class="p-macro__v">29 g</span><span class="p-macro__l">białko</span></div>
<div class="p-macro"><span class="p-macro__v">41 g</span><span class="p-macro__l">węgl.</span></div>
<div class="p-macro"><span class="p-macro__v">23 g</span><span class="p-macro__l">tłuszcz</span></div>
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
<li><span class="p-ing__q">3 sztuki</span><span>jajek kurzych</span><span class="p-ing__g">168 g</span></li>
<li><span class="p-ing__q">5 sztuk</span><span>pieczarek</span><span class="p-ing__g">100 g</span></li>
<li><span class="p-ing__q">0.5 sztuki</span><span>cebuli</span><span class="p-ing__g">55 g</span></li>
<li><span class="p-ing__q">1 garść</span><span>szpinaku</span><span class="p-ing__g">25 g</span></li>
<li><span class="p-ing__q">3 sztuki</span><span>rzodkiewki</span><span class="p-ing__g">45 g</span></li>
<li><span class="p-ing__q">1 łyżeczka</span><span>oleju rzepakowego</span><span class="p-ing__g">5 g</span></li>
<li><span class="p-ing__q">2 kromki</span><span>chleba żytniego razowego</span><span class="p-ing__g">60 g</span></li>
<li data-pantry="1"><span class="p-ing__q">1 szczypta</span><span>soli</span><span class="p-ing__g">0.25 g</span></li>
<li data-pantry="1"><span class="p-ing__q">1 szczypta</span><span>pieprzu</span><span class="p-ing__g">0.25 g</span></li>
</ul>

<div class="p-actions">
<button type="button" class="p-btn p-btn--block" id="open-shopping">&#128722; Lista zakupów</button>
<button type="button" class="p-btn p-btn--primary p-btn--block" id="cook-start">Gotujmy &rarr;</button>
</div>

<h2>Sposób przygotowania</h2>
<ol class="p-steps">
<li>Na patelni rozgrzewamy olej i podsmażamy pokrojone pieczarki oraz cebulę.</li>
<li>Do zeszklonych warzyw wbijamy jajka.</li>
<li>Smażymy na małym ogniu, cały czas mieszając, aż jajka się zetną.</li>
<li>Gotową jajecznicę doprawiamy solą i pieprzem.</li>
<li>Podajemy z pieczywem, szpinakiem i pokrojonymi rzodkiewkami. Smacznego!</li>
</ol>

<div class="p-cook" id="cook" data-open="0" role="dialog" aria-modal="true" aria-label="Gotowanie: Jajecznica z pieczarkami, cebulą i pieczywem">
<div class="p-cook__bar">
<span class="p-cook__title">Jajecznica z pieczarkami, cebulą i pieczywem</span>
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

<script>window.RECIPE = {"slug": "jajecznica", "title": "Jajecznica z pieczarkami, cebulą i pieczywem", "day": 1, "slotLabel": "II śniadanie", "time": "10:00-13:00", "baseServings": 1, "ingredients": [{"qty": 3.0, "unit": "sztuki", "unitLemma": "sztuka", "name": "jajek kurzych", "grams": 168.0, "pantry": false, "tag": "jajka"}, {"qty": 5.0, "unit": "sztuk", "unitLemma": "sztuka", "name": "pieczarek", "grams": 100.0, "pantry": false, "tag": "pieczarki"}, {"qty": 0.5, "unit": "sztuki", "unitLemma": "sztuka", "name": "cebuli", "grams": 55.0, "pantry": false, "tag": "cebula"}, {"qty": 1.0, "unit": "garść", "unitLemma": "garść", "name": "szpinaku", "grams": 25.0, "pantry": false, "tag": "szpinak"}, {"qty": 3.0, "unit": "sztuki", "unitLemma": "sztuka", "name": "rzodkiewki", "grams": 45.0, "pantry": false, "tag": "rzodkiewka"}, {"qty": 1.0, "unit": "łyżeczka", "unitLemma": "łyżeczka", "name": "oleju rzepakowego", "grams": 5.0, "pantry": false, "tag": "oliwa"}, {"qty": 2.0, "unit": "kromki", "unitLemma": "kromka", "name": "chleba żytniego razowego", "grams": 60.0, "pantry": false, "tag": "chleb"}, {"qty": 1.0, "unit": "szczypta", "unitLemma": "szczypta", "name": "soli", "grams": 0.25, "pantry": true, "tag": null}, {"qty": 1.0, "unit": "szczypta", "unitLemma": "szczypta", "name": "pieprzu", "grams": 0.25, "pantry": true, "tag": null}], "steps": ["Na patelni rozgrzewamy olej i podsmażamy pokrojone pieczarki oraz cebulę.", "Do zeszklonych warzyw wbijamy jajka.", "Smażymy na małym ogniu, cały czas mieszając, aż jajka się zetną.", "Gotową jajecznicę doprawiamy solą i pieprzem.", "Podajemy z pieczywem, szpinakiem i pokrojonymi rzodkiewkami. Smacznego!"]};
window.UNITS = {"łyżka": ["łyżka", "łyżki", "łyżek", "łyżki"], "łyżeczka": ["łyżeczka", "łyżeczki", "łyżeczek", "łyżeczki"], "sztuka": ["sztuka", "sztuki", "sztuk", "sztuki"], "garść": ["garść", "garście", "garści", "garści"], "kromka": ["kromka", "kromki", "kromek", "kromki"], "plaster": ["plaster", "plastry", "plastrów", "plastra"], "szklanka": ["szklanka", "szklanki", "szklanek", "szklanki"], "opakowanie": ["opakowanie", "opakowania", "opakowań", "opakowania"], "ząbek": ["ząbek", "ząbki", "ząbków", "ząbka"], "szczypta": ["szczypta", "szczypty", "szczypt", "szczypty"], "porcja": ["porcja", "porcje", "porcji", "porcji"], "puszka": ["puszka", "puszki", "puszek", "puszki"]};</script>
