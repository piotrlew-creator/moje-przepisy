# Tosty z jajkiem sadzonym i awokado

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

- <span class="ing-item" data-base="60" data-unit="g" data-name="chleb tostowy pełnoziarnisty">60 g chleba tostowego pełnoziarnistego</span> (2 kromki)
- <span class="ing-item" data-base="70" data-unit="g" data-name="awokado">70 g awokado</span> (0.5 sztuki)
- <span class="ing-item" data-base="112" data-unit="g" data-name="jajko">112 g jajka</span> (2 sztuki)
- <span class="ing-item" data-base="40" data-unit="g" data-name="rukola">40 g rukoli</span> (2 garści)
- <span class="ing-item" data-base="10" data-unit="g" data-name="szczypiorek">10 g szczypiorku</span> (2 łyżeczki)
- <span class="ing-item" data-base="0.25" data-unit="g" data-name="sól">0.25 g soli</span> (1 szczypta)
- <span class="ing-item" data-base="0.25" data-unit="g" data-name="pieprz">0.25 g pieprzu</span> (1 szczypta)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Pieczywo opiekamy w tosterze lub na patelni.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Awokado obieramy ze skórki i smarujemy kromki chleba.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Na rozgrzanej patelni, pod przykryciem przygotowujemy jajka sadzone. Doprawiamy solą i pieprzem.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 4:</strong> Na posmarowanych kanapkach układamy rukolę i jajka. Posypujemy posiekanym szczypiorkiem. Smacznego!</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>