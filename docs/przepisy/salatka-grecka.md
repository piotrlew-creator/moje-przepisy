# Sałatka grecka z serem sałatkowym i pieczywem

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

- <span class="ing-item" data-base="50" data-unit="g" data-name="miks sałat">50 g miksu sałat</span> (2 garści)
- <span class="ing-item" data-base="100" data-unit="g" data-name="ser feta">100 g sera feta</span> (0.5 sztuki)
- <span class="ing-item" data-base="20" data-unit="g" data-name="oliwki zielone">20 g oliwek zielonych</span> (0.5 garści)
- <span class="ing-item" data-base="3" data-unit="g" data-name="suszone oregano">3 g suszonego oregano</span> (1 łyżeczka)
- <span class="ing-item" data-base="85" data-unit="g" data-name="papryka żółta">85 g papryki żółtej</span> (0.5 sztuki)
- <span class="ing-item" data-base="55" data-unit="g" data-name="cebula">55 g cebuli</span> (0.5 sztuki)
- <span class="ing-item" data-base="5" data-unit="g" data-name="oliwa z oliwek">5 g oliwy z oliwek</span> (1 łyżeczka)
- <span class="ing-item" data-base="3" data-unit="g" data-name="sok z cytryny">3 g soku z cytryny</span> (0.5 łyżki)
- <span class="ing-item" data-base="160" data-unit="g" data-name="pomidor">160 g pomidora</span> (1 sztuka)
- <span class="ing-item" data-base="150" data-unit="g" data-name="ogórek zielony">150 g ogórka zielonego</span> (1 sztuka)
- <span class="ing-item" data-base="30" data-unit="g" data-name="chleb żytni razowy">30 g chleba żytniego razowego</span> (1 kromka)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Kroimy paprykę, cebulę, pomidor, ogórek, oliwki i ser feta/sałatkowy.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Mieszamy oliwę, oregano, sól, pieprz, sok z cytryny.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Na talerz nakładamy sałatę, pokrojone warzywa, oliwki, ser sałatkowy, polewamy sosem, dokładnie mieszamy i podajemy z pieczywem. Smacznego!</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>