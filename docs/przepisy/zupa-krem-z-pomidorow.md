# Zupa krem z pomidorów z bazylią Chef select

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