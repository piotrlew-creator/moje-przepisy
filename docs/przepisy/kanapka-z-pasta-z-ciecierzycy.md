# Kanapka z pastą z ciecierzycy

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

- <span class="ing-item" data-base="80" data-unit="g" data-name="ciecierzyca konserwowa">80 g ciecierzycy konserwowej</span> (4 łyżki)
- <span class="ing-item" data-base="6" data-unit="g" data-name="czosnek">6 g czosnku</span> (1 ząbek)
- <span class="ing-item" data-base="15" data-unit="g" data-name="oliwa">15 g oliwy</span> (3 łyżeczki)
- <span class="ing-item" data-base="1" data-unit="g" data-name="kumin">1 g kuminu</span> (1 szczypta)
- <span class="ing-item" data-base="1" data-unit="g" data-name="kolendra">1 g kolendry</span> (1 łyżeczka)
- <span class="ing-item" data-base="3" data-unit="g" data-name="papryka słodka">3 g papryki słodkiej</span> (1 łyżeczka)
- <span class="ing-item" data-base="12" data-unit="g" data-name="sok z cytryny">12 g soku z cytryny</span> (2 łyżki)
- <span class="ing-item" data-base="60" data-unit="g" data-name="chleb żytni">60 g chleba żytniego</span> (2 kromki)
- <span class="ing-item" data-base="24" data-unit="g" data-name="kiełki rzodkiewki">24 g kiełków rzodkiewki</span> (3 łyżki)
- <span class="ing-item" data-base="75" data-unit="g" data-name="ogórek">75 g ogórka</span> (0.5 sztuki)
- <span class="ing-item" data-base="45" data-unit="g" data-name="marchewka">45 g marchewki</span> (1 sztuka)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Do blendera wkładamy składniki na pastę, blendujemy do momentu uzyskania jednolitej masy, doprawiamy solą i znowu mieszamy.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Kromki pieczywa smarujemy pastą i układamy kiełki, plastry ogórka i wstążki z marchewki.</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>