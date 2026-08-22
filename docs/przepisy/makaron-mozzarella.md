# Makaron z mozzarellą, szpinakiem, ogórkiem i pomidorkami koktajlowymi

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

- <span class="ing-item" data-base="50" data-unit="g" data-name="makaron pełnoziarnisty">50 g makaronu pełnoziarnistego</span> (1 porcja)
- <span class="ing-item" data-base="10" data-unit="g" data-name="zielone pesto">10 g zielonego pesto</span> (2 łyżeczki)
- <span class="ing-item" data-base="140" data-unit="g" data-name="pomidorki koktajlowe">140 g pomidorków koktajlowych</span> (7 sztuk)
- <span class="ing-item" data-base="1.5" data-unit="g" data-name="bazylia świeża">1.5 g bazylii świeżej</span> (0.5 garści)
- <span class="ing-item" data-base="50" data-unit="g" data-name="szpinak">50 g szpinaku</span> (2 garści)
- <span class="ing-item" data-base="75" data-unit="g" data-name="ogórek">75 g ogórka</span> (0.5 sztuki)
- <span class="ing-item" data-base="45" data-unit="g" data-name="mozzarella light">45 g mozzarelli light</span> (3 plastry)
- <span class="ing-item" data-base="10" data-unit="g" data-name="ser grana padano">10 g sera grana padano</span> (1 łyżka)
- <span class="ing-item" data-base="0.25" data-unit="g" data-name="sól">0.25 g soli</span> (1 szczypta)
- <span class="ing-item" data-base="0.25" data-unit="g" data-name="pieprz">0.25 g pieprzu</span> (1 szczypta)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Makaron gotujemy według instrukcji umieszczonej na opakowaniu.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Kroimy pomidorki, ogórek zielony, siekamy bazylię.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Do miski dodajemy makaron, pokrojone warzywa, posiekaną bazylię, umyty szpinak, czerwone pesto i całość dokładnie mieszamy, w razie potrzeby przyprawiamy solą i pieprzem.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 4:</strong> Gotowy makaron z warzywami wykładamy na talerz. Posypujmy tartym serem grana padano i układamy mozzarellę. Smacznego!</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>