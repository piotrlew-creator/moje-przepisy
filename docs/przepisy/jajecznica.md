# Jajecznica z pieczarkami, cebulą i pieczywem

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

- <span class="ing-item" data-base="168" data-unit="g" data-name="jajka kurze">168 g jajek kurzych</span> (3 sztuki)
- <span class="ing-item" data-base="100" data-unit="g" data-name="pieczarki">100 g pieczarek</span> (5 sztuk)
- <span class="ing-item" data-base="55" data-unit="g" data-name="cebula">55 g cebuli</span> (0.5 sztuki)
- <span class="ing-item" data-base="25" data-unit="g" data-name="szpinak">25 g szpinaku</span> (1 garść)
- <span class="ing-item" data-base="45" data-unit="g" data-name="rzodkiewka">45 g rzodkiewki</span> (3 sztuki)
- <span class="ing-item" data-base="5" data-unit="g" data-name="olej rzepakowy">5 g oleju rzepakowego</span> (1 łyżeczka)
- <span class="ing-item" data-base="60" data-unit="g" data-name="chleb żytni razowy">60 g chleba żytniego razowego</span> (2 kromki)
- <span class="ing-item" data-base="0.25" data-unit="g" data-name="sól">0.25 g soli</span> (1 szczypta)
- <span class="ing-item" data-base="0.25" data-unit="g" data-name="pieprz">0.25 g pieprzu</span> (1 szczypta)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Na patelni rozgrzewamy olej i podsmażamy pokrojone pieczarki oraz cebulę.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Do zeszklonych warzyw wbijamy jajka.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Smażymy na małym ogniu, cały czas mieszając, aż jajka się zetną.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 4:</strong> Gotową jajecznicę doprawiamy solą i pieprzem.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 5:</strong> Podajemy z pieczywem, szpinakiem i pokrojonymi rzodkiewkami. Smacznego!</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>