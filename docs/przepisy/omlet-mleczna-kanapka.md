# Omlet mleczna kanapka

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

- <span class="ing-item" data-base="56" data-unit="g" data-name="jajko">56 g jajko</span> (1 sztuka)
- <span class="ing-item" data-base="35" data-unit="g" data-name="mąka pszenna pełnoziarnista">35 g mąki pszennej pełnoziarnistej</span> (2.5 łyżki)
- <span class="ing-item" data-base="10" data-unit="g" data-name="kakao">10 g kakao</span> (1 łyżka)
- <span class="ing-item" data-base="60" data-unit="g" data-name="jogurt naturalny">60 g jogurtu naturalnego</span> (3 łyżki)
- <span class="ing-item" data-base="2" data-unit="g" data-name="proszek do pieczenia">2 g proszku do pieczenia</span> (0.5 łyżeczki)
- <span class="ing-item" data-base="40" data-unit="g" data-name="jogurt naturalny (do kremu)">40 g jogurtu naturalnego</span> (2 łyżki)
- <span class="ing-item" data-base="90" data-unit="g" data-name="twaróg chudy">90 g twarogu chudego</span> (3 plastry)
- <span class="ing-item" data-base="23" data-unit="g" data-name="ksylitol">23 g ksylitolu</span> (1.5 łyżki)
- <span class="ing-item" data-base="3" data-unit="g" data-name="ekstrakt waniliowy">3 g ekstraktu waniliowego</span> (1 łyżeczka)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Składniki omletu mieszamy lub blendujemy ze sobą, smażymy na patelni pod przykryciem przez 3-5 minut na średnim ogniu.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Składniki kremu blendujemy na gładką masę.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Omlet ściągamy z patelni. Odstawiamy, żeby nieco ostygł. Smarujemy kremem i składamy na pół. Smacznego!</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>