# Klejący ryż z prażonym jabłkiem

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
    <p><strong>Krok 3:</strong> Do rondelka po jabłkach wsypujemy ryż, odżywkę i zalewamy napojem roślinnym oraz mleczkiem kokosowym. Gotujemy na wolnym ogólniu.</p>
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