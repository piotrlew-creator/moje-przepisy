---
title: "Omlet na słodko z miodem"
description: "Śniadanie, 521 kcal, 33 g białka. Składniki: jajek kurzych, mąki pszennej pełnoziarnistej, miodu, świeżych lub mrożonych owoców."
hide:
  - toc
---

<a class="p-back" href="../../">&larr; Wszystkie przepisy</a>

# Omlet na słodko z miodem

<div class="p-hero" data-slot="1">
<div class="p-hero__top">
<span>Śniadanie</span><span class="p-num">7:00-10:00</span>
<button type="button" class="p-fav p-fav--hero" data-fav="omlet-na-slodko-z-miodem" aria-pressed="false" aria-label="Dodaj do ulubionych"><span aria-hidden="true">&#9825;</span></button>
</div>
<div class="p-macros">
<div class="p-macro"><span class="p-macro__v">521</span><span class="p-macro__l">kcal</span></div>
<div class="p-macro"><span class="p-macro__v">33 g</span><span class="p-macro__l">białko</span></div>
<div class="p-macro"><span class="p-macro__v">49 g</span><span class="p-macro__l">węgl.</span></div>
<div class="p-macro"><span class="p-macro__v">23 g</span><span class="p-macro__l">tłuszcz</span></div>
</div>
<p style="margin:0;font-size:.66rem;color:var(--p-ink-3);font-weight:600">Wartości dla jednej porcji, tak jak w planie diety.</p>
<p class="p-cooked" id="cooked-note" hidden></p>
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
<li><div class="p-ing__row"><span class="p-ing__q">4 szt.</span><span class="p-ing__n">jajek kurzych</span><span class="p-ing__g">224 g</span></div>
</li>
<li><div class="p-ing__row"><span class="p-ing__q">2 łyżki</span><span class="p-ing__n">mąki pszennej pełnoziarnistej</span><span class="p-ing__g">30 g</span></div>
</li>
<li><div class="p-ing__row"><span class="p-ing__q">1 łyżeczka</span><span class="p-ing__n">miodu</span><span class="p-ing__g">12 g</span></div>
<div class="p-ing__swap">
<label class="p-swaplabel" for="swap-2">Zamień na</label>
<select class="p-select" id="swap-2" data-ing="2">
<option value="miod" selected>Miód · oryginał</option>
<option value="syrop-klonowy">Syrop klonowy</option>
<option value="syrop-z-agawy">Syrop z agawy</option>
</select>
</div>
</li>
<li data-pantry="1"><div class="p-ing__row"><span class="p-ing__q">1 szcz.</span><span class="p-ing__n">soli</span><span class="p-ing__g">0.25 g</span></div>
</li>
<li><div class="p-ing__row"><span class="p-ing__q">3 garści</span><span class="p-ing__n">świeżych lub mrożonych owoców</span><span class="p-ing__g">210 g</span></div>
</li>
</ul>

<div class="p-actions">
<button type="button" class="p-btn p-btn--block" id="open-shopping">&#128722; Lista zakupów</button>
<button type="button" class="p-btn p-btn--primary p-btn--block" id="cook-start">Gotujmy &rarr;</button>
</div>
<noscript><p class="p-note">Lista zakupów, przelicznik porcji i tryb gotowania krok po kroku wymagają JavaScriptu. Składniki i sposób przygotowania czytasz normalnie — ilości są podane dla jednej porcji z planu.</p></noscript>

<h2>Sposób przygotowania</h2>
<ol class="p-steps" id="steps-list">
<li data-sec="240"><span class="p-step__text">Jaja, mąkę i sól połącz ze sobą i wylej na rozgrzaną patelnię. Smaż omlet przez 4 minuty na średnim ogniu, przekręć i smaż jeszcze 1 minutę.</span><button type="button" class="p-timer__btn" data-timer="0">&#9201; 4:00</button></li>
<li><span class="p-step__text">Omlet przełóż na talerz, posmaruj miodem i ułóż owoce.</span></li>
</ol>

<div class="p-cook" id="cook" data-open="0" role="dialog" aria-modal="true" aria-label="Gotowanie: Omlet na słodko z miodem">
<div class="p-cook__bar">
<span class="p-cook__title">Omlet na słodko z miodem</span>
<button type="button" class="p-iconbtn" id="cook-close" aria-label="Zamknij tryb gotowania">&times;</button>
</div>
<div class="p-progress" id="cook-progress"></div>
<div class="p-cook__body">
<span class="p-cook__step" id="cook-label"></span>
<p class="p-cook__text" id="cook-text"></p>
<button type="button" class="p-timer__btn p-timer__btn--cook" id="cook-timer" hidden></button>
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

