# Bowl śniadaniowy z jabłkiem i kaki

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

- <span class="ing-item" data-base="10" data-unit="g" data-name="płatki owsiane górskie">10 g płatków owsianych górskich</span> (1 łyżka)
- <span class="ing-item" data-base="30" data-unit="g" data-name="mieszanka orzechów">30 g mieszanki orzechów</span> (1 garść)
- <span class="ing-item" data-base="80" data-unit="g" data-name="małe jabłko">80 g małego jabłka</span> (1 sztuka)
- <span class="ing-item" data-base="125" data-unit="g" data-name="kaki">125 g kaki</span> (0.5 sztuki)
- <span class="ing-item" data-base="4" data-unit="g" data-name="cynamon">4 g cynamonu</span> (1 łyżeczka)
- <span class="ing-item" data-base="150" data-unit="g" data-name="jogurt skyr">150 g jogurtu skyr</span> (1 opakowanie)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Owoce kroimy.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Orzechy siekamy i w miseczce łączymy z płatkami owsianymi.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Dodajemy cynamon.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 4:</strong> Do połączonych składników dodajemy jogurt i pokrojone owoce. Smacznego!</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>