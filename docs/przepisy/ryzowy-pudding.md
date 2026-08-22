# Ryżowy pudding z prażonymi gruszkami

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

- <span class="ing-item" data-base="30" data-unit="g" data-name="ryż basmati">30 g ryżu basmati</span> (2 łyżki)
- <span class="ing-item" data-base="75" data-unit="g" data-name="jogurt skyr">75 g jogurtu skyr</span> (0.5 opakowania)
- <span class="ing-item" data-base="130" data-unit="g" data-name="gruszka">130 g gruszki</span> (1 sztuka)
- <span class="ing-item" data-base="8" data-unit="g" data-name="cynamon">8 g cynamonu</span> (2 łyżeczki)
- <span class="ing-item" data-base="20" data-unit="g" data-name="erytrol">20 g erytrolu</span> (4 łyżeczki)
- <span class="ing-item" data-base="5" data-unit="g" data-name="olej rzepakowy">5 g oleju rzepakowego</span> (1 łyżeczka)
- <span class="ing-item" data-base="0.25" data-unit="g" data-name="sól">0.25 g soli</span> (1 szczypta)
- <span class="ing-item" data-base="30" data-unit="g" data-name="masło orzechowe">30 g masła orzechowego</span> (3 łyżeczki)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Ryż gotujemy według instrukcji na opakowaniu i odsączamy.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Gruszkę obieramy i kroimy w kostkę. Podsmażamy na oleju ze wskazaną połową porcji erytrolu przez 10 minut na patelni.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Jogurt skyr łączymy z masłem orzechowym, erytrolem i cynamonem w miseczce.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 4:</strong> Ugotowany ryż łączymy z jogurtem i prażoną gruszką.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 5:</strong> Całość przekładamy do miseczek. Smacznego!</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>