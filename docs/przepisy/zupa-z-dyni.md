# Zupa z dyni z pieczoną ciecierzycą - przepis na 3 porcje

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

- <span class="ing-item" data-base="300" data-unit="g" data-name="dynia">300 g dyni</span> (3 porcje)
- <span class="ing-item" data-base="200" data-unit="g" data-name="mleczko kokosowe">200 g mleczka kokosowego</span> (0.5 opakowania)
- <span class="ing-item" data-base="480" data-unit="g" data-name="ciecierzyca konserwowa">480 g ciecierzycy konserwowej</span> (2 opakowania)
- <span class="ing-item" data-base="12" data-unit="g" data-name="sok z cytryny">12 g soku z cytryny</span> (2 łyżki)
- <span class="ing-item" data-base="45" data-unit="g" data-name="marchew">45 g marchwi</span> (1 sztuka)
- <span class="ing-item" data-base="70" data-unit="g" data-name="ziemniaki">70 g ziemniaków</span> (1 sztuka)
- <span class="ing-item" data-base="4" data-unit="g" data-name="świeża kolendra">4 g świeżej kolendry</span> (1 garść)
- <span class="ing-item" data-base="1" data-unit="g" data-name="czosnek granulowany">1 g czosnku granulowanego</span> (1 szczypta)
- <span class="ing-item" data-base="3" data-unit="g" data-name="papryka słodka">3 g papryki słodkiej</span> (1 łyżeczka)
- <span class="ing-item" data-base="0.25" data-unit="g" data-name="sól i pieprz">0.25 g soli i pieprzu</span> (1 szczypta)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Dynię, marchew, ziemniaki obieramy i kroimy na duże kawałki. Układamy na blaszce wyłożonej papierem do pieczenia. Odsączoną ciecierzycę układamy obok, wszystko przyprawiamy solą, pieprzem, czosnkiem granulowanym, słodką papryką. Pieczemy w piekarniku z termoobiegiem rozgrzanym do 230 stopni przez 25 minut.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Warzywa przekładamy do garnka (trochę ciecierzycy zostawiamy do posypania), zalewamy mlekiem kokosowym, dolewamy ok 300 ml wody, zagotowujemy.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Zupę gotujemy przez 10 minut, blendujemy na gładki krem. Podajemy z pieczoną ciecierzycą i posiekaną kolendrą. Smacznego!</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>