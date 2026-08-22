# Placuszki owsiane orzechowe

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

- <span class="ing-item" data-base="60" data-unit="g" data-name="mały banan">60 g małego banana</span> (1 sztuka)
- <span class="ing-item" data-base="56" data-unit="g" data-name="jajo kurze">56 g jaja kurzego</span> (1 sztuka)
- <span class="ing-item" data-base="24" data-unit="g" data-name="mąka owsiana pełnoziarnista">24 g mąki owsianej pełnoziarnistej</span> (2 łyżki)
- <span class="ing-item" data-base="10" data-unit="g" data-name="masło orzechowe">10 g masła orzechowego</span> (1 łyżeczka)
- <span class="ing-item" data-base="16" data-unit="g" data-name="odżywka białkowa">16 g odżywki białkowej</span> (2 łyżki)
- <span class="ing-item" data-base="15" data-unit="g" data-name="mieszanka orzechów">15 g mieszanki orzechów</span> (0.5 garści)
- <span class="ing-item" data-base="15" data-unit="g" data-name="syrop z agawy">15 g syropu z agawy</span> (1 łyżka)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Składniki na ciasto blendujemy i odstawiamy na 5-10 minut.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Placuszki smażymy bez tłuszczu na nieprzywierającej patelni, podajemy polane syropem z agawy i posypane posiekanymi orzechami.</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>