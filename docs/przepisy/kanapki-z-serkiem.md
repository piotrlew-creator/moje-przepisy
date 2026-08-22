# Kanapki z serkiem śmietankowym, pomidorem i szczypiorkiem

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

- <span class="ing-item" data-base="90" data-unit="g" data-name="chleb żytni razowy">90 g chleba żytniego razowego</span> (3 kromki)
- <span class="ing-item" data-base="75" data-unit="g" data-name="serek kanapkowy">75 g serka kanapkowego</span> (3 łyżki)
- <span class="ing-item" data-base="160" data-unit="g" data-name="pomidor">160 g pomidora</span> (1 sztuka)
- <span class="ing-item" data-base="10" data-unit="g" data-name="szczypiorek">10 g szczypiorku</span> (2 łyżeczki)
- <span class="ing-item" data-base="10" data-unit="g" data-name="nasiona słonecznika">10 g nasion słonecznika</span> (2 łyżeczki)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Pieczywo smarujemy serkiem.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Pomidora i szczypiorek kroimy. Pomidora kroimy w plasterki, nakładamy na kanapki. Szczypiorek drobno siekamy.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Kanapki posypujemy szczypiorkiem i nasionami słonecznika.</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>