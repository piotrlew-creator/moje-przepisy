# Owsianka

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

- <span class="ing-item" data-base="30" data-unit="g" data-name="płatki owsiane">30 g płatków owsianych</span> (3 łyżki)
- <span class="ing-item" data-base="100" data-unit="g" data-name="mały banan">100 g małego banana</span> (1 sztuka)
- <span class="ing-item" data-base="30" data-unit="g" data-name="orzechy nerkowca">30 g orzechów nerkowca</span> (1 garść)
- <span class="ing-item" data-base="24" data-unit="g" data-name="odżywka białkowa">24 g odżywki białkowej</span> (3 łyżki)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Płatki owsiane zalewamy wrzątkiem do linii płatków, pozostawiamy na 3 minuty.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Banana kroimy w plasterki, dodajemy odżywkę białkową i nerkowce.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Całość mieszamy i gotowe! Smacznego!</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>