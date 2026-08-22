# Kasza z tofu

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

- <span class="ing-item" data-base="45" data-unit="g" data-name="kasza gryczana">45 g kaszy gryczanej</span> (3 łyżki)
- <span class="ing-item" data-base="90" data-unit="g" data-name="tofu naturalne">90 g tofu naturalnego</span> (0.5 opakowania)
- <span class="ing-item" data-base="225" data-unit="g" data-name="brokuł">225 g brokuła</span> (0.5 sztuki)
- <span class="ing-item" data-base="20" data-unit="g" data-name="cebula">20 g cebuli</span> (1 sztuka)
- <span class="ing-item" data-base="50" data-unit="g" data-name="szpinak">50 g szpinaku</span> (2 garści)
- <span class="ing-item" data-base="6" data-unit="g" data-name="czosnek">6 g czosnku</span> (1 ząbek)
- <span class="ing-item" data-base="5" data-unit="g" data-name="oliwa z oliwek">5 g oliwy z oliwek</span> (1 łyżeczka)
- <span class="ing-item" data-base="125" data-unit="g" data-name="bulion warzywny">125 g bulionu warzywnego</span> (0.5 szklanki)
- <span class="ing-item" data-base="0.25" data-unit="g" data-name="sól i pieprz">0.25 g soli i pieprzu</span> (1 szczypta)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Kaszę gryczaną gotujemy w osolonej wodzie i odcedzamy.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Na patelni rozgrzewamy oliwę i podsmażamy posiekaną cebulę i czosnek.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Dodajemy różyczki brokuła, tofu, kaszę, wlewamy bulion, mieszamy i przykrywamy patelnię pokrywką na 5 minut.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 4:</strong> Dodajemy szpinak i mieszamy.</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>