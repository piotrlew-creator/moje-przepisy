---
hide:
  - toc
---

<a class="p-back" href="../../">&larr; Wszystkie przepisy</a>

# Pancakes

<div class="p-hero" data-slot="3">
<div class="p-hero__top">
<span>Kolacja</span><span class="p-num">18:00-20:00</span>
</div>
<div class="p-macros">
<div class="p-macro"><span class="p-macro__v">473</span><span class="p-macro__l">kcal</span></div>
<div class="p-macro"><span class="p-macro__v">17 g</span><span class="p-macro__l">białko</span></div>
<div class="p-macro"><span class="p-macro__v">51 g</span><span class="p-macro__l">węgl.</span></div>
<div class="p-macro"><span class="p-macro__v">24 g</span><span class="p-macro__l">tłuszcz</span></div>
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
<li><div class="p-ing__row"><span class="p-ing__q">1 sztuka</span><span class="p-ing__n">małego banana</span><span class="p-ing__g">60 g</span></div>
<div class="p-ing__swap">
<label class="p-swaplabel" for="swap-0">Zamień na</label>
<select class="p-select" id="swap-0" data-ing="0">
<option value="jablko">Jabłko</option>
<option value="gruszka">Gruszka</option>
<option value="banan" selected>Banan · oryginał</option>
<option value="mandarynka">Mandarynka</option>
<option value="brzoskwinia">Brzoskwinia</option>
<option value="kiwi">Kiwi</option>
<option value="kaki">Kaki</option>
</select>
</div>
</li>
<li><div class="p-ing__row"><span class="p-ing__q">1 sztuka</span><span class="p-ing__n">jajka</span><span class="p-ing__g">56 g</span></div>
</li>
<li><div class="p-ing__row"><span class="p-ing__q">4 łyżki</span><span class="p-ing__n">płatków owsianych</span><span class="p-ing__g">40 g</span></div>
<div class="p-ing__swap">
<label class="p-swaplabel" for="swap-2">Zamień na</label>
<select class="p-select" id="swap-2" data-ing="2">
<option value="platki-owsiane" selected>Płatki owsiane · oryginał</option>
<option value="platki-jaglane">Płatki jaglane</option>
<option value="platki-gryczane">Płatki gryczane</option>
<option value="platki-ryzowe">Płatki ryżowe</option>
<option value="platki-orkiszowe">Płatki orkiszowe</option>
</select>
</div>
</li>
<li><div class="p-ing__row"><span class="p-ing__q">1 łyżeczka</span><span class="p-ing__n">masła orzechowego</span><span class="p-ing__g">10 g</span></div>
</li>
<li><div class="p-ing__row"><span class="p-ing__q">1 porcja</span><span class="p-ing__n">gorzkiej czekolady</span><span class="p-ing__g">10 g</span></div>
</li>
<li><div class="p-ing__row"><span class="p-ing__q">1 łyżeczka</span><span class="p-ing__n">oleju kokosowego</span><span class="p-ing__g">5 g</span></div>
<div class="p-ing__swap">
<label class="p-swaplabel" for="swap-5">Zamień na</label>
<select class="p-select" id="swap-5" data-ing="5">
<option value="oliwa">Oliwa z oliwek</option>
<option value="olej-rzepakowy">Olej rzepakowy</option>
<option value="olej-kokosowy" selected>Olej kokosowy · oryginał</option>
<option value="olej-z-awokado">Olej z awokado</option>
</select>
</div>
</li>
<li><div class="p-ing__row"><span class="p-ing__q">2 łyżki</span><span class="p-ing__n">jogurtu naturalnego</span><span class="p-ing__g">40 g</span></div>
</li>
</ul>

<div class="p-actions">
<button type="button" class="p-btn p-btn--block" id="open-shopping">&#128722; Lista zakupów</button>
<button type="button" class="p-btn p-btn--primary p-btn--block" id="cook-start">Gotujmy &rarr;</button>
</div>

<h2>Sposób przygotowania</h2>
<ol class="p-steps" id="steps-list">
<li>Banany rozgnieć widelcem, dodaj jajka, jogurt i dokładnie wymieszaj</li>
<li>Dodaj płatki owsiane i następnie całość wymieszaj</li>
<li>Do gotowej masy możesz dodać gorzką czekoladę</li>
<li>Smaż na patelni lekko zwilżonej olejem kokosowym, udekoruj i gotowe! Smacznego!</li>
</ol>

<div class="p-cook" id="cook" data-open="0" role="dialog" aria-modal="true" aria-label="Gotowanie: Pancakes">
<div class="p-cook__bar">
<span class="p-cook__title">Pancakes</span>
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

<script>window.RECIPE = {"slug": "pancakes", "title": "Pancakes", "slotLabel": "Kolacja", "time": "18:00-20:00", "baseServings": 1, "ingredients": [{"qty": 1.0, "unit": "sztuka", "unitLemma": "sztuka", "name": "małego banana", "grams": 60.0, "pantry": false, "tag": "banan", "swap": {"group": "owoce", "self": "banan", "nameCase": "D"}}, {"qty": 1.0, "unit": "sztuka", "unitLemma": "sztuka", "name": "jajka", "grams": 56.0, "pantry": false, "tag": "jajka"}, {"qty": 4.0, "unit": "łyżki", "unitLemma": "łyżka", "name": "płatków owsianych", "grams": 40.0, "pantry": false, "tag": "platki-owsiane", "swap": {"group": "platki", "self": "platki-owsiane", "nameCase": "D"}}, {"qty": 1.0, "unit": "łyżeczka", "unitLemma": "łyżeczka", "name": "masła orzechowego", "grams": 10.0, "pantry": false, "tag": "maslo-orzechowe"}, {"qty": 1.0, "unit": "porcja", "unitLemma": "porcja", "name": "gorzkiej czekolady", "grams": 10.0, "pantry": false, "tag": "czekolada"}, {"qty": 1.0, "unit": "łyżeczka", "unitLemma": "łyżeczka", "name": "oleju kokosowego", "grams": 5.0, "pantry": false, "tag": "olej-kokosowy", "swap": {"group": "tluszcz", "self": "olej-kokosowy", "nameCase": "M"}}, {"qty": 2.0, "unit": "łyżki", "unitLemma": "łyżka", "name": "jogurtu naturalnego", "grams": 40.0, "pantry": false, "tag": "jogurt"}], "steps": ["«0|Bpl|||U» rozgnieć widelcem, dodaj jajka, jogurt i dokładnie wymieszaj", "Dodaj «2|B|||» i następnie całość wymieszaj", "Do gotowej masy możesz dodać gorzką czekoladę", "Smaż na patelni lekko zwilżonej «5|N|||», udekoruj i gotowe! Smacznego!"]};
window.UNITS = {"łyżka": ["łyżka", "łyżki", "łyżek", "łyżki"], "łyżeczka": ["łyżeczka", "łyżeczki", "łyżeczek", "łyżeczki"], "sztuka": ["sztuka", "sztuki", "sztuk", "sztuki"], "garść": ["garść", "garście", "garści", "garści"], "kromka": ["kromka", "kromki", "kromek", "kromki"], "plaster": ["plaster", "plastry", "plastrów", "plastra"], "szklanka": ["szklanka", "szklanki", "szklanek", "szklanki"], "opakowanie": ["opakowanie", "opakowania", "opakowań", "opakowania"], "ząbek": ["ząbek", "ząbki", "ząbków", "ząbka"], "szczypta": ["szczypta", "szczypty", "szczypt", "szczypty"], "porcja": ["porcja", "porcje", "porcji", "porcji"], "puszka": ["puszka", "puszki", "puszek", "puszki"], "kostka": ["kostka", "kostki", "kostek", "kostki"], "listek": ["listek", "listki", "listków", "listka"], "łodyga": ["łodyga", "łodygi", "łodyg", "łodygi"]};
window.SWAPS = {"owoce": {"label": "Owoce", "options": [{"id": "jablko", "label": "Jabłko", "rodzaj": "n", "formy": {"M": "jabłko", "D": "jabłka", "B": "jabłko", "N": "jabłkiem", "Ms": "jabłku", "Mpl": "jabłka", "Dpl": "jabłek", "Bpl": "jabłka", "Npl": "jabłkami", "Mspl": "jabłkach"}, "equiv": 170, "rodzajB": "n"}, {"id": "gruszka", "label": "Gruszka", "rodzaj": "f", "formy": {"M": "gruszka", "D": "gruszki", "B": "gruszkę", "N": "gruszką", "Ms": "gruszce", "Mpl": "gruszki", "Dpl": "gruszek", "Bpl": "gruszki", "Npl": "gruszkami", "Mspl": "gruszkach"}, "equiv": 170, "rodzajB": "f"}, {"id": "banan", "label": "Banan", "rodzaj": "m", "formy": {"M": "banan", "D": "banana", "B": "banan", "N": "bananem", "Ms": "bananie", "Bpot": "banana", "Mpl": "banany", "Dpl": "bananów", "Bpl": "banany", "Npl": "bananami", "Mspl": "bananach"}, "equiv": 120, "rodzajB": "mz"}, {"id": "mandarynka", "label": "Mandarynka", "rodzaj": "f", "formy": {"M": "mandarynka", "D": "mandarynki", "B": "mandarynkę", "N": "mandarynką", "Ms": "mandarynce", "Mpl": "mandarynki", "Dpl": "mandarynek", "Bpl": "mandarynki", "Npl": "mandarynkami", "Mspl": "mandarynkach"}, "equiv": 65, "rodzajB": "f"}, {"id": "brzoskwinia", "label": "Brzoskwinia", "rodzaj": "f", "formy": {"M": "brzoskwinia", "D": "brzoskwini", "B": "brzoskwinię", "N": "brzoskwinią", "Ms": "brzoskwini", "Mpl": "brzoskwinie", "Dpl": "brzoskwiń", "Bpl": "brzoskwinie", "Npl": "brzoskwiniami", "Mspl": "brzoskwiniach"}, "equiv": 90, "rodzajB": "f"}, {"id": "kiwi", "label": "Kiwi", "rodzaj": "n", "formy": {"M": "kiwi", "D": "kiwi", "B": "kiwi", "N": "kiwi", "Ms": "kiwi", "Mpl": "kiwi", "Dpl": "kiwi", "Bpl": "kiwi", "Npl": "kiwi", "Mspl": "kiwi"}, "equiv": 80, "rodzajB": "n"}, {"id": "kaki", "label": "Kaki", "rodzaj": "n", "formy": {"M": "kaki", "D": "kaki", "B": "kaki", "N": "kaki", "Ms": "kaki", "Mpl": "kaki", "Dpl": "kaki", "Bpl": "kaki", "Npl": "kaki", "Mspl": "kaki"}, "equiv": 250, "rodzajB": "n"}]}, "platki": {"label": "Płatki", "options": [{"id": "platki-owsiane", "label": "Płatki owsiane", "rodzaj": "pl", "formy": {"M": "płatki owsiane", "D": "płatków owsianych", "B": "płatki owsiane", "N": "płatkami owsianymi", "Ms": "płatkach owsianych"}, "rodzajB": "pl"}, {"id": "platki-jaglane", "label": "Płatki jaglane", "rodzaj": "pl", "formy": {"M": "płatki jaglane", "D": "płatków jaglanych", "B": "płatki jaglane", "N": "płatkami jaglanymi", "Ms": "płatkach jaglanych"}, "rodzajB": "pl"}, {"id": "platki-gryczane", "label": "Płatki gryczane", "rodzaj": "pl", "formy": {"M": "płatki gryczane", "D": "płatków gryczanych", "B": "płatki gryczane", "N": "płatkami gryczanymi", "Ms": "płatkach gryczanych"}, "rodzajB": "pl"}, {"id": "platki-ryzowe", "label": "Płatki ryżowe", "rodzaj": "pl", "formy": {"M": "płatki ryżowe", "D": "płatków ryżowych", "B": "płatki ryżowe", "N": "płatkami ryżowymi", "Ms": "płatkach ryżowych"}, "rodzajB": "pl"}, {"id": "platki-orkiszowe", "label": "Płatki orkiszowe", "rodzaj": "pl", "formy": {"M": "płatki orkiszowe", "D": "płatków orkiszowych", "B": "płatki orkiszowe", "N": "płatkami orkiszowymi", "Ms": "płatkach orkiszowych"}, "rodzajB": "pl"}]}, "tluszcz": {"label": "Oliwa i oleje", "options": [{"id": "oliwa", "label": "Oliwa z oliwek", "rodzaj": "f", "formy": {"M": "oliwa z oliwek", "D": "oliwy z oliwek", "B": "oliwę z oliwek", "N": "oliwą z oliwek", "Ms": "oliwie z oliwek"}, "rodzajB": "f"}, {"id": "olej-rzepakowy", "label": "Olej rzepakowy", "rodzaj": "m", "formy": {"M": "olej rzepakowy", "D": "oleju rzepakowego", "B": "olej rzepakowy", "N": "olejem rzepakowym", "Ms": "oleju rzepakowym"}, "rodzajB": "m"}, {"id": "olej-kokosowy", "label": "Olej kokosowy", "rodzaj": "m", "formy": {"M": "olej kokosowy", "D": "oleju kokosowego", "B": "olej kokosowy", "N": "olejem kokosowym", "Ms": "oleju kokosowym"}, "rodzajB": "m"}, {"id": "olej-z-awokado", "label": "Olej z awokado", "rodzaj": "m", "formy": {"M": "olej z awokado", "D": "oleju z awokado", "B": "olej z awokado", "N": "olejem z awokado", "Ms": "oleju z awokado"}, "rodzajB": "m"}]}};
window.SWAP_ADJ = {"umyty_B": {"m": "umyty", "f": "umytą", "n": "umyte", "pl": "umyte", "mz": "umytego"}, "swiezy_B": {"m": "świeży", "f": "świeżą", "n": "świeże", "pl": "świeże", "mz": "świeżego"}, "odsaczony_B": {"m": "odsączony", "f": "odsączoną", "n": "odsączone", "pl": "odsączone", "mz": "odsączonego"}, "pieczony_N": {"m": "pieczonym", "f": "pieczoną", "n": "pieczonym", "pl": "pieczonymi", "mz": "pieczonym"}, "pokrojony_B": {"m": "pokrojony", "f": "pokrojoną", "n": "pokrojone", "pl": "pokrojone", "mz": "pokrojonego"}, "ugotowany_B": {"m": "ugotowany", "f": "ugotowaną", "n": "ugotowane", "pl": "ugotowane", "mz": "ugotowanego"}, "podsmazony_B": {"m": "podsmażony", "f": "podsmażoną", "n": "podsmażone", "pl": "podsmażone", "mz": "podsmażonego"}, "przyprawiony_B": {"m": "przyprawiony", "f": "przyprawioną", "n": "przyprawione", "pl": "przyprawione", "mz": "przyprawionego"}, "prazony_N": {"m": "prażonym", "f": "prażoną", "n": "prażonym", "pl": "prażonymi", "mz": "prażonym"}, "pokrojony_N": {"m": "pokrojonym", "f": "pokrojoną", "n": "pokrojonym", "pl": "pokrojonymi", "mz": "pokrojonym"}, "starty_B": {"m": "starty", "f": "startą", "n": "starte", "pl": "starte", "mz": "startego"}, "ugotowany_N": {"m": "ugotowanym", "f": "ugotowaną", "n": "ugotowanym", "pl": "ugotowanymi", "mz": "ugotowanym"}, "przygotowany_B": {"m": "przygotowany", "f": "przygotowaną", "n": "przygotowane", "pl": "przygotowane", "mz": "przygotowanego"}};</script>
