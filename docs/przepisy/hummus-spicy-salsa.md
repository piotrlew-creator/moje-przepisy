# Hummus spicy salsa z waflami ryżowymi

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