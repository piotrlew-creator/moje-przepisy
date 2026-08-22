# Roślinne kabanosy Bez kęsa mięsa Tarczyński z pieczywem i warzywami

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