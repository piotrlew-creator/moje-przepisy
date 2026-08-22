# Jaglany snickers

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

- <span class="ing-item" data-base="10" data-unit="g" data-name="gorzka czekolada">10 g gorzkiej czekolady</span> (1 porcja)
- <span class="ing-item" data-base="30" data-unit="g" data-name="kasza jaglana">30 g kaszy jaglanej</span> (2 łyżki)
- <span class="ing-item" data-base="80" data-unit="g" data-name="jogurt roślinny">80 g jogurtu roślinnego</span> (0.5 opakowania)
- <span class="ing-item" data-base="105" data-unit="g" data-name="napój sojowy">105 g napoju sojowego</span> (9 łyżek)
- <span class="ing-item" data-base="10" data-unit="g" data-name="masło orzechowe">10 g masła orzechowego</span> (1 łyżeczka)
- <span class="ing-item" data-base="10" data-unit="g" data-name="świeże daktyle">10 g świeżych daktyli</span> (2 sztuki)
- <span class="ing-item" data-base="8" data-unit="g" data-name="orzechy włoskie">8 g orzechów włoskich</span> (2 sztuki posiekane)
- <span class="ing-item" data-base="7" data-unit="g" data-name="syrop z agawy">7 g syropu z agawy</span> (0.5 łyżki)
- <span class="ing-item" data-base="16" data-unit="g" data-name="wegańska odżywka białkowa">16 g wegańskiej odżywki białkowej</span> (2 łyżki)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Kaszę gotujemy w osolonej wodzie według instrukcji na opakowaniu.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Daktyle jeśli mamy suszone, zalewamy gorącą wodą na 10 minut. W przypadku daktyli świeżych pomijamy ten krok.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Do blendera przekładamy czekoladę, daktyle, masło orzechowe, napój roślinny, jogurt, odżywkę wegańską oraz ugotowaną kaszę.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 4:</strong> Całość blendujemy, przekładamy do szklanek oblanych syropem z agawy i posypanych posiekanymi orzechami. Jeśli jest za gęste, dolewamy wody. Na wierzchu układamy pozostałą posiekaną czekoladę. Smacznego!</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>