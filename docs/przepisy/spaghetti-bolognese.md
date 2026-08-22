# Wegańskie spaghetti bolognese

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

- <span class="ing-item" data-base="180" data-unit="g" data-name="tofu naturalne">180 g tofu naturalnego</span> (1 opakowanie)
- <span class="ing-item" data-base="50" data-unit="g" data-name="makaron spaghetti pełnoziarnisty">50 g makaronu spaghetti pełnoziarnistego</span> (1 porcja)
- <span class="ing-item" data-base="45" data-unit="g" data-name="marchewka">45 g marchewki</span> (1 sztuka)
- <span class="ing-item" data-base="20" data-unit="g" data-name="cebula">20 g cebuli</span> (1 sztuka)
- <span class="ing-item" data-base="6" data-unit="g" data-name="czosnek">6 g czosnku</span> (1 ząbek)
- <span class="ing-item" data-base="200" data-unit="g" data-name="pomidory w puszce">200 g pomidorów w puszce</span> (0.5 opakowania)
- <span class="ing-item" data-base="5" data-unit="g" data-name="sos sojowy">5 g sosu sojowego</span> (0.5 łyżki)
- <span class="ing-item" data-base="0.5" data-unit="g" data-name="papryka wędzona słodka">0.5 g papryki wędzonej słodkiej</span> (1 szczypta)
- <span class="ing-item" data-base="0.25" data-unit="g" data-name="sól">0.25 g soli</span> (1 szczypta)
- <span class="ing-item" data-base="0.25" data-unit="g" data-name="pieprz">0.25 g pieprzu</span> (1 szczypta)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Tofu odsączamy i rozdrabniamy, dodajemy do niego sos sojowy i paprykę wędzoną. Smażymy na rozgrzanej patelni przez 7-8 minut, następnie odstawiamy na bok.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Na tej samej patelni podsmażamy pokrojoną cebulę, czosnek oraz startą marchewkę przez około 8 minut.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Dodajemy podsmażone tofu i puszkę pomidorów oraz 100 ml wody.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 4:</strong> Dusimy przez 25 minut, następnie dodajemy listki bazylii oraz doprawiamy solą i pieprzem.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 5:</strong> Makaron gotujemy według instrukcji na opakowaniu.</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>