---
title: "Fit Placuszki"
hide:
  - toc
---

<a class="p-back" href="../../">&larr; Wszystkie przepisy</a>

# Fit Placuszki

<div class="p-hero" data-slot="1">
<div class="p-hero__top">
<span>Śniadanie</span><span class="p-num">7:00-10:00</span>
</div>
<div class="p-macros">
<div class="p-macro"><span class="p-macro__v">473</span><span class="p-macro__l">kcal</span></div>
<div class="p-macro"><span class="p-macro__v">28 g</span><span class="p-macro__l">białko</span></div>
<div class="p-macro"><span class="p-macro__v">53 g</span><span class="p-macro__l">węgl.</span></div>
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

<div class="p-ings__head">
<h2 id="ing-heading" style="margin:0">Składniki na 1 osobę</h2>
<button type="button" class="p-btn p-btn--ghost" id="swap-reset" style="min-height:auto;padding:6px 8px" hidden>Przywróć oryginał</button>
</div>
<ul class="p-ings" id="ing-list">
<li><div class="p-ing__row"><span class="p-ing__q">1 szt.</span><span class="p-ing__n">jaja kurzego</span><span class="p-ing__g">56 g</span></div>
</li>
<li><div class="p-ing__row"><span class="p-ing__q">3 łyżki</span><span class="p-ing__n">mąki owsianej pełnoziarnistej</span><span class="p-ing__g">36 g</span></div>
</li>
<li><div class="p-ing__row"><span class="p-ing__q">2 łyżki</span><span class="p-ing__n">odżywki białkowej</span><span class="p-ing__g">16 g</span></div>
</li>
<li><div class="p-ing__row"><span class="p-ing__q">3 łyżki</span><span class="p-ing__n">napoju roślinnego, np. migdałowego</span><span class="p-ing__g">45 g</span></div>
</li>
<li data-pantry="1"><div class="p-ing__row"><span class="p-ing__q">1 szcz.</span><span class="p-ing__n">cynamonu</span><span class="p-ing__g">1 g</span></div>
</li>
<li data-pantry="1"><div class="p-ing__row"><span class="p-ing__q">1 szcz.</span><span class="p-ing__n">kardamonu</span><span class="p-ing__g">1 g</span></div>
</li>
<li data-pantry="1"><div class="p-ing__row"><span class="p-ing__q">0.5 łyżeczki</span><span class="p-ing__n">proszku do pieczenia</span><span class="p-ing__g">2 g</span></div>
</li>
<li><div class="p-ing__row"><span class="p-ing__q">3 garści</span><span class="p-ing__n">malin</span><span class="p-ing__g">210 g</span></div>
</li>
<li><div class="p-ing__row"><span class="p-ing__q">2 łyżeczki</span><span class="p-ing__n">oleju kokosowego</span><span class="p-ing__g">10 g</span></div>
<div class="p-ing__swap">
<label class="p-swaplabel" for="swap-8">Zamień na</label>
<select class="p-select" id="swap-8" data-ing="8">
<option value="oliwa">Oliwa z oliwek</option>
<option value="olej-rzepakowy">Olej rzepakowy</option>
<option value="olej-kokosowy" selected>Olej kokosowy · oryginał</option>
<option value="olej-z-awokado">Olej z awokado</option>
</select>
</div>
</li>
</ul>

<div class="p-actions">
<button type="button" class="p-btn p-btn--block" id="open-shopping">&#128722; Lista zakupów</button>
<button type="button" class="p-btn p-btn--primary p-btn--block" id="cook-start">Gotujmy &rarr;</button>
</div>
<noscript><p class="p-note">Lista zakupów, przelicznik porcji i tryb gotowania krok po kroku wymagają JavaScriptu. Składniki i sposób przygotowania czytasz normalnie — ilości są podane dla jednej porcji z planu.</p></noscript>

