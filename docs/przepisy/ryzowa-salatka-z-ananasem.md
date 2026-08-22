# Ryżowa sałatka z ananasem, ogórkiem, selerem i kukurydzą + shake białkowy

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

- <span class="ing-item" data-base="30" data-unit="g" data-name="ryż basmati">30 g ryżu basmati</span> (2 łyżki)
- <span class="ing-item" data-base="60" data-unit="g" data-name="kukurydza konserwowa">60 g kukurydzy konserwowej</span> (3 łyżki)
- <span class="ing-item" data-base="80" data-unit="g" data-name="ananas świeży">80 g ananasa świeżego</span> (1 plaster)
- <span class="ing-item" data-base="70" data-unit="g" data-name="mały ogórek">70 g małego ogórka</span> (1 sztuka)
- <span class="ing-item" data-base="45" data-unit="g" data-name="seler naciowy">45 g selera naciowego</span> (1 sztuka)
- <span class="ing-item" data-base="2" data-unit="g" data-name="świeża kolendra">2 g świeżej kolendry</span> (0.5 garści)
- <span class="ing-item" data-base="25" data-unit="g" data-name="majonez wegański">25 g majonezu wegańskiego</span> (1 łyżka)
- <span class="ing-item" data-base="6" data-unit="g" data-name="sok z cytryny">6 g soku z cytryny</span> (1 łyżka)
- <span class="ing-item" data-base="0.25" data-unit="g" data-name="sól i pieprz">0.25 g soli i pieprzu</span> (1 szczypta)
- <span class="ing-item" data-base="24" data-unit="g" data-name="wegańska odżywka białkowa">24 g wegańskiej odżywki białkowej</span> (3 łyżki)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Ryż gotujemy według instrukcji na opakowaniu.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Do ugotowanego, ostudzonego ryżu dodajemy odcedzoną kukurydzę, posiekaną kolendrę i sok z cytryny.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Ananasa, ogórka, seler naciowy kroimy w drobną kostkę i dodajemy do ryżu.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 4:</strong> Doprawiamy solą, pieprzem, dodajemy majonez wegański. Dokładnie mieszamy. Odżywkę mieszamy z wodą i wypijamy shake białkowy. Smacznego!</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>