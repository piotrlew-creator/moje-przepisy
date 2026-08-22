# Pasta z wędzonego pstrąga i twarogu ze szczypiorkiem, warzywami i pieczywem

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
- <span class="ing-item" data-base="60" data-unit="g" data-name="twaróg tłusty">60 g twarogu tłustego</span> (2 opakowania)
- <span class="ing-item" data-base="60" data-unit="g" data-name="pstrąg wędzony">60 g pstrąga wędzonego</span> (2 porcje)
- <span class="ing-item" data-base="75" data-unit="g" data-name="ogórek zielony">75 g ogórka zielonego</span> (0.5 sztuki)
- <span class="ing-item" data-base="90" data-unit="g" data-name="rzodkiewki">90 g rzodkiewek</span> (6 sztuk)
- <span class="ing-item" data-base="20" data-unit="g" data-name="rukola">20 g rukoli</span> (1 garść)
- <span class="ing-item" data-base="12" data-unit="g" data-name="koperek">12 g koperku</span> (3 łyżeczki)
- <span class="ing-item" data-base="10" data-unit="g" data-name="szczypiorek">10 g szczypiorku</span> (2 łyżeczki)
- <span class="ing-item" data-base="0.25" data-unit="g" data-name="sól i pieprz">0.25 g soli i pieprzu</span> (1 szczypta)
- <span class="ing-item" data-base="10" data-unit="g" data-name="masło">10 g masła</span> (2 łyżeczki)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Pstrąga obieramy z ości i dzielimy na mniejsze kawałki.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Siekamy szczypiorek i przekładamy do miski.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Dodajemy twaróg, dokładnie mieszamy. Doprawiamy solą i pieprzem.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 4:</strong> Gotową pastę podajemy z pokrojonymi warzywami: rzodkiewką, ogórkiem, rukolą i pieczywem posmarowanym masłem. Smacznego!</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>