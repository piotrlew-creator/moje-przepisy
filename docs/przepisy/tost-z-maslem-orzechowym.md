# Tost z chlebem żytnim, masłem orzechowym i bananem + shake białkowy

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

- <span class="ing-item" data-base="60" data-unit="g" data-name="chleb żytni">60 g chleba żytniego</span> (2 kromki)
- <span class="ing-item" data-base="40" data-unit="g" data-name="masło orzechowe">40 g masła orzechowego</span> (4 łyżeczki)
- <span class="ing-item" data-base="60" data-unit="g" data-name="banan">60 g banana</span> (0.5 sztuki)
- <span class="ing-item" data-base="16" data-unit="g" data-name="odżywka białkowa">16 g odżywki białkowej</span> (2 łyżki)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Pokrojone kromki chleba żytniego przypiekamy na patelni.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Pieczywo smarujemy masłem orzechowym i na wierzch układamy pokrojonego banana.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Z odżywki i wody przygotowujemy shake, pijemy do posiłku.</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>