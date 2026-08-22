# Wyszukiwarka Przepisów

Wybierz kategorię posiłku oraz składniki, na które masz ochotę:

<div class="filter-section">
  <h3>1. Wybierz Pora Dnia / Posiłek</h3>
  <div style="display:flex; gap:10px; margin-bottom:15px;">
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

<div id="recipes-list">

- [Klejący ryż z prażonym jabłkiem](przepisy/klejacy-ryz.md) { .recipe-card data-category="sniadanie" data-ingredients="ryz,jablko,mleko,odzywka" }
- [Jajecznica z pieczarkami, cebulą i pieczywem](przepisy/jajecznica.md) { .recipe-card data-category="obiad" data-ingredients="jajka,pieczarki,cebula,chleb" }
- [Makaron z mozzarellą, szpinakiem, ogórkiem i pomidorkami](przepisy/makaron-mozzarella.md) { .recipe-card data-category="obiad" data-ingredients="makaron,mozzarella,ogorek,pomidor" }
- [Daktylowo-kakaowe kulki mocy z orzechami](przepisy/kulki-mocy.md) { .recipe-card data-category="kolacja" data-ingredients="daktyle,orzechy" }
- [Owsianka](przepisy/owsianka.md) { .recipe-card data-category="sniadanie" data-ingredients="platki-owsiane,banan,orzechy,odzywka" }
- [Serek wiejski, papryka, grahamka i orzechy](przepisy/serek-wiejski-grahamka.md) { .recipe-card data-category="obiad" data-ingredients="serek-wiejski,papryka,bulka,orzechy" }
- [Krem paprykowo-pomidorowy](przepisy/krem-paprykowo-pomidorowy.md) { .recipe-card data-category="obiad" data-ingredients="papryka,pomidor,makaron,mozzarella" }
- [Kanapki z serkiem śmietankowym, pomidorem i szczypiorkiem](przepisy/kanapki-z-serkiem.md) { .recipe-card data-category="kolacja" data-ingredients="chleb,serek-wiejski,pomidor" }
- [Placuszki owsiane orzechowe](przepisy/placuszki-owsiane.md) { .recipe-card data-category="sniadanie" data-ingredients="banan,jajka,platki-owsiane,maslo-orzechowe,odzywka,orzechy" }
- [Kanapki z żółtym serem, roszponką i pomidorem](przepisy/kanapki-z-serem.md) { .recipe-card data-category="obiad" data-ingredients="chleb,pomidor" }
- [Pierożki gyoza z warzywami chef select z kimchi](przepisy/gyoza.md) { .recipe-card data-category="obiad" data-ingredients="" }
- [Koktajl bananowo-orzechowy](przepisy/koktajl-bananowy.md) { .recipe-card data-category="kolacja" data-ingredients="banan,mleko,maslo-orzechowe" }
- [Jaglanka na mleku roślinnym z gruszką](przepisy/jaglanka-gruszka.md) { .recipe-card data-category="sniadanie" data-ingredients="platki-owsiane,mleko,gruszka,odzywka,orzechy" }
- [Kasza z tofu](przepisy/kasza-z-tofu.md) { .recipe-card data-category="obiad" data-ingredients="kaszka,brokul,cebula" }
- [Wegańskie spaghetti bolognese](przepisy/spaghetti-bolognese.md) { .recipe-card data-category="obiad" data-ingredients="makaron,marchewka,cebula,pomidor" }
- [Bowl śniadaniowy z jabłkiem i kaki](przepisy/bowl-sniadaniowy.md) { .recipe-card data-category="sniadanie" data-ingredients="platki-owsiane,orzechy,jablko,jogurt" }
- [Tosty z jajkiem sadzonym i awokado](przepisy/tosty-awokado.md) { .recipe-card data-category="obiad" data-ingredients="chleb,awokado,jajka" }
- [Zupa z dyni z pieczoną ciecierzycą](przepisy/zupa-z-dyni.md) { .recipe-card data-category="obiad" data-ingredients="dynia,ciecierzyca,marchewka" }
- [Omlet mleczna kanapka](przepisy/omlet-mleczna-kanapka.md) { .recipe-card data-category="sniadanie" data-ingredients="jajka,jogurt,serek-wiejski" }
- [Zapiekanka ziemniaczana z mozzarellą](przepisy/zapiekanka-ziemniaczana.md) { .recipe-card data-category="obiad" data-ingredients="mozzarella,pomidor" }
- [Jaglany snickers](przepisy/jaglany-snickers.md) { .recipe-card data-category="sniadanie" data-ingredients="kaszka,jogurt,mleko,maslo-orzechowe,daktyle,orzechy,odzywka" }
- [Pasta z wędzonego pstrąga i twarogu](przepisy/pasta-z-pstroga.md) { .recipe-card data-category="obiad" data-ingredients="chleb,serek-wiejski,pstrog,ogorek" }
- [Tost z chlebem żytnim, masłem orzechowym i bananem](przepisy/tost-z-maslem-orzechowym.md) { .recipe-card data-category="sniadanie" data-ingredients="chleb,maslo-orzechowe,banan,odzywka" }
- [Makaron penne ze szpinakiem, pieczarkami i pomidorkami](przepisy/makaron-penne.md) { .recipe-card data-category="obiad" data-ingredients="makaron,cebula,pieczarki,brokul,pomidor" }
- [Kanapka z pastą pomidorową](przepisy/kanapka-z-pasta-pomidorowa.md) { .recipe-card data-category="kolacja" data-ingredients="chleb,pomidor" }

</div>

<script>
function filterCategory(cat) {
  const cards = document.querySelectorAll('#recipes-list li');
  cards.forEach(card => {
    if (cat === 'all' || card.getAttribute('data-category') === cat) {
      card.style.display = 'block';
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
      card.style.display = 'block';
    } else {
      card.style.display = 'none';
    }
  });
}
</script>