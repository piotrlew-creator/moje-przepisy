---
title: "Pudding czekoladowy z truskawkami"
hide:
  - toc
---

<a class="p-back" href="../../">&larr; Wszystkie przepisy</a>

# Pudding czekoladowy z truskawkami

<div class="p-hero" data-slot="3">
<div class="p-hero__top">
<span>Kolacja</span><span class="p-num">18:00-20:00</span>
</div>
<div class="p-macros">
<div class="p-macro"><span class="p-macro__v">456</span><span class="p-macro__l">kcal</span></div>
<div class="p-macro"><span class="p-macro__v">21 g</span><span class="p-macro__l">białko</span></div>
<div class="p-macro"><span class="p-macro__v">54 g</span><span class="p-macro__l">węgl.</span></div>
<div class="p-macro"><span class="p-macro__v">14 g</span><span class="p-macro__l">tłuszcz</span></div>
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
<li><div class="p-ing__row"><span class="p-ing__q">0.5 szklanki</span><span class="p-ing__n">mleka roślinnego np. migdałowe</span><span class="p-ing__g">125 g</span></div>
</li>
<li><div class="p-ing__row"><span class="p-ing__q">1 garść</span><span class="p-ing__n">truskawek</span><span class="p-ing__g">70 g</span></div>
</li>
<li data-pantry="1"><div class="p-ing__row"><span class="p-ing__q">3 łyżeczki</span><span class="p-ing__n">ksylitolu</span><span class="p-ing__g">21 g</span></div>
</li>
<li><div class="p-ing__row"><span class="p-ing__q">1 łyżka</span><span class="p-ing__n">kakao</span><span class="p-ing__g">10 g</span></div>
</li>
<li><div class="p-ing__row"><span class="p-ing__q">3 łyżki</span><span class="p-ing__n">płatków ryżowych</span><span class="p-ing__g">36 g</span></div>
<div class="p-ing__swap">
<label class="p-swaplabel" for="swap-4">Zamień na</label>
<select class="p-select" id="swap-4" data-ing="4">
<option value="platki-owsiane">Płatki owsiane</option>
<option value="platki-jaglane">Płatki jaglane</option>
<option value="platki-gryczane">Płatki gryczane</option>
<option value="platki-ryzowe" selected>Płatki ryżowe · oryginał</option>
<option value="platki-orkiszowe">Płatki orkiszowe</option>
</select>
</div>
</li>
<li><div class="p-ing__row"><span class="p-ing__q">2 łyżki</span><span class="p-ing__n">wegańskiej odżywki białkowej</span><span class="p-ing__g">16 g</span></div>
</li>
<li><div class="p-ing__row"><span class="p-ing__q">1 łyżka</span><span class="p-ing__n">wiórek kokosowych</span><span class="p-ing__g">15 g</span></div>
</li>
</ul>

<div class="p-actions">
<button type="button" class="p-btn p-btn--block" id="open-shopping">&#128722; Lista zakupów</button>
<button type="button" class="p-btn p-btn--primary p-btn--block" id="cook-start">Gotujmy &rarr;</button>
</div>
<noscript><p class="p-note">Lista zakupów, przelicznik porcji i tryb gotowania krok po kroku wymagają JavaScriptu. Składniki i sposób przygotowania czytasz normalnie — ilości są podane dla jednej porcji z planu.</p></noscript>

<h2>Sposób przygotowania</h2>
<ol class="p-steps" id="steps-list">
<li>Wszystkie składniki puddingu gotuj w rondelku przez 6 minut.</li>
<li>Jeżeli składniki się nie połączą, zblenduj na wysokich obrotach.</li>
<li>Gotowy pudding przełóż do miseczek i podaj z truskawkami.</li>
</ol>

<div class="p-cook" id="cook" data-open="0" role="dialog" aria-modal="true" aria-label="Gotowanie: Pudding czekoladowy z truskawkami">
<div class="p-cook__bar">
<span class="p-cook__title">Pudding czekoladowy z truskawkami</span>
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

