import os

recipes = {
    # DAY 1
    "klejacy-ryz.md": """# Klejący ryż z prażonym jabłkiem

<div class="portion-selector">
  <label for="persons-count">Liczba osób:</label>
  <input type="number" id="persons-count" value="1" min="1" onchange="updatePortions()">
  <button class="btn-action" onclick="toggleShoppingList()">🛒 Lista zakupów</button>
</div>

<div id="shopping-list-box" class="shopping-list-box">
  <h3>Lista zakupów</h3>
  <ul id="shopping-list-items"></ul>
  <button class="btn-action" onclick="printShoppingList()">📄 Wygeneruj PDF</button>
</div>

## Składniki (na 1 osobę)

- <span class="ing-item" data-base="30" data-unit="g" data-name="ryż basmati">30 g ryżu basmati</span> (2 łyżki)
- <span class="ing-item" data-base="125" data-unit="g" data-name="mleko roślinne">125 g mleka roślinnego</span> (0.5 szklanki)
- <span class="ing-item" data-base="150" data-unit="g" data-name="jabłko">150 g jabłka</span> (1 sztuka)
- <span class="ing-item" data-base="4" data-unit="g" data-name="cynamon">4 g cynamonu</span> (1 łyżeczka)
- <span class="ing-item" data-base="15" data-unit="g" data-name="ksylitol">15 g ksylitolu</span> (1 łyżka)
- <span class="ing-item" data-base="24" data-unit="g" data-name="wegańska odżywka białkowa">24 g wegańskiej odżywki białkowej</span> (3 łyżki)
- <span class="ing-item" data-base="80" data-unit="g" data-name="mleczko kokosowe 12%">80 g mleczka kokosowego 12%</span> (4 łyżki)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Jabłko kroimy w kostkę i doprawiamy cynamonem, w razie potrzeby dodajemy ksylitol.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Przyprawione jabłko dusimy w rondelku, aż puści soki i zacznie się rozpadać. Tak przygotowane jabłko przekładamy do miseczki.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Do rondelka po jabłkach wsypujemy ryż, odżywkę i zalewamy napojem roślinnym oraz mleczkiem kokosowym. Gotujemy na wolnym ogniu.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 4:</strong> Gdy ryż zacznie się rozklejać, dokładamy do niego około 2/3 masy jabłek, które wcześniej przygotowaliśmy.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 5:</strong> Wystarczająco gęsty i miękki ryż z jabłkami przekładamy do miseczki, a na niego układamy resztę jabłek, które nam zostały. Smacznego!</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>
""",

    "jajecznica.md": """# Jajecznica z pieczarkami, cebulą i pieczywem

<div class="portion-selector">
  <label for="persons-count">Liczba osób:</label>
  <input type="number" id="persons-count" value="1" min="1" onchange="updatePortions()">
  <button class="btn-action" onclick="toggleShoppingList()">🛒 Lista zakupów</button>
</div>

<div id="shopping-list-box" class="shopping-list-box">
  <h3>Lista zakupów</h3>
  <ul id="shopping-list-items"></ul>
  <button class="btn-action" onclick="printShoppingList()">📄 Wygeneruj PDF</button>
</div>

## Składniki (na 1 osobę)

- <span class="ing-item" data-base="168" data-unit="g" data-name="jajka kurze">168 g jajek kurzych</span> (3 sztuki)
- <span class="ing-item" data-base="100" data-unit="g" data-name="pieczarki">100 g pieczarek</span> (5 sztuk)
- <span class="ing-item" data-base="55" data-unit="g" data-name="cebula">55 g cebuli</span> (0.5 sztuki)
- <span class="ing-item" data-base="25" data-unit="g" data-name="szpinak">25 g szpinaku</span> (1 garść)
- <span class="ing-item" data-base="45" data-unit="g" data-name="rzodkiewka">45 g rzodkiewki</span> (3 sztuki)
- <span class="ing-item" data-base="5" data-unit="g" data-name="olej rzepakowy">5 g oleju rzepakowego</span> (1 łyżeczka)
- <span class="ing-item" data-base="60" data-unit="g" data-name="chleb żytni razowy">60 g chleba żytniego razowego</span> (2 kromki)
- <span class="ing-item" data-base="0.25" data-unit="g" data-name="sól">0.25 g soli</span> (1 szczypta)
- <span class="ing-item" data-base="0.25" data-unit="g" data-name="pieprz">0.25 g pieprzu</span> (1 szczypta)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Na patelni rozgrzewamy olej i podsmażamy pokrojone pieczarki oraz cebulę.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Do zeszklonych warzyw wbijamy jajka.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Smażymy na małym ogniu, cały czas mieszając, aż jajka się zetną.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 4:</strong> Gotową jajecznicę doprawiamy solą i pieprzem.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 5:</strong> Podajemy z pieczywem, szpinakiem i pokrojonymi rzodkiewkami. Smacznego!</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>
""",

    "makaron-mozzarella.md": """# Makaron z mozzarellą, szpinakiem, ogórkiem i pomidorkami koktajlowymi

<div class="portion-selector">
  <label for="persons-count">Liczba osób:</label>
  <input type="number" id="persons-count" value="1" min="1" onchange="updatePortions()">
  <button class="btn-action" onclick="toggleShoppingList()">🛒 Lista zakupów</button>
</div>

<div id="shopping-list-box" class="shopping-list-box">
  <h3>Lista zakupów</h3>
  <ul id="shopping-list-items"></ul>
  <button class="btn-action" onclick="printShoppingList()">📄 Wygeneruj PDF</button>
</div>

## Składniki (na 1 osobę)

- <span class="ing-item" data-base="50" data-unit="g" data-name="makaron pełnoziarnisty">50 g makaronu pełnoziarnistego</span> (1 porcja)
- <span class="ing-item" data-base="10" data-unit="g" data-name="zielone pesto">10 g zielonego pesto</span> (2 łyżeczki)
- <span class="ing-item" data-base="140" data-unit="g" data-name="pomidorki koktajlowe">140 g pomidorków koktajlowych</span> (7 sztuk)
- <span class="ing-item" data-base="1.5" data-unit="g" data-name="bazylia świeża">1.5 g bazylii świeżej</span> (0.5 garści)
- <span class="ing-item" data-base="50" data-unit="g" data-name="szpinak">50 g szpinaku</span> (2 garści)
- <span class="ing-item" data-base="75" data-unit="g" data-name="ogórek">75 g ogórka</span> (0.5 sztuki)
- <span class="ing-item" data-base="45" data-unit="g" data-name="mozzarella light">45 g mozzarelli light</span> (3 plastry)
- <span class="ing-item" data-base="10" data-unit="g" data-name="ser grana padano">10 g sera grana padano</span> (1 łyżka)
- <span class="ing-item" data-base="0.25" data-unit="g" data-name="sól">0.25 g soli</span> (1 szczypta)
- <span class="ing-item" data-base="0.25" data-unit="g" data-name="pieprz">0.25 g pieprzu</span> (1 szczypta)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Makaron gotujemy według instrukcji umieszczonej na opakowaniu.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Kroimy pomidorki, ogórek zielony, siekamy bazylię.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Do miski dodajemy makaron, pokrojone warzywa, posiekaną bazylię, umyty szpinak, czerwone pesto i całość dokładnie mieszamy, w razie potrzeby przyprawiamy solą i pieprzem.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 4:</strong> Gotowy makaron z warzywami wykładamy na talerz. Posypujmy tartym serem grana padano i układamy mozzarellę. Smacznego!</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>
""",

    "kulki-mocy.md": """# Daktylowo-kakaowe kulki mocy z orzechami

<div class="portion-selector">
  <label for="persons-count">Liczba osób:</label>
  <input type="number" id="persons-count" value="1" min="1" onchange="updatePortions()">
  <button class="btn-action" onclick="toggleShoppingList()">🛒 Lista zakupów</button>
</div>

<div id="shopping-list-box" class="shopping-list-box">
  <h3>Lista zakupów</h3>
  <ul id="shopping-list-items"></ul>
  <button class="btn-action" onclick="printShoppingList()">📄 Wygeneruj PDF</button>
</div>

## Składniki (na 1 osobę)

- <span class="ing-item" data-base="65" data-unit="g" data-name="daktyle">65 g daktyli</span> (13 sztuk)
- <span class="ing-item" data-base="20" data-unit="g" data-name="orzechy włoskie">20 g orzechów włoskich</span> (5 sztuk)
- <span class="ing-item" data-base="10" data-unit="g" data-name="kakao">10 g kakao</span> (1 łyżka)
- <span class="ing-item" data-base="15" data-unit="g" data-name="wiórki kokosowe">15 g wiórków kokosowych</span> (1 łyżka)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Daktyle namaczamy we wrzątku przez ok. 10 minut. Następnie wszystkie składniki blendujemy ze sobą, formujemy kulki i obtaczamy w wiórkach kokosowych. Smacznego!</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>
""",

    # DAY 2
    "owsianka.md": """# Owsianka

<div class="portion-selector">
  <label for="persons-count">Liczba osób:</label>
  <input type="number" id="persons-count" value="1" min="1" onchange="updatePortions()">
  <button class="btn-action" onclick="toggleShoppingList()">🛒 Lista zakupów</button>
</div>

<div id="shopping-list-box" class="shopping-list-box">
  <h3>Lista zakupów</h3>
  <ul id="shopping-list-items"></ul>
  <button class="btn-action" onclick="printShoppingList()">📄 Wygeneruj PDF</button>
</div>

## Składniki (na 1 osobę)

- <span class="ing-item" data-base="30" data-unit="g" data-name="płatki owsiane">30 g płatków owsianych</span> (3 łyżki)
- <span class="ing-item" data-base="100" data-unit="g" data-name="mały banan">100 g małego banana</span> (1 sztuka)
- <span class="ing-item" data-base="30" data-unit="g" data-name="orzechy nerkowca">30 g orzechów nerkowca</span> (1 garść)
- <span class="ing-item" data-base="24" data-unit="g" data-name="odżywka białkowa">24 g odżywki białkowej</span> (3 łyżki)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Płatki owsiane zalewamy wrzątkiem do linii płatków, pozostawiamy na 3 minuty.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Banana kroimy w plasterki, dodajemy odżywkę białkową i nerkowce.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Całość mieszamy i gotowe! Smacznego!</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>
""",

    "serek-wiejski-grahamka.md": """# Serek wiejski, papryka, grahamka i orzechy

<div class="portion-selector">
  <label for="persons-count">Liczba osób:</label>
  <input type="number" id="persons-count" value="1" min="1" onchange="updatePortions()">
  <button class="btn-action" onclick="toggleShoppingList()">🛒 Lista zakupów</button>
</div>

<div id="shopping-list-box" class="shopping-list-box">
  <h3>Lista zakupów</h3>
  <ul id="shopping-list-items"></ul>
  <button class="btn-action" onclick="printShoppingList()">📄 Wygeneruj PDF</button>
</div>

## Składniki (na 1 osobę)

- <span class="ing-item" data-base="150" data-unit="g" data-name="serek wiejski">150 g serka wiejskiego</span> (1 opakowanie)
- <span class="ing-item" data-base="85" data-unit="g" data-name="papryka żółta">85 g papryki żółtej</span> (0.5 sztuki)
- <span class="ing-item" data-base="80" data-unit="g" data-name="bułka grahamka">80 g bułki grahamki</span> (1 sztuka)
- <span class="ing-item" data-base="24" data-unit="g" data-name="orzechy włoskie">24 g orzechów włoskich</span> (6 sztuk)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Bułkę kroimy na pół, smarujemy serkiem wiejskim, układamy paprykę i orzechy. Smacznego!</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>
""",

    "krem-paprykowo-pomidorowy.md": """# Krem paprykowo-pomidorowy

<div class="portion-selector">
  <label for="persons-count">Liczba osób:</label>
  <input type="number" id="persons-count" value="1" min="1" onchange="updatePortions()">
  <button class="btn-action" onclick="toggleShoppingList()">🛒 Lista zakupów</button>
</div>

<div id="shopping-list-box" class="shopping-list-box">
  <h3>Lista zakupów</h3>
  <ul id="shopping-list-items"></ul>
  <button class="btn-action" onclick="printShoppingList()">📄 Wygeneruj PDF</button>
</div>

## Składniki (na 1 osobę)

- <span class="ing-item" data-base="200" data-unit="g" data-name="pomidory w puszce">200 g pomidorów w puszce</span> (0.5 opakowania)
- <span class="ing-item" data-base="0.5" data-unit="g" data-name="papryka wędzona">0.5 g papryki wędzonej</span> (1 szczypta)
- <span class="ing-item" data-base="3" data-unit="g" data-name="świeża bazylia">3 g świeżej bazylii</span> (1 garść)
- <span class="ing-item" data-base="0.25" data-unit="g" data-name="sól i pieprz">0.25 g soli i pieprzu</span> (1 szczypta)
- <span class="ing-item" data-base="35" data-unit="g" data-name="makaron razowy">35 g makaronu razowego</span> (7 łyżek)
- <span class="ing-item" data-base="5" data-unit="g" data-name="oliwa z oliwek">5 g oliwy z oliwek</span> (1 łyżeczka)
- <span class="ing-item" data-base="45" data-unit="g" data-name="mozzarella">45 g mozzarelli</span> (3 plastry)
- <span class="ing-item" data-base="45" data-unit="g" data-name="seler naciowy">45 g selera naciowego</span> (1 sztuka)
- <span class="ing-item" data-base="30" data-unit="g" data-name="mała cebula">30 g małej cebuli</span> (1 sztuka)
- <span class="ing-item" data-base="6" data-unit="g" data-name="czosnek">6 g czosnku</span> (1 ząbek)
- <span class="ing-item" data-base="45" data-unit="g" data-name="marchewka">45 g marchewki</span> (1 sztuka)
- <span class="ing-item" data-base="250" data-unit="g" data-name="woda">250 g wody</span> (1 szklanka)
- <span class="ing-item" data-base="85" data-unit="g" data-name="papryka czerwona">85 g papryki czerwonej</span> (0.5 sztuki)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Paprykę, seler, cebulę i marchewkę kroimy w kostkę, czosnek siekamy.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Na rozgrzanej oliwie w rondelku podsmażamy warzywa, dodajemy paprykę wędzoną. Po 7 minutach dodajemy pomidory, wodę i bazylię. Gotujemy przez 10 minut.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Całość blendujemy i doprawiamy solą i pieprzem. Gotujemy jeszcze przez 5 minut.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 4:</strong> Makaron gotujemy według instrukcji na opakowaniu.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 5:</strong> Mozzarellę kroimy w drobną kostkę.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 6:</strong> Zupę podajemy z makaronem i mozzarellą.</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>
""",

    "kanapki-z-serkiem.md": """# Kanapki z serkiem śmietankowym, pomidorem i szczypiorkiem

<div class="portion-selector">
  <label for="persons-count">Liczba osób:</label>
  <input type="number" id="persons-count" value="1" min="1" onchange="updatePortions()">
  <button class="btn-action" onclick="toggleShoppingList()">🛒 Lista zakupów</button>
</div>

<div id="shopping-list-box" class="shopping-list-box">
  <h3>Lista zakupów</h3>
  <ul id="shopping-list-items"></ul>
  <button class="btn-action" onclick="printShoppingList()">📄 Wygeneruj PDF</button>
</div>

## Składniki (na 1 osobę)

- <span class="ing-item" data-base="90" data-unit="g" data-name="chleb żytni razowy">90 g chleba żytniego razowego</span> (3 kromki)
- <span class="ing-item" data-base="75" data-unit="g" data-name="serek kanapkowy">75 g serka kanapkowego</span> (3 łyżki)
- <span class="ing-item" data-base="160" data-unit="g" data-name="pomidor">160 g pomidora</span> (1 sztuka)
- <span class="ing-item" data-base="10" data-unit="g" data-name="szczypiorek">10 g szczypiorku</span> (2 łyżeczki)
- <span class="ing-item" data-base="10" data-unit="g" data-name="nasiona słonecznika">10 g nasion słonecznika</span> (2 łyżeczki)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Pieczywo smarujemy serkiem.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Pomidora i szczypiorek kroimy. Pomidora kroimy w plasterki, nakładamy na kanapki. Szczypiorek drobno siekamy.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Kanapki posypujemy szczypiorkiem i nasionami słonecznika.</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>
""",

    # DAY 3
    "placuszki-owsiane.md": """# Placuszki owsiane orzechowe

<div class="portion-selector">
  <label for="persons-count">Liczba osób:</label>
  <input type="number" id="persons-count" value="1" min="1" onchange="updatePortions()">
  <button class="btn-action" onclick="toggleShoppingList()">🛒 Lista zakupów</button>
</div>

<div id="shopping-list-box" class="shopping-list-box">
  <h3>Lista zakupów</h3>
  <ul id="shopping-list-items"></ul>
  <button class="btn-action" onclick="printShoppingList()">📄 Wygeneruj PDF</button>
</div>

## Składniki (na 1 osobę)

- <span class="ing-item" data-base="60" data-unit="g" data-name="mały banan">60 g małego banana</span> (1 sztuka)
- <span class="ing-item" data-base="56" data-unit="g" data-name="jajo kurze">56 g jaja kurzego</span> (1 sztuka)
- <span class="ing-item" data-base="24" data-unit="g" data-name="mąka owsiana pełnoziarnista">24 g mąki owsianej pełnoziarnistej</span> (2 łyżki)
- <span class="ing-item" data-base="10" data-unit="g" data-name="masło orzechowe">10 g masła orzechowego</span> (1 łyżeczka)
- <span class="ing-item" data-base="16" data-unit="g" data-name="odżywka białkowa">16 g odżywki białkowej</span> (2 łyżki)
- <span class="ing-item" data-base="15" data-unit="g" data-name="mieszanka orzechów">15 g mieszanki orzechów</span> (0.5 garści)
- <span class="ing-item" data-base="15" data-unit="g" data-name="syrop z agawy">15 g syropu z agawy</span> (1 łyżka)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Składniki na ciasto blendujemy i odstawiamy na 5-10 minut.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Placuszki smażymy bez tłuszczu na nieprzywierającej patelni, podajemy polane syropem z agawy i posypane posiekanymi orzechami.</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>
""",

    "kanapki-z-serem.md": """# Kanapki z żółtym serem, roszponką i pomidorem

<div class="portion-selector">
  <label for="persons-count">Liczba osób:</label>
  <input type="number" id="persons-count" value="1" min="1" onchange="updatePortions()">
  <button class="btn-action" onclick="toggleShoppingList()">🛒 Lista zakupów</button>
</div>

<div id="shopping-list-box" class="shopping-list-box">
  <h3>Lista zakupów</h3>
  <ul id="shopping-list-items"></ul>
  <button class="btn-action" onclick="printShoppingList()">📄 Wygeneruj PDF</button>
</div>

## Składniki (na 1 osobę)

- <span class="ing-item" data-base="60" data-unit="g" data-name="chleb żytni razowy">60 g chleba żytniego razowego</span> (2 kromki)
- <span class="ing-item" data-base="75" data-unit="g" data-name="ser gouda">75 g sera gouda</span> (5 plastrów)
- <span class="ing-item" data-base="12.5" data-unit="g" data-name="roszponka">12.5 g roszponki</span> (0.5 garści)
- <span class="ing-item" data-base="160" data-unit="g" data-name="pomidor">160 g pomidora</span> (1 sztuka)
- <span class="ing-item" data-base="10" data-unit="g" data-name="margaryna">10 g margaryny</span> (2 łyżeczki)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Pieczywo smarujemy margaryną. Kładziemy na nie plastry sera.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Warzywa myjemy. Pomidora kroimy w plastry i układamy na kanapce razem z roszponką. Smacznego!</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>
""",

    "gyoza.md": """# Pierożki gyoza z warzywami chef select z kimchi

<div class="portion-selector">
  <label for="persons-count">Liczba osób:</label>
  <input type="number" id="persons-count" value="1" min="1" onchange="updatePortions()">
  <button class="btn-action" onclick="toggleShoppingList()">🛒 Lista zakupów</button>
</div>

<div id="shopping-list-box" class="shopping-list-box">
  <h3>Lista zakupów</h3>
  <ul id="shopping-list-items"></ul>
  <button class="btn-action" onclick="printShoppingList()">📄 Wygeneruj PDF</button>
</div>

## Składniki (na 1 osobę)

- <span class="ing-item" data-base="230" data-unit="g" data-name="Pierożki gyoza z warzywami chef select">230 g Pierożków gyoza z warzywami chef select</span> (1 opakowanie)
- <span class="ing-item" data-base="65" data-unit="g" data-name="mandarynka">65 g mandarynki</span> (1 sztuka)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Pierożki podgrzewamy wg instrukcji na opakowaniu. Na deser zjadamy mandarynkę.</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>
""",

    "koktajl-bananowy.md": """# Koktajl bananowo-orzechowy

<div class="portion-selector">
  <label for="persons-count">Liczba osób:</label>
  <input type="number" id="persons-count" value="1" min="1" onchange="updatePortions()">
  <button class="btn-action" onclick="toggleShoppingList()">🛒 Lista zakupów</button>
</div>

<div id="shopping-list-box" class="shopping-list-box">
  <h3>Lista zakupów</h3>
  <ul id="shopping-list-items"></ul>
  <button class="btn-action" onclick="printShoppingList()">📄 Wygeneruj PDF</button>
</div>

## Składniki (na 1 osobę)

- <span class="ing-item" data-base="120" data-unit="g" data-name="banan">120 g banana</span> (1 sztuka)
- <span class="ing-item" data-base="250" data-unit="g" data-name="napój sojowy">250 g napoju sojowego</span> (1 szklanka)
- <span class="ing-item" data-base="10" data-unit="g" data-name="erytrol">10 g erytrolu</span> (2 łyżeczki)
- <span class="ing-item" data-base="30" data-unit="g" data-name="masło orzechowe">30 g masła orzechowego</span> (3 łyżeczki)
- <span class="ing-item" data-base="15" data-unit="g" data-name="nasiona chia">15 g nasion chia</span> (3 łyżeczki)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Zblenduj wszystkie składniki. W razie potrzeby dodaj wody.</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>
""",

    # DAY 4
    "jaglanka-gruszka.md": """# Jaglanka na mleku roślinnym z gruszką

<div class="portion-selector">
  <label for="persons-count">Liczba osób:</label>
  <input type="number" id="persons-count" value="1" min="1" onchange="updatePortions()">
  <button class="btn-action" onclick="toggleShoppingList()">🛒 Lista zakupów</button>
</div>

<div id="shopping-list-box" class="shopping-list-box">
  <h3>Lista zakupów</h3>
  <ul id="shopping-list-items"></ul>
  <button class="btn-action" onclick="printShoppingList()">📄 Wygeneruj PDF</button>
</div>

## Składniki (na 1 osobę)

- <span class="ing-item" data-base="40" data-unit="g" data-name="płatki jaglane">40 g płatków jaglanych</span> (4 łyżki)
- <span class="ing-item" data-base="125" data-unit="g" data-name="mleko roślinne">125 g mleka roślinnego</span> (0.5 szklanki)
- <span class="ing-item" data-base="130" data-unit="g" data-name="gruszka">130 g gruszki</span> (1 sztuka)
- <span class="ing-item" data-base="2" data-unit="g" data-name="cynamon">2 g cynamonu</span> (0.5 łyżeczki)
- <span class="ing-item" data-base="16" data-unit="g" data-name="odżywka białkowa">16 g odżywki białkowej</span> (2 łyżki)
- <span class="ing-item" data-base="15" data-unit="g" data-name="orzechy włoskie">15 g orzechów włoskich</span> (0.5 garści)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Do rondelka wsypujemy płatki jaglane i zalewamy mlekiem. Gotujemy na małym ogniu, aż płatki będą miękkie. Mieszamy co chwilę.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Gruszkę kroimy w kostkę.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Gdy jaglanka zgęstnieje, dodajemy pokrojony owoc, odżywkę białkową i cynamon. Dokładnie mieszamy.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 4:</strong> Gotową jaglankę przekładamy do miseczki i posypujemy orzechami. Smacznego!</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>
""",

    "kanapki-z-pasta-warzywna.md": """# Kanapki z pastą warzywną, serem mozzarellą i ogórkiem

<div class="portion-selector">
  <label for="persons-count">Liczba osób:</label>
  <input type="number" id="persons-count" value="1" min="1" onchange="updatePortions()">
  <button class="btn-action" onclick="toggleShoppingList()">🛒 Lista zakupów</button>
</div>

<div id="shopping-list-box" class="shopping-list-box">
  <h3>Lista zakupów</h3>
  <ul id="shopping-list-items"></ul>
  <button class="btn-action" onclick="printShoppingList()">📄 Wygeneruj PDF</button>
</div>

## Składniki (na 1 osobę)

- <span class="ing-item" data-base="60" data-unit="g" data-name="chleb żytni razowy">60 g chleba żytniego razowego</span> (2 kromki)
- <span class="ing-item" data-base="40" data-unit="g" data-name="pasta warzywna">40 g pasty warzywnej</span> (2 łyżki)
- <span class="ing-item" data-base="90" data-unit="g" data-name="mozzarella">90 g mozzarelli</span> (6 plastrów)
- <span class="ing-item" data-base="75" data-unit="g" data-name="ogórek">75 g ogórka</span> (0.5 sztuki)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Pieczywo smarujemy pastą warzywną, kładziemy plasterki mozzarelli.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Ogórka myjemy, kroimy i nakładamy na kanapki.</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>
""",

    "kasza-z-tofu.md": """# Kasza z tofu

<div class="portion-selector">
  <label for="persons-count">Liczba osób:</label>
  <input type="number" id="persons-count" value="1" min="1" onchange="updatePortions()">
  <button class="btn-action" onclick="toggleShoppingList()">🛒 Lista zakupów</button>
</div>

<div id="shopping-list-box" class="shopping-list-box">
  <h3>Lista zakupów</h3>
  <ul id="shopping-list-items"></ul>
  <button class="btn-action" onclick="printShoppingList()">📄 Wygeneruj PDF</button>
</div>

## Składniki (na 1 osobę)

- <span class="ing-item" data-base="45" data-unit="g" data-name="kasza gryczana">45 g kaszy gryczanej</span> (3 łyżki)
- <span class="ing-item" data-base="90" data-unit="g" data-name="tofu naturalne">90 g tofu naturalnego</span> (0.5 opakowania)
- <span class="ing-item" data-base="225" data-unit="g" data-name="brokuł">225 g brokuła</span> (0.5 sztuki)
- <span class="ing-item" data-base="20" data-unit="g" data-name="cebula">20 g cebuli</span> (1 sztuka)
- <span class="ing-item" data-base="50" data-unit="g" data-name="szpinak">50 g szpinaku</span> (2 garści)
- <span class="ing-item" data-base="6" data-unit="g" data-name="czosnek">6 g czosnku</span> (1 ząbek)
- <span class="ing-item" data-base="5" data-unit="g" data-name="oliwa z oliwek">5 g oliwy z oliwek</span> (1 łyżeczka)
- <span class="ing-item" data-base="125" data-unit="g" data-name="bulion warzywny">125 g bulionu warzywnego</span> (0.5 szklanki)
- <span class="ing-item" data-base="0.25" data-unit="g" data-name="sól i pieprz">0.25 g soli i pieprzu</span> (1 szczypta)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Kaszę gryczaną gotujemy w osolonej wodzie i odcedzamy.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Na patelni rozgrzewamy oliwę i podsmażamy posiekaną cebulę i czosnek.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Dodajemy różyczki brokuła, tofu, kaszę, wlewamy bulion, mieszamy i przykrywamy patelnię pokrywką na 5 minut.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 4:</strong> Dodajemy szpinak i mieszamy.</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>
""",

    "smoothie-strawberry.md": """# Smoothie strawberry and friends Solevita i batonik protein bar

<div class="portion-selector">
  <label for="persons-count">Liczba osób:</label>
  <input type="number" id="persons-count" value="1" min="1" onchange="updatePortions()">
  <button class="btn-action" onclick="toggleShoppingList()">🛒 Lista zakupów</button>
</div>

<div id="shopping-list-box" class="shopping-list-box">
  <h3>Lista zakupów</h3>
  <ul id="shopping-list-items"></ul>
  <button class="btn-action" onclick="printShoppingList()">📄 Wygeneruj PDF</button>
</div>

## Składniki (na 1 osobę)

- <span class="ing-item" data-base="45" data-unit="g" data-name="Protein Bar cookies and cream flavoured crisps">45 g Protein Bar cookies and cream flavoured crisps</span> (1 sztuka)
- <span class="ing-item" data-base="250" data-unit="g" data-name="smoothie strawberry & friends Solevita">250 g smoothie strawberry & friends Solevita</span> (1 opakowanie)
- <span class="ing-item" data-base="15" data-unit="g" data-name="orzechy włoskie">15 g orzechów włoskich</span> (0.5 garści)
- <span class="ing-item" data-base="130" data-unit="g" data-name="mandarynka">130 g mandarynki</span> (2 sztuki)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Batonik, orzechy, mandarynki i smoothie jemy na posiłek.</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>
""",

    # DAY 5
    "serek-wiejski-z-miodem.md": """# Serek wiejski z miodem, orzechami i gruszką

<div class="portion-selector">
  <label for="persons-count">Liczba osób:</label>
  <input type="number" id="persons-count" value="1" min="1" onchange="updatePortions()">
  <button class="btn-action" onclick="toggleShoppingList()">🛒 Lista zakupów</button>
</div>

<div id="shopping-list-box" class="shopping-list-box">
  <h3>Lista zakupów</h3>
  <ul id="shopping-list-items"></ul>
  <button class="btn-action" onclick="printShoppingList()">📄 Wygeneruj PDF</button>
</div>

## Składniki (na 1 osobę)

- <span class="ing-item" data-base="200" data-unit="g" data-name="serek wiejski">200 g serka wiejskiego</span> (1 opakowanie)
- <span class="ing-item" data-base="6" data-unit="g" data-name="miód">6 g miodu</span> (0.5 łyżeczki)
- <span class="ing-item" data-base="20" data-unit="g" data-name="orzechy włoskie">20 g orzechów włoskich</span> (5 sztuk)
- <span class="ing-item" data-base="130" data-unit="g" data-name="gruszka">130 g gruszki</span> (1 sztuka)
- <span class="ing-item" data-base="10" data-unit="g" data-name="wafle ryżowe">10 g wafli ryżowych</span> (1 sztuka)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Gruszkę myjemy i kroimy w kostkę, orzechy siekamy.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Pokrojoną gruszkę wraz z orzechami dodajemy do serka wiejskiego, polewamy miodem i mieszamy. Zjadamy z waflami ryżowymi.</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>
""",

    "kanapka-z-pasta-z-ciecierzycy.md": """# Kanapka z pastą z ciecierzycy

<div class="portion-selector">
  <label for="persons-count">Liczba osób:</label>
  <input type="number" id="persons-count" value="1" min="1" onchange="updatePortions()">
  <button class="btn-action" onclick="toggleShoppingList()">🛒 Lista zakupów</button>
</div>

<div id="shopping-list-box" class="shopping-list-box">
  <h3>Lista zakupów</h3>
  <ul id="shopping-list-items"></ul>
  <button class="btn-action" onclick="printShoppingList()">📄 Wygeneruj PDF</button>
</div>

## Składniki (na 1 osobę)

- <span class="ing-item" data-base="80" data-unit="g" data-name="ciecierzyca konserwowa">80 g ciecierzycy konserwowej</span> (4 łyżki)
- <span class="ing-item" data-base="6" data-unit="g" data-name="czosnek">6 g czosnku</span> (1 ząbek)
- <span class="ing-item" data-base="15" data-unit="g" data-name="oliwa">15 g oliwy</span> (3 łyżeczki)
- <span class="ing-item" data-base="1" data-unit="g" data-name="kumin">1 g kuminu</span> (1 szczypta)
- <span class="ing-item" data-base="1" data-unit="g" data-name="kolendra">1 g kolendry</span> (1 łyżeczka)
- <span class="ing-item" data-base="3" data-unit="g" data-name="papryka słodka">3 g papryki słodkiej</span> (1 łyżeczka)
- <span class="ing-item" data-base="12" data-unit="g" data-name="sok z cytryny">12 g soku z cytryny</span> (2 łyżki)
- <span class="ing-item" data-base="60" data-unit="g" data-name="chleb żytni">60 g chleba żytniego</span> (2 kromki)
- <span class="ing-item" data-base="24" data-unit="g" data-name="kiełki rzodkiewki">24 g kiełków rzodkiewki</span> (3 łyżki)
- <span class="ing-item" data-base="75" data-unit="g" data-name="ogórek">75 g ogórka</span> (0.5 sztuki)
- <span class="ing-item" data-base="45" data-unit="g" data-name="marchewka">45 g marchewki</span> (1 sztuka)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Do blendera wkładamy składniki na pastę, blendujemy do momentu uzyskania jednolitej masy, doprawiamy solą i znowu mieszamy.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Kromki pieczywa smarujemy pastą i układamy kiełki, plastry ogórka i wstążki z marchewki.</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>
""",

    "spaghetti-bolognese.md": """# Wegańskie spaghetti bolognese

<div class="portion-selector">
  <label for="persons-count">Liczba osób:</label>
  <input type="number" id="persons-count" value="1" min="1" onchange="updatePortions()">
  <button class="btn-action" onclick="toggleShoppingList()">🛒 Lista zakupów</button>
</div>

<div id="shopping-list-box" class="shopping-list-box">
  <h3>Lista zakupów</h3>
  <ul id="shopping-list-items"></ul>
  <button class="btn-action" onclick="printShoppingList()">📄 Wygeneruj PDF</button>
</div>

## Składniki (na 1 osobę)

- <span class="ing-item" data-base="180" data-unit="g" data-name="tofu naturalne">180 g tofu naturalnego</span> (1 opakowanie)
- <span class="ing-item" data-base="50" data-unit="g" data-name="makaron spaghetti pełnoziarnisty">50 g makaronu spaghetti pełnoziarnistego</span> (1 porcja)
- <span class="ing-item" data-base="45" data-unit="g" data-name="marchewka">45 g marchewki</span> (1 sztuka)
- <span class="ing-item" data-base="20" data-unit="g" data-name="cebula">20 g cebuli</span> (1 sztuka)
- <span class="ing-item" data-base="6" data-unit="g" data-name="czosnek">6 g czosnku</span> (1 ząbek)
- <span class="ing-item" data-base="200" data-unit="g" data-name="pomidory w puszce">200 g pomidorów w puszce</span> (0.5 opakowania)
- <span class="ing-item" data-base="5" data-unit="g" data-name="sos sojowy">5 g sosu sojowego</span> (0.5 łyżki)
- <span class="ing-item" data-base="0.5" data-unit="g" data-name="papryka wędzona słodka">0.5 g papryki wędzonej słodkiej</span> (1 szczypta)
- <span class="ing-item" data-base="0.25" data-unit="g" data-name="sól">0.25 g soli</span> (1 szczypta)
- <span class="ing-item" data-base="0.25" data-unit="g" data-name="pieprz">0.25 g pieprzu</span> (1 szczypta)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Tofu odsączamy i rozdrabniamy, dodajemy do niego sos sojowy i paprykę wędzoną. Smażymy na rozgrzanej patelni przez 7-8 minut, następnie odstawiamy na bok.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Na tej samej patelni podsmażamy pokrojoną cebulę, czosnek oraz startą marchewkę przez około 8 minut.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Dodajemy podsmażone tofu i puszkę pomidorów oraz 100 ml wody.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 4:</strong> Dusimy przez 25 minut, następnie dodajemy listki bazylii oraz doprawiamy solą i pieprzem.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 5:</strong> Makaron gotujemy według instrukcji na opakowaniu.</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>
""",

    "salatka-grecka.md": """# Sałatka grecka z serem sałatkowym i pieczywem

<div class="portion-selector">
  <label for="persons-count">Liczba osób:</label>
  <input type="number" id="persons-count" value="1" min="1" onchange="updatePortions()">
  <button class="btn-action" onclick="toggleShoppingList()">🛒 Lista zakupów</button>
</div>

<div id="shopping-list-box" class="shopping-list-box">
  <h3>Lista zakupów</h3>
  <ul id="shopping-list-items"></ul>
  <button class="btn-action" onclick="printShoppingList()">📄 Wygeneruj PDF</button>
</div>

## Składniki (na 1 osobę)

- <span class="ing-item" data-base="50" data-unit="g" data-name="miks sałat">50 g miksu sałat</span> (2 garści)
- <span class="ing-item" data-base="100" data-unit="g" data-name="ser feta">100 g sera feta</span> (0.5 sztuki)
- <span class="ing-item" data-base="20" data-unit="g" data-name="oliwki zielone">20 g oliwek zielonych</span> (0.5 garści)
- <span class="ing-item" data-base="3" data-unit="g" data-name="suszone oregano">3 g suszonego oregano</span> (1 łyżeczka)
- <span class="ing-item" data-base="85" data-unit="g" data-name="papryka żółta">85 g papryki żółtej</span> (0.5 sztuki)
- <span class="ing-item" data-base="55" data-unit="g" data-name="cebula">55 g cebuli</span> (0.5 sztuki)
- <span class="ing-item" data-base="5" data-unit="g" data-name="oliwa z oliwek">5 g oliwy z oliwek</span> (1 łyżeczka)
- <span class="ing-item" data-base="3" data-unit="g" data-name="sok z cytryny">3 g soku z cytryny</span> (0.5 łyżki)
- <span class="ing-item" data-base="160" data-unit="g" data-name="pomidor">160 g pomidora</span> (1 sztuka)
- <span class="ing-item" data-base="150" data-unit="g" data-name="ogórek zielony">150 g ogórka zielonego</span> (1 sztuka)
- <span class="ing-item" data-base="30" data-unit="g" data-name="chleb żytni razowy">30 g chleba żytniego razowego</span> (1 kromka)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Kroimy paprykę, cebulę, pomidor, ogórek, oliwki i ser feta/sałatkowy.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Mieszamy oliwę, oregano, sól, pieprz, sok z cytryny.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Na talerz nakładamy sałatę, pokrojone warzywa, oliwki, ser sałatkowy, polewamy sosem, dokładnie mieszamy i podajemy z pieczywem. Smacznego!</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>
""",

    # DAY 6
    "bowl-sniadaniowy.md": """# Bowl śniadaniowy z jabłkiem i kaki

<div class="portion-selector">
  <label for="persons-count">Liczba osób:</label>
  <input type="number" id="persons-count" value="1" min="1" onchange="updatePortions()">
  <button class="btn-action" onclick="toggleShoppingList()">🛒 Lista zakupów</button>
</div>

<div id="shopping-list-box" class="shopping-list-box">
  <h3>Lista zakupów</h3>
  <ul id="shopping-list-items"></ul>
  <button class="btn-action" onclick="printShoppingList()">📄 Wygeneruj PDF</button>
</div>

## Składniki (na 1 osobę)

- <span class="ing-item" data-base="10" data-unit="g" data-name="płatki owsiane górskie">10 g płatków owsianych górskich</span> (1 łyżka)
- <span class="ing-item" data-base="30" data-unit="g" data-name="mieszanka orzechów">30 g mieszanki orzechów</span> (1 garść)
- <span class="ing-item" data-base="80" data-unit="g" data-name="małe jabłko">80 g małego jabłka</span> (1 sztuka)
- <span class="ing-item" data-base="125" data-unit="g" data-name="kaki">125 g kaki</span> (0.5 sztuki)
- <span class="ing-item" data-base="4" data-unit="g" data-name="cynamon">4 g cynamonu</span> (1 łyżeczka)
- <span class="ing-item" data-base="150" data-unit="g" data-name="jogurt skyr">150 g jogurtu skyr</span> (1 opakowanie)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Owoce kroimy.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Orzechy siekamy i w miseczce łączymy z płatkami owsianymi.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Dodajemy cynamon.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 4:</strong> Do połączonych składników dodajemy jogurt i pokrojone owoce. Smacznego!</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>
""",

    "tosty-awokado.md": """# Tosty z jajkiem sadzonym i awokado

<div class="portion-selector">
  <label for="persons-count">Liczba osób:</label>
  <input type="number" id="persons-count" value="1" min="1" onchange="updatePortions()">
  <button class="btn-action" onclick="toggleShoppingList()">🛒 Lista zakupów</button>
</div>

<div id="shopping-list-box" class="shopping-list-box">
  <h3>Lista zakupów</h3>
  <ul id="shopping-list-items"></ul>
  <button class="btn-action" onclick="printShoppingList()">📄 Wygeneruj PDF</button>
</div>

## Składniki (na 1 osobę)

- <span class="ing-item" data-base="60" data-unit="g" data-name="chleb tostowy pełnoziarnisty">60 g chleba tostowego pełnoziarnistego</span> (2 kromki)
- <span class="ing-item" data-base="70" data-unit="g" data-name="awokado">70 g awokado</span> (0.5 sztuki)
- <span class="ing-item" data-base="112" data-unit="g" data-name="jajko">112 g jajka</span> (2 sztuki)
- <span class="ing-item" data-base="40" data-unit="g" data-name="rukola">40 g rukoli</span> (2 garści)
- <span class="ing-item" data-base="10" data-unit="g" data-name="szczypiorek">10 g szczypiorku</span> (2 łyżeczki)
- <span class="ing-item" data-base="0.25" data-unit="g" data-name="sól">0.25 g soli</span> (1 szczypta)
- <span class="ing-item" data-base="0.25" data-unit="g" data-name="pieprz">0.25 g pieprzu</span> (1 szczypta)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Pieczywo opiekamy w tosterze lub na patelni.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Awokado obieramy ze skórki i smarujemy kromki chleba.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Na rozgrzanej patelni, pod przykryciem przygotowujemy jajka sadzone. Doprawiamy solą i pieprzem.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 4:</strong> Na posmarowanych kanapkach układamy rukolę i jajka. Posypujemy posiekanym szczypiorkiem. Smacznego!</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>
""",

    "zupa-z-dyni.md": """# Zupa z dyni z pieczoną ciecierzycą - przepis na 3 porcje

<div class="portion-selector">
  <label for="persons-count">Liczba osób:</label>
  <input type="number" id="persons-count" value="1" min="1" onchange="updatePortions()">
  <button class="btn-action" onclick="toggleShoppingList()">🛒 Lista zakupów</button>
</div>

<div id="shopping-list-box" class="shopping-list-box">
  <h3>Lista zakupów</h3>
  <ul id="shopping-list-items"></ul>
  <button class="btn-action" onclick="printShoppingList()">📄 Wygeneruj PDF</button>
</div>

## Składniki (na 1 osobę)

- <span class="ing-item" data-base="300" data-unit="g" data-name="dynia">300 g dyni</span> (3 porcje)
- <span class="ing-item" data-base="200" data-unit="g" data-name="mleczko kokosowe">200 g mleczka kokosowego</span> (0.5 opakowania)
- <span class="ing-item" data-base="480" data-unit="g" data-name="ciecierzyca konserwowa">480 g ciecierzycy konserwowej</span> (2 opakowania)
- <span class="ing-item" data-base="12" data-unit="g" data-name="sok z cytryny">12 g soku z cytryny</span> (2 łyżki)
- <span class="ing-item" data-base="45" data-unit="g" data-name="marchew">45 g marchwi</span> (1 sztuka)
- <span class="ing-item" data-base="70" data-unit="g" data-name="ziemniaki">70 g ziemniaków</span> (1 sztuka)
- <span class="ing-item" data-base="4" data-unit="g" data-name="świeża kolendra">4 g świeżej kolendry</span> (1 garść)
- <span class="ing-item" data-base="1" data-unit="g" data-name="czosnek granulowany">1 g czosnku granulowanego</span> (1 szczypta)
- <span class="ing-item" data-base="3" data-unit="g" data-name="papryka słodka">3 g papryki słodkiej</span> (1 łyżeczka)
- <span class="ing-item" data-base="0.25" data-unit="g" data-name="sól i pieprz">0.25 g soli i pieprzu</span> (1 szczypta)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Dynię, marchew, ziemniaki obieramy i kroimy na duże kawałki. Układamy na blaszce wyłożonej papierem do pieczenia. Odsączoną ciecierzycę układamy obok, wszystko przyprawiamy solą, pieprzem, czosnkiem granulowanym, słodką papryką. Pieczemy w piekarniku z termoobiegiem rozgrzanym do 230 stopni przez 25 minut.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Warzywa przekładamy do garnka (trochę ciecierzycy zostawiamy do posypania), zalewamy mlekiem kokosowym, dolewamy ok 300 ml wody, zagotowujemy.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Zupę gotujemy przez 10 minut, blendujemy na gładki krem. Podajemy z pieczoną ciecierzycą i posiekaną kolendrą. Smacznego!</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>
""",

    "owsianka-malinowa.md": """# Owsianka malinowa Crownfield

<div class="portion-selector">
  <label for="persons-count">Liczba osób:</label>
  <input type="number" id="persons-count" value="1" min="1" onchange="updatePortions()">
  <button class="btn-action" onclick="toggleShoppingList()">🛒 Lista zakupów</button>
</div>

<div id="shopping-list-box" class="shopping-list-box">
  <h3>Lista zakupów</h3>
  <ul id="shopping-list-items"></ul>
  <button class="btn-action" onclick="printShoppingList()">📄 Wygeneruj PDF</button>
</div>

## Składniki (na 1 osobę)

- <span class="ing-item" data-base="65" data-unit="g" data-name="owsianka malinowa Crownfield">65 g owsianki malinowej Crownfield</span> (1 opakowanie)
- <span class="ing-item" data-base="150" data-unit="g" data-name="jogurt skyr">150 g jogurtu skyr</span> (1 opakowanie)
- <span class="ing-item" data-base="250" data-unit="g" data-name="Smoothie strawberry Solevita">250 g Smoothie strawberry Solevita</span> (1 opakowanie)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Owsiankę przygotowujemy zgodnie z instrukcją na opakowaniu. Zjadamy z dodatkami.</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>
""",

    # DAY 7
    "owsianka-z-marchewka.md": """# Owsianka z marchewką

<div class="portion-selector">
  <label for="persons-count">Liczba osób:</label>
  <input type="number" id="persons-count" value="1" min="1" onchange="updatePortions()">
  <button class="btn-action" onclick="toggleShoppingList()">🛒 Lista zakupów</button>
</div>

<div id="shopping-list-box" class="shopping-list-box">
  <h3>Lista zakupów</h3>
  <ul id="shopping-list-items"></ul>
  <button class="btn-action" onclick="printShoppingList()">📄 Wygeneruj PDF</button>
</div>

## Składniki (na 1 osobę)

- <span class="ing-item" data-base="125" data-unit="g" data-name="napój roślinny">125 g napoju roślinnego</span> (0.5 szklanki)
- <span class="ing-item" data-base="20" data-unit="g" data-name="płatki owsiane górskie">20 g płatków owsianych górskich</span> (2 łyżki)
- <span class="ing-item" data-base="45" data-unit="g" data-name="marchewka">45 g marchewki</span> (1 sztuka)
- <span class="ing-item" data-base="0.25" data-unit="g" data-name="sól">0.25 g soli</span> (1 szczypta)
- <span class="ing-item" data-base="4" data-unit="g" data-name="cynamon">4 g cynamonu</span> (1 łyżeczka)
- <span class="ing-item" data-base="60" data-unit="g" data-name="mały banan">60 g małego banana</span> (1 sztuka)
- <span class="ing-item" data-base="30" data-unit="g" data-name="mieszanka orzechów">30 g mieszanki orzechów</span> (1 garść)
- <span class="ing-item" data-base="16" data-unit="g" data-name="wegańska odżywka białkowa">16 g wegańskiej odżywki białkowej</span> (2 łyżki)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> W rondelku podgrzewamy mleko roślinne, następnie dodajemy startą na drobnych oczkach marchewkę oraz płatki owsiane, odżywkę, sól i cynamon. Gotujemy przez 5-7 minut.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Przekładamy owsiankę do miski i na wierzch dodajemy posiekane orzechy oraz pokrojonego banana. Smacznego!</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>
""",

    "kanapka-z-tofu-twarozkiem.md": """# Kanapka z tofu twarożkiem

<div class="portion-selector">
  <label for="persons-count">Liczba osób:</label>
  <input type="number" id="persons-count" value="1" min="1" onchange="updatePortions()">
  <button class="btn-action" onclick="toggleShoppingList()">🛒 Lista zakupów</button>
</div>

<div id="shopping-list-box" class="shopping-list-box">
  <h3>Lista zakupów</h3>
  <ul id="shopping-list-items"></ul>
  <button class="btn-action" onclick="printShoppingList()">📄 Wygeneruj PDF</button>
</div>

## Składniki (na 1 osobę)

- <span class="ing-item" data-base="80" data-unit="g" data-name="bułka grahamka">80 g bułki grahamki</span> (1 sztuka)
- <span class="ing-item" data-base="25" data-unit="g" data-name="serek śmietankowy">25 g serka śmietankowego</span> (1 łyżka)
- <span class="ing-item" data-base="15" data-unit="g" data-name="majonez wegański">15 g majonezu wegańskiego</span> (1 łyżeczka)
- <span class="ing-item" data-base="90" data-unit="g" data-name="tofu naturalne">90 g tofu naturalnego</span> (0.5 opakowania)
- <span class="ing-item" data-base="100" data-unit="g" data-name="ogórki kiszone">100 g ogórków kiszonych</span> (2 sztuki)
- <span class="ing-item" data-base="160" data-unit="g" data-name="pomidor">160 g pomidora</span> (1 sztuka)
- <span class="ing-item" data-base="15" data-unit="g" data-name="szczypiorek">15 g szczypiorku</span> (3 łyżeczki)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Bułkę kroimy na pół, smarujemy serkiem śmietankowym.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Tofu przekładamy do miseczki, dodajemy majonez i rozgniatamy widelcem.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Ogórki drobno siekamy. Dodajemy do twarożku, mieszamy.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 4:</strong> Bułkę smarujemy twarożkiem, jemy z pomidorem i posiekanym szczypiorkiem.</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>
""",

    "roslinna-kaszanka.md": """# Roślinna kaszanka Dobra Kaloria z pieczywem i warzywami

<div class="portion-selector">
  <label for="persons-count">Liczba osób:</label>
  <input type="number" id="persons-count" value="1" min="1" onchange="updatePortions()">
  <button class="btn-action" onclick="toggleShoppingList()">🛒 Lista zakupów</button>
</div>

<div id="shopping-list-box" class="shopping-list-box">
  <h3>Lista zakupów</h3>
  <ul id="shopping-list-items"></ul>
  <button class="btn-action" onclick="printShoppingList()">📄 Wygeneruj PDF</button>
</div>

## Składniki (na 1 osobę)

- <span class="ing-item" data-base="90" data-unit="g" data-name="Roślinna kaszanka na grilla i na patelnię Dobra Kaloria">90 g Roślinna kaszanka na grilla i na patelnię Dobra Kaloria</span> (0.5 opakowania)
- <span class="ing-item" data-base="60" data-unit="g" data-name="bułka">60 g bułki</span> (1 sztuka)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Kaszankę podgrzewamy, jemy z pieczywem.</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>
""",

    "bruschetta.md": """# Bruschetta z pomidorami, świeżymi ziołami i serem grana padano

<div class="portion-selector">
  <label for="persons-count">Liczba osób:</label>
  <input type="number" id="persons-count" value="1" min="1" onchange="updatePortions()">
  <button class="btn-action" onclick="toggleShoppingList()">🛒 Lista zakupów</button>
</div>

<div id="shopping-list-box" class="shopping-list-box">
  <h3>Lista zakupów</h3>
  <ul id="shopping-list-items"></ul>
  <button class="btn-action" onclick="printShoppingList()">📄 Wygeneruj PDF</button>
</div>

## Składniki (na 1 osobę)

- <span class="ing-item" data-base="70" data-unit="g" data-name="bagietka">70 g bagietki</span> (0.5 sztuki)
- <span class="ing-item" data-base="100" data-unit="g" data-name="pomidor">100 g pomidora</span> (1 sztuka)
- <span class="ing-item" data-base="20" data-unit="g" data-name="mała cebula czerwona">20 g małej cebuli czerwonej</span> (1 sztuka)
- <span class="ing-item" data-base="6" data-unit="g" data-name="czosnek">6 g czosnku</span> (1 ząbek)
- <span class="ing-item" data-base="3" data-unit="g" data-name="bazylia świeża">3 g bazylii świeżej</span> (1 garść)
- <span class="ing-item" data-base="50" data-unit="g" data-name="ser grana padano">50 g sera grana padano</span> (2 porcje)
- <span class="ing-item" data-base="3" data-unit="g" data-name="ocet balsamiczny">3 g octu balsamicznego</span> (0.5 łyżki)
- <span class="ing-item" data-base="5" data-unit="g" data-name="oliwa z oliwek">5 g oliwy z oliwek</span> (1 łyżeczka)
- <span class="ing-item" data-base="0.25" data-unit="g" data-name="sól i pieprz">0.25 g soli i pieprzu</span> (1 szczypta)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Pomidory myjemy, cebulę i czosnek obieramy. Warzywa kroimy w kostkę.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Pokrojone warzywa mieszamy ze sobą, dodajemy posiekaną bazylię. Całość doprawiamy solą, pieprzem, octem i oliwą z oliwek.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Bagietkę kroimy na kromki i pieczemy w piekarniku rozgrzanym do 180 stopni przez około 5 minut, aż będą chrupkie.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 4:</strong> Na grzanki nakładamy pomidory z cebulką i czosnkiem, posypujemy startym serem grana padano.</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>
""",

    # DAY 8
    "omlet-mleczna-kanapka.md": """# Omlet mleczna kanapka

<div class="portion-selector">
  <label for="persons-count">Liczba osób:</label>
  <input type="number" id="persons-count" value="1" min="1" onchange="updatePortions()">
  <button class="btn-action" onclick="toggleShoppingList()">🛒 Lista zakupów</button>
</div>

<div id="shopping-list-box" class="shopping-list-box">
  <h3>Lista zakupów</h3>
  <ul id="shopping-list-items"></ul>
  <button class="btn-action" onclick="printShoppingList()">📄 Wygeneruj PDF</button>
</div>

## Składniki (na 1 osobę)

- <span class="ing-item" data-base="56" data-unit="g" data-name="jajko">56 g jajko</span> (1 sztuka)
- <span class="ing-item" data-base="35" data-unit="g" data-name="mąka pszenna pełnoziarnista">35 g mąki pszennej pełnoziarnistej</span> (2.5 łyżki)
- <span class="ing-item" data-base="10" data-unit="g" data-name="kakao">10 g kakao</span> (1 łyżka)
- <span class="ing-item" data-base="60" data-unit="g" data-name="jogurt naturalny">60 g jogurtu naturalnego</span> (3 łyżki)
- <span class="ing-item" data-base="2" data-unit="g" data-name="proszek do pieczenia">2 g proszku do pieczenia</span> (0.5 łyżeczki)
- <span class="ing-item" data-base="40" data-unit="g" data-name="jogurt naturalny (do kremu)">40 g jogurtu naturalnego</span> (2 łyżki)
- <span class="ing-item" data-base="90" data-unit="g" data-name="twaróg chudy">90 g twarogu chudego</span> (3 plastry)
- <span class="ing-item" data-base="23" data-unit="g" data-name="ksylitol">23 g ksylitolu</span> (1.5 łyżki)
- <span class="ing-item" data-base="3" data-unit="g" data-name="ekstrakt waniliowy">3 g ekstraktu waniliowego</span> (1 łyżeczka)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Składniki omletu mieszamy lub blendujemy ze sobą, smażymy na patelni pod przykryciem przez 3-5 minut na średnim ogniu.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Składniki kremu blendujemy na gładką masę.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Omlet ściągamy z patelni. Odstawiamy, żeby nieco ostygł. Smarujemy kremem i składamy na pół. Smacznego!</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>
""",

    "hummus-spicy-salsa.md": """# Hummus spicy salsa z waflami ryżowymi

<div class="portion-selector">
  <label for="persons-count">Liczba osób:</label>
  <input type="number" id="persons-count" value="1" min="1" onchange="updatePortions()">
  <button class="btn-action" onclick="toggleShoppingList()">🛒 Lista zakupów</button>
</div>

<div id="shopping-list-box" class="shopping-list-box">
  <h3>Lista zakupów</h3>
  <ul id="shopping-list-items"></ul>
  <button class="btn-action" onclick="printShoppingList()">📄 Wygeneruj PDF</button>
</div>

## Składniki (na 1 osobę)

- <span class="ing-item" data-base="80" data-unit="g" data-name="hummus spicy salsa">80 g hummusu spicy salsa</span> (0.5 opakowania)
- <span class="ing-item" data-base="30" data-unit="g" data-name="wafle ryżowe">30 g wafli ryżowych</span> (3 sztuki)
- <span class="ing-item" data-base="100" data-unit="g" data-name="pomidorki koktajlowe">100 g pomidorków koktajlowych</span> (5 sztuk)
- <span class="ing-item" data-base="250" data-unit="g" data-name="Fruvity pure (banan, truskawka, jabłko)">250 g Fruvity pure (banan, truskawka, jabłko)</span> (1 opakowanie)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Wafle ryżowe zjadamy z hummusem i pomidorkami koktajlowymi. Na deser zjadamy jogurt.</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>
""",

    "zapiekanka-ziemniaczana.md": """# Zapiekanka ziemniaczana z mozzarellą

<div class="portion-selector">
  <label for="persons-count">Liczba osób:</label>
  <input type="number" id="persons-count" value="1" min="1" onchange="updatePortions()">
  <button class="btn-action" onclick="toggleShoppingList()">🛒 Lista zakupów</button>
</div>

<div id="shopping-list-box" class="shopping-list-box">
  <h3>Lista zakupów</h3>
  <ul id="shopping-list-items"></ul>
  <button class="btn-action" onclick="printShoppingList()">📄 Wygeneruj PDF</button>
</div>

## Składniki (na 1 osobę)

- <span class="ing-item" data-base="140" data-unit="g" data-name="ziemniaki">140 g ziemniaków</span> (2 sztuki)
- <span class="ing-item" data-base="100" data-unit="g" data-name="szpinak">100 g szpinaku</span> (4 garści)
- <span class="ing-item" data-base="125" data-unit="g" data-name="passata pomidorowa">125 g passaty pomidorowej</span> (0.5 szklanki)
- <span class="ing-item" data-base="18" data-unit="g" data-name="czosnek">18 g czosnku</span> (3 ząbki)
- <span class="ing-item" data-base="5" data-unit="g" data-name="oliwa z oliwek">5 g oliwy z oliwek</span> (1 łyżeczka)
- <span class="ing-item" data-base="3" data-unit="g" data-name="świeża bazylia">3 g świeżej bazylii</span> (1 garść)
- <span class="ing-item" data-base="0.5" data-unit="g" data-name="gałka muszkatołowa">0.5 g gałki muszkatołowej</span> (2 szczypty)
- <span class="ing-item" data-base="0.25" data-unit="g" data-name="sól i pieprz">0.25 g soli i pieprzu</span> (1 szczypta)
- <span class="ing-item" data-base="45" data-unit="g" data-name="ser mozzarella">45 g sera mozzarella</span> (3 plastry)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Piekarnik nagrzewamy do 190 stopni.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Ziemniaki obieramy i kroimy w cienkie plasterki, czosnek siekamy.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Na patelni rozgrzewamy oliwę. Podsmażamy czosnek i dodajemy do niego umyty szpinak i gałkę muszkatołową. Przyprawiamy solą i pieprzem.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 4:</strong> Mozzarellę odsączamy i kroimy na plasterki.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 5:</strong> Do naczynia żaroodpornego wlewamy 1/3 passaty z pomidorów, układamy na niej kilka liści bazylii, posypujemy solą, układamy plastry ziemniaków, sera mozzarella i szpinak. Układamy kolejne warstwy, aż do wyczerpania wszystkich składników. Ostatnią warstwę wykańczamy serem mozzarella.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 6:</strong> Naczynie przykrywamy folią do pieczenia. Pieczemy przez 30 minut, po czym zdejmujemy folię i zapiekamy bez przykrycia, przez 10 minut na trybie termoobieg. Smacznego!</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>
""",

    "ryzowy-pudding.md": """# Ryżowy pudding z prażonymi gruszkami

<div class="portion-selector">
  <label for="persons-count">Liczba osób:</label>
  <input type="number" id="persons-count" value="1" min="1" onchange="updatePortions()">
  <button class="btn-action" onclick="toggleShoppingList()">🛒 Lista zakupów</button>
</div>

<div id="shopping-list-box" class="shopping-list-box">
  <h3>Lista zakupów</h3>
  <ul id="shopping-list-items"></ul>
  <button class="btn-action" onclick="printShoppingList()">📄 Wygeneruj PDF</button>
</div>

## Składniki (na 1 osobę)

- <span class="ing-item" data-base="30" data-unit="g" data-name="ryż basmati">30 g ryżu basmati</span> (2 łyżki)
- <span class="ing-item" data-base="75" data-unit="g" data-name="jogurt skyr">75 g jogurtu skyr</span> (0.5 opakowania)
- <span class="ing-item" data-base="130" data-unit="g" data-name="gruszka">130 g gruszki</span> (1 sztuka)
- <span class="ing-item" data-base="8" data-unit="g" data-name="cynamon">8 g cynamonu</span> (2 łyżeczki)
- <span class="ing-item" data-base="20" data-unit="g" data-name="erytrol">20 g erytrolu</span> (4 łyżeczki)
- <span class="ing-item" data-base="5" data-unit="g" data-name="olej rzepakowy">5 g oleju rzepakowego</span> (1 łyżeczka)
- <span class="ing-item" data-base="0.25" data-unit="g" data-name="sól">0.25 g soli</span> (1 szczypta)
- <span class="ing-item" data-base="30" data-unit="g" data-name="masło orzechowe">30 g masła orzechowego</span> (3 łyżeczki)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Ryż gotujemy według instrukcji na opakowaniu i odsączamy.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Gruszkę obieramy i kroimy w kostkę. Podsmażamy na oleju ze wskazaną połową porcji erytrolu przez 10 minut na patelni.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Jogurt skyr łączymy z masłem orzechowym, erytrolem i cynamonem w miseczce.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 4:</strong> Ugotowany ryż łączymy z jogurtem i prażoną gruszką.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 5:</strong> Całość przekładamy do miseczek. Smacznego!</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>
""",

    # DAY 9
    "jaglany-snickers.md": """# Jaglany snickers

<div class="portion-selector">
  <label for="persons-count">Liczba osób:</label>
  <input type="number" id="persons-count" value="1" min="1" onchange="updatePortions()">
  <button class="btn-action" onclick="toggleShoppingList()">🛒 Lista zakupów</button>
</div>

<div id="shopping-list-box" class="shopping-list-box">
  <h3>Lista zakupów</h3>
  <ul id="shopping-list-items"></ul>
  <button class="btn-action" onclick="printShoppingList()">📄 Wygeneruj PDF</button>
</div>

## Składniki (na 1 osobę)

- <span class="ing-item" data-base="10" data-unit="g" data-name="gorzka czekolada">10 g gorzkiej czekolady</span> (1 porcja)
- <span class="ing-item" data-base="30" data-unit="g" data-name="kasza jaglana">30 g kaszy jaglanej</span> (2 łyżki)
- <span class="ing-item" data-base="80" data-unit="g" data-name="jogurt roślinny">80 g jogurtu roślinnego</span> (0.5 opakowania)
- <span class="ing-item" data-base="105" data-unit="g" data-name="napój sojowy">105 g napoju sojowego</span> (9 łyżek)
- <span class="ing-item" data-base="10" data-unit="g" data-name="masło orzechowe">10 g masła orzechowego</span> (1 łyżeczka)
- <span class="ing-item" data-base="10" data-unit="g" data-name="świeże daktyle">10 g świeżych daktyli</span> (2 sztuki)
- <span class="ing-item" data-base="8" data-unit="g" data-name="orzechy włoskie">8 g orzechów włoskich</span> (2 sztuki posiekane)
- <span class="ing-item" data-base="7" data-unit="g" data-name="syrop z agawy">7 g syropu z agawy</span> (0.5 łyżki)
- <span class="ing-item" data-base="16" data-unit="g" data-name="wegańska odżywka białkowa">16 g wegańskiej odżywki białkowej</span> (2 łyżki)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Kaszę gotujemy w osolonej wodzie według instrukcji na opakowaniu.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Daktyle jeśli mamy suszone, zalewamy gorącą wodą na 10 minut. W przypadku daktyli świeżych pomijamy ten krok.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Do blendera przekładamy czekoladę, daktyle, masło orzechowe, napój roślinny, jogurt, odżywkę wegańską oraz ugotowaną kaszę.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 4:</strong> Całość blendujemy, przekładamy do szklanek oblanych syropem z agawy i posypanych posiekanymi orzechami. Jeśli jest za gęste, dolewamy wody. Na wierzchu układamy pozostałą posiekaną czekoladę. Smacznego!</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>
""",

    "pasta-z-pstroga.md": """# Pasta z wędzonego pstrąga i twarogu ze szczypiorkiem, warzywami i pieczywem

<div class="portion-selector">
  <label for="persons-count">Liczba osób:</label>
  <input type="number" id="persons-count" value="1" min="1" onchange="updatePortions()">
  <button class="btn-action" onclick="toggleShoppingList()">🛒 Lista zakupów</button>
</div>

<div id="shopping-list-box" class="shopping-list-box">
  <h3>Lista zakupów</h3>
  <ul id="shopping-list-items"></ul>
  <button class="btn-action" onclick="printShoppingList()">📄 Wygeneruj PDF</button>
</div>

## Składniki (na 1 osobę)

- <span class="ing-item" data-base="60" data-unit="g" data-name="chleb żytni razowy">60 g chleba żytniego razowego</span> (2 kromki)
- <span class="ing-item" data-base="60" data-unit="g" data-name="twaróg tłusty">60 g twarogu tłustego</span> (2 opakowania)
- <span class="ing-item" data-base="60" data-unit="g" data-name="pstrąg wędzony">60 g pstrąga wędzonego</span> (2 porcje)
- <span class="ing-item" data-base="75" data-unit="g" data-name="ogórek zielony">75 g ogórka zielonego</span> (0.5 sztuki)
- <span class="ing-item" data-base="90" data-unit="g" data-name="rzodkiewki">90 g rzodkiewek</span> (6 sztuk)
- <span class="ing-item" data-base="20" data-unit="g" data-name="rukola">20 g rukoli</span> (1 garść)
- <span class="ing-item" data-base="12" data-unit="g" data-name="koperek">12 g koperku</span> (3 łyżeczki)
- <span class="ing-item" data-base="10" data-unit="g" data-name="szczypiorek">10 g szczypiorku</span> (2 łyżeczki)
- <span class="ing-item" data-base="0.25" data-unit="g" data-name="sól i pieprz">0.25 g soli i pieprzu</span> (1 szczypta)
- <span class="ing-item" data-base="10" data-unit="g" data-name="masło">10 g masła</span> (2 łyżeczki)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Pstrąga obieramy z ości i dzielimy na mniejsze kawałki.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Siekamy szczypiorek i przekładamy do miski.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Dodajemy twaróg, dokładnie mieszamy. Doprawiamy solą i pieprzem.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 4:</strong> Gotową pastę podajemy z pokrojonymi warzywami: rzodkiewką, ogórkiem, rukolą i pieczywem posmarowanym masłem. Smacznego!</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>
""",

    "zupa-krem-z-pomidorow.md": """# Zupa krem z pomidorów z bazylią Chef select

<div class="portion-selector">
  <label for="persons-count">Liczba osób:</label>
  <input type="number" id="persons-count" value="1" min="1" onchange="updatePortions()">
  <button class="btn-action" onclick="toggleShoppingList()">🛒 Lista zakupów</button>
</div>

<div id="shopping-list-box" class="shopping-list-box">
  <h3>Lista zakupów</h3>
  <ul id="shopping-list-items"></ul>
  <button class="btn-action" onclick="printShoppingList()">📄 Wygeneruj PDF</button>
</div>

## Składniki (na 1 osobę)

- <span class="ing-item" data-base="450" data-unit="g" data-name="Zupa krem z pomidorów z bazylią Chef select">450 g Zupy krem z pomidorów z bazylią Chef select</span> (1 opakowanie)
- <span class="ing-item" data-base="50" data-unit="g" data-name="baton Raw Alesto kakao, ziarna kakaowca">50 g batona Raw Alesto kakao, ziarna kakaowca</span> (1 sztuka)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Podgrzewamy zupę wg instrukcji na opakowaniu. Na deser zjadamy batona.</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>
""",

    "ryzowa-salatka-z-ananasem.md": """# Ryżowa sałatka z ananasem, ogórkiem, selerem i kukurydzą + shake białkowy

<div class="portion-selector">
  <label for="persons-count">Liczba osób:</label>
  <input type="number" id="persons-count" value="1" min="1" onchange="updatePortions()">
  <button class="btn-action" onclick="toggleShoppingList()">🛒 Lista zakupów</button>
</div>

<div id="shopping-list-box" class="shopping-list-box">
  <h3>Lista zakupów</h3>
  <ul id="shopping-list-items"></ul>
  <button class="btn-action" onclick="printShoppingList()">📄 Wygeneruj PDF</button>
</div>

## Składniki (na 1 osobę)

- <span class="ing-item" data-base="30" data-unit="g" data-name="ryż basmati">30 g ryżu basmati</span> (2 łyżki)
- <span class="ing-item" data-base="60" data-unit="g" data-name="kukurydza konserwowa">60 g kukurydzy konserwowej</span> (3 łyżki)
- <span class="ing-item" data-base="80" data-unit="g" data-name="ananas świeży">80 g ananasa świeżego</span> (1 plaster)
- <span class="ing-item" data-base="70" data-unit="g" data-name="mały ogórek">70 g małego ogórka</span> (1 sztuka)
- <span class="ing-item" data-base="45" data-unit="g" data-name="seler naciowy">45 g selera naciowego</span> (1 sztuka)
- <span class="ing-item" data-base="2" data-unit="g" data-name="świeża kolendra">2 g świeżej kolendry</span> (0.5 garści)
- <span class="ing-item" data-base="25" data-unit="g" data-name="majonez wegański">25 g majonezu wegańskiego</span> (1 łyżka)
- <span class="ing-item" data-base="6" data-unit="g" data-name="sok z cytryny">6 g soku z cytryny</span> (1 łyżka)
- <span class="ing-item" data-base="0.25" data-unit="g" data-name="sól i pieprz">0.25 g soli i pieprzu</span> (1 szczypta)
- <span class="ing-item" data-base="24" data-unit="g" data-name="wegańska odżywka białkowa">24 g wegańskiej odżywki białkowej</span> (3 łyżki)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Ryż gotujemy według instrukcji na opakowaniu.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Do ugotowanego, ostudzonego ryżu dodajemy odcedzoną kukurydzę, posiekaną kolendrę i sok z cytryny.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Ananasa, ogórka, seler naciowy kroimy w drobną kostkę i dodajemy do ryżu.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 4:</strong> Doprawiamy solą, pieprzem, dodajemy majonez wegański. Dokładnie mieszamy. Odżywkę mieszamy z wodą i wypijamy shake białkowy. Smacznego!</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>
""",

    # DAY 10
    "tost-z-maslem-orzechowym.md": """# Tost z chlebem żytnim, masłem orzechowym i bananem + shake białkowy

<div class="portion-selector">
  <label for="persons-count">Liczba osób:</label>
  <input type="number" id="persons-count" value="1" min="1" onchange="updatePortions()">
  <button class="btn-action" onclick="toggleShoppingList()">🛒 Lista zakupów</button>
</div>

<div id="shopping-list-box" class="shopping-list-box">
  <h3>Lista zakupów</h3>
  <ul id="shopping-list-items"></ul>
  <button class="btn-action" onclick="printShoppingList()">📄 Wygeneruj PDF</button>
</div>

## Składniki (na 1 osobę)

- <span class="ing-item" data-base="60" data-unit="g" data-name="chleb żytni">60 g chleba żytniego</span> (2 kromki)
- <span class="ing-item" data-base="40" data-unit="g" data-name="masło orzechowe">40 g masła orzechowego</span> (4 łyżeczki)
- <span class="ing-item" data-base="60" data-unit="g" data-name="banan">60 g banana</span> (0.5 sztuki)
- <span class="ing-item" data-base="16" data-unit="g" data-name="odżywka białkowa">16 g odżywki białkowej</span> (2 łyżki)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Pokrojone kromki chleba żytniego przypiekamy na patelni.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Pieczywo smarujemy masłem orzechowym i na wierzch układamy pokrojonego banana.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Z odżywki i wody przygotowujemy shake, pijemy do posiłku.</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>
""",

    "roslinne-kabanosy.md": """# Roślinne kabanosy Bez kęsa mięsa Tarczyński z pieczywem i warzywami

<div class="portion-selector">
  <label for="persons-count">Liczba osób:</label>
  <input type="number" id="persons-count" value="1" min="1" onchange="updatePortions()">
  <button class="btn-action" onclick="toggleShoppingList()">🛒 Lista zakupów</button>
</div>

<div id="shopping-list-box" class="shopping-list-box">
  <h3>Lista zakupów</h3>
  <ul id="shopping-list-items"></ul>
  <button class="btn-action" onclick="printShoppingList()">📄 Wygeneruj PDF</button>
</div>

## Składniki (na 1 osobę)

- <span class="ing-item" data-base="90" data-unit="g" data-name="Roślinne kabanosy Bez kęsa mięsa Tarczyński">90 g Roślinne kabanosy Bez kęsa mięsa Tarczyński</span> (1 opakowanie)
- <span class="ing-item" data-base="160" data-unit="g" data-name="pomidor">160 g pomidora</span> (1 sztuka)
- <span class="ing-item" data-base="100" data-unit="g" data-name="Przekąska na 2 śniadanie kasza jaglana-jabłko-cynamon Tymbark">100 g Przekąski na 2 śniadanie kasza jaglana-jabłko-cynamon Tymbark</span> (1 opakowanie)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Kabanosy jemy z warzywami. Po posiłku zjadamy przekąskę.</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>
""",

    "makaron-penne.md": """# Makaron penne ze szpinakiem, pieczarkami, pomidorkami cherry i serem grana padano

<div class="portion-selector">
  <label for="persons-count">Liczba osób:</label>
  <input type="number" id="persons-count" value="1" min="1" onchange="updatePortions()">
  <button class="btn-action" onclick="toggleShoppingList()">🛒 Lista zakupów</button>
</div>

<div id="shopping-list-box" class="shopping-list-box">
  <h3>Lista zakupów</h3>
  <ul id="shopping-list-items"></ul>
  <button class="btn-action" onclick="printShoppingList()">📄 Wygeneruj PDF</button>
</div>

## Składniki (na 1 osobę)

- <span class="ing-item" data-base="60" data-unit="g" data-name="makaron penne">60 g makaronu penne</span> (12 łyżek)
- <span class="ing-item" data-base="75" data-unit="g" data-name="szpinak">75 g szpinaku</span> (3 garści)
- <span class="ing-item" data-base="108" data-unit="g" data-name="śmietanka 12%">108 g śmietanki 12%</span> (6 łyżek)
- <span class="ing-item" data-base="6" data-unit="g" data-name="czosnek">6 g czosnku</span> (1 ząbek)
- <span class="ing-item" data-base="55" data-unit="g" data-name="cebula">55 g cebuli</span> (0.5 sztuki)
- <span class="ing-item" data-base="200" data-unit="g" data-name="pieczarki">200 g pieczarek</span> (10 sztuk)
- <span class="ing-item" data-base="10" data-unit="g" data-name="ser grana padano">10 g sera grana padano</span> (1 łyżka)
- <span class="ing-item" data-base="225" data-unit="g" data-name="brokuł">225 g brokuła</span> (0.5 sztuki)
- <span class="ing-item" data-base="200" data-unit="g" data-name="pomidorki">200 g pomidorków</span> (10 sztuk)
- <span class="ing-item" data-base="15" data-unit="g" data-name="ksylitol">15 g ksylitolu</span> (1 łyżka)
- <span class="ing-item" data-base="0.25" data-unit="g" data-name="sól">0.25 g soli</span> (1 szczypta)
- <span class="ing-item" data-base="0.25" data-unit="g" data-name="pieprz">0.25 g pieprzu</span> (1 szczypta)
- <span class="ing-item" data-base="10" data-unit="g" data-name="oliwa z oliwek">10 g oliwy z oliwek</span> (2 łyżeczki)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Brokuł kroimy na mniejsze różyczki.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> W rondlu gotujemy wodę i doprawiamy ją solą, pieprzem i ksylitolem. Brokuł gotujemy, aż będzie miękki, około 5-7 minut.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Czosnek i cebulę siekamy, pieczarki kroimy. W rondelku z odrobiną oliwy dusimy czosnek z cebulką.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 4:</strong> Gdy cebulka z czosnkiem się zeszklą, dodajemy pieczarki i wszystko razem dusimy.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 5:</strong> Do uduszonych warzyw wlewamy śmietankę i gotujemy, aż lekko zgęstnieje.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 6:</strong> Gdy sos się gotuje, gotujemy makaron według instrukcji umieszczonej na opakowaniu.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 7:</strong> Do ugotowanego sosu dodajemy ugotowany brokuł, świeży szpinak, pokrojone pomidorki cherry, całość mieszamy i doprawiamy solą z pieprzem.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 8:</strong> Gotowy sos mieszamy z makaronem i posypujemy serem grana padano. Smacznego!</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>
""",

    "kanapka-z-pasta-pomidorowa.md": """# Kanapka z pastą pomidorową

<div class="portion-selector">
  <label for="persons-count">Liczba osób:</label>
  <input type="number" id="persons-count" value="1" min="1" onchange="updatePortions()">
  <button class="btn-action" onclick="toggleShoppingList()">🛒 Lista zakupów</button>
</div>

<div id="shopping-list-box" class="shopping-list-box">
  <h3>Lista zakupów</h3>
  <ul id="shopping-list-items"></ul>
  <button class="btn-action" onclick="printShoppingList()">📄 Wygeneruj PDF</button>
</div>

## Składniki (na 1 osobę)

- <span class="ing-item" data-base="40" data-unit="g" data-name="soczewica czerwona">40 g soczewicy czerwonej</span> (4 łyżki)
- <span class="ing-item" data-base="60" data-unit="g" data-name="chleb żytni razowy">60 g chleba żytniego razowego</span> (2 kromki)
- <span class="ing-item" data-base="18" data-unit="g" data-name="pasta tahini">18 g pasty tahini</span> (3 łyżeczki)
- <span class="ing-item" data-base="20" data-unit="g" data-name="pomidory suszone">20 g pomidorów suszonych</span> (1 sztuka)
- <span class="ing-item" data-base="6" data-unit="g" data-name="czosnek">6 g czosnku</span> (1 ząbek)
- <span class="ing-item" data-base="3" data-unit="g" data-name="tymianek">3 g tymianku</span> (1 łyżeczka)
- <span class="ing-item" data-base="1" data-unit="g" data-name="kumin">1 g kuminu</span> (1 szczypta)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Soczewicę gotujemy zgodnie z instrukcją na opakowaniu.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Po ugotowaniu soczewicę studzimy.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Przekładamy do blendera wszystkie składniki pasty i blendujemy na gładką masę.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 4:</strong> Podajemy z pieczywem.</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>
"""
}

# Utworzenie katalogu docelowego i zapisanie wszystkich plików
output_dir = os.path.join("docs", "przepisy")
os.makedirs(output_dir, exist_ok=True)

for filename, content in recipes.items():
    file_path = os.path.join(output_dir, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Utworzono: {file_path}")

print(f"\nPomyślnie wygenerowano {len(recipes)} plików z przepisami w katalogu '{output_dir}'.")