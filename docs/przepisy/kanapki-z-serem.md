# Kanapki z żółtym serem, roszponką i pomidorem

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

- <span class="ing-item" data-base="60" data-unit="g" data-name="chleb żytni razowy">60 g chleba żytniego razowego</span> (2 kromki)
- <span class="ing-item" data-base="75" data-unit="g" data-name="ser gouda">75 g sera gouda</span> (5 plastrów)
- <span class="ing-item" data-base="12.5" data-unit="g" data-name="roszponka">12.5 g roszponki</span> (0.5 garści)
- <span class="ing-item" data-base="160" data-unit="g" data-name="pomidor">160 g pomidora</span> (1 sztuka)
- <span class="ing-item" data-base="10" data-unit="g" data-name="margaryna">10 g margaryny</span> (2 łyżeczki)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Pieczywo smarujemy margaryną. Kładziemy na nie plastry sera.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Warzywa myjemy. Pomidora kroimy w plastry i układamy na kanapce razem z roszponką. Smacznego!</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>