<h2>Sposób przygotowania</h2>
<ol class="p-steps" id="steps-list">
<li>Żółtko jaja energicznie wymieszaj widelcem</li>
<li>Mąkę połącz z proszkiem do pieczenia i odżywką białkową. Dodaj je do żółtka i napoju roślinnego</li>
<li>Białka jaj ubij na sztywną pianę i dodaj do ciasta delikatnie mieszając</li>
<li>Rozgrzej patelnię z odrobiną oleju kokosowego i smaż na małym ogniu pod przykryciem</li>
<li>Placuszki smakują najlepiej na ciepło z ulubiony dodatkami. Polecam borówki, maliny lub truskawki. Smacznego!</li>
</ol>

<div class="p-cook" id="cook" data-open="0" role="dialog" aria-modal="true" aria-label="Gotowanie: Fit Placuszki">
<div class="p-cook__bar">
<span class="p-cook__title">Fit Placuszki</span>
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

<script>window.RECIPE = {"slug": "fit-placuszki", "title": "Fit Placuszki", "slotLabel": "Śniadanie", "time": "7:00-10:00", "baseServings": 1, "kcal": 473, "ingredients": [{"qty": 1.0, "unit": "sztuka", "unitLemma": "sztuka", "name": "jaja kurzego", "grams": 56.0, "pantry": false, "tag": "jajka"}, {"qty": 3.0, "unit": "łyżki", "unitLemma": "łyżka", "name": "mąki owsianej pełnoziarnistej", "grams": 36.0, "pantry": false, "tag": "maka"}, {"qty": 2.0, "unit": "łyżki", "unitLemma": "łyżka", "name": "odżywki białkowej", "grams": 16.0, "pantry": false, "tag": "odzywka"}, {"qty": 3.0, "unit": "łyżki", "unitLemma": "łyżka", "name": "napoju roślinnego, np. migdałowego", "grams": 45.0, "pantry": false, "tag": "mleko"}, {"qty": 1.0, "unit": "szczypta", "unitLemma": "szczypta", "name": "cynamonu", "grams": 1.0, "pantry": true, "tag": null}, {"qty": 1.0, "unit": "szczypta", "unitLemma": "szczypta", "name": "kardamonu", "grams": 1.0, "pantry": true, "tag": null}, {"qty": 0.5, "unit": "łyżeczki", "unitLemma": "łyżeczka", "name": "proszku do pieczenia", "grams": 2.0, "pantry": true, "tag": null}, {"qty": 3.0, "unit": "garści", "unitLemma": "garść", "name": "malin", "grams": 210.0, "pantry": false, "tag": "maliny"}, {"qty": 2.0, "unit": "łyżeczki", "unitLemma": "łyżeczka", "name": "oleju kokosowego", "grams": 10.0, "pantry": false, "tag": "olej-kokosowy", "swap": {"group": "tluszcz", "self": "olej-kokosowy", "nameCase": "M"}}], "steps": ["Żółtko jaja energicznie wymieszaj widelcem", "Mąkę połącz z proszkiem do pieczenia i odżywką białkową. Dodaj je do żółtka i napoju roślinnego", "Białka jaj ubij na sztywną pianę i dodaj do ciasta delikatnie mieszając", "Rozgrzej patelnię z odrobiną «8|D|||» i smaż na małym ogniu pod przykryciem", "Placuszki smakują najlepiej na ciepło z ulubiony dodatkami. Polecam borówki, maliny lub truskawki. Smacznego!"]};
window.UNITS = {"łyżka": ["łyżka", "łyżki", "łyżek", "łyżki"], "łyżeczka": ["łyżeczka", "łyżeczki", "łyżeczek", "łyżeczki"], "sztuka": ["sztuka", "sztuki", "sztuk", "sztuki"], "garść": ["garść", "garście", "garści", "garści"], "kromka": ["kromka", "kromki", "kromek", "kromki"], "plaster": ["plaster", "plastry", "plastrów", "plastra"], "szklanka": ["szklanka", "szklanki", "szklanek", "szklanki"], "opakowanie": ["opakowanie", "opakowania", "opakowań", "opakowania"], "ząbek": ["ząbek", "ząbki", "ząbków", "ząbka"], "szczypta": ["szczypta", "szczypty", "szczypt", "szczypty"], "porcja": ["porcja", "porcje", "porcji", "porcji"], "puszka": ["puszka", "puszki", "puszek", "puszki"], "kostka": ["kostka", "kostki", "kostek", "kostki"], "listek": ["listek", "listki", "listków", "listka"], "łodyga": ["łodyga", "łodygi", "łodyg", "łodygi"]};
window.SWAPS = {"tluszcz": {"label": "Oliwa i oleje", "options": [{"id": "oliwa", "label": "Oliwa z oliwek", "rodzaj": "f", "formy": {"M": "oliwa z oliwek", "D": "oliwy z oliwek", "B": "oliwę z oliwek", "N": "oliwą z oliwek", "Ms": "oliwie z oliwek"}, "rodzajB": "f"}, {"id": "olej-rzepakowy", "label": "Olej rzepakowy", "rodzaj": "m", "formy": {"M": "olej rzepakowy", "D": "oleju rzepakowego", "B": "olej rzepakowy", "N": "olejem rzepakowym", "Ms": "oleju rzepakowym"}, "rodzajB": "m"}, {"id": "olej-kokosowy", "label": "Olej kokosowy", "rodzaj": "m", "formy": {"M": "olej kokosowy", "D": "oleju kokosowego", "B": "olej kokosowy", "N": "olejem kokosowym", "Ms": "oleju kokosowym"}, "rodzajB": "m"}, {"id": "olej-z-awokado", "label": "Olej z awokado", "rodzaj": "m", "formy": {"M": "olej z awokado", "D": "oleju z awokado", "B": "olej z awokado", "N": "olejem z awokado", "Ms": "oleju z awokado"}, "rodzajB": "m"}]}};
window.SWAP_ADJ = {"umyty_B": {"m": "umyty", "f": "umytą", "n": "umyte", "pl": "umyte", "mz": "umytego"}, "swiezy_B": {"m": "świeży", "f": "świeżą", "n": "świeże", "pl": "świeże", "mz": "świeżego"}, "odsaczony_B": {"m": "odsączony", "f": "odsączoną", "n": "odsączone", "pl": "odsączone", "mz": "odsączonego"}, "pieczony_N": {"m": "pieczonym", "f": "pieczoną", "n": "pieczonym", "pl": "pieczonymi", "mz": "pieczonym"}, "pokrojony_B": {"m": "pokrojony", "f": "pokrojoną", "n": "pokrojone", "pl": "pokrojone", "mz": "pokrojonego"}, "ugotowany_B": {"m": "ugotowany", "f": "ugotowaną", "n": "ugotowane", "pl": "ugotowane", "mz": "ugotowanego"}, "podsmazony_B": {"m": "podsmażony", "f": "podsmażoną", "n": "podsmażone", "pl": "podsmażone", "mz": "podsmażonego"}, "przyprawiony_B": {"m": "przyprawiony", "f": "przyprawioną", "n": "przyprawione", "pl": "przyprawione", "mz": "przyprawionego"}, "prazony_N": {"m": "prażonym", "f": "prażoną", "n": "prażonym", "pl": "prażonymi", "mz": "prażonym"}, "pokrojony_N": {"m": "pokrojonym", "f": "pokrojoną", "n": "pokrojonym", "pl": "pokrojonymi", "mz": "pokrojonym"}, "starty_B": {"m": "starty", "f": "startą", "n": "starte", "pl": "starte", "mz": "startego"}, "ugotowany_N": {"m": "ugotowanym", "f": "ugotowaną", "n": "ugotowanym", "pl": "ugotowanymi", "mz": "ugotowanym"}, "przygotowany_B": {"m": "przygotowany", "f": "przygotowaną", "n": "przygotowane", "pl": "przygotowane", "mz": "przygotowanego"}};</script>
