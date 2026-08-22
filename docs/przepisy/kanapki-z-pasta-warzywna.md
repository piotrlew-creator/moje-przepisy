# Kanapki z pastą warzywną, serem mozzarellą i ogórkiem

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