<script>window.RECIPE = {"slug": "pudding-czekoladowy-z-truskawkami", "title": "Pudding czekoladowy z truskawkami", "slotLabel": "Kolacja", "time": "18:00-20:00", "baseServings": 1, "kcal": 456, "ingredients": [{"qty": 0.5, "unit": "szklanki", "unitLemma": "szklanka", "name": "mleka roślinnego np. migdałowe", "grams": 125.0, "pantry": false, "tag": "mleko"}, {"qty": 1.0, "unit": "garść", "unitLemma": "garść", "name": "truskawek", "grams": 70.0, "pantry": false, "tag": "truskawki"}, {"qty": 3.0, "unit": "łyżeczki", "unitLemma": "łyżeczka", "name": "ksylitolu", "grams": 21.0, "pantry": true, "tag": null}, {"qty": 1.0, "unit": "łyżka", "unitLemma": "łyżka", "name": "kakao", "grams": 10.0, "pantry": false, "tag": "kakao"}, {"qty": 3.0, "unit": "łyżki", "unitLemma": "łyżka", "name": "płatków ryżowych", "grams": 36.0, "pantry": false, "tag": "platki-inne", "swap": {"group": "platki", "self": "platki-ryzowe", "nameCase": "M"}}, {"qty": 2.0, "unit": "łyżki", "unitLemma": "łyżka", "name": "wegańskiej odżywki białkowej", "grams": 16.0, "pantry": false, "tag": "odzywka"}, {"qty": 1.0, "unit": "łyżka", "unitLemma": "łyżka", "name": "wiórek kokosowych", "grams": 15.0, "pantry": false, "tag": "wiorki"}], "steps": ["Wszystkie składniki puddingu gotuj w rondelku przez 6 minut.", "Jeżeli składniki się nie połączą, zblenduj na wysokich obrotach.", "Gotowy pudding przełóż do miseczek i podaj z truskawkami."]};
window.UNITS = {"łyżka": ["łyżka", "łyżki", "łyżek", "łyżki"], "łyżeczka": ["łyżeczka", "łyżeczki", "łyżeczek", "łyżeczki"], "sztuka": ["sztuka", "sztuki", "sztuk", "sztuki"], "garść": ["garść", "garście", "garści", "garści"], "kromka": ["kromka", "kromki", "kromek", "kromki"], "plaster": ["plaster", "plastry", "plastrów", "plastra"], "szklanka": ["szklanka", "szklanki", "szklanek", "szklanki"], "opakowanie": ["opakowanie", "opakowania", "opakowań", "opakowania"], "ząbek": ["ząbek", "ząbki", "ząbków", "ząbka"], "szczypta": ["szczypta", "szczypty", "szczypt", "szczypty"], "porcja": ["porcja", "porcje", "porcji", "porcji"], "puszka": ["puszka", "puszki", "puszek", "puszki"], "kostka": ["kostka", "kostki", "kostek", "kostki"], "listek": ["listek", "listki", "listków", "listka"], "łodyga": ["łodyga", "łodygi", "łodyg", "łodygi"]};
window.SWAPS = {"platki": {"label": "Płatki", "options": [{"id": "platki-owsiane", "label": "Płatki owsiane", "rodzaj": "pl", "formy": {"M": "płatki owsiane", "D": "płatków owsianych", "B": "płatki owsiane", "N": "płatkami owsianymi", "Ms": "płatkach owsianych"}, "rodzajB": "pl"}, {"id": "platki-jaglane", "label": "Płatki jaglane", "rodzaj": "pl", "formy": {"M": "płatki jaglane", "D": "płatków jaglanych", "B": "płatki jaglane", "N": "płatkami jaglanymi", "Ms": "płatkach jaglanych"}, "rodzajB": "pl"}, {"id": "platki-gryczane", "label": "Płatki gryczane", "rodzaj": "pl", "formy": {"M": "płatki gryczane", "D": "płatków gryczanych", "B": "płatki gryczane", "N": "płatkami gryczanymi", "Ms": "płatkach gryczanych"}, "rodzajB": "pl"}, {"id": "platki-ryzowe", "label": "Płatki ryżowe", "rodzaj": "pl", "formy": {"M": "płatki ryżowe", "D": "płatków ryżowych", "B": "płatki ryżowe", "N": "płatkami ryżowymi", "Ms": "płatkach ryżowych"}, "rodzajB": "pl"}, {"id": "platki-orkiszowe", "label": "Płatki orkiszowe", "rodzaj": "pl", "formy": {"M": "płatki orkiszowe", "D": "płatków orkiszowych", "B": "płatki orkiszowe", "N": "płatkami orkiszowymi", "Ms": "płatkach orkiszowych"}, "rodzajB": "pl"}]}};
window.SWAP_ADJ = {"umyty_B": {"m": "umyty", "f": "umytą", "n": "umyte", "pl": "umyte", "mz": "umytego"}, "swiezy_B": {"m": "świeży", "f": "świeżą", "n": "świeże", "pl": "świeże", "mz": "świeżego"}, "odsaczony_B": {"m": "odsączony", "f": "odsączoną", "n": "odsączone", "pl": "odsączone", "mz": "odsączonego"}, "pieczony_N": {"m": "pieczonym", "f": "pieczoną", "n": "pieczonym", "pl": "pieczonymi", "mz": "pieczonym"}, "pokrojony_B": {"m": "pokrojony", "f": "pokrojoną", "n": "pokrojone", "pl": "pokrojone", "mz": "pokrojonego"}, "ugotowany_B": {"m": "ugotowany", "f": "ugotowaną", "n": "ugotowane", "pl": "ugotowane", "mz": "ugotowanego"}, "podsmazony_B": {"m": "podsmażony", "f": "podsmażoną", "n": "podsmażone", "pl": "podsmażone", "mz": "podsmażonego"}, "przyprawiony_B": {"m": "przyprawiony", "f": "przyprawioną", "n": "przyprawione", "pl": "przyprawione", "mz": "przyprawionego"}, "prazony_N": {"m": "prażonym", "f": "prażoną", "n": "prażonym", "pl": "prażonymi", "mz": "prażonym"}, "pokrojony_N": {"m": "pokrojonym", "f": "pokrojoną", "n": "pokrojonym", "pl": "pokrojonymi", "mz": "pokrojonym"}, "starty_B": {"m": "starty", "f": "startą", "n": "starte", "pl": "starte", "mz": "startego"}, "ugotowany_N": {"m": "ugotowanym", "f": "ugotowaną", "n": "ugotowanym", "pl": "ugotowanymi", "mz": "ugotowanym"}, "przygotowany_B": {"m": "przygotowany", "f": "przygotowaną", "n": "przygotowane", "pl": "przygotowane", "mz": "przygotowanego"}};</script>
