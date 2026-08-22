---
hide:
  - toc
---

<a class="p-back" href="../../">&larr; Wszystkie przepisy</a>

# Klejący ryż z prażonym jabłkiem

<div class="p-hero" data-slot="1">
<div class="p-hero__top">
<span>Śniadanie</span><span class="p-num">6:00-9:00</span><span class="p-num">Dzień 1</span>
</div>
<div class="p-macros">
<div class="p-macro"><span class="p-macro__v">464</span><span class="p-macro__l">kcal</span></div>
<div class="p-macro"><span class="p-macro__v">25 g</span><span class="p-macro__l">białko</span></div>
<div class="p-macro"><span class="p-macro__v">60 g</span><span class="p-macro__l">węgl.</span></div>
<div class="p-macro"><span class="p-macro__v">12 g</span><span class="p-macro__l">tłuszcz</span></div>
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
<li><span class="p-ing__q">2 łyżki</span><span>ryżu basmati</span><span class="p-ing__g">30 g</span></li>
<li><span class="p-ing__q">0.5 szklanki</span><span>mleka roślinnego</span><span class="p-ing__g">125 g</span></li>
<li><span class="p-ing__q">1 sztuka</span><span>jabłka</span><span class="p-ing__g">150 g</span></li>
<li data-pantry="1"><span class="p-ing__q">1 łyżeczka</span><span>cynamonu</span><span class="p-ing__g">4 g</span></li>
<li data-pantry="1"><span class="p-ing__q">1 łyżka</span><span>ksylitolu</span><span class="p-ing__g">15 g</span></li>
<li><span class="p-ing__q">3 łyżki</span><span>wegańskiej odżywki białkowej</span><span class="p-ing__g">24 g</span></li>
<li><span class="p-ing__q">4 łyżki</span><span>mleczka kokosowego 12%</span><span class="p-ing__g">80 g</span></li>
</ul>

<div class="p-actions">
<button type="button" class="p-btn p-btn--block" id="open-shopping">&#128722; Lista zakupów</button>
<button type="button" class="p-btn p-btn--primary p-btn--block" id="cook-start">Gotujmy &rarr;</button>
</div>

<h2>Sposób przygotowania</h2>
<ol class="p-steps">
<li>Jabłko kroimy w kostkę i doprawiamy cynamonem, w razie potrzeby dodajemy ksylitol.</li>
<li>Przyprawione jabłko dusimy w rondelku, aż puści soki i zacznie się rozpadać. Tak przygotowane jabłko przekładamy do miseczki.</li>
<li>Do rondelka po jabłkach wsypujemy ryż, odżywkę i zalewamy napojem roślinnym oraz mleczkiem kokosowym. Gotujemy na wolnym ogniu.</li>
<li>Gdy ryż zacznie się rozklejać, dokładamy do niego około 2/3 masy jabłek, które wcześniej przygotowaliśmy.</li>
<li>Wystarczająco gęsty i miękki ryż z jabłkami przekładamy do miseczki, a na niego układamy resztę jabłek, które nam zostały. Smacznego!</li>
</ol>

<div class="p-cook" id="cook" data-open="0" role="dialog" aria-modal="true" aria-label="Gotowanie: Klejący ryż z prażonym jabłkiem">
<div class="p-cook__bar">
<span class="p-cook__title">Klejący ryż z prażonym jabłkiem</span>
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

<script>window.RECIPE = {"slug": "klejacy-ryz", "title": "Klejący ryż z prażonym jabłkiem", "day": 1, "slotLabel": "Śniadanie", "time": "6:00-9:00", "baseServings": 1, "ingredients": [{"qty": 2.0, "unit": "łyżki", "unitLemma": "łyżka", "name": "ryżu basmati", "grams": 30.0, "pantry": false, "tag": "ryz"}, {"qty": 0.5, "unit": "szklanki", "unitLemma": "szklanka", "name": "mleka roślinnego", "grams": 125.0, "pantry": false, "tag": "mleko"}, {"qty": 1.0, "unit": "sztuka", "unitLemma": "sztuka", "name": "jabłka", "grams": 150.0, "pantry": false, "tag": "jablko"}, {"qty": 1.0, "unit": "łyżeczka", "unitLemma": "łyżeczka", "name": "cynamonu", "grams": 4.0, "pantry": true, "tag": null}, {"qty": 1.0, "unit": "łyżka", "unitLemma": "łyżka", "name": "ksylitolu", "grams": 15.0, "pantry": true, "tag": null}, {"qty": 3.0, "unit": "łyżki", "unitLemma": "łyżka", "name": "wegańskiej odżywki białkowej", "grams": 24.0, "pantry": false, "tag": "odzywka"}, {"qty": 4.0, "unit": "łyżki", "unitLemma": "łyżka", "name": "mleczka kokosowego 12%", "grams": 80.0, "pantry": false, "tag": "mleczko-kokosowe"}], "steps": ["Jabłko kroimy w kostkę i doprawiamy cynamonem, w razie potrzeby dodajemy ksylitol.", "Przyprawione jabłko dusimy w rondelku, aż puści soki i zacznie się rozpadać. Tak przygotowane jabłko przekładamy do miseczki.", "Do rondelka po jabłkach wsypujemy ryż, odżywkę i zalewamy napojem roślinnym oraz mleczkiem kokosowym. Gotujemy na wolnym ogniu.", "Gdy ryż zacznie się rozklejać, dokładamy do niego około 2/3 masy jabłek, które wcześniej przygotowaliśmy.", "Wystarczająco gęsty i miękki ryż z jabłkami przekładamy do miseczki, a na niego układamy resztę jabłek, które nam zostały. Smacznego!"]};
window.UNITS = {"łyżka": ["łyżka", "łyżki", "łyżek", "łyżki"], "łyżeczka": ["łyżeczka", "łyżeczki", "łyżeczek", "łyżeczki"], "sztuka": ["sztuka", "sztuki", "sztuk", "sztuki"], "garść": ["garść", "garście", "garści", "garści"], "kromka": ["kromka", "kromki", "kromek", "kromki"], "plaster": ["plaster", "plastry", "plastrów", "plastra"], "szklanka": ["szklanka", "szklanki", "szklanek", "szklanki"], "opakowanie": ["opakowanie", "opakowania", "opakowań", "opakowania"], "ząbek": ["ząbek", "ząbki", "ząbków", "ząbka"], "szczypta": ["szczypta", "szczypty", "szczypt", "szczypty"], "porcja": ["porcja", "porcje", "porcji", "porcji"], "puszka": ["puszka", "puszki", "puszek", "puszki"]};</script>