<script>window.RECIPE = {"slug": "omlet-na-slodko-z-miodem", "title": "Omlet na słodko z miodem", "slotLabel": "Śniadanie", "time": "7:00-10:00", "baseServings": 1, "kcal": 521, "times": [240, null], "ingredients": [{"qty": 4.0, "unit": "sztuki", "unitLemma": "sztuka", "name": "jajek kurzych", "grams": 224.0, "pantry": false, "tag": "jajka"}, {"qty": 2.0, "unit": "łyżki", "unitLemma": "łyżka", "name": "mąki pszennej pełnoziarnistej", "grams": 30.0, "pantry": false, "tag": "maka"}, {"qty": 1.0, "unit": "łyżeczka", "unitLemma": "łyżeczka", "name": "miodu", "grams": 12.0, "pantry": false, "tag": "miod", "swap": {"group": "slodziki", "self": "miod", "nameCase": "D"}}, {"qty": 1.0, "unit": "szczypta", "unitLemma": "szczypta", "name": "soli", "grams": 0.25, "pantry": true, "tag": null}, {"qty": 3.0, "unit": "garści", "unitLemma": "garść", "name": "świeżych lub mrożonych owoców", "grams": 210.0, "pantry": false, "tag": "owoce-mrozone"}], "steps": ["Jaja, mąkę i sól połącz ze sobą i wylej na rozgrzaną patelnię. Smaż omlet przez 4 minuty na średnim ogniu, przekręć i smaż jeszcze 1 minutę.", "Omlet przełóż na talerz, posmaruj «2|N|||» i ułóż owoce."]};
window.UNITS = {"łyżka": ["łyżka", "łyżki", "łyżek", "łyżki"], "łyżeczka": ["łyżeczka", "łyżeczki", "łyżeczek", "łyżeczki"], "sztuka": ["sztuka", "sztuki", "sztuk", "sztuki"], "garść": ["garść", "garście", "garści", "garści"], "kromka": ["kromka", "kromki", "kromek", "kromki"], "plaster": ["plaster", "plastry", "plastrów", "plastra"], "szklanka": ["szklanka", "szklanki", "szklanek", "szklanki"], "opakowanie": ["opakowanie", "opakowania", "opakowań", "opakowania"], "ząbek": ["ząbek", "ząbki", "ząbków", "ząbka"], "szczypta": ["szczypta", "szczypty", "szczypt", "szczypty"], "porcja": ["porcja", "porcje", "porcji", "porcji"], "puszka": ["puszka", "puszki", "puszek", "puszki"], "kostka": ["kostka", "kostki", "kostek", "kostki"], "listek": ["listek", "listki", "listków", "listka"], "łodyga": ["łodyga", "łodygi", "łodyg", "łodygi"]};
window.SWAPS = {"slodziki": {"label": "Miód i syropy", "options": [{"id": "miod", "label": "Miód", "rodzaj": "m", "formy": {"M": "miód", "D": "miodu", "B": "miód", "N": "miodem", "Ms": "miodzie"}, "rodzajB": "m"}, {"id": "syrop-klonowy", "label": "Syrop klonowy", "rodzaj": "m", "formy": {"M": "syrop klonowy", "D": "syropu klonowego", "B": "syrop klonowy", "N": "syropem klonowym", "Ms": "syropie klonowym"}, "rodzajB": "m"}, {"id": "syrop-z-agawy", "label": "Syrop z agawy", "rodzaj": "m", "formy": {"M": "syrop z agawy", "D": "syropu z agawy", "B": "syrop z agawy", "N": "syropem z agawy", "Ms": "syropie z agawy"}, "rodzajB": "m"}]}};
window.SWAP_ADJ = {"umyty_B": {"m": "umyty", "f": "umytą", "n": "umyte", "pl": "umyte", "mz": "umytego"}, "swiezy_B": {"m": "świeży", "f": "świeżą", "n": "świeże", "pl": "świeże", "mz": "świeżego"}, "odsaczony_B": {"m": "odsączony", "f": "odsączoną", "n": "odsączone", "pl": "odsączone", "mz": "odsączonego"}, "pieczony_N": {"m": "pieczonym", "f": "pieczoną", "n": "pieczonym", "pl": "pieczonymi", "mz": "pieczonym"}, "pokrojony_B": {"m": "pokrojony", "f": "pokrojoną", "n": "pokrojone", "pl": "pokrojone", "mz": "pokrojonego"}, "ugotowany_B": {"m": "ugotowany", "f": "ugotowaną", "n": "ugotowane", "pl": "ugotowane", "mz": "ugotowanego"}, "podsmazony_B": {"m": "podsmażony", "f": "podsmażoną", "n": "podsmażone", "pl": "podsmażone", "mz": "podsmażonego"}, "przyprawiony_B": {"m": "przyprawiony", "f": "przyprawioną", "n": "przyprawione", "pl": "przyprawione", "mz": "przyprawionego"}, "prazony_N": {"m": "prażonym", "f": "prażoną", "n": "prażonym", "pl": "prażonymi", "mz": "prażonym"}, "pokrojony_N": {"m": "pokrojonym", "f": "pokrojoną", "n": "pokrojonym", "pl": "pokrojonymi", "mz": "pokrojonym"}, "starty_B": {"m": "starty", "f": "startą", "n": "starte", "pl": "starte", "mz": "startego"}, "ugotowany_N": {"m": "ugotowanym", "f": "ugotowaną", "n": "ugotowanym", "pl": "ugotowanymi", "mz": "ugotowanym"}, "przygotowany_B": {"m": "przygotowany", "f": "przygotowaną", "n": "przygotowane", "pl": "przygotowane", "mz": "przygotowanego"}};</script>
