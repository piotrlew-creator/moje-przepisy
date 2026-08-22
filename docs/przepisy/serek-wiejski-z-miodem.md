# Serek wiejski z miodem, orzechami i gruszką

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

- <span class="ing-item" data-base="200" data-unit="g" data-name="serek wiejski">200 g serka wiejskiego</span> (1 opakowanie)
- <span class="ing-item" data-base="6" data-unit="g" data-name="miód">6 g miodu</span> (0.5 łyżeczki)
- <span class="ing-item" data-base="20" data-unit="g" data-name="orzechy włoskie">20 g orzechów włoskich</span> (5 sztuk)
- <span class="ing-item" data-base="130" data-unit="g" data-name="gruszka">130 g gruszki</span> (1 sztuka)
- <span class="ing-item" data-base="10" data-unit="g" data-name="wafle ryżowe">10 g wafli ryżowych</span> (1 sztuka)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Gruszkę myjemy i kroimy w kostkę, orzechy siekamy.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Pokrojoną gruszkę wraz z orzechami dodajemy do serka wiejskiego, polewamy miodem i mieszamy. Zjadamy z waflami ryżowymi.</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>