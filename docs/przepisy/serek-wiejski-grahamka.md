# Serek wiejski, papryka, grahamka i orzechy

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

- <span class="ing-item" data-base="150" data-unit="g" data-name="serek wiejski">150 g serka wiejskiego</span> (1 opakowanie)
- <span class="ing-item" data-base="85" data-unit="g" data-name="papryka żółta">85 g papryki żółtej</span> (0.5 sztuki)
- <span class="ing-item" data-base="80" data-unit="g" data-name="bułka grahamka">80 g bułki grahamki</span> (1 sztuka)
- <span class="ing-item" data-base="24" data-unit="g" data-name="orzechy włoskie">24 g orzechów włoskich</span> (6 sztuk)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Bułkę kroimy na pół, smarujemy serkiem wiejskim, układamy paprykę i orzechy. Smacznego!</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>