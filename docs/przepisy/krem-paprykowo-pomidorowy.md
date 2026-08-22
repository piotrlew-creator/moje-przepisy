# Krem paprykowo-pomidorowy

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

- <span class="ing-item" data-base="200" data-unit="g" data-name="pomidory w puszce">200 g pomidorów w puszce</span> (0.5 opakowania)
- <span class="ing-item" data-base="0.5" data-unit="g" data-name="papryka wędzona">0.5 g papryki wędzonej</span> (1 szczypta)
- <span class="ing-item" data-base="3" data-unit="g" data-name="świeża bazylia">3 g świeżej bazylii</span> (1 garść)
- <span class="ing-item" data-base="0.25" data-unit="g" data-name="sól i pieprz">0.25 g soli i pieprzu</span> (1 szczypta)
- <span class="ing-item" data-base="35" data-unit="g" data-name="makaron razowy">35 g makaronu razowego</span> (7 łyżek)
- <span class="ing-item" data-base="5" data-unit="g" data-name="oliwa z oliwek">5 g oliwy z oliwek</span> (1 łyżeczka)
- <span class="ing-item" data-base="45" data-unit="g" data-name="mozzarella">45 g mozzarelli</span> (3 plastry)
- <span class="ing-item" data-base="45" data-unit="g" data-name="seler naciowy">45 g selera naciowego</span> (1 sztuka)
- <span class="ing-item" data-base="30" data-unit="g" data-name="mała cebula">30 g małej cebuli</span> (1 sztuka)
- <span class="ing-item" data-base="6" data-unit="g" data-name="czosnek">6 g czosnku</span> (1 ząbek)
- <span class="ing-item" data-base="45" data-unit="g" data-name="marchewka">45 g marchewki</span> (1 sztuka)
- <span class="ing-item" data-base="250" data-unit="g" data-name="woda">250 g wody</span> (1 szklanka)
- <span class="ing-item" data-base="85" data-unit="g" data-name="papryka czerwona">85 g papryki czerwonej</span> (0.5 sztuki)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Paprykę, seler, cebulę i marchewkę kroimy w kostkę, czosnek siekamy.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Na rozgrzanej oliwie w rondelku podsmażamy warzywa, dodajemy paprykę wędzoną. Po 7 minutach dodajemy pomidory, wodę i bazylię. Gotujemy przez 10 minut.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Całość blendujemy i doprawiamy solą i pieprzem. Gotujemy jeszcze przez 5 minut.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 4:</strong> Makaron gotujemy według instrukcji na opakowaniu.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 5:</strong> Mozzarellę kroimy w drobną kostkę.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 6:</strong> Zupę podajemy z makaronem i mozzarellą.</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>