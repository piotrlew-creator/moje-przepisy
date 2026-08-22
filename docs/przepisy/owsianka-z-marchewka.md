---
hide:
  - toc
---

<a class="p-back" href="../../">&larr; Wszystkie przepisy</a>

# Owsianka z marchewką

<div class="p-hero" data-slot="1">
<div class="p-hero__top">
<span>Śniadanie</span><span class="p-num">6:00-9:00</span><span class="p-num">Dzień 7</span>
</div>
<div class="p-macros">
<div class="p-macro"><span class="p-macro__v">453</span><span class="p-macro__l">kcal</span></div>
<div class="p-macro"><span class="p-macro__v">24 g</span><span class="p-macro__l">białko</span></div>
<div class="p-macro"><span class="p-macro__v">54 g</span><span class="p-macro__l">węgl.</span></div>
<div class="p-macro"><span class="p-macro__v">20 g</span><span class="p-macro__l">tłuszcz</span></div>
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
<li><span class="p-ing__q">0.5 szklanki</span><span>napoju roślinnego</span><span class="p-ing__g">125 g</span></li>
<li><span class="p-ing__q">2 łyżki</span><span>płatków owsianych górskich</span><span class="p-ing__g">20 g</span></li>
<li><span class="p-ing__q">1 sztuka</span><span>marchewki</span><span class="p-ing__g">45 g</span></li>
<li data-pantry="1"><span class="p-ing__q">1 szczypta</span><span>soli</span><span class="p-ing__g">0.25 g</span></li>
<li data-pantry="1"><span class="p-ing__q">1 łyżeczka</span><span>cynamonu</span><span class="p-ing__g">4 g</span></li>
<li><span class="p-ing__q">1 sztuka</span><span>małego banana</span><span class="p-ing__g">60 g</span></li>
<li><span class="p-ing__q">1 garść</span><span>mieszanki orzechów</span><span class="p-ing__g">30 g</span></li>
<li><span class="p-ing__q">2 łyżki</span><span>wegańskiej odżywki białkowej</span><span class="p-ing__g">16 g</span></li>
</ul>

<div class="p-actions">
<button type="button" class="p-btn p-btn--block" id="open-shopping">&#128722; Lista zakupów</button>
<button type="button" class="p-btn p-btn--primary p-btn--block" id="cook-start">Gotujmy &rarr;</button>
</div>

<h2>Sposób przygotowania</h2>
<ol class="p-steps">
<li>W rondelku podgrzewamy mleko roślinne, następnie dodajemy startą na drobnych oczkach marchewkę oraz płatki owsiane, odżywkę, sól i cynamon. Gotujemy przez 5-7 minut.</li>
<li>Przekładamy owsiankę do miski i na wierzch dodajemy posiekane orzechy oraz pokrojonego banana. Smacznego!</li>
</ol>

<div class="p-cook" id="cook" data-open="0" role="dialog" aria-modal="true" aria-label="Gotowanie: Owsianka z marchewką">
<div class="p-cook__bar">
<span class="p-cook__title">Owsianka z marchewką</span>
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

<script>window.RECIPE = {"slug": "owsianka-z-marchewka", "title": "Owsianka z marchewką", "day": 7, "slotLabel": "Śniadanie", "time": "6:00-9:00", "baseServings": 1, "ingredients": [{"qty": 0.5, "unit": "szklanki", "unitLemma": "szklanka", "name": "napoju roślinnego", "grams": 125.0, "pantry": false, "tag": "mleko"}, {"qty": 2.0, "unit": "łyżki", "unitLemma": "łyżka", "name": "płatków owsianych górskich", "grams": 20.0, "pantry": false, "tag": "platki-owsiane"}, {"qty": 1.0, "unit": "sztuka", "unitLemma": "sztuka", "name": "marchewki", "grams": 45.0, "pantry": false, "tag": "marchewka"}, {"qty": 1.0, "unit": "szczypta", "unitLemma": "szczypta", "name": "soli", "grams": 0.25, "pantry": true, "tag": null}, {"qty": 1.0, "unit": "łyżeczka", "unitLemma": "łyżeczka", "name": "cynamonu", "grams": 4.0, "pantry": true, "tag": null}, {"qty": 1.0, "unit": "sztuka", "unitLemma": "sztuka", "name": "małego banana", "grams": 60.0, "pantry": false, "tag": "banan"}, {"qty": 1.0, "unit": "garść", "unitLemma": "garść", "name": "mieszanki orzechów", "grams": 30.0, "pantry": false, "tag": "orzechy"}, {"qty": 2.0, "unit": "łyżki", "unitLemma": "łyżka", "name": "wegańskiej odżywki białkowej", "grams": 16.0, "pantry": false, "tag": "odzywka"}], "steps": ["W rondelku podgrzewamy mleko roślinne, następnie dodajemy startą na drobnych oczkach marchewkę oraz płatki owsiane, odżywkę, sól i cynamon. Gotujemy przez 5-7 minut.", "Przekładamy owsiankę do miski i na wierzch dodajemy posiekane orzechy oraz pokrojonego banana. Smacznego!"]};
window.UNITS = {"łyżka": ["łyżka", "łyżki", "łyżek", "łyżki"], "łyżeczka": ["łyżeczka", "łyżeczki", "łyżeczek", "łyżeczki"], "sztuka": ["sztuka", "sztuki", "sztuk", "sztuki"], "garść": ["garść", "garście", "garści", "garści"], "kromka": ["kromka", "kromki", "kromek", "kromki"], "plaster": ["plaster", "plastry", "plastrów", "plastra"], "szklanka": ["szklanka", "szklanki", "szklanek", "szklanki"], "opakowanie": ["opakowanie", "opakowania", "opakowań", "opakowania"], "ząbek": ["ząbek", "ząbki", "ząbków", "ząbka"], "szczypta": ["szczypta", "szczypty", "szczypt", "szczypty"], "porcja": ["porcja", "porcje", "porcji", "porcji"], "puszka": ["puszka", "puszki", "puszek", "puszki"]};</script>
