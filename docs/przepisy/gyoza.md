# Pierożki gyoza z warzywami chef select z kimchi

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