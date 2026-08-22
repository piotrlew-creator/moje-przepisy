# Koktajl bananowo-orzechowy

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