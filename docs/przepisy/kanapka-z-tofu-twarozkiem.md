# Kanapka z tofu twarożkiem

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