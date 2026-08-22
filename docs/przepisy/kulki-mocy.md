# Daktylowo-kakaowe kulki mocy z orzechami

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