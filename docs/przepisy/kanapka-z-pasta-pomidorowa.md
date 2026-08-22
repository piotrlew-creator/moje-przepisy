# Kanapka z pastą pomidorową

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

- <span class="ing-item" data-base="40" data-unit="g" data-name="soczewica czerwona">40 g soczewicy czerwonej</span> (4 łyżki)
- <span class="ing-item" data-base="60" data-unit="g" data-name="chleb żytni razowy">60 g chleba żytniego razowego</span> (2 kromki)
- <span class="ing-item" data-base="18" data-unit="g" data-name="pasta tahini">18 g pasty tahini</span> (3 łyżeczki)
- <span class="ing-item" data-base="20" data-unit="g" data-name="pomidory suszone">20 g pomidorów suszonych</span> (1 sztuka)
- <span class="ing-item" data-base="6" data-unit="g" data-name="czosnek">6 g czosnku</span> (1 ząbek)
- <span class="ing-item" data-base="3" data-unit="g" data-name="tymianek">3 g tymianku</span> (1 łyżeczka)
- <span class="ing-item" data-base="1" data-unit="g" data-name="kumin">1 g kuminu</span> (1 szczypta)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Soczewicę gotujemy zgodnie z instrukcją na opakowaniu.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Po ugotowaniu soczewicę studzimy.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Przekładamy do blendera wszystkie składniki pasty i blendujemy na gładką masę.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 4:</strong> Podajemy z pieczywem.</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>