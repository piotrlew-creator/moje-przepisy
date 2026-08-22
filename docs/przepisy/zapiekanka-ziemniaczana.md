# Zapiekanka ziemniaczana z mozzarellą

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

- <span class="ing-item" data-base="140" data-unit="g" data-name="ziemniaki">140 g ziemniaków</span> (2 sztuki)
- <span class="ing-item" data-base="100" data-unit="g" data-name="szpinak">100 g szpinaku</span> (4 garści)
- <span class="ing-item" data-base="125" data-unit="g" data-name="passata pomidorowa">125 g passaty pomidorowej</span> (0.5 szklanki)
- <span class="ing-item" data-base="18" data-unit="g" data-name="czosnek">18 g czosnku</span> (3 ząbki)
- <span class="ing-item" data-base="5" data-unit="g" data-name="oliwa z oliwek">5 g oliwy z oliwek</span> (1 łyżeczka)
- <span class="ing-item" data-base="3" data-unit="g" data-name="świeża bazylia">3 g świeżej bazylii</span> (1 garść)
- <span class="ing-item" data-base="0.5" data-unit="g" data-name="gałka muszkatołowa">0.5 g gałki muszkatołowej</span> (2 szczypty)
- <span class="ing-item" data-base="0.25" data-unit="g" data-name="sól i pieprz">0.25 g soli i pieprzu</span> (1 szczypta)
- <span class="ing-item" data-base="45" data-unit="g" data-name="ser mozzarella">45 g sera mozzarella</span> (3 plastry)

## Sposób przygotowania

<div id="steps-container">
  <div class="step-card">
    <p><strong>Krok 1:</strong> Piekarnik nagrzewamy do 190 stopni.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 2:</strong> Ziemniaki obieramy i kroimy w cienkie plasterki, czosnek siekamy.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 3:</strong> Na patelni rozgrzewamy oliwę. Podsmażamy czosnek i dodajemy do niego umyty szpinak i gałkę muszkatołową. Przyprawiamy solą i pieprzem.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 4:</strong> Mozzarellę odsączamy i kroimy na plasterki.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 5:</strong> Do naczynia żaroodpornego wlewamy 1/3 passaty z pomidorów, układamy na niej kilka liści bazylii, posypujemy solą, układamy plastry ziemniaków, sera mozzarella i szpinak. Układamy kolejne warstwy, aż do wyczerpania wszystkich składników. Ostatnią warstwę wykańczamy serem mozzarella.</p>
  </div>
  <div class="step-card">
    <p><strong>Krok 6:</strong> Naczynie przykrywamy folią do pieczenia. Pieczemy przez 30 minut, po czym zdejmujemy folię i zapiekamy bez przykrycia, przez 10 minut na trybie termoobieg. Smacznego!</p>
  </div>
</div>

<div class="step-nav">
  <button id="btn-prev" class="btn-action" onclick="prevStep()">Poprzedni krok</button>
  <span id="step-indicator"></span>
  <button id="btn-next" class="btn-action" onclick="nextStep()">Następny krok</button>
</div>