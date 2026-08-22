# Owsianka z marchewką

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

- <span class="ing-item" data-base="125" data-unit="g" data-name="napój roślinny">125 g napoju roślinnego</span> (0.5 szklanki)
- <span class="ing-item" data-base="20" data-unit="g" data-name="płatki owsiane górskie">20 g płatków owsianych górskich</span> (2 łyżki)
- <span class="ing-item" data-base="45" data-unit="g" data-name="marchewka">45 g marchewki</span> (1 sztuka)
- <span class="ing-item" data-base="0.25" data-unit="g" data-name="sól">0.25 g soli</span> (1 szczypta)
- <span class="ing-item" data-base="4" data-unit="g" data-name="cynamon">4 g cynamonu</span> (1 łyżeczka)
- <span class="ing-item" data-base="60" data-unit="g" data-name="mały banan">60 g małego banana</span> (1 sztuka)
- <span class="ing-item" data-base="30" data-unit="g" data-name="mieszanka orzechów">30 g mieszanki orzechów</span> (1 garść)
- <span class="ing-item" data-base="16" data-unit="g" data-name="wegańska odżywka białkowa">16 g wegańskiej odżywki białkowej</span> (2 łyżki)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> W rondelku podgrzewamy mleko roślinne, następnie dodajemy startą na drobnych oczkach marchewkę oraz płatki owsiane, odżywkę, sól i cynamon. Gotujemy przez 5-7 minut.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Przekładamy owsiankę do miski i na wierzch dodajemy posiekane orzechy oraz pokrojonego banana. Smacznego!</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>