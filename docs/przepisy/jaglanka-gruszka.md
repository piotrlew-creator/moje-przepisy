# Jaglanka na mleku roślinnym z gruszką

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

- <span class="ing-item" data-base="40" data-unit="g" data-name="płatki jaglane">40 g płatków jaglanych</span> (4 łyżki)
- <span class="ing-item" data-base="125" data-unit="g" data-name="mleko roślinne">125 g mleka roślinnego</span> (0.5 szklanki)
- <span class="ing-item" data-base="130" data-unit="g" data-name="gruszka">130 g gruszki</span> (1 sztuka)
- <span class="ing-item" data-base="2" data-unit="g" data-name="cynamon">2 g cynamonu</span> (0.5 łyżeczki)
- <span class="ing-item" data-base="16" data-unit="g" data-name="odżywka białkowa">16 g odżywki białkowej</span> (2 łyżki)
- <span class="ing-item" data-base="15" data-unit="g" data-name="orzechy włoskie">15 g orzechów włoskich</span> (0.5 garści)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Do rondelka wsypujemy płatki jaglane i zalewamy mlekiem. Gotujemy na małym ogniu, aż płatki będą miękkie. Mieszamy co chwilę.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Gruszkę kroimy w kostkę.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Gdy jaglanka zgęstnieje, dodajemy pokrojony owoc, odżywkę białkową i cynamon. Dokładnie mieszamy.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 4:</strong> Gotową jaglankę przekładamy do miseczki i posypujemy orzechami. Smacznego!</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>