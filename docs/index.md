# Baza Przepisów Dietetycznych

Wybierz typ posiłku oraz składniki, na które masz ochotę.

<div class="filter-section">
  <h3>1. Wybierz porę dnia:</h3>
  <select id="meal-type-filter" style="padding: 8px; width: 100%; font-size: 1em;">
    <option value="all">Wszystkie posiłki</option>
    <option value="sniadanie">Śniadanie</option>
    <option value="obiad">Obiad</option>
    <option value="kolacja">Kolacja</option>
  </select>

  <h3 style="margin-top: 15px;">2. Wybierz składniki (przyprawy wykluczone):</h3>
  <div class="ingredient-grid">
    <label><input type="checkbox" class="ingredient-checkbox" value="Jaja"> Jaja</label>
    <label><input type="checkbox" class="ingredient-checkbox" value="Pomidory"> Pomidory</label>
    <label><input type="checkbox" class="ingredient-checkbox" value="Cebula"> Cebula</label>
    <label><input type="checkbox" class="ingredient-checkbox" value="Oliwa z oliwek"> Oliwa z oliwek</label>
    <label><input type="checkbox" class="ingredient-checkbox" value="Pierś z kurczaka"> Pierś z kurczaka</label>
    <label><input type="checkbox" class="ingredient-checkbox" value="Ryż"> Ryż</label>
  </div>
</div>

## Dostępne przepisy

<div id="recipes-list">

  <div class="recipe-card" data-meal-type="sniadanie" data-ingredients="Jaja,Pomidory,Cebula,Oliwa z oliwek">
    <h3><a href="przepisy/szakszuka-z-pomidorami/">Szakszuka z pomidorami</a></h3>
    <p>Typ: Śniadanie | Składniki główne: Jaja, Pomidory, Cebula</p>
  </div>

</div>