---
hide:
  - toc
---

<a class="p-back" href="../../">&larr; Wszystkie przepisy</a>

# Omlet mleczna kanapka

<div class="p-hero" data-slot="1">
<div class="p-hero__top">
<span>Śniadanie</span><span class="p-num">7:00-10:00</span>
</div>
<div class="p-macros">
<div class="p-macro"><span class="p-macro__v">454</span><span class="p-macro__l">kcal</span></div>
<div class="p-macro"><span class="p-macro__v">35 g</span><span class="p-macro__l">białko</span></div>
<div class="p-macro"><span class="p-macro__v">41 g</span><span class="p-macro__l">węgl.</span></div>
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

<div class="p-ings__head">
<h2 id="ing-heading" style="margin:0">Składniki na 1 osobę</h2>
<button type="button" class="p-btn p-btn--ghost" id="swap-reset" style="min-height:auto;padding:6px 8px" hidden>Przywróć oryginał</button>
</div>
<ul class="p-ings" id="ing-list">
<li><div class="p-ing__row"><span class="p-ing__q">1 sztuka</span><span class="p-ing__n">jajko</span><span class="p-ing__g">56 g</span></div>
</li>
<li><div class="p-ing__row"><span class="p-ing__q">2.5 łyżki</span><span class="p-ing__n">mąki pszennej pełnoziarnistej</span><span class="p-ing__g">35 g</span></div>
</li>
<li><div class="p-ing__row"><span class="p-ing__q">1 łyżka</span><span class="p-ing__n">kakao</span><span class="p-ing__g">10 g</span></div>
</li>
<li><div class="p-ing__row"><span class="p-ing__q">3 łyżki</span><span class="p-ing__n">jogurtu naturalnego</span><span class="p-ing__g">60 g</span></div>
</li>
<li data-pantry="1"><div class="p-ing__row"><span class="p-ing__q">0.5 łyżeczki</span><span class="p-ing__n">proszku do pieczenia</span><span class="p-ing__g">2 g</span></div>
</li>
<li><div class="p-ing__row"><span class="p-ing__q">2 łyżki</span><span class="p-ing__n">jogurtu naturalnego</span><span class="p-ing__g">40 g</span></div>
</li>
<li><div class="p-ing__row"><span class="p-ing__q">3 plastry</span><span class="p-ing__n">twarogu chudego</span><span class="p-ing__g">90 g</span></div>
<div class="p-ing__swap">
<label class="p-swaplabel" for="swap-6">Zamień na</label>
<select class="p-select" id="swap-6" data-ing="6">
<option value="serek-wiejski">Serek wiejski</option>
<option value="twarog-chudy" selected>Twaróg chudy · oryginał</option>
<option value="tofu-naturalne">Tofu naturalne</option>
</select>
</div>
</li>
<li data-pantry="1"><div class="p-ing__row"><span class="p-ing__q">1.5 łyżki</span><span class="p-ing__n">ksylitolu</span><span class="p-ing__g">23 g</span></div>
</li>
<li data-pantry="1"><div class="p-ing__row"><span class="p-ing__q">1 łyżeczka</span><span class="p-ing__n">ekstraktu waniliowego</span><span class="p-ing__g">3 g</span></div>
</li>
</ul>

<div class="p-actions">
<button type="button" class="p-btn p-btn--block" id="open-shopping">&#128722; Lista zakupów</button>
<button type="button" class="p-btn p-btn--primary p-btn--block" id="cook-start">Gotujmy &rarr;</button>
</div>

<h2>Sposób przygotowania</h2>
<ol class="p-steps" id="steps-list">
<li>Składniki omletu mieszaj lub zblenduj ze sobą, smaż na patelni pod przykryciem przez 3-5 minut na średnim ogniu.</li>
<li>Składniki kremu zblenduj na gładką masę.</li>
<li>Omlet ściągnij z patelni. Odstaw, żeby nieco ostygł. Posmaruj kremem i złóż na pół. Smacznego!</li>
</ol>

<div class="p-cook" id="cook" data-open="0" role="dialog" aria-modal="true" aria-label="Gotowanie: Omlet mleczna kanapka">
<div class="p-cook__bar">
<span class="p-cook__title">Omlet mleczna kanapka</span>
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
</div></div>
<div class="p-sheet" id="shopping" data-open="0" role="dialog" aria-modal="true" aria-label="Lista zakupów">
<button type="button" class="p-sheet__scrim" id="shopping-scrim" aria-label="Zamknij listę zakupów"></button>
<div class="p-sheet__panel">
<div class="p-sheet__head"><h2>Lista zakupów</h2><button type="button" class="p-iconbtn" id="close-shopping" aria-label="Zamknij">&times;</button></div>
<div class="p-sheet__body" id="shopping-body"></div>
<div class="p-sheet__foot">
<button type="button" class="p-btn" id="reset-shopping">Odznacz wszystko</button>
<button type="button" class="p-btn p-btn--primary" id="pdf-btn">Wygeneruj PDF</button>
</div></div></div>
<div class="p-toast" id="toast" role="status" data-on="0"></div>

<script>window.RECIPE = {"slug": "omlet-mleczna-kanapka", "title": "Omlet mleczna kanapka", "slotLabel": "Śniadanie", "time": "7:00-10:00", "baseServings": 1, "ingredients": [{"qty": 1.0, "unit": "sztuka", "unitLemma": "sztuka", "name": "jajko", "grams": 56.0, "pantry": false, "tag": "jajka"}, {"qty": 2.5, "unit": "łyżki", "unitLemma": "łyżka", "name": "mąki pszennej pełnoziarnistej", "grams": 35.0, "pantry": false, "tag": "maka"}, {"qty": 1.0, "unit": "łyżka", "unitLemma": "łyżka", "name": "kakao", "grams": 10.0, "pantry": false, "tag": "kakao"}, {"qty": 3.0, "unit": "łyżki", "unitLemma": "łyżka", "name": "jogurtu naturalnego", "grams": 60.0, "pantry": false, "tag": "jogurt"}, {"qty": 0.5, "unit": "łyżeczki", "unitLemma": "łyżeczka", "name": "proszku do pieczenia", "grams": 2.0, "pantry": true, "tag": null}, {"qty": 2.0, "unit": "łyżki", "unitLemma": "łyżka", "name": "jogurtu naturalnego", "grams": 40.0, "pantry": false, "tag": "jogurt"}, {"qty": 3.0, "unit": "plastry", "unitLemma": "plaster", "name": "twarogu chudego", "grams": 90.0, "pantry": false, "tag": "twarog", "swap": {"group": "twarogowe", "self": "twarog-chudy", "nameCase": "D"}}, {"qty": 1.5, "unit": "łyżki", "unitLemma": "łyżka", "name": "ksylitolu", "grams": 23.0, "pantry": true, "tag": null}, {"qty": 1.0, "unit": "łyżeczka", "unitLemma": "łyżeczka", "name": "ekstraktu waniliowego", "grams": 3.0, "pantry": true, "tag": null}], "steps": ["Składniki omletu mieszaj lub zblenduj ze sobą, smaż na patelni pod przykryciem przez 3-5 minut na średnim ogniu.", "Składniki kremu zblenduj na gładką masę.", "Omlet ściągnij z patelni. Odstaw, żeby nieco ostygł. Posmaruj kremem i złóż na pół. Smacznego!"]};
window.UNITS = {"łyżka": ["łyżka", "łyżki", "łyżek", "łyżki"], "łyżeczka": ["łyżeczka", "łyżeczki", "łyżeczek", "łyżeczki"], "sztuka": ["sztuka", "sztuki", "sztuk", "sztuki"], "garść": ["garść", "garście", "garści", "garści"], "kromka": ["kromka", "kromki", "kromek", "kromki"], "plaster": ["plaster", "plastry", "plastrów", "plastra"], "szklanka": ["szklanka", "szklanki", "szklanek", "szklanki"], "opakowanie": ["opakowanie", "opakowania", "opakowań", "opakowania"], "ząbek": ["ząbek", "ząbki", "ząbków", "ząbka"], "szczypta": ["szczypta", "szczypty", "szczypt", "szczypty"], "porcja": ["porcja", "porcje", "porcji", "porcji"], "puszka": ["puszka", "puszki", "puszek", "puszki"], "kostka": ["kostka", "kostki", "kostek", "kostki"], "listek": ["listek", "listki", "listków", "listka"], "łodyga": ["łodyga", "łodygi", "łodyg", "łodygi"]};
window.SWAPS = {"twarogowe": {"label": "Serek wiejski i zamienniki", "options": [{"id": "serek-wiejski", "label": "Serek wiejski", "rodzaj": "m", "formy": {"M": "serek wiejski", "D": "serka wiejskiego", "B": "serek wiejski", "N": "serkiem wiejskim", "Ms": "serku wiejskim"}, "rodzajB": "m"}, {"id": "twarog-chudy", "label": "Twaróg chudy", "rodzaj": "m", "formy": {"M": "twaróg chudy", "D": "twarogu chudego", "B": "twaróg chudy", "N": "twarogiem chudym", "Ms": "twarogu chudym"}, "rodzajB": "m"}, {"id": "tofu-naturalne", "label": "Tofu naturalne", "rodzaj": "n", "formy": {"M": "tofu naturalne", "D": "tofu naturalnego", "B": "tofu naturalne", "N": "tofu naturalnym", "Ms": "tofu naturalnym"}, "rodzajB": "n"}]}};
window.SWAP_ADJ = {"umyty_B": {"m": "umyty", "f": "umytą", "n": "umyte", "pl": "umyte", "mz": "umytego"}, "swiezy_B": {"m": "świeży", "f": "świeżą", "n": "świeże", "pl": "świeże", "mz": "świeżego"}, "odsaczony_B": {"m": "odsączony", "f": "odsączoną", "n": "odsączone", "pl": "odsączone", "mz": "odsączonego"}, "pieczony_N": {"m": "pieczonym", "f": "pieczoną", "n": "pieczonym", "pl": "pieczonymi", "mz": "pieczonym"}, "pokrojony_B": {"m": "pokrojony", "f": "pokrojoną", "n": "pokrojone", "pl": "pokrojone", "mz": "pokrojonego"}, "ugotowany_B": {"m": "ugotowany", "f": "ugotowaną", "n": "ugotowane", "pl": "ugotowane", "mz": "ugotowanego"}, "podsmazony_B": {"m": "podsmażony", "f": "podsmażoną", "n": "podsmażone", "pl": "podsmażone", "mz": "podsmażonego"}, "przyprawiony_B": {"m": "przyprawiony", "f": "przyprawioną", "n": "przyprawione", "pl": "przyprawione", "mz": "przyprawionego"}, "prazony_N": {"m": "prażonym", "f": "prażoną", "n": "prażonym", "pl": "prażonymi", "mz": "prażonym"}, "pokrojony_N": {"m": "pokrojonym", "f": "pokrojoną", "n": "pokrojonym", "pl": "pokrojonymi", "mz": "pokrojonym"}, "starty_B": {"m": "starty", "f": "startą", "n": "starte", "pl": "starte", "mz": "startego"}, "ugotowany_N": {"m": "ugotowanym", "f": "ugotowaną", "n": "ugotowanym", "pl": "ugotowanymi", "mz": "ugotowanym"}, "przygotowany_B": {"m": "przygotowany", "f": "przygotowaną", "n": "przygotowane", "pl": "przygotowane", "mz": "przygotowanego"}};</script>
