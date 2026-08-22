# Bruschetta z pomidorami, świeżymi ziołami i serem grana padano

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

- <span class="ing-item" data-base="70" data-unit="g" data-name="bagietka">70 g bagietki</span> (0.5 sztuki)
- <span class="ing-item" data-base="100" data-unit="g" data-name="pomidor">100 g pomidora</span> (1 sztuka)
- <span class="ing-item" data-base="20" data-unit="g" data-name="mała cebula czerwona">20 g małej cebuli czerwonej</span> (1 sztuka)
- <span class="ing-item" data-base="6" data-unit="g" data-name="czosnek">6 g czosnku</span> (1 ząbek)
- <span class="ing-item" data-base="3" data-unit="g" data-name="bazylia świeża">3 g bazylii świeżej</span> (1 garść)
- <span class="ing-item" data-base="50" data-unit="g" data-name="ser grana padano">50 g sera grana padano</span> (2 porcje)
- <span class="ing-item" data-base="3" data-unit="g" data-name="ocet balsamiczny">3 g octu balsamicznego</span> (0.5 łyżki)
- <span class="ing-item" data-base="5" data-unit="g" data-name="oliwa z oliwek">5 g oliwy z oliwek</span> (1 łyżeczka)
- <span class="ing-item" data-base="0.25" data-unit="g" data-name="sól i pieprz">0.25 g soli i pieprzu</span> (1 szczypta)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Pomidory myjemy, cebulę i czosnek obieramy. Warzywa kroimy w kostkę.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Pokrojone warzywa mieszamy ze sobą, dodajemy posiekaną bazylię. Całość doprawiamy solą, pieprzem, octem i oliwą z oliwek.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Bagietkę kroimy na kromki i pieczemy w piekarniku rozgrzanym do 180 stopni przez około 5 minut, aż będą chrupkie.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 4:</strong> Na grzanki nakładamy pomidory z cebulką i czosnkiem, posypujemy startym serem grana padano.</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>