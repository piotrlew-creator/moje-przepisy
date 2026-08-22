# Wyszukiwarka Przepisów

Wybierz kategorię posiłku oraz składniki, na które masz ochotę:

<div class="filter-section">
  <h3>1. Wybierz Porę Dnia / Posiłek</h3>
  <div style="display:flex; gap:10px; margin-bottom:15px; flex-wrap: wrap;">
    <button class="btn-action" onclick="filterCategory('all')">Wszystkie</button>
    <button class="btn-action" onclick="filterCategory('sniadanie')">Śniadania</button>
    <button class="btn-action" onclick="filterCategory('obiad')">Obiady / 2. Śniadania</button>
    <button class="btn-action" onclick="filterCategory('kolacja')">Kolacje / Przekąski</button>
  </div>

  <h3>2. Wybierz Składniki</h3>
  <div class="ingredient-grid">
    <label><input type="checkbox" class="ing-filter" value="awokado" onchange="filterRecipes()"> Awokado</label>
    <label><input type="checkbox" class="ing-filter" value="banan" onchange="filterRecipes()"> Banan</label>
    <label><input type="checkbox" class="ing-filter" value="brokul" onchange="filterRecipes()"> Brokuł</label>
    <label><input type="checkbox" class="ing-filter" value="bulka" onchange="filterRecipes()"> Bułka / Grahamka</label>
    <label><input type="checkbox" class="ing-filter" value="cebula" onchange="filterRecipes()"> Cebula</label>
    <label><input type="checkbox" class="ing-filter" value="chleb" onchange="filterRecipes()"> Chleb żytni / razowy</label>
    <label><input type="checkbox" class="ing-filter" value="ciecierzyca" onchange="filterRecipes()"> Ciecierzyca</label>
    <label><input type="checkbox" class="ing-filter" value="daktyle" onchange="filterRecipes()"> Daktyle</label>
    <label><input type="checkbox" class="ing-filter" value="dynia" onchange="filterRecipes()"> Dynia</label>
    <label><input type="checkbox" class="ing-filter" value="gruszka" onchange="filterRecipes()"> Gruszka</label>
    <label><input type="checkbox" class="ing-filter" value="jablko" onchange="filterRecipes()"> Jabłko</label>
    <label><input type="checkbox" class="ing-filter" value="jajka" onchange="filterRecipes()"> Jajka</label>
    <label><input type="checkbox" class="ing-filter" value="jogurt" onchange="filterRecipes()"> Jogurt / Skyr</label>
    <label><input type="checkbox" class="ing-filter" value="kaszka" onchange="filterRecipes()"> Kasza gryczana / jaglana</label>
    <label><input type="checkbox" class="ing-filter" value="makaron" onchange="filterRecipes()"> Makaron</label>
    <label><input type="checkbox" class="ing-filter" value="marchewka" onchange="filterRecipes()"> Marchewka</label>
    <label><input type="checkbox" class="ing-filter" value="maslo-orzechowe" onchange="filterRecipes()"> Masło orzechowe</label>
    <label><input type="checkbox" class="ing-filter" value="mleko" onchange="filterRecipes()"> Mleko roślinne</label>
    <label><input type="checkbox" class="ing-filter" value="mozzarella" onchange="filterRecipes()"> Mozzarella</label>
    <label><input type="checkbox" class="ing-filter" value="odzywka" onchange="filterRecipes()"> Odżywka białkowa</label>
    <label><input type="checkbox" class="ing-filter" value="ogorek" onchange="filterRecipes()"> Ogórek</label>
    <label><input type="checkbox" class="ing-filter" value="orzechy" onchange="filterRecipes()"> Orzechy</label>
    <label><input type="checkbox" class="ing-filter" value="papryka" onchange="filterRecipes()"> Papryka</label>
    <label><input type="checkbox" class="ing-filter" value="pieczarki" onchange="filterRecipes()"> Pieczarki</label>
    <label><input type="checkbox" class="ing-filter" value="platki-owsiane" onchange="filterRecipes()"> Płatki owsiane / jaglane</label>
    <label><input type="checkbox" class="ing-filter" value="pomidor" onchange="filterRecipes()"> Pomidor / Pomidorki</label>
    <label><input type="checkbox" class="ing-filter" value="pstrog" onchange="filterRecipes()"> Pstrąg wędzony</label>
    <label><input type="checkbox" class="ing-filter" value="ryz" onchange="filterRecipes()"> Ryż</label>
    <label><input type="checkbox" class="ing-filter" value="serek-wiejski" onchange="filterRecipes()"> Serek wiejski / Twaróg</label>
  </div>
</div>

## Dostępne Przepisy

<ul id="recipes-list" style="list-style-type: square; padding-left: 20px;">
  <li data-category="sniadanie" data-ingredients="ryz,jablko,mleko,odzywka"><a href="przepisy/klejacy-ryz/">Klejący ryż z prażonym jabłkiem</a></li>
  <li data-category="obiad" data-ingredients="jajka,pieczarki,cebula,chleb"><a href="przepisy/jajecznica/">Jajecznica z pieczarkami, cebulą i pieczywem</a></li>
  <li data-category="obiad" data-ingredients="makaron,mozzarella,ogorek,pomidor"><a href="przepisy/makaron-mozzarella/">Makaron z mozzarellą, szpinakiem, ogórkiem i pomidorkami</a></li>
  <li data-category="kolacja" data-ingredients="daktyle,orzechy"><a href="przepisy/kulki-mocy/">Daktylowo-kakaowe kulki mocy z orzechami</a></li>
  <li data-category="sniadanie" data-ingredients="platki-owsiane,banan,orzechy,odzywka"><a href="przepisy/owsianka/">Owsianka</a></li>
  <li data-category="obiad" data-ingredients="serek-wiejski,papryka,bulka,orzechy"><a href="przepisy/serek-wiejski-grahamka/">Serek wiejski, papryka, grahamka i orzechy</a></li>
  <li data-category="obiad" data-ingredients="papryka,pomidor,makaron,mozzarella"><a href="przepisy/krem-paprykowo-pomidorowy/">Krem paprykowo-pomidorowy</a></li>
  <li data-category="kolacja" data-ingredients="chleb,serek-wiejski,pomidor"><a href="przepisy/kanapki-z-serkiem/">Kanapki z serkiem śmietankowym, pomidorem i szczypiorkiem</a></li>
  <li data-category="sniadanie" data-ingredients="banan,jajka,platki-owsiane,maslo-orzechowe,odzywka,orzechy"><a href="przepisy/placuszki-owsiane/">Placuszki owsiane orzechowe</a></li>
  <li data-category="obiad" data-ingredients="chleb,pomidor"><a href="przepisy/kanapki-z-serem/">Kanapki z żółtym serem, roszponką i pomidorem</a></li>
  <li data-category="obiad" data-ingredients=""><a href="przepisy/gyoza/">Pierożki gyoza z warzywami chef select z kimchi</a></li>
  <li data-category="kolacja" data-ingredients="banan,mleko,maslo-orzechowe"><a href="przepisy/koktajl-bananowy/">Koktajl bananowo-orzechowy</a></li>
  <li data-category="sniadanie" data-ingredients="platki-owsiane,mleko,gruszka,odzywka,orzechy"><a href="przepisy/jaglanka-gruszka/">Jaglanka na mleku roślinnym z gruszką</a></li>
  <li data-category="obiad" data-ingredients="kaszka,brokul,cebula"><a href="przepisy/kasza-z-tofu/">Kasza z tofu</a></li>
  <li data-category="obiad" data-ingredients="makaron,marchewka,cebula,pomidor"><a href="przepisy/spaghetti-bolognese/">Wegańskie spaghetti bolognese</a></li>
</ul>

<script>
function filterCategory(cat) {
  const cards = document.querySelectorAll('#recipes-list li');
  cards.forEach(card => {
    if (cat === 'all' || card.getAttribute('data-category') === cat) {
      card.style.display = 'list-item';
    } else {
      card.style.display = 'none';
    }
  });
}

function filterRecipes() {
  const selected = Array.from(document.querySelectorAll('.ing-filter:checked')).map(cb => cb.value);
  const cards = document.querySelectorAll('#recipes-list li');
  
  cards.forEach(card => {
    const cardIngs = (card.getAttribute('data-ingredients') || '').split(',');
    if (selected.length === 0 || selected.every(ing => cardIngs.includes(ing))) {
      card.style.display = 'list-item';
    } else {
      card.style.display = 'none';
    }
  });
}
</script>