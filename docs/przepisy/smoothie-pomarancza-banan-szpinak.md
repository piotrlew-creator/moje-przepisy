---
hide:
  - toc
---

<a class="p-back" href="../../">&larr; Wszystkie przepisy</a>

# Smoothie pomarańcza banan szpinak

<div class="p-hero" data-slot="3">
<div class="p-hero__top">
<span>Kolacja</span><span class="p-num">18:00-20:00</span>
</div>
<div class="p-macros">
<div class="p-macro"><span class="p-macro__v">184</span><span class="p-macro__l">kcal</span></div>
<div class="p-macro"><span class="p-macro__v">5 g</span><span class="p-macro__l">białko</span></div>
<div class="p-macro"><span class="p-macro__v">43 g</span><span class="p-macro__l">węgl.</span></div>
<div class="p-macro"><span class="p-macro__v">1 g</span><span class="p-macro__l">tłuszcz</span></div>
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
<li data-order="name"><div class="p-ing__row"><span class="p-ing__q">0.5 sztuki</span><span class="p-ing__n">Pomarańcza</span><span class="p-ing__g">120 g</span></div>
</li>
<li data-order="name"><div class="p-ing__row"><span class="p-ing__q">2 garści</span><span class="p-ing__n">Szpinak</span><span class="p-ing__g">50 g</span></div>
<div class="p-ing__swap">
<label class="p-swaplabel" for="swap-1">Zamień na</label>
<select class="p-select" id="swap-1" data-ing="1">
<option value="szpinak" selected>Szpinak · oryginał</option>
<option value="rukola">Rukola</option>
<option value="roszponka">Roszponka</option>
<option value="jarmuz">Jarmuż</option>
<option value="salata-rzymska">Sałata rzymska</option>
<option value="miks-salat">Miks sałat</option>
</select>
</div>
</li>
<li data-order="name"><div class="p-ing__row"><span class="p-ing__q">1 sztuka</span><span class="p-ing__n">Banan</span><span class="p-ing__g">120 g</span></div>
<div class="p-ing__swap">
<label class="p-swaplabel" for="swap-2">Zamień na</label>
<select class="p-select" id="swap-2" data-ing="2">
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
<li data-pantry="1" data-order="name"><div class="p-ing__row"><span class="p-ing__q">1 szklanka</span><span class="p-ing__n">Woda</span><span class="p-ing__g">250 g</span></div>
</li>
</ul>

<div class="p-actions">
<button type="button" class="p-btn p-btn--block" id="open-shopping">&#128722; Lista zakupów</button>
<button type="button" class="p-btn p-btn--primary p-btn--block" id="cook-start">Gotujmy &rarr;</button>
</div>

<h2>Sposób przygotowania</h2>
<ol class="p-steps" id="steps-list">
<li>Do blendera wlej sok z wyciśniętych pomarańczy lub obrane pomarańcze, dodaj liście szpinaku i pokrojony banan oraz wodę.</li>
<li>Wszystkie składniki zmiksuj ze sobą na gładkie smoothie. Smacznego!</li>
</ol>

<div class="p-cook" id="cook" data-open="0" role="dialog" aria-modal="true" aria-label="Gotowanie: Smoothie pomarańcza banan szpinak">
<div class="p-cook__bar">
<span class="p-cook__title">Smoothie pomarańcza banan szpinak</span>
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

<script>window.RECIPE = {"slug": "smoothie-pomarancza-banan-szpinak", "title": "Smoothie pomarańcza banan szpinak", "slotLabel": "Kolacja", "time": "18:00-20:00", "baseServings": 1, "ingredients": [{"qty": 0.5, "unit": "sztuki", "unitLemma": "sztuka", "name": "Pomarańcza", "grams": 120.0, "pantry": false, "tag": "pomarancza", "nameFirst": true}, {"qty": 2.0, "unit": "garści", "unitLemma": "garść", "name": "Szpinak", "grams": 50.0, "pantry": false, "tag": "szpinak", "nameFirst": true, "swap": {"group": "liscizielone", "self": "szpinak", "nameCase": "M"}}, {"qty": 1.0, "unit": "sztuka", "unitLemma": "sztuka", "name": "Banan", "grams": 120.0, "pantry": false, "tag": "banan", "nameFirst": true, "swap": {"group": "owoce", "self": "banan", "nameCase": "M"}}, {"qty": 1.0, "unit": "szklanka", "unitLemma": "szklanka", "name": "Woda", "grams": 250.0, "pantry": true, "tag": null, "nameFirst": true}], "steps": ["Do blendera wlej sok z wyciśniętych pomarańczy lub obrane pomarańcze, dodaj liście «1|D|||» i «2|B|pokrojony_B||» oraz wodę.", "Wszystkie składniki zmiksuj ze sobą na gładkie smoothie. Smacznego!"]};
window.UNITS = {"łyżka": ["łyżka", "łyżki", "łyżek", "łyżki"], "łyżeczka": ["łyżeczka", "łyżeczki", "łyżeczek", "łyżeczki"], "sztuka": ["sztuka", "sztuki", "sztuk", "sztuki"], "garść": ["garść", "garście", "garści", "garści"], "kromka": ["kromka", "kromki", "kromek", "kromki"], "plaster": ["plaster", "plastry", "plastrów", "plastra"], "szklanka": ["szklanka", "szklanki", "szklanek", "szklanki"], "opakowanie": ["opakowanie", "opakowania", "opakowań", "opakowania"], "ząbek": ["ząbek", "ząbki", "ząbków", "ząbka"], "szczypta": ["szczypta", "szczypty", "szczypt", "szczypty"], "porcja": ["porcja", "porcje", "porcji", "porcji"], "puszka": ["puszka", "puszki", "puszek", "puszki"], "kostka": ["kostka", "kostki", "kostek", "kostki"], "listek": ["listek", "listki", "listków", "listka"], "łodyga": ["łodyga", "łodygi", "łodyg", "łodygi"]};
window.SWAPS = {"liscizielone": {"label": "Zielone warzywa liściaste", "options": [{"id": "szpinak", "label": "Szpinak", "rodzaj": "m", "formy": {"M": "szpinak", "D": "szpinaku", "B": "szpinak", "N": "szpinakiem", "Ms": "szpinaku"}, "rodzajB": "m"}, {"id": "rukola", "label": "Rukola", "rodzaj": "f", "formy": {"M": "rukola", "D": "rukoli", "B": "rukolę", "N": "rukolą", "Ms": "rukoli"}, "rodzajB": "f"}, {"id": "roszponka", "label": "Roszponka", "rodzaj": "f", "formy": {"M": "roszponka", "D": "roszponki", "B": "roszponkę", "N": "roszponką", "Ms": "roszponce"}, "rodzajB": "f"}, {"id": "jarmuz", "label": "Jarmuż", "rodzaj": "m", "formy": {"M": "jarmuż", "D": "jarmużu", "B": "jarmuż", "N": "jarmużem", "Ms": "jarmużu"}, "rodzajB": "m"}, {"id": "salata-rzymska", "label": "Sałata rzymska", "rodzaj": "f", "formy": {"M": "sałata rzymska", "D": "sałaty rzymskiej", "B": "sałatę rzymską", "N": "sałatą rzymską", "Ms": "sałacie rzymskiej"}, "rodzajB": "f"}, {"id": "miks-salat", "label": "Miks sałat", "rodzaj": "m", "formy": {"M": "miks sałat", "D": "miksu sałat", "B": "miks sałat", "N": "miksem sałat", "Ms": "miksie sałat"}, "rodzajB": "m"}]}, "owoce": {"label": "Owoce", "options": [{"id": "jablko", "label": "Jabłko", "rodzaj": "n", "formy": {"M": "jabłko", "D": "jabłka", "B": "jabłko", "N": "jabłkiem", "Ms": "jabłku", "Mpl": "jabłka", "Dpl": "jabłek", "Bpl": "jabłka", "Npl": "jabłkami", "Mspl": "jabłkach"}, "equiv": 170, "rodzajB": "n"}, {"id": "gruszka", "label": "Gruszka", "rodzaj": "f", "formy": {"M": "gruszka", "D": "gruszki", "B": "gruszkę", "N": "gruszką", "Ms": "gruszce", "Mpl": "gruszki", "Dpl": "gruszek", "Bpl": "gruszki", "Npl": "gruszkami", "Mspl": "gruszkach"}, "equiv": 170, "rodzajB": "f"}, {"id": "banan", "label": "Banan", "rodzaj": "m", "formy": {"M": "banan", "D": "banana", "B": "banan", "N": "bananem", "Ms": "bananie", "Bpot": "banana", "Mpl": "banany", "Dpl": "bananów", "Bpl": "banany", "Npl": "bananami", "Mspl": "bananach"}, "equiv": 120, "rodzajB": "mz"}, {"id": "mandarynka", "label": "Mandarynka", "rodzaj": "f", "formy": {"M": "mandarynka", "D": "mandarynki", "B": "mandarynkę", "N": "mandarynką", "Ms": "mandarynce", "Mpl": "mandarynki", "Dpl": "mandarynek", "Bpl": "mandarynki", "Npl": "mandarynkami", "Mspl": "mandarynkach"}, "equiv": 65, "rodzajB": "f"}, {"id": "brzoskwinia", "label": "Brzoskwinia", "rodzaj": "f", "formy": {"M": "brzoskwinia", "D": "brzoskwini", "B": "brzoskwinię", "N": "brzoskwinią", "Ms": "brzoskwini", "Mpl": "brzoskwinie", "Dpl": "brzoskwiń", "Bpl": "brzoskwinie", "Npl": "brzoskwiniami", "Mspl": "brzoskwiniach"}, "equiv": 90, "rodzajB": "f"}, {"id": "kiwi", "label": "Kiwi", "rodzaj": "n", "formy": {"M": "kiwi", "D": "kiwi", "B": "kiwi", "N": "kiwi", "Ms": "kiwi", "Mpl": "kiwi", "Dpl": "kiwi", "Bpl": "kiwi", "Npl": "kiwi", "Mspl": "kiwi"}, "equiv": 80, "rodzajB": "n"}, {"id": "kaki", "label": "Kaki", "rodzaj": "n", "formy": {"M": "kaki", "D": "kaki", "B": "kaki", "N": "kaki", "Ms": "kaki", "Mpl": "kaki", "Dpl": "kaki", "Bpl": "kaki", "Npl": "kaki", "Mspl": "kaki"}, "equiv": 250, "rodzajB": "n"}]}};
window.SWAP_ADJ = {"umyty_B": {"m": "umyty", "f": "umytą", "n": "umyte", "pl": "umyte", "mz": "umytego"}, "swiezy_B": {"m": "świeży", "f": "świeżą", "n": "świeże", "pl": "świeże", "mz": "świeżego"}, "odsaczony_B": {"m": "odsączony", "f": "odsączoną", "n": "odsączone", "pl": "odsączone", "mz": "odsączonego"}, "pieczony_N": {"m": "pieczonym", "f": "pieczoną", "n": "pieczonym", "pl": "pieczonymi", "mz": "pieczonym"}, "pokrojony_B": {"m": "pokrojony", "f": "pokrojoną", "n": "pokrojone", "pl": "pokrojone", "mz": "pokrojonego"}, "ugotowany_B": {"m": "ugotowany", "f": "ugotowaną", "n": "ugotowane", "pl": "ugotowane", "mz": "ugotowanego"}, "podsmazony_B": {"m": "podsmażony", "f": "podsmażoną", "n": "podsmażone", "pl": "podsmażone", "mz": "podsmażonego"}, "przyprawiony_B": {"m": "przyprawiony", "f": "przyprawioną", "n": "przyprawione", "pl": "przyprawione", "mz": "przyprawionego"}, "prazony_N": {"m": "prażonym", "f": "prażoną", "n": "prażonym", "pl": "prażonymi", "mz": "prażonym"}, "pokrojony_N": {"m": "pokrojonym", "f": "pokrojoną", "n": "pokrojonym", "pl": "pokrojonymi", "mz": "pokrojonym"}, "starty_B": {"m": "starty", "f": "startą", "n": "starte", "pl": "starte", "mz": "startego"}, "ugotowany_N": {"m": "ugotowanym", "f": "ugotowaną", "n": "ugotowanym", "pl": "ugotowanymi", "mz": "ugotowanym"}, "przygotowany_B": {"m": "przygotowany", "f": "przygotowaną", "n": "przygotowane", "pl": "przygotowane", "mz": "przygotowanego"}};</script>
