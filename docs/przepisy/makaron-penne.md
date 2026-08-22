# Makaron penne ze szpinakiem, pieczarkami, pomidorkami cherry i serem grana padano

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

- <span class="ing-item" data-base="60" data-unit="g" data-name="makaron penne">60 g makaronu penne</span> (12 łyżek)
- <span class="ing-item" data-base="75" data-unit="g" data-name="szpinak">75 g szpinaku</span> (3 garści)
- <span class="ing-item" data-base="108" data-unit="g" data-name="śmietanka 12%">108 g śmietanki 12%</span> (6 łyżek)
- <span class="ing-item" data-base="6" data-unit="g" data-name="czosnek">6 g czosnku</span> (1 ząbek)
- <span class="ing-item" data-base="55" data-unit="g" data-name="cebula">55 g cebuli</span> (0.5 sztuki)
- <span class="ing-item" data-base="200" data-unit="g" data-name="pieczarki">200 g pieczarek</span> (10 sztuk)
- <span class="ing-item" data-base="10" data-unit="g" data-name="ser grana padano">10 g sera grana padano</span> (1 łyżka)
- <span class="ing-item" data-base="225" data-unit="g" data-name="brokuł">225 g brokuła</span> (0.5 sztuki)
- <span class="ing-item" data-base="200" data-unit="g" data-name="pomidorki">200 g pomidorków</span> (10 sztuk)
- <span class="ing-item" data-base="15" data-unit="g" data-name="ksylitol">15 g ksylitolu</span> (1 łyżka)
- <span class="ing-item" data-base="0.25" data-unit="g" data-name="sól">0.25 g soli</span> (1 szczypta)
- <span class="ing-item" data-base="0.25" data-unit="g" data-name="pieprz">0.25 g pieprzu</span> (1 szczypta)
- <span class="ing-item" data-base="10" data-unit="g" data-name="oliwa z oliwek">10 g oliwy z oliwek</span> (2 łyżeczki)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Brokuł kroimy na mniejsze różyczki.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> W rondlu gotujemy wodę i doprawiamy ją solą, pieprzem i ksylitolem. Brokuł gotujemy, aż będzie miękki, około 5-7 minut.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Czosnek i cebulę siekamy, pieczarki kroimy. W rondelku z odrobiną oliwy dusimy czosnek z cebulką.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 4:</strong> Gdy cebulka z czosnkiem się zeszklą, dodajemy pieczarki i wszystko razem dusimy.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 5:</strong> Do uduszonych warzyw wlewamy śmietankę i gotujemy, aż lekko zgęstnieje.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 6:</strong> Gdy sos się gotuje, gotujemy makaron według instrukcji umieszczonej na opakowaniu.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 7:</strong> Do ugotowanego sosu dodajemy ugotowany brokuł, świeży szpinak, pokrojone pomidorki cherry, całość mieszamy i doprawiamy solą z pieprzem.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 8:</strong> Gotowy sos mieszamy z makaronem i posypujemy serem grana padano. Smacznego!</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>