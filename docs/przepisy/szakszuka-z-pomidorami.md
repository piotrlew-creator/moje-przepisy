# Szakszuka z pomidorami

<div class="recipe-box">
  <div class="portion-selector">
    <label for="persons-count"><strong>Wybierz liczbę osób:</strong> </label>
    <input type="number" id="persons-count" value="1" min="1" max="20">
  </div>

  <button class="btn-action" onclick="toggleShoppingList()">Lista zakupów</button>

  <div id="shopping-list-container" class="shopping-list-modal">
    <div id="pdf-area">
      <h3>Lista zakupów - Szakszuka z pomidorami</h3>
      <div id="shopping-list-items"></div>
    </div>
    <br>
    <button class="btn-action" onclick="downloadPDF()">Wygeneruj PDF</button>
  </div>
</div>

### Składniki (na 1 porcję):
<ul id="ingredients-list">
  <li class="ingredient-item">
    <span class="ing-name">Jaja kurze</span>: 
    <span class="ingredient" data-base-qty="2" data-unit="szt."><span class="qty-value">2</span></span> <span class="ing-unit">szt.</span>
  </li>
  <li class="ingredient-item">
    <span class="ing-name">Pomidory krojone</span>: 
    <span class="ingredient" data-base-qty="200" data-unit="g"><span class="qty-value">200</span></span> <span class="ing-unit">g</span>
  </li>
  <li class="ingredient-item">
    <span class="ing-name">Cebula</span>: 
    <span class="ingredient" data-base-qty="50" data-unit="g"><span class="qty-value">50</span></span> <span class="ing-unit">g</span>
  </li>
  <li class="ingredient-item">
    <span class="ing-name">Oliwa z oliwek</span>: 
    <span class="ingredient" data-base-qty="10" data-unit="g"><span class="qty-value">10</span></span> <span class="ing-unit">g</span>
  </li>
</ul>

---

### Sposób przygotowania (Krok po kroku)

<div id="wizard-steps">
  <div class="step-card active" data-step="1">
    <h4>Krok 1 z 3</h4>
    <p>Drobno posiekaj cebulę i zeszklij ją na rozgrzanej oliwie z oliwek na patelni.</p>
    <button class="btn-action" onclick="nextStep()">Następny krok</button>
  </div>

  <div class="step-card" data-step="2">
    <h4>Krok 2 z 3</h4>
    <p>Dodaj krojone pomidory i duś całość na średnim ogniu przez około 5-7 minut, aż sos zgęstnieje.</p>
    <button class="btn-action" onclick="prevStep()">Poprzedni krok</button>
    <button class="btn-action" onclick="nextStep()">Następny krok</button>
  </div>

  <div class="step-card" data-step="3">
    <h4>Krok 3 z 3</h4>
    <p>Zrób wgłębienia w sosie, wbij w nie jaja, przykryj patelnię pokrywką i gotuj na małym ogniu do ścięcia białek.</p>
    <button class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  </div>
</div>