# Smoothie strawberry and friends Solevita i batonik protein bar

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