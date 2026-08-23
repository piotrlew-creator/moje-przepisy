---
hide:
  - toc
---

# Co dziś jesz?

Wybierz porę posiłku, zaznacz produkty, na które masz ochotę — albo po prostu przewiń wszystkie 280 przepisów z Twoich planów.

<div class="p-finder" id="finder">
<div class="p-slotbar" role="group" aria-label="Pora posiłku">
<button type="button" class="p-chip" data-slot-filter="all" data-on="1" aria-pressed="true">Wszystkie</button>
<button type="button" class="p-chip p-chip--slot1" data-slot-filter="sniadanie" data-slot-label="Śniadanie" aria-pressed="false"><span class="p-dot"></span>Śniadanie <span class="p-num" style="opacity:.7">7:00-10:00</span></button>
<button type="button" class="p-chip p-chip--slot2" data-slot-filter="obiad" data-slot-label="Obiad" aria-pressed="false"><span class="p-dot"></span>Obiad <span class="p-num" style="opacity:.7">13:00-16:00</span></button>
<button type="button" class="p-chip p-chip--slot3" data-slot-filter="kolacja" data-slot-label="Kolacja" aria-pressed="false"><span class="p-dot"></span>Kolacja <span class="p-num" style="opacity:.7">18:00-20:00</span></button>
</div>
<details class="p-panel" id="ing-panel">
<summary class="p-panel__summary">
<span class="p-eyebrow">Mam ochotę na…</span>
<span class="p-panel__state" id="ing-state">wybierz składniki</span>
</summary>
<div class="p-panel__inner">
<div class="p-searchrow">
<div class="p-search"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg><input type="search" id="ing-search" inputmode="search" placeholder="Szukaj składnika…" aria-label="Szukaj składnika"><button type="button" class="p-search__x" id="search-clear" aria-label="Wyczyść wyszukiwanie" hidden>&times;</button></div>
<button type="button" class="p-btn p-btn--clear" id="clear-filters" hidden>Wyczyść <span class="p-num" id="clear-count"></span></button>
</div>
<div class="p-chips" id="ing-chips">
<label class="p-chip" data-rank="top" data-label="Jajka"><input type="checkbox" value="jajka">Jajka <span class="p-num" style="opacity:.55">43</span></label>
<label class="p-chip" data-rank="top" data-label="Makaron"><input type="checkbox" value="makaron">Makaron <span class="p-num" style="opacity:.55">19</span></label>
<label class="p-chip" data-rank="top" data-label="Ryż"><input type="checkbox" value="ryz">Ryż <span class="p-num" style="opacity:.55">20</span></label>
<label class="p-chip" data-rank="top" data-label="Kasza"><input type="checkbox" value="kasza">Kasza <span class="p-num" style="opacity:.55">12</span></label>
<label class="p-chip" data-rank="top" data-label="Płatki owsiane"><input type="checkbox" value="platki-owsiane">Płatki owsiane <span class="p-num" style="opacity:.55">41</span></label>
<label class="p-chip" data-rank="top" data-label="Chleb"><input type="checkbox" value="chleb">Chleb <span class="p-num" style="opacity:.55">65</span></label>
<label class="p-chip" data-rank="top" data-label="Tortilla"><input type="checkbox" value="tortilla">Tortilla <span class="p-num" style="opacity:.55">10</span></label>
<label class="p-chip" data-rank="top" data-label="Banan"><input type="checkbox" value="banan">Banan <span class="p-num" style="opacity:.55">33</span></label>
<label class="p-chip" data-rank="top" data-label="Jabłko"><input type="checkbox" value="jablko">Jabłko <span class="p-num" style="opacity:.55">19</span></label>
<label class="p-chip" data-rank="top" data-label="Pomidor"><input type="checkbox" value="pomidor">Pomidor <span class="p-num" style="opacity:.55">70</span></label>
<label class="p-chip" data-rank="top" data-label="Ogórek"><input type="checkbox" value="ogorek">Ogórek <span class="p-num" style="opacity:.55">34</span></label>
<label class="p-chip" data-rank="top" data-label="Papryka"><input type="checkbox" value="papryka">Papryka <span class="p-num" style="opacity:.55">36</span></label>
<label class="p-chip" data-rank="top" data-label="Szpinak"><input type="checkbox" value="szpinak">Szpinak <span class="p-num" style="opacity:.55">22</span></label>
<label class="p-chip" data-rank="top" data-label="Cukinia"><input type="checkbox" value="cukinia">Cukinia <span class="p-num" style="opacity:.55">19</span></label>
<label class="p-chip" data-rank="top" data-label="Mozzarella"><input type="checkbox" value="mozzarella">Mozzarella <span class="p-num" style="opacity:.55">22</span></label>
<label class="p-chip" data-rank="top" data-label="Jogurt / skyr"><input type="checkbox" value="jogurt">Jogurt / skyr <span class="p-num" style="opacity:.55">52</span></label>
<label class="p-chip" data-rank="top" data-label="Tofu"><input type="checkbox" value="tofu">Tofu <span class="p-num" style="opacity:.55">15</span></label>
<label class="p-chip" data-rank="top" data-label="Łosoś"><input type="checkbox" value="losos">Łosoś <span class="p-num" style="opacity:.55">15</span></label>
<label class="p-chip" data-rank="top" data-label="Orzechy"><input type="checkbox" value="orzechy">Orzechy <span class="p-num" style="opacity:.55">47</span></label>
<label class="p-chip" data-rank="top" data-label="Masło orzechowe"><input type="checkbox" value="maslo-orzechowe">Masło orzechowe <span class="p-num" style="opacity:.55">23</span></label>
<label class="p-chip" data-rank="rest" data-label="Oliwa / olej" hidden><input type="checkbox" value="oliwa">Oliwa / olej <span class="p-num" style="opacity:.55">118</span></label>
<label class="p-chip" data-rank="rest" data-label="Cebula" hidden><input type="checkbox" value="cebula">Cebula <span class="p-num" style="opacity:.55">66</span></label>
<label class="p-chip" data-rank="rest" data-label="Czosnek" hidden><input type="checkbox" value="czosnek">Czosnek <span class="p-num" style="opacity:.55">60</span></label>
<label class="p-chip" data-rank="rest" data-label="Mleko roślinne" hidden><input type="checkbox" value="mleko">Mleko roślinne <span class="p-num" style="opacity:.55">49</span></label>
<label class="p-chip" data-rank="rest" data-label="Odżywka białkowa" hidden><input type="checkbox" value="odzywka">Odżywka białkowa <span class="p-num" style="opacity:.55">48</span></label>
<label class="p-chip" data-rank="rest" data-label="Cytryna" hidden><input type="checkbox" value="cytryna">Cytryna <span class="p-num" style="opacity:.55">34</span></label>
<label class="p-chip" data-rank="rest" data-label="Marchewka" hidden><input type="checkbox" value="marchewka">Marchewka <span class="p-num" style="opacity:.55">33</span></label>
<label class="p-chip" data-rank="rest" data-label="Sałata / rukola / roszponka" hidden><input type="checkbox" value="salata">Sałata / rukola / roszponka <span class="p-num" style="opacity:.55">31</span></label>
<label class="p-chip" data-rank="rest" data-label="Mąka" hidden><input type="checkbox" value="maka">Mąka <span class="p-num" style="opacity:.55">27</span></label>
<label class="p-chip" data-rank="rest" data-label="Pomidory z puszki / passata" hidden><input type="checkbox" value="pomidory-puszka">Pomidory z puszki / passata <span class="p-num" style="opacity:.55">25</span></label>
<label class="p-chip" data-rank="rest" data-label="Czekolada" hidden><input type="checkbox" value="czekolada">Czekolada <span class="p-num" style="opacity:.55">19</span></label>
<label class="p-chip" data-rank="rest" data-label="Kakao" hidden><input type="checkbox" value="kakao">Kakao <span class="p-num" style="opacity:.55">19</span></label>
<label class="p-chip" data-rank="rest" data-label="Fasola" hidden><input type="checkbox" value="fasola">Fasola <span class="p-num" style="opacity:.55">15</span></label>
<label class="p-chip" data-rank="rest" data-label="Ciecierzyca" hidden><input type="checkbox" value="ciecierzyca">Ciecierzyca <span class="p-num" style="opacity:.55">14</span></label>
<label class="p-chip" data-rank="rest" data-label="Migdały" hidden><input type="checkbox" value="migdaly">Migdały <span class="p-num" style="opacity:.55">14</span></label>
<label class="p-chip" data-rank="rest" data-label="Sos sojowy" hidden><input type="checkbox" value="sos-sojowy">Sos sojowy <span class="p-num" style="opacity:.55">14</span></label>
<label class="p-chip" data-rank="rest" data-label="Awokado" hidden><input type="checkbox" value="awokado">Awokado <span class="p-num" style="opacity:.55">13</span></label>
<label class="p-chip" data-rank="rest" data-label="Bułka" hidden><input type="checkbox" value="bulka">Bułka <span class="p-num" style="opacity:.55">13</span></label>
<label class="p-chip" data-rank="rest" data-label="Soczewica" hidden><input type="checkbox" value="soczewica">Soczewica <span class="p-num" style="opacity:.55">13</span></label>
<label class="p-chip" data-rank="rest" data-label="Rzodkiewka" hidden><input type="checkbox" value="rzodkiewka">Rzodkiewka <span class="p-num" style="opacity:.55">12</span></label>
<label class="p-chip" data-rank="rest" data-label="Seler" hidden><input type="checkbox" value="seler">Seler <span class="p-num" style="opacity:.55">12</span></label>
<label class="p-chip" data-rank="rest" data-label="Twaróg" hidden><input type="checkbox" value="twarog">Twaróg <span class="p-num" style="opacity:.55">12</span></label>
<label class="p-chip" data-rank="rest" data-label="Ziemniaki" hidden><input type="checkbox" value="ziemniaki">Ziemniaki <span class="p-num" style="opacity:.55">12</span></label>
<label class="p-chip" data-rank="rest" data-label="Feta" hidden><input type="checkbox" value="feta">Feta <span class="p-num" style="opacity:.55">11</span></label>
<label class="p-chip" data-rank="rest" data-label="Maliny" hidden><input type="checkbox" value="maliny">Maliny <span class="p-num" style="opacity:.55">11</span></label>
<label class="p-chip" data-rank="rest" data-label="Serek śmietankowy" hidden><input type="checkbox" value="serek-smietankowy">Serek śmietankowy <span class="p-num" style="opacity:.55">11</span></label>
<label class="p-chip" data-rank="rest" data-label="Imbir" hidden><input type="checkbox" value="imbir">Imbir <span class="p-num" style="opacity:.55">10</span></label>
<label class="p-chip" data-rank="rest" data-label="Miód" hidden><input type="checkbox" value="miod">Miód <span class="p-num" style="opacity:.55">10</span></label>
<label class="p-chip" data-rank="rest" data-label="Serek wiejski" hidden><input type="checkbox" value="serek-wiejski">Serek wiejski <span class="p-num" style="opacity:.55">10</span></label>
<label class="p-chip" data-rank="rest" data-label="Syrop klonowy" hidden><input type="checkbox" value="syrop-klonowy">Syrop klonowy <span class="p-num" style="opacity:.55">9</span></label>
<label class="p-chip" data-rank="rest" data-label="Truskawki" hidden><input type="checkbox" value="truskawki">Truskawki <span class="p-num" style="opacity:.55">9</span></label>
<label class="p-chip" data-rank="rest" data-label="Borówki" hidden><input type="checkbox" value="borowki">Borówki <span class="p-num" style="opacity:.55">8</span></label>
<label class="p-chip" data-rank="rest" data-label="Majonez" hidden><input type="checkbox" value="majonez">Majonez <span class="p-num" style="opacity:.55">8</span></label>
<label class="p-chip" data-rank="rest" data-label="Masło / margaryna" hidden><input type="checkbox" value="maslo">Masło / margaryna <span class="p-num" style="opacity:.55">8</span></label>
<label class="p-chip" data-rank="rest" data-label="Pieczarki" hidden><input type="checkbox" value="pieczarki">Pieczarki <span class="p-num" style="opacity:.55">8</span></label>
<label class="p-chip" data-rank="rest" data-label="Por" hidden><input type="checkbox" value="por">Por <span class="p-num" style="opacity:.55">8</span></label>
<label class="p-chip" data-rank="rest" data-label="Wiórki kokosowe" hidden><input type="checkbox" value="wiorki">Wiórki kokosowe <span class="p-num" style="opacity:.55">8</span></label>
<label class="p-chip" data-rank="rest" data-label="Ananas" hidden><input type="checkbox" value="ananas">Ananas <span class="p-num" style="opacity:.55">7</span></label>
<label class="p-chip" data-rank="rest" data-label="Brokuł" hidden><input type="checkbox" value="brokul">Brokuł <span class="p-num" style="opacity:.55">7</span></label>
<label class="p-chip" data-rank="rest" data-label="Gruszka" hidden><input type="checkbox" value="gruszka">Gruszka <span class="p-num" style="opacity:.55">7</span></label>
<label class="p-chip" data-rank="rest" data-label="Kiełki" hidden><input type="checkbox" value="kielki">Kiełki <span class="p-num" style="opacity:.55">7</span></label>
<label class="p-chip" data-rank="rest" data-label="Mango" hidden><input type="checkbox" value="mango">Mango <span class="p-num" style="opacity:.55">7</span></label>
<label class="p-chip" data-rank="rest" data-label="Musztarda" hidden><input type="checkbox" value="musztarda">Musztarda <span class="p-num" style="opacity:.55">7</span></label>
<label class="p-chip" data-rank="rest" data-label="Oliwki" hidden><input type="checkbox" value="oliwki">Oliwki <span class="p-num" style="opacity:.55">7</span></label>
<label class="p-chip" data-rank="rest" data-label="Płatki jaglane" hidden><input type="checkbox" value="platki-jaglane">Płatki jaglane <span class="p-num" style="opacity:.55">7</span></label>
<label class="p-chip" data-rank="rest" data-label="Dynia" hidden><input type="checkbox" value="dynia">Dynia <span class="p-num" style="opacity:.55">6</span></label>
<label class="p-chip" data-rank="rest" data-label="Grana padano" hidden><input type="checkbox" value="grana-padano">Grana padano <span class="p-num" style="opacity:.55">6</span></label>
<label class="p-chip" data-rank="rest" data-label="Kapusta" hidden><input type="checkbox" value="kapusta">Kapusta <span class="p-num" style="opacity:.55">6</span></label>
<label class="p-chip" data-rank="rest" data-label="Pietruszka korzeń" hidden><input type="checkbox" value="pietruszka-korzen">Pietruszka korzeń <span class="p-num" style="opacity:.55">6</span></label>
<label class="p-chip" data-rank="rest" data-label="Płatki drożdżowe" hidden><input type="checkbox" value="platki-drozdzowe">Płatki drożdżowe <span class="p-num" style="opacity:.55">6</span></label>
<label class="p-chip" data-rank="rest" data-label="Słonecznik" hidden><input type="checkbox" value="slonecznik">Słonecznik <span class="p-num" style="opacity:.55">6</span></label>
<label class="p-chip" data-rank="rest" data-label="Baton / przekąska" hidden><input type="checkbox" value="baton">Baton / przekąska <span class="p-num" style="opacity:.55">5</span></label>
<label class="p-chip" data-rank="rest" data-label="Burak" hidden><input type="checkbox" value="burak">Burak <span class="p-num" style="opacity:.55">5</span></label>
<label class="p-chip" data-rank="rest" data-label="Gouda" hidden><input type="checkbox" value="gouda">Gouda <span class="p-num" style="opacity:.55">5</span></label>
<label class="p-chip" data-rank="rest" data-label="Halloumi" hidden><input type="checkbox" value="halloumi">Halloumi <span class="p-num" style="opacity:.55">5</span></label>
<label class="p-chip" data-rank="rest" data-label="Hummus" hidden><input type="checkbox" value="hummus">Hummus <span class="p-num" style="opacity:.55">5</span></label>
<label class="p-chip" data-rank="rest" data-label="Limonka" hidden><input type="checkbox" value="limonka">Limonka <span class="p-num" style="opacity:.55">5</span></label>
<label class="p-chip" data-rank="rest" data-label="Mleczko kokosowe" hidden><input type="checkbox" value="mleczko-kokosowe">Mleczko kokosowe <span class="p-num" style="opacity:.55">5</span></label>
<label class="p-chip" data-rank="rest" data-label="Nasiona chia" hidden><input type="checkbox" value="chia">Nasiona chia <span class="p-num" style="opacity:.55">5</span></label>
<label class="p-chip" data-rank="rest" data-label="Pomarańcza" hidden><input type="checkbox" value="pomarancza">Pomarańcza <span class="p-num" style="opacity:.55">5</span></label>
<label class="p-chip" data-rank="rest" data-label="Pomidory suszone" hidden><input type="checkbox" value="pomidory-suszone">Pomidory suszone <span class="p-num" style="opacity:.55">5</span></label>
<label class="p-chip" data-rank="rest" data-label="Siemię lniane" hidden><input type="checkbox" value="siemie-lniane">Siemię lniane <span class="p-num" style="opacity:.55">5</span></label>
<label class="p-chip" data-rank="rest" data-label="Bagietka" hidden><input type="checkbox" value="bagietka">Bagietka <span class="p-num" style="opacity:.55">4</span></label>
<label class="p-chip" data-rank="rest" data-label="Batat" hidden><input type="checkbox" value="batat">Batat <span class="p-num" style="opacity:.55">4</span></label>
<label class="p-chip" data-rank="rest" data-label="Daktyle" hidden><input type="checkbox" value="daktyle">Daktyle <span class="p-num" style="opacity:.55">4</span></label>
<label class="p-chip" data-rank="rest" data-label="Kasza kuskus" hidden><input type="checkbox" value="kuskus">Kasza kuskus <span class="p-num" style="opacity:.55">4</span></label>
<label class="p-chip" data-rank="rest" data-label="Kukurydza" hidden><input type="checkbox" value="kukurydza">Kukurydza <span class="p-num" style="opacity:.55">4</span></label>
<label class="p-chip" data-rank="rest" data-label="Mandarynka" hidden><input type="checkbox" value="mandarynka">Mandarynka <span class="p-num" style="opacity:.55">4</span></label>
<label class="p-chip" data-rank="rest" data-label="Ogórki kiszone" hidden><input type="checkbox" value="ogorki-kiszone">Ogórki kiszone <span class="p-num" style="opacity:.55">4</span></label>
<label class="p-chip" data-rank="rest" data-label="Papryczka chili" hidden><input type="checkbox" value="papryczka-chili">Papryczka chili <span class="p-num" style="opacity:.55">4</span></label>
<label class="p-chip" data-rank="rest" data-label="Pesto" hidden><input type="checkbox" value="pesto">Pesto <span class="p-num" style="opacity:.55">4</span></label>
<label class="p-chip" data-rank="rest" data-label="Plastry wegańskie" hidden><input type="checkbox" value="plastry-wegan">Plastry wegańskie <span class="p-num" style="opacity:.55">4</span></label>
<label class="p-chip" data-rank="rest" data-label="Płatki inne" hidden><input type="checkbox" value="platki-inne">Płatki inne <span class="p-num" style="opacity:.55">4</span></label>
<label class="p-chip" data-rank="rest" data-label="Smoothie / sok" hidden><input type="checkbox" value="smoothie">Smoothie / sok <span class="p-num" style="opacity:.55">4</span></label>
<label class="p-chip" data-rank="rest" data-label="Syrop z agawy" hidden><input type="checkbox" value="syrop-agawa">Syrop z agawy <span class="p-num" style="opacity:.55">4</span></label>
<label class="p-chip" data-rank="rest" data-label="Wafle ryżowe" hidden><input type="checkbox" value="wafle">Wafle ryżowe <span class="p-num" style="opacity:.55">4</span></label>
<label class="p-chip" data-rank="rest" data-label="Chrzan" hidden><input type="checkbox" value="chrzan">Chrzan <span class="p-num" style="opacity:.55">3</span></label>
<label class="p-chip" data-rank="rest" data-label="Ciasto na naleśniki" hidden><input type="checkbox" value="ciasto-nalesniki">Ciasto na naleśniki <span class="p-num" style="opacity:.55">3</span></label>
<label class="p-chip" data-rank="rest" data-label="Dorsz" hidden><input type="checkbox" value="dorsz">Dorsz <span class="p-num" style="opacity:.55">3</span></label>
<label class="p-chip" data-rank="rest" data-label="Kiwi" hidden><input type="checkbox" value="kiwi">Kiwi <span class="p-num" style="opacity:.55">3</span></label>
<label class="p-chip" data-rank="rest" data-label="Olej kokosowy" hidden><input type="checkbox" value="olej-kokosowy">Olej kokosowy <span class="p-num" style="opacity:.55">3</span></label>
<label class="p-chip" data-rank="rest" data-label="Papryka konserwowa" hidden><input type="checkbox" value="papryka-konserwowa">Papryka konserwowa <span class="p-num" style="opacity:.55">3</span></label>
<label class="p-chip" data-rank="rest" data-label="Sezam" hidden><input type="checkbox" value="sezam">Sezam <span class="p-num" style="opacity:.55">3</span></label>
<label class="p-chip" data-rank="rest" data-label="Sos ostry / rybny" hidden><input type="checkbox" value="sos-ostry">Sos ostry / rybny <span class="p-num" style="opacity:.55">3</span></label>
<label class="p-chip" data-rank="rest" data-label="Wiśnie" hidden><input type="checkbox" value="wisnie">Wiśnie <span class="p-num" style="opacity:.55">3</span></label>
<label class="p-chip" data-rank="rest" data-label="Żurawina" hidden><input type="checkbox" value="zurawina">Żurawina <span class="p-num" style="opacity:.55">3</span></label>
<label class="p-chip" data-rank="rest" data-label="Biszkopty" hidden><input type="checkbox" value="biszkopty">Biszkopty <span class="p-num" style="opacity:.55">2</span></label>
<label class="p-chip" data-rank="rest" data-label="Budyń" hidden><input type="checkbox" value="budyn">Budyń <span class="p-num" style="opacity:.55">2</span></label>
<label class="p-chip" data-rank="rest" data-label="Camembert" hidden><input type="checkbox" value="camembert">Camembert <span class="p-num" style="opacity:.55">2</span></label>
<label class="p-chip" data-rank="rest" data-label="Jagody" hidden><input type="checkbox" value="jagody">Jagody <span class="p-num" style="opacity:.55">2</span></label>
<label class="p-chip" data-rank="rest" data-label="Ketchup" hidden><input type="checkbox" value="ketchup">Ketchup <span class="p-num" style="opacity:.55">2</span></label>
<label class="p-chip" data-rank="rest" data-label="Olej sezamowy" hidden><input type="checkbox" value="olej-sezamowy">Olej sezamowy <span class="p-num" style="opacity:.55">2</span></label>
<label class="p-chip" data-rank="rest" data-label="Parówki roślinne" hidden><input type="checkbox" value="parowki">Parówki roślinne <span class="p-num" style="opacity:.55">2</span></label>
<label class="p-chip" data-rank="rest" data-label="Porzeczki" hidden><input type="checkbox" value="porzeczki">Porzeczki <span class="p-num" style="opacity:.55">2</span></label>
<label class="p-chip" data-rank="rest" data-label="Pstrąg" hidden><input type="checkbox" value="pstrag">Pstrąg <span class="p-num" style="opacity:.55">2</span></label>
<label class="p-chip" data-rank="rest" data-label="Pudding proteinowy" hidden><input type="checkbox" value="pudding">Pudding proteinowy <span class="p-num" style="opacity:.55">2</span></label>
<label class="p-chip" data-rank="rest" data-label="Ser pleśniowy" hidden><input type="checkbox" value="ser-plesniowy">Ser pleśniowy <span class="p-num" style="opacity:.55">2</span></label>
<label class="p-chip" data-rank="rest" data-label="Tahini" hidden><input type="checkbox" value="tahini">Tahini <span class="p-num" style="opacity:.55">2</span></label>
<label class="p-chip" data-rank="rest" data-label="Śmietanka" hidden><input type="checkbox" value="smietanka">Śmietanka <span class="p-num" style="opacity:.55">2</span></label>
<label class="p-chip" data-rank="rest" data-label="Bajgiel" hidden><input type="checkbox" value="bajgiel">Bajgiel <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Bułka tarta" hidden><input type="checkbox" value="bulka-tarta">Bułka tarta <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Bób" hidden><input type="checkbox" value="bob">Bób <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Cheddar" hidden><input type="checkbox" value="cheddar">Cheddar <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Grejpfrut" hidden><input type="checkbox" value="grejpfrut">Grejpfrut <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Groszek" hidden><input type="checkbox" value="groszek">Groszek <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Kabanosy roślinne" hidden><input type="checkbox" value="kabanosy">Kabanosy roślinne <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Kaki" hidden><input type="checkbox" value="kaki">Kaki <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Kaszanka roślinna" hidden><input type="checkbox" value="kaszanka">Kaszanka roślinna <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Kawa" hidden><input type="checkbox" value="kawa">Kawa <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Kiełbaski roślinne" hidden><input type="checkbox" value="kielbaski">Kiełbaski roślinne <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Komosa ryżowa" hidden><input type="checkbox" value="komosa">Komosa ryżowa <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Makrela" hidden><input type="checkbox" value="makrela">Makrela <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Maślanka" hidden><input type="checkbox" value="maslanka">Maślanka <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Melon" hidden><input type="checkbox" value="melon">Melon <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Mintaj" hidden><input type="checkbox" value="mintaj">Mintaj <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Miso" hidden><input type="checkbox" value="miso">Miso <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Mięso wegańskie" hidden><input type="checkbox" value="mieso-wegan">Mięso wegańskie <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Owoce mrożone" hidden><input type="checkbox" value="owoce-mrozone">Owoce mrożone <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Owsianka instant" hidden><input type="checkbox" value="owsianka-instant">Owsianka instant <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Papier ryżowy" hidden><input type="checkbox" value="papier-ryzowy">Papier ryżowy <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Pasta warzywna" hidden><input type="checkbox" value="pasta-warzywna">Pasta warzywna <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Pierożki gyoza" hidden><input type="checkbox" value="gyoza">Pierożki gyoza <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Pistacje" hidden><input type="checkbox" value="pistacje">Pistacje <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Ser żółty" hidden><input type="checkbox" value="ser-zolty">Ser żółty <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Serek proteinowy" hidden><input type="checkbox" value="serek-proteinowy">Serek proteinowy <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Sok" hidden><input type="checkbox" value="sok">Sok <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Zupa gotowa" hidden><input type="checkbox" value="zupa-gotowa">Zupa gotowa <span class="p-num" style="opacity:.55">1</span></label>
</div>
<p class="p-hint" id="ing-hint">Widzisz 20 najczęstszych składników. Pozostałe 127 znajdziesz przez wyszukiwanie.</p>
</div>
</details>
</div>
<div class="p-count"><span id="result-count" class="p-num"></span></div>

<p class="p-empty" id="empty-state" hidden>Żaden przepis nie pasuje do tego wyboru. Odznacz część składników albo wróć do wszystkich pór dnia.</p>

<ul class="p-cards" id="recipes">
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="jablko mleczko-kokosowe mleko odzywka ryz">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/klejacy-ryz/">Klejący ryż z prażonym jabłkiem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">464 kcal</span>
</div>
<div class="p-card__tags">ryżu basmati, mleka roślinnego, jabłka, wegańskiej odżywki białkowej…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="cebula chleb jajka oliwa pieczarki rzodkiewka szpinak">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/jajecznica/">Jajecznica z pieczarkami, cebulą i pieczywem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">470 kcal</span>
</div>
<div class="p-card__tags">jajek kurzych, pieczarek, cebuli, szpinaku, rzodkiewki, oleju rzepakowego…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="grana-padano makaron mozzarella ogorek pesto pomidor szpinak">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/makaron-mozzarella/">Makaron z mozzarellą, szpinakiem, ogórkiem i pomidorkami koktajlowymi</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">381 kcal</span>
</div>
<div class="p-card__tags">makaronu pełnoziarnistego, zielonego pesto, pomidorków koktajlowych…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="daktyle kakao orzechy wiorki">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/kulki-mocy/">Daktylowo-kakaowe kulki mocy z orzechami</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">466 kcal</span>
</div>
<div class="p-card__tags">daktyli, orzechów włoskich, kakao, wiórków kokosowych</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="banan odzywka orzechy platki-owsiane">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/owsianka/">Owsianka</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">468 kcal</span>
</div>
<div class="p-card__tags">płatków owsianych, małego banana, orzechów nerkowca, odżywki białkowej</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="bulka orzechy papryka serek-wiejski">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/serek-wiejski-grahamka/">Serek wiejski, papryka, grahamka i orzechy</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">514 kcal</span>
</div>
<div class="p-card__tags">serka wiejskiego, papryki żółtej, bułki grahamki, orzechów włoskich</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="cebula czosnek makaron marchewka mozzarella oliwa papryka pomidory-puszka seler">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/krem-paprykowo-pomidorowy/">Krem paprykowo-pomidorowy</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">385 kcal</span>
</div>
<div class="p-card__tags">pomidorów w puszce, makaronu razowego, oliwy z oliwek, mozzarelli…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="chleb pomidor serek-smietankowy slonecznik">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/kanapki-z-serkiem/">Kanapki z serkiem śmietankowym, pomidorem i szczypiorkiem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">439 kcal</span>
</div>
<div class="p-card__tags">chleba żytniego razowego, serka kanapkowego, pomidor, nasion słonecznika</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="banan jajka maka maslo-orzechowe odzywka orzechy syrop-agawa">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/placuszki-owsiane/">Placuszki owsiane orzechowe</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">482 kcal</span>
</div>
<div class="p-card__tags">małego banana, jaja kurzego, mąki owsianej pełnoziarnistej…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="chleb gouda maslo pomidor salata">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/kanapki-z-serem/">Kanapki z żółtym serem, roszponką i pomidorem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">462 kcal</span>
</div>
<div class="p-card__tags">chleba żytniego razowego, sera gouda, roszponki, pomidora, margaryny</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="gyoza mandarynka">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/gyoza/">Pierożki gyoza z warzywami chef select z kimchi</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">358 kcal</span>
</div>
<div class="p-card__tags">Pierożków gyoza z warzywami chef select, mandarynki</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="banan chia maslo-orzechowe mleko">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/koktajl-bananowy/">Koktajl bananowo-orzechowy</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">468 kcal</span>
</div>
<div class="p-card__tags">banana, napoju sojowego, masła orzechowego, nasion chia</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="gruszka mleko odzywka orzechy platki-jaglane">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/jaglanka-gruszka/">Jaglanka na mleku roślinnym z gruszką</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">457 kcal</span>
</div>
<div class="p-card__tags">płatków jaglanych, mleka roślinnego, gruszki, odżywki białkowej…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="chleb mozzarella ogorek pasta-warzywna">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/kanapki-z-pasta-warzywna/">Kanapki z pastą warzywną, serem mozzarellą i ogórkiem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">484 kcal</span>
</div>
<div class="p-card__tags">chleba żytniego razowego, pasty warzywnej, mozzarelli, ogórka</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="brokul cebula czosnek kasza oliwa szpinak tofu">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/kasza-z-tofu/">Kasza z tofu</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">372 kcal</span>
</div>
<div class="p-card__tags">kaszy gryczanej, tofu naturalnego, brokuła, cebuli, szpinaku, czosnku…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="baton mandarynka orzechy smoothie">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/smoothie-strawberry/">Smoothie strawberry and friends Solevita i batonik protein bar</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">462 kcal</span>
</div>
<div class="p-card__tags">Protein Bar cookies and cream fllavoured crisps…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="gruszka miod orzechy serek-wiejski wafle">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/serek-wiejski-z-miodem/">Serek wiejski z miodem, orzechami i gruszką</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">467 kcal</span>
</div>
<div class="p-card__tags">serka wiejskiego, miodu, orzechów włoskich, gruszki, wafli ryżowych</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="chleb ciecierzyca cytryna czosnek kielki marchewka ogorek oliwa">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/kanapka-z-pasta-z-ciecierzycy/">Kanapka z pastą z ciecierzycy</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">465 kcal</span>
</div>
<div class="p-card__tags">ciecierzycy konserwowej, czosnku, oliwy, soku z cytryny, chleba żytniego…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="cebula czosnek makaron marchewka pomidory-puszka sos-sojowy tofu">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/spaghetti-bolognese/">Wegańskie spaghetti bolognese</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">385 kcal</span>
</div>
<div class="p-card__tags">tofu naturalnego, makaronu spaghetti pełnoziarnistego, marchewki, cebuli…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="cebula chleb cytryna feta ogorek oliwa oliwki papryka pomidor salata">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/salatka-grecka/">Sałatka grecka z serem sałatkowym i pieczywem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">464 kcal</span>
</div>
<div class="p-card__tags">miksu sałat, sera feta, oliwek zielonych, papryki żółtej, cebuli…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="jablko jogurt kaki orzechy platki-owsiane">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/bowl-sniadaniowy/">Bowl śniadaniowy z jabłkiem i kaki</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">449 kcal</span>
</div>
<div class="p-card__tags">płatków owsianych górskich, mieszanki orzechów, małego jabłka, kaki…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="awokado chleb jajka salata">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/tosty-awokado/">Tosty z jajkiem sadzonym i awokado</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">469 kcal</span>
</div>
<div class="p-card__tags">chleba tostowego pełnoziarnistego, awokado, jajka, rukoli</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="ciecierzyca cytryna dynia marchewka mleczko-kokosowe ziemniaki">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/zupa-z-dyni/">Zupa z dyni z pieczoną ciecierzycą - przepis na 3 porcje</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">404 kcal</span>
</div>
<div class="p-card__tags">dyni, mleczka kokosowego, ciecierzycy konserwowej, soku z cytryny, marchwi…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="jogurt owsianka-instant smoothie">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/owsianka-malinowa/">Owsianka malinowa Crownfield</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">475 kcal</span>
</div>
<div class="p-card__tags">owsianki malinowej Crownfield, jogurtu skyr, Smoothie strawberry Solevita</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="banan marchewka mleko odzywka orzechy platki-owsiane">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/owsianka-z-marchewka/">Owsianka z marchewką</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">453 kcal</span>
</div>
<div class="p-card__tags">napoju roślinnego, płatków owsianych górskich, marchewki, małego banana…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="bulka majonez ogorki-kiszone pomidor serek-smietankowy tofu">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/kanapka-z-tofu-twarozkiem/">Kanapka z tofu twarożkiem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">457 kcal</span>
</div>
<div class="p-card__tags">bułki grahamki, serka śmietankowego, majonezu wegańskiego…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="bulka kaszanka">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/roslinna-kaszanka/">Roślinna kaszanka Dobra Kaloria z pieczywem i warzywami</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">388 kcal</span>
</div>
<div class="p-card__tags">Roślinna kaszanka na grilla i na patelnię Dobra Kaloria, bułki</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="bagietka cebula czosnek grana-padano oliwa pomidor">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/bruschetta/">Bruschetta z pomidorami, świeżymi ziołami i serem grana padano</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">480 kcal</span>
</div>
<div class="p-card__tags">bagietki, pomidora, małej cebuli czerwonej, czosnku, sera grana padano…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="jajka jogurt kakao maka twarog">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/omlet-mleczna-kanapka/">Omlet mleczna kanapka</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">454 kcal</span>
</div>
<div class="p-card__tags">jajko, mąki pszennej pełnoziarnistej, kakao, jogurtu naturalnego…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="hummus pomidor smoothie wafle">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/hummus-spicy-salsa/">Hummus spicy salsa z waflami ryżowymi</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">458 kcal</span>
</div>
<div class="p-card__tags">hummusu spicy salsa, wafli ryżowych, pomidorków koktajlowych…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="czosnek mozzarella oliwa pomidory-puszka szpinak ziemniaki">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/zapiekanka-ziemniaczana/">Zapiekanka ziemniaczana z mozzarellą</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">373 kcal</span>
</div>
<div class="p-card__tags">ziemniaków, szpinaku, passaty pomidorowej, czosnku, oliwy z oliwek…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="gruszka jogurt maslo-orzechowe oliwa ryz">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/ryzowy-pudding/">Ryżowy pudding z prażonymi gruszkami</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">472 kcal</span>
</div>
<div class="p-card__tags">ryżu basmati, jogurtu skyr, gruszki, oleju rzepakowego, masła orzechowego</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="czekolada daktyle jogurt kasza maslo-orzechowe mleko odzywka orzechy syrop-agawa">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/jaglany-snickers/">Jaglany snickers</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">466 kcal</span>
</div>
<div class="p-card__tags">gorzkiej czekolady, kaszy jaglanej, jogurtu roślinnego, napoju sojowego…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="chleb maslo ogorek pstrag rzodkiewka salata twarog">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/pasta-z-pstroga/">Pasta z wędzonego pstrąga i twarogu ze szczypiorkiem, warzywami i pieczywem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">446 kcal</span>
</div>
<div class="p-card__tags">chleba żytniego razowego, twarogu tłustego, pstrąga wędzonego…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="baton zupa-gotowa">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/zupa-krem-z-pomidorow/">Zupa krem z pomidorów z bazylią Chef select</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">370 kcal</span>
</div>
<div class="p-card__tags">Zupy krem z pomidorów z bazylią Chef select, batona Raw Alesto kakao…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="ananas cytryna kukurydza majonez odzywka ogorek ryz seler">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/ryzowa-salatka-z-ananasem/">Ryżowa sałatka z ananasem, ogórkiem, selerem i kukurydzą + shake białkowy</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">458 kcal</span>
</div>
<div class="p-card__tags">ryżu basmati, kukurydzy konserwowej, ananasa świeżego, małego ogórka…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="banan chleb maslo-orzechowe odzywka">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/tost-z-maslem-orzechowym/">Tost z chlebem żytnim, masłem orzechowym i bananem + shake białkowy</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">491 kcal</span>
</div>
<div class="p-card__tags">chleba żytniego, masła orzechowego, banana, odżywki białkowej</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="kabanosy pomidor">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/roslinne-kabanosy/">Roślinne kabanosy Bez kęsa mięsa Tarczyński z pieczywem i warzywami</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">475 kcal</span>
</div>
<div class="p-card__tags">Roślinne kabanosy Bez kęsa mięsa Tarczyński, pomidora</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="brokul cebula czosnek grana-padano makaron oliwa pieczarki pomidor smietanka szpinak">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/makaron-penne/">Makaron penne ze szpinakiem, pieczarkami, pomidorkami cherry i serem grana padano</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">360 kcal</span>
</div>
<div class="p-card__tags">makaronu penne, szpinaku, śmietanki 12%, czosnku, cebuli, pieczarek…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="chleb czosnek pomidory-suszone soczewica tahini">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/kanapka-z-pasta-pomidorowa/">Kanapka z pastą pomidorową</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">443 kcal</span>
</div>
<div class="p-card__tags">soczewicy czerwonej, chleba żytniego razowego, pasty tahini…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="banan czekolada jogurt maslo-orzechowe platki-owsiane">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/owsianka-brownie-z-mikrofali/">Owsianka brownie z mikrofali</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">491 kcal</span>
</div>
<div class="p-card__tags">Płatki owsiane górskie, Banan, Czekolada gorzka 70%, Masło orzechowe…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="chleb ciecierzyca majonez musztarda odzywka pomidor">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/kanapki-z-pasta-bezjajeczna-z-ciecierzycy/">Kanapki z pastą bezjajeczną z ciecierzycy + shake</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">397 kcal</span>
</div>
<div class="p-card__tags">Ciecierzyca konserwowa, Majonez wegański, Musztarda, Chleb żytni razowy…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="ananas awokado cebula czosnek imbir komosa limonka losos ogorek sezam sos-sojowy syrop-agawa">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/bowl-z-lososiem-teriyaki/">Bowl z łososiem teriyaki</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">596 kcal</span>
</div>
<div class="p-card__tags">Łosoś świeży, Sos sojowy, Sok z limonki, Imbir, Czosnek, Limonka…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="banan orzechy">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/banan-orzechy-wloskie/">Banan + orzechy włoskie</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">216 kcal</span>
</div>
<div class="p-card__tags">Banan, Orzechy włoskie</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="czekolada jogurt mango maslo-orzechowe mleko platki-inne platki-owsiane">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/owsianka-w-stylu-kinder-country/">Owsianka w stylu kinder country</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">478 kcal</span>
</div>
<div class="p-card__tags">Płatki owsiane górskie, Mango świeże lub mrożone…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="ananas cytryna fasola jogurt kukurydza makaron papryczka-chili papryka por">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/salatka-meksykanska/">Sałatka meksykańska</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">415 kcal</span>
</div>
<div class="p-card__tags">Fasola czerwona konserwowa, Ananas świeży, Makaron pełnoziarnisty…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="batat cebula czosnek fasola odzywka oliwa papryka pomidory-puszka tortilla">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/tortille-z-batatami-i-fasola/">Tortille z batatami i fasolą</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">615 kcal</span>
</div>
<div class="p-card__tags">Fasola czerwona konserwowa, Batat, Cebula, Czosnek, Pomidory z puszki…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="baton borowki">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/baton-wysokobialkowy-smak-karmelowy-go-active/">Baton wysokobiałkowy smak karmelowy Go Active</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">213 kcal</span>
</div>
<div class="p-card__tags">Baton wysokobiałkowy smak karmelowy Go Active, Borówki amerykańskie</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="jogurt orzechy ryz syrop-klonowy truskawki">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/ryz-z-jogurtem-i-owocami/">Ryż z jogurtem i owocami</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">501 kcal</span>
</div>
<div class="p-card__tags">Ryż basmati, Jogurt skyr bez laktozy, Syrop klonowy, Truskawki…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="chleb cukinia jajka">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/jajecznica-z-cukinia/">Jajecznica z cukinią</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">391 kcal</span>
</div>
<div class="p-card__tags">Jajko kurze całe, Cukinia, Chleb żytni razowy</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="cebula cukinia czosnek fasola marchewka oliwa pomidory-puszka szpinak ziemniaki">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/zupa-srodziemnomorska/">Zupa śródziemnomorska</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">586 kcal</span>
</div>
<div class="p-card__tags">Cebula, Ziemniaki, Cukinia, Fasola biała konserwowa, Passata pomidorowa…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="pudding truskawki">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/pudding-proteinowy-wanilia-beza-valio/">Pudding proteinowy wanilia beza Valio</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">194 kcal</span>
</div>
<div class="p-card__tags">Pudding proteinowy o smaku wanilia - beza Valio, Truskawki, świeże lub mrożone</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="banan jajka kakao maka truskawki wiorki">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/omlet-na-slodko-z-bananem/">Omlet na słodko z bananem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">504 kcal</span>
</div>
<div class="p-card__tags">Jajko kurze całe, Mąka pszenna pełnoziarnista, Wiórki kokosowe, Kakao 16%…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="chleb jajka maslo ogorek pomidor">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/kanapki-z-jajkiem-na-miekko/">Kanapki z jajkiem na miękko</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">412 kcal</span>
</div>
<div class="p-card__tags">Jajko kurze całe, Chleb żytni razowy, Masło extra, Pomidor, Ogórek</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="cebula cytryna czosnek feta groszek makaron oliwa orzechy por">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/zielony-makaron-z-groszkiem/">Zielony makaron z groszkiem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">598 kcal</span>
</div>
<div class="p-card__tags">Groszek mrożony, Makaron pełnoziarnisty, Ser typu Feta, Por, Cebula…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="banan miod sok szpinak">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/szpinakowy-koktajl-z-bananem/">Szpinakowy koktajl z bananem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">204 kcal</span>
</div>
<div class="p-card__tags">Sok jabłkowy, Banan, Szpinak, Miód</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="jablko jogurt maka mleko oliwa platki-owsiane">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/racuszki-jablkowo-owsiane/">Racuszki jabłkowo-owsiane</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">504 kcal</span>
</div>
<div class="p-card__tags">Jabłko, Mąka pszenna pełnoziarnista, Płatki owsiane górskie…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="hummus kuskus marchewka papryka seler">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/buddha-bowl-z-hummusem-i-kasza/">Buddha bowl z hummusem i kaszą kuskus</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">401 kcal</span>
</div>
<div class="p-card__tags">Hummus, Papryka czerwona, Marchew, Kasza kuskus, Seler naciowy</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="cukinia czosnek losos makaron mleczko-kokosowe oliwa pomidor">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/makaron-z-lososiem-w-delikatnym-sosie/">Makaron z łososiem w delikatnym sosie kokosowym</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">615 kcal</span>
</div>
<div class="p-card__tags">Łosoś wędzony, Makaron pełnoziarnisty, Cukinia, Czosnek…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="orzechy">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/orzechy-wloskie/">Orzechy włoskie</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">200 kcal</span>
</div>
<div class="p-card__tags">Orzechy włoskie</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="chia kiwi mleko odzywka orzechy platki-owsiane pomarancza">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/chia-bowl-z-kiwi-i-pomarancza/">Chia bowl z kiwi i pomarańczą</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">517 kcal</span>
</div>
<div class="p-card__tags">Mleko roślinne niesłodzone, Kiwi, Pomarańcza, Nasiona chia…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="chleb gruszka odzywka oliwa ser-plesniowy">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/grzanki-z-gruszka-i-serem-z/">Grzanki z gruszką i serem z niebieską pleśnią</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">404 kcal</span>
</div>
<div class="p-card__tags">Chleb żytni razowy, Ser z niebieską pleśnią, Lazur, Gruszka…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="cebula czosnek fasola marchewka mleko oliwa pieczarki pietruszka-korzen ziemniaki">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/zupa-z-bialej-fasoli-ziemniakow-i/">Zupa z białej fasoli, ziemniaków i pieczarek</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">603 kcal</span>
</div>
<div class="p-card__tags">Ziemniaki, Fasola biała konserwowa, Olej rzepakowy, Cebula, Czosnek…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="banan pomarancza szpinak">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/smoothie-pomarancza-banan-szpinak/">Smoothie pomarańcza banan szpinak</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">184 kcal</span>
</div>
<div class="p-card__tags">Pomarańcza, Szpinak, Banan</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="chleb jablko maslo-orzechowe twarog">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/kanapki-na-slodko-z-maslem-orzechowym/">Kanapki na słodko z masłem orzechowym, twarogiem i jabłkiem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">497 kcal</span>
</div>
<div class="p-card__tags">Chleb żytni razowy, Masło orzechowe, Ser twarogowy półtłusty, Jabłko</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="cebula gouda jajka papryka tortilla">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/zapiekana-tortilla/">Zapiekana tortilla</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">413 kcal</span>
</div>
<div class="p-card__tags">Tortilla pszenna, Jajko kurze całe, Cebula czerwona, Papryka czerwona…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="cebula czosnek oliwa platki-drozdzowe pomidory-puszka ryz siemie-lniane soczewica sos-sojowy">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/pulpeciki-z-soczewicy-w-sosie-pomidorowym/">Pulpeciki z soczewicy w sosie pomidorowym z ryżem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">612 kcal</span>
</div>
<div class="p-card__tags">Ryż basmati, Soczewica zielona, Passata pomidorowa, Cebula, Czosnek…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="maslanka">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/maslanka/">Maślanka</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">180 kcal</span>
</div>
<div class="p-card__tags">Maślanka 1.5%</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="banan mleko odzywka orzechy platki-owsiane porzeczki">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/orzechowa-owsianka-z-bananem-i-dzemem/">Orzechowa owsianka z bananem i dżemem porzeczkowym</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">470 kcal</span>
</div>
<div class="p-card__tags">płatków owsianych, mleka roślinnego, orzechów, banana, dżemu porzeczkowego…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="cebula chleb ogorki-kiszone oliwa tofu">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/kanapki-z-pasta-tofu/">Kanapki z pastą tofu</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">446 kcal</span>
</div>
<div class="p-card__tags">tofu wędzonego, cebuli, ogórków kiszonych, soku z ogórków kiszonych…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="cytryna kapusta mintaj ogorek oliwa papryka ryz">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/ryba-na-parze-z-ryzem-i/">Ryba na parze z ryżem i surówką z kapusty pekińskiej</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">369 kcal</span>
</div>
<div class="p-card__tags">świeżego mintaja, ryżu, kapusty pekińskiej, papryki czerwonej, ogórka…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="banan czekolada fasola kakao maka mango mleko odzywka oliwa siemie-lniane">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/brownie-z-fasoli-z-bananem-i/">Brownie z fasoli z bananem i mango</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">462 kcal</span>
</div>
<div class="p-card__tags">czerwonej fasoli konserwowej, mąki pszennej pełnoziarnistej, kakao…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="banan jogurt kakao orzechy">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/fit-monte/">Fit Monte</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">477 kcal</span>
</div>
<div class="p-card__tags">orzechów laskowych, jogurtu skyr, kakao, banana</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="cebula chleb czosnek oliwa pomidory-puszka seler soczewica">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/weganska-pasta-z-czerwonej-soczewicy/">Wegańska pasta z czerwonej soczewicy</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">451 kcal</span>
</div>
<div class="p-card__tags">czerwonej soczewicy, cebuli, czosnku, selera, pomidorów z puszki…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="cebula czosnek fasola limonka marchewka oliwa papryka pomidory-puszka ryz">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/gotowana-czerwona-fasola-po-meksykansku/">Gotowana czerwona fasola po meksykańsku</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">382 kcal</span>
</div>
<div class="p-card__tags">ryżu brązowego, fasoli czerwonej konserwowej, marchewki, cebuli, czosnku…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="cebula chleb ogorek oliwa papryka platki-drozdzowe pomidor rzodkiewka salata tofu">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/tofucznica-z-warzywami-i-pieczywem/">Tofucznica z warzywami i pieczywem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">468 kcal</span>
</div>
<div class="p-card__tags">tofu naturalnego, płatków drożdżowych, małej cebuli, papryki czerwonej…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="banan jogurt orzechy">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/skyr-orzechy-banan/">Skyr + orzechy + banan</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">474 kcal</span>
</div>
<div class="p-card__tags">jogurtu skyr, banana, orzechów włoskich</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="chleb jajka oliwa pomidor">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/jajecznica-z-pieczywem/">Jajecznica z pieczywem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">438 kcal</span>
</div>
<div class="p-card__tags">jajek kurzych, oliwy z oliwek, chleba żytniego razowego…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="cebula fasola kasza oliwa papryka-konserwowa pomidory-puszka">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/fasola-z-papryka-i-pomidorami-z/">Fasola z papryką i pomidorami z kaszą jęczmienną</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">372 kcal</span>
</div>
<div class="p-card__tags">fasoli białej konserwowej, papryki pieczona w zalewie…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="banan limonka mango mleko odzywka wiorki">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/smoothie-z-mango-i-banana-na/">Smoothie z mango i banana na mleku roślinnym</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">461 kcal</span>
</div>
<div class="p-card__tags">mango, małego banana, napoju migdałowego, soku z limonki…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="gruszka migdaly mleko odzywka platki-owsiane">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/owsianka-z-gruszka/">Owsianka z gruszką</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">468 kcal</span>
</div>
<div class="p-card__tags">płatków owsianych, mleka roślinnego, małej gruszki, migdałów…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="awokado chleb cytryna kielki losos rzodkiewka">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/tost-z-awokado-i-lososiem/">Tost z awokado i łososiem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">470 kcal</span>
</div>
<div class="p-card__tags">chleba żytniego razowego, awokado, łososia wędzonego, rzodkiewki…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="cebula cukinia czosnek maka marchewka mleko oliwa pomidory-puszka seler soczewica">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/cukinia-zapiekana-z-sosem-pomidorowym-soczewica/">Cukinia zapiekana z sosem pomidorowym, soczewicą i beszamelem na mleku roślinnym</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">367 kcal</span>
</div>
<div class="p-card__tags">soczewicy czerwonej, cebuli, selera naciowego, marchwi, pomidorów z puszki…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="daktyle kakao odzywka orzechy">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/kakaowo-orzechowe-trufle-z-daktyli/">Kakaowo-orzechowe trufle z daktyli</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">463 kcal</span>
</div>
<div class="p-card__tags">daktyli świeżych, kakao, orzechów, wegańskiej odżywki białkowej</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="jagody maslo-orzechowe platki-owsiane serek-wiejski">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/serek-wiejski-na-slodko-z-maslem/">Serek wiejski na słodko z masłem orzechowym, domową konfiturą jagodową i płatkami owsianymi</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">460 kcal</span>
</div>
<div class="p-card__tags">serka wiejskiego, masła orzechowego, dżemu niskosłodzonego np. jagodowego…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="cebula mozzarella oliwa pomidor salata tortilla">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/wrap-z-mozzarella/">Wrap z mozzarellą</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">462 kcal</span>
</div>
<div class="p-card__tags">tortilli pełnoziarnistej, sera mozzarella, rukoli, cebuli czerwonej…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="bulka cytryna losos majonez salata sezam sos-ostry">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/burger-z-lososia/">Burger z łososia</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">362 kcal</span>
</div>
<div class="p-card__tags">łososia, bułki, sezamu, soku z cytryny, majonezu, sosu sriracha, rukoli</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="banan czekolada jajka jogurt maslo-orzechowe olej-kokosowy platki-owsiane">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/pancakes/">Pancakes</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">473 kcal</span>
</div>
<div class="p-card__tags">małego banana, jajka, płatków owsianych, masła orzechowego…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="jablko jajka maka oliwa twarog">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/placuszki-twarogowe-z-jablkiem/">Placuszki twarogowe z jabłkiem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">447 kcal</span>
</div>
<div class="p-card__tags">sera twarogowego chudego, małego jabłka, jajek kurzych, mąki orkiszowej…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="chleb mozzarella papryka-konserwowa">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/sniadania-z-biedronki-tosty/">Śniadania z Biedronki: Tosty</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">477 kcal</span>
</div>
<div class="p-card__tags">chleba tostowego, sera mozzarella light, papryki konserwowej</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="brokul cebula czosnek imbir marchewka oliwa ryz sos-sojowy tahini tofu">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/smazony-ryz-z-brokulami-i-tofu/">Smażony ryż z brokułami i tofu</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">367 kcal</span>
</div>
<div class="p-card__tags">ryżu basmati, tofu naturalnego, sosu sojowego, brokuła, marchewki…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="jablko maka mleko odzywka oliwa">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/weganskie-nalesniki-z-jablkami/">Wegańskie naleśniki z jabłkami</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">458 kcal</span>
</div>
<div class="p-card__tags">napoju roślinnego, mąki pszennej pełnoziarnistej, oleju rzepakowego…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="banan kakao maka mleko odzywka oliwa orzechy">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/chlebek-bananowy-z-kakao-i-orzechami/">Chlebek bananowy z kakao i orzechami</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">443 kcal</span>
</div>
<div class="p-card__tags">małego banana, mąki pszennej pełnoziarnistej, mleka roślinnego…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="chleb jajka jogurt makrela">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/kanapka-z-pasta-z-makreli-i/">Kanapka z pastą z makreli i jajek</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">439 kcal</span>
</div>
<div class="p-card__tags">makreli wędzonej, jajka, jogurtu naturalnego, chleba żytniego</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="cebula cukinia kasza oliwa pomidor tofu">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/kasza-jaglana-z-cukinia-i-pomidorami/">Kasza jaglana z cukinią i pomidorami</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">366 kcal</span>
</div>
<div class="p-card__tags">kaszy jaglanej, cukinii, pomidora, cebuli, oliwy z oliwek, tofu naturalnego</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="bulka camembert gruszka mandarynka pomidor salata">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/kanapki-z-gruszka-i-serem-camembert/">Kanapki z gruszką i serem camembert</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">474 kcal</span>
</div>
<div class="p-card__tags">gruszki, sera camembert, rukoli, pomidorków koktajlowych, bułki grahamki…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="jablko mleko odzywka orzechy platki-jaglane">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/krem-jaglany-z-jablkiem-i-orzechami/">Krem jaglany z jabłkiem i orzechami</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">467 kcal</span>
</div>
<div class="p-card__tags">mleka roślinnego, płatków jaglanych, jabłek, orzechów, odżywki białkowej</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="bulka ketchup parowki pomidor">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/roslinne-parowki-bez-kesa-miesa-tarczynski/">Roślinne parówki Bez kęsa mięsa Tarczyński z pieczywem i warzywami</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">472 kcal</span>
</div>
<div class="p-card__tags">Roślinnych parówek Bez kęsa mięsa Tarczyński, bułki…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="batat cebula czosnek fasola jogurt mango oliwa pomidor">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/bataty-z-burgerem-z-czerwonej-fasoli/">Bataty z burgerem z czerwonej fasoli i sosem salsa</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">382 kcal</span>
</div>
<div class="p-card__tags">czerwonej fasoli konserwowej, batata (0,5 średniej wielkości), cebuli…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="mango mleko odzywka platki-owsiane wiorki">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/owsianka-z-mango/">Owsianka z mango</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">472 kcal</span>
</div>
<div class="p-card__tags">płatków owsianych, mango, wiórków kokosowych, napoju migdałowego…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="chia maslo-orzechowe mleko odzywka platki-owsiane">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/owsiany-batonik-z-maslem-orzechowym/">Owsiany batonik z masłem orzechowym</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">477 kcal</span>
</div>
<div class="p-card__tags">płatków owsianych górskich, masła orzechowego…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="bagietka cebula czosnek mozzarella oliwa pomidor">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/bruschetta-2/">Bruschetta</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">460 kcal</span>
</div>
<div class="p-card__tags">bagietki, pomidora, cebuli, czosnku, oliwy z oliwek, sera mozzarella w kulkach</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="cebula cytryna czosnek imbir marchewka mleczko-kokosowe oliwa papryczka-chili pomidory-puszka ryz soczewica">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/curry-z-soczewicy-przepis-na-2/">Curry z soczewicy - przepis na 2 porcje</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">377 kcal</span>
</div>
<div class="p-card__tags">oliwy z oliwek, ryżu basmati, małej cebuli, czosnku, imbiru, marchewki…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="jablko kasza mleko odzywka orzechy">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/budyn-jaglany/">Budyń jaglany</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">438 kcal</span>
</div>
<div class="p-card__tags">kaszy jaglanej, małego jabłka, napoju sojowego, orzechów włoskich…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="kakao mleko odzywka orzechy platki-owsiane">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/kakaowa-owsianka-z-siekanymi-orzechami/">Kakaowa owsianka z siekanymi orzechami</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">450 kcal</span>
</div>
<div class="p-card__tags">płatków owsianych górskich, napoju sojowego, kakao…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="chleb czosnek jajka pomidor szpinak">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/omlet-ze-szpinakiem/">Omlet ze szpinakiem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">439 kcal</span>
</div>
<div class="p-card__tags">szpinaku, jajek kurzych, czosnku, pomidorków koktajlowych…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="cebula czosnek makaron oliwa pomidory-puszka seler slonecznik soczewica">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/makaron-penne-z-sosem-bolonskim-z/">Makaron penne z sosem bolońskim z soczewicy</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">378 kcal</span>
</div>
<div class="p-card__tags">soczewicy zielonej, selera naciowego, czosnku, małej cebuli…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="jogurt orzechy platki-owsiane syrop-agawa zurawina">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/jogurt-naturalny-z-domowa-granola-orzechami/">Jogurt naturalny z domową granolą, orzechami i żurawiną</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">467 kcal</span>
</div>
<div class="p-card__tags">płatków owsianych górskich, syropu z agawy, żurawiny suszonej…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="bulka gouda maliny pomidor salata serek-smietankowy smoothie">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/lunchbox-kanapki-z-serem-gouda-i/">Lunchbox Kanapki z serem gouda i warzywami + jogurt + owoc</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">615 kcal</span>
</div>
<div class="p-card__tags">Bułka owsiana, Pomidor, Rukola, Ser gouda, Serek śmietankowy bez laktozy…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="halloumi ogorek oliwki papryka pomidor salata tortilla">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/tortilla-z-salatka-po-grecku-i/">Tortilla z sałatką po grecku i serem halloumi</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">509 kcal</span>
</div>
<div class="p-card__tags">Ser halloumi, Ogórek świeży, Papryka czerwona, Pomidor, Oliwki zielone…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="bulka losos oliwa papryka pomidor">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/bulka-owsiana-z-lososiem-i-warzywami/">Bułka owsiana z łososiem i warzywami</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">615 kcal</span>
</div>
<div class="p-card__tags">Bułka owsiana, Pomidor, Papryka czerwona, Łosoś wędzony, Oliwa z oliwek</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="cytryna halloumi kuskus ogorek oliwa oliwki papryka pomidor salata">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/salatka-z-serem-halloumi-kuskusem-pomidorem/">Sałatka z serem halloumi, kuskusem, pomidorem oraz ogórkiem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">595 kcal</span>
</div>
<div class="p-card__tags">Kasza kuskus, Oliwki zielone, Papryka czerwona, Pomidor, Ogórek świeży…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="ciasto-nalesniki jogurt maliny twarog">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/nalesniki-z-serem-twarogowym-bez-laktozy/">Naleśniki z serem twarogowym bez laktozy oraz malinami</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">514 kcal</span>
</div>
<div class="p-card__tags">Ciasto do naleśników low fodmap, Ser twarogowy półtłusty bez laktozy…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="chleb feta ogorek papryka pomidor">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/kanapki-w-greckim-stylu/">Kanapki w greckim stylu</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">598 kcal</span>
</div>
<div class="p-card__tags">Chleb bezglutenowy, Ser typu Feta, Ogórek świeży, Pomidorki koktajlowe…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="chleb gouda papryka pesto">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/kanapki-z-zielonym-pesto-serem-gouda/">Kanapki z zielonym pesto, serem gouda i papryką czerwoną</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">577 kcal</span>
</div>
<div class="p-card__tags">Chleb bezglutenowy, Pesto zielone, Ser gouda, Papryka czerwona</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="dynia feta kasza oliwa szpinak">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/kasza-jaglana-z-dynia-i-serem/">Kasza jaglana z dynią i serem typu feta</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">469 kcal</span>
</div>
<div class="p-card__tags">Dynia świeża lub mrożona, Ser typu Feta, Kasza jaglana, Oliwa z oliwek…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="chleb jajka majonez oliwa papryka pomidor salata">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/jajka-w-koszulkach-z-chlebem-bezglutenowym/">Jajka w koszulkach z chlebem bezglutenowym</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">618 kcal</span>
</div>
<div class="p-card__tags">Jajko kurze całe, Chleb bezglutenowy, Miks sałat, Papryka czerwona…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="chrzan losos ogorek szpinak tortilla">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/tortilla-z-lososiem-szpinakiem-koperkiem-oraz/">Tortilla z łososiem, szpinakiem, koperkiem oraz ogórkiem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">610 kcal</span>
</div>
<div class="p-card__tags">Ogórek świeży, Szpinak, Chrzan (tarty), Tortilla bezglutenowa, Łosoś wędzony</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="banan jajka jogurt maka oliwa">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/placki-bananowe/">Placki bananowe</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">609 kcal</span>
</div>
<div class="p-card__tags">Banan, Mąka jaglana, Jajko kurze całe, Olej rzepakowy, Jogurt skyr bez laktozy</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="budyn cytryna jajka jogurt maliny migdaly">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/cytrynowy-skyrnik-proteinowy/">Cytrynowy skyrnik proteinowy</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">602 kcal</span>
</div>
<div class="p-card__tags">Jogurt skyr bez laktozy, Jajko kurze całe, Budyń w proszku (z cukrem)…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="cytryna dorsz oliwa pomidor szpinak ziemniaki">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/dorsz-z-ziemniakami-szpinakiem-oraz-pomidorkami/">Dorsz z ziemniakami, szpinakiem oraz pomidorkami koktajlowymi</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">493 kcal</span>
</div>
<div class="p-card__tags">Dorsz, Ziemniaki, Szpinak, Pomidorki koktajlowe, Oliwa z oliwek, Sok z cytryny</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="chleb cytryna feta ogorek oliwa oliwki papryka pomidor salata">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/salatka-grecka-z-serem-typu-feta/">Sałatka grecka z serem typu feta oraz chlebem bezglutenowym</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">603 kcal</span>
</div>
<div class="p-card__tags">Miks sałat, Ser typu Feta, Oliwki zielone, Papryka czerwona…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="makaron mozzarella oliwa pesto pomidor">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/spaghetti-z-pesto/">Spaghetti z pesto</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">494 kcal</span>
</div>
<div class="p-card__tags">Makaron bezglutenowy, Ser mozzarella kulka…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="borowki jogurt kiwi migdaly platki-owsiane">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/owsianka-z-kawalkami-kiwi-oraz-borowkami/">Owsianka z kawałkami kiwi oraz borówkami</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">600 kcal</span>
</div>
<div class="p-card__tags">Płatki owsiane górskie, Jogurt skyr bez laktozy, Kiwi…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="jogurt maliny orzechy platki-jaglane">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/platki-z-malinami-oraz-orzechami-wloskimi/">Płatki z malinami oraz orzechami włoskimi</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">588 kcal</span>
</div>
<div class="p-card__tags">Jogurt skyr bez laktozy, Płatki jaglane, Orzechy włoskie…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="cukinia cytryna losos oliwa pomidor ryz sos-sojowy syrop-klonowy">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/szybka-pieczona-ryba/">Szybka pieczona ryba</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">510 kcal</span>
</div>
<div class="p-card__tags">Łosoś świeży, Ryż basmati, Pomidorki koktajlowe, Cukinia, Cytryna…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="chleb jajka kielbaski ogorek oliwa">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/jajecznica-z-kielbaska-roslinna/">Jajecznica z kiełbaską roślinną</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">613 kcal</span>
</div>
<div class="p-card__tags">Oliwa z oliwek, Kiełbaski roślinne węgierskie Dobra Kaloria…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="banan migdaly pomarancza serek-wiejski syrop-klonowy">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/serek-wiejski-bez-laktozy-z-owocami/">Serek wiejski bez laktozy z owocami i syropem klonowym</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">606 kcal</span>
</div>
<div class="p-card__tags">Serek wiejski bez laktozy, Banan, Pomarańcza, Syrop klonowy, Migdały</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="chleb feta oliwa papryka pomidory-puszka">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/zupa-pomidorowo-paprykowa/">Zupa pomidorowo paprykowa</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">487 kcal</span>
</div>
<div class="p-card__tags">Papryka czerwona, Oliwa z oliwek, Pomidory z puszki, Chleb bezglutenowy…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="jogurt maslo-orzechowe orzechy platki-owsiane syrop-klonowy">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/owsiane-batoniki-z-syropem-klonowym-oraz/">Owsiane batoniki z syropem klonowym oraz masłem orzechowym</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">600 kcal</span>
</div>
<div class="p-card__tags">Płatki owsiane górskie, Masło orzechowe, Mieszanka orzechów, Syrop klonowy…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="chleb halloumi ogorek pomidor salata">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/salatka-z-grillowanym-serem-halloumi/">Sałatka z grillowanym serem halloumi</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">579 kcal</span>
</div>
<div class="p-card__tags">Ser halloumi, Miks sałat, Pomidor, Ogórek świeży, Chleb bezglutenowy</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="jajka makaron marchewka mleko oliwa pieczarki ser-plesniowy">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/zapiekanka-makaronowa-z-suszonymi-pomidorami-w/">Zapiekanka makaronowa z suszonymi pomidorami w kremowo-serowym sosie (liczba porcji: 2)</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">482 kcal</span>
</div>
<div class="p-card__tags">Makaron bezglutenowy, Marchew, Pomidory suszone w oleju (odsączone)…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="chleb mozzarella papryka pomidor szpinak">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/kanapka-z-mozzarella-i-warzywami/">Kanapka z mozzarellą i warzywami</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">612 kcal</span>
</div>
<div class="p-card__tags">Chleb bezglutenowy, Szpinak, Ser mozzarella kulka, Pomidor, Papryka czerwona</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="borowki maliny maslo-orzechowe platki-owsiane serek-wiejski">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/serek-wiejski-z-malinami-borowkami-oraz/">Serek wiejski z malinami, borówkami oraz masłem orzechowym</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">610 kcal</span>
</div>
<div class="p-card__tags">Serek wiejski bez laktozy, Płatki owsiane górskie, Masło orzechowe…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="ciasto-nalesniki jogurt truskawki twarog">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/nalesniki-z-serem-twarogowym-bez-laktozy-2/">Naleśniki z serem twarogowym bez laktozy i owocami</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">504 kcal</span>
</div>
<div class="p-card__tags">Ciasto do naleśników low fodmap, Ser twarogowy półtłusty bez laktozy…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="banan borowki jogurt migdaly platki-owsiane">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/owsianka-z-bananem-oraz-borowkami/">Owsianka z bananem oraz borówkami</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">601 kcal</span>
</div>
<div class="p-card__tags">Płatki owsiane górskie, Banan, Borówki amerykańskie, Płatki migdałów…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="jajka jogurt maka oliwa truskawki">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/jogurtowe-placki-z-owocami/">Jogurtowe placki z owocami</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">521 kcal</span>
</div>
<div class="p-card__tags">jogurtu skyr, jajka, oliwy z oliwek, mąki orkiszowej białej, truskawek</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="awokado cheddar chleb jajka mandarynka">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/kanapka-z-jajkiem-awokado-i-serem/">Kanapka z jajkiem, awokado i serem cheddar + mandarynka</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">568 kcal</span>
</div>
<div class="p-card__tags">jajka, sera cheddar, awokado, chleba żytniego razowego, mandarynek</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="cebula chleb ciecierzyca czosnek marchewka mozzarella oliwa pietruszka-korzen seler">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/zupa-krem-z-ciecierzycy-z-grzankami/">Zupa krem z ciecierzycy z grzankami</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">415 kcal</span>
</div>
<div class="p-card__tags">pietruszki, selera, ciecierzycy konserwowej, małej cebuli, czosnku…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="jablko orzechy">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/jablko-z-orzechami-wloskimi/">Jabłko z orzechami włoskimi</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">208 kcal</span>
</div>
<div class="p-card__tags">jabłko, orzechów włoskich</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="banan borowki pistacje platki-owsiane twarog">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/owsianka-z-twarogiem-i-owocami/">Owsianka z twarogiem i owocami</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">554 kcal</span>
</div>
<div class="p-card__tags">płatków owsianych, twarogu półtłustego, banana, borówek, pistacji</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="chleb maslo ogorek pomidory-suszone seler serek-wiejski">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/serek-wiejski-z-ogorkiem-suszonymi-pomidorami/">Serek wiejski z ogórkiem, suszonymi pomidorami i pieczywem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">526 kcal</span>
</div>
<div class="p-card__tags">serka wiejskiego, selera naciowego, ogórka, pomidorów suszonych…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="cukinia jajka jogurt maka oliwa">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/placuszki-z-cukinii/">Placuszki z cukinii</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">480 kcal</span>
</div>
<div class="p-card__tags">cukinii, mąki orkiszowej pełnoziarnistej, jajka kurzego, jogurtu skyr…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="banan orzechy">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/banan-z-nerkowcami/">Banan z nerkowcami</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">199 kcal</span>
</div>
<div class="p-card__tags">banana, nerkowców</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="ananas czekolada jogurt platki-owsiane syrop-klonowy wiorki">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/jogurt-naturalny-z-domowa-granola-ananasem/">Jogurt naturalny z domową granolą, ananasem i czekoladą</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">550 kcal</span>
</div>
<div class="p-card__tags">jogurtu naturalnego, ananasa, czekolady, płatków owsianych…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="chleb jablko jajka jogurt musztarda ogorek slonecznik">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/pasta-jajeczna-z-ogorkiem-szczypiorkiem-koperkiem/">Pasta jajeczna z ogórkiem, szczypiorkiem, koperkiem i pieczywem + jabłko</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">556 kcal</span>
</div>
<div class="p-card__tags">jajek, chleba żytniego, musztardy, ogórka zielonego, jogurtu naturalnego…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="cebula ciecierzyca czosnek imbir oliwa papryczka-chili pomidor pomidory-puszka ryz">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/curry-z-ciecierzycy/">Curry z ciecierzycy</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">481 kcal</span>
</div>
<div class="p-card__tags">ryżu basmati, małej cebuli, imbiru, czosnku, papryczki chili…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="czekolada">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/czekolada-gorzka/">Czekolada gorzka</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">179 kcal</span>
</div>
<div class="p-card__tags">czekolady gorzkiej</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="awokado imbir mango mleko odzywka pomarancza">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/koktajl-mango-lassi/">Koktajl mango lassi</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">522 kcal</span>
</div>
<div class="p-card__tags">mango, napoju sojowego, wegańskiej odżywki białkowej, awokado, pomarańczy…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="chleb ciecierzyca cytryna czosnek oliwa oliwki">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/sniadania-z-biedronki-hummus-pietruszkowy/">Śniadania z Biedronki: Hummus pietruszkowy</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">525 kcal</span>
</div>
<div class="p-card__tags">ciecierzycy konserwowej, czosnku, soku z cytryny, oliwy z oliwek…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="cebula czosnek makaron marchewka oliwa pomidory-puszka sos-sojowy tofu">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/vege-spaghetti-bolognese/">Vege spaghetti bolognese</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">489 kcal</span>
</div>
<div class="p-card__tags">tofu naturalnego, makaronu spaghetti, pomidorów w puszce, sosu sojowego…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="cebula czosnek oliwa pomidory-puszka seler">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/frytki-z-selera-z-domowym-ketchupem/">Frytki z selera z domowym ketchupem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">199 kcal</span>
</div>
<div class="p-card__tags">selera, oliwy z oliwek, pomidorów z puszki, oleju rzepakowego, cebuli, czosnku</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="jogurt limonka mango migdaly mleko odzywka platki-owsiane">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/jogurtowo-mleczny-koktajl-z-mieta-i/">Jogurtowo-mleczny koktajl z miętą i mango</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">533 kcal</span>
</div>
<div class="p-card__tags">napoju sojowego, jogurtu roślinnego, mango, limonki, płatków migdałów…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="chleb cytryna czosnek mozzarella oliwa pomidor salata">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/salatka-caprese-z-sosem-bazyliowym-i/">Sałatka caprese z sosem bazyliowym i pieczywem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">518 kcal</span>
</div>
<div class="p-card__tags">sera mozzarella, pomidora, rukoli, czosnku, soku z cytryny…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="cebula czosnek dynia imbir marchewka oliwa pomidory-puszka ryz soczewica">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/dahl-z-soczewicy-z-pestkami-dyni/">Dahl z soczewicy z pestkami dyni</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">511 kcal</span>
</div>
<div class="p-card__tags">żółtej soczewicy, cebuli, czosnku, imbiru, marchwii, pomidorów w puszce…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="hummus marchewka ogorek papryka">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/hummus-z-marchewka-ogorkiem-i-papryka/">Hummus z marchewką, ogórkiem i papryką</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">209 kcal</span>
</div>
<div class="p-card__tags">hummusu, marchewki, papryki czerwonej, ogórka</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="banan czekolada mleko odzywka orzechy platki-owsiane wisnie">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/owsianka-na-mleku-roslinnym-z-wisniami/">Owsianka na mleku roślinnym z wiśniami, orzechami, bananem i czekoladą</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">565 kcal</span>
</div>
<div class="p-card__tags">napoju sojowego, płatków owsianych, wiśni, orzechów włoskich, banana…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="awokado cebula chleb oliwa platki-drozdzowe pomidor slonecznik tofu">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/tofucznica-z-awokado-pomidorem-i-pieczywem/">Tofucznica z awokado, pomidorem i pieczywem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">536 kcal</span>
</div>
<div class="p-card__tags">tofu naturalnego, awokado, pomidora, cebuli, nasion słonecznika…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="cebula czosnek marchewka mozzarella oliwa pomidor pomidory-puszka seler">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/zupa-krem-z-pomidorow-2/">Zupa krem z pomidorów</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">503 kcal</span>
</div>
<div class="p-card__tags">marchewki, selera naciowego, cebuli, czosnku, pomidora, oliwy z oliwek…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="marchewka oliwa pietruszka-korzen">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/frytki-z-marchewki-i-pietruszki/">Frytki z marchewki i pietruszki</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">188 kcal</span>
</div>
<div class="p-card__tags">marchwi, oliwy z oliwek, korzenia pietruszki</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="jogurt orzechy wafle">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/skyr-orzechy-wafle-ryzowe/">Skyr + orzechy + wafle ryżowe</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">521 kcal</span>
</div>
<div class="p-card__tags">jogurtu skyr, wafli ryżowych, orzechów włoskich</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="cytryna czosnek losos oliwa serek-smietankowy szpinak tortilla">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/roladki-z-lososiem-i-twarozkiem-szpinakowym/">Roladki z łososiem i twarożkiem szpinakowym</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">557 kcal</span>
</div>
<div class="p-card__tags">łososia wędzonego, tortilli pełnoziarnistej, serka śmietankowego, szpinaku…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="brokul cytryna oliwa pstrag ziemniaki">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/filet-z-pstraga-z-ziemniakami-i/">Filet z pstrąga z ziemniakami i brokułami</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">504 kcal</span>
</div>
<div class="p-card__tags">fileta z pstrąga, ziemniaków, brokuła, oleju, cytryny</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="ananas jablko salata">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/zielone-smoothie-z-ananasem-jablkiem-i/">Zielone smoothie z ananasem, jabłkiem i jarmużem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">203 kcal</span>
</div>
<div class="p-card__tags">ananasa, jabłka, jarmużu</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="kakao maliny migdaly mleko odzywka platki-owsiane">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/czekoladowa-owsianka-na-mleku-roslinnym-z/">Czekoladowa owsianka na mleku roślinnym z malinami</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">561 kcal</span>
</div>
<div class="p-card__tags">napoju sojowego, płatków owsianych, kakao, malin, płatków migdałów…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="brokul chleb cukinia jajka maka oliwa pomidory-suszone szpinak">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/wytrawny-omlet-z-warzywami-i-suszonymi/">Wytrawny omlet z warzywami i suszonymi pomidorami</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">521 kcal</span>
</div>
<div class="p-card__tags">jajek, cukinii, pomidora suszonego, brokuła, mąki pszennej pełnoziarnistej…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="cebula czosnek imbir marchewka oliwa por ryz seler sos-sojowy tofu">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/ryz-smazony-z-warzywami-i-tofu/">Ryż smażony z warzywami i tofu</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">487 kcal</span>
</div>
<div class="p-card__tags">tofu, marchwii, pora, selera naciowego, ryżu, cebuli, imbiru (2cm)…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="baton">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/baton-proteinowy-vitanella/">Baton proteinowy Vitanella</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">241 kcal</span>
</div>
<div class="p-card__tags">Baton proteinowy Vitanella</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="czekolada maliny mleko odzywka ryz">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/ryz-na-mleku-z-czekolada-i/">Ryż na mleku z czekoladą i malinami</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">544 kcal</span>
</div>
<div class="p-card__tags">ryżu białego, mleka roślinnego, czekolady gorzkiej, malin…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="chleb jogurt maslo pomidor rzodkiewka twarog">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/kanapki-z-ziolowym-twarozkiem/">Kanapki z ziołowym twarożkiem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">524 kcal</span>
</div>
<div class="p-card__tags">chleba żytniego razowego, sera twarogowego półtłustego…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="cebula czosnek fasola jogurt kapusta musztarda oliwa pietruszka-korzen platki-owsiane por sos-sojowy">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/kotlety-z-fasoli-z-surowka/">Kotlety z fasoli z surówką</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">476 kcal</span>
</div>
<div class="p-card__tags">czerwonej fasoli konserwowej, płatków owsianych górskich, pietruszki…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="baton">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/baton-wysokobialkowy-smak-malinowy-go-active/">Baton wysokobiałkowy smak malinowy Go Active</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">147 kcal</span>
</div>
<div class="p-card__tags">Baton wysokobiałkowy smak malinowy Go Active</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="jajka maka miod owoce-mrozone">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/omlet-na-slodko-z-miodem/">Omlet na słodko z miodem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">521 kcal</span>
</div>
<div class="p-card__tags">jajek kurzych, mąki pszennej pełnoziarnistej, miodu…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="chleb jajka mozzarella oliwa pomidor salata">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/omletowa-tortilla/">Omletowa tortilla</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">548 kcal</span>
</div>
<div class="p-card__tags">jajek kurzych, pomidorków koktajlowych, sera mozzarella, roszponki…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="cebula czosnek kapusta makaron oliwa pieczarki soczewica">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/makaron-lazanki-z-soczewica-pieczarkami-i/">Makaron łazanki z soczewicą, pieczarkami i kapustą kiszoną</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">482 kcal</span>
</div>
<div class="p-card__tags">soczewicy zielonej, kapusty kiszonej, makaronu łazanki, pieczarek…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="jogurt orzechy">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/jogurt-naturalny-z-orzechami/">Jogurt naturalny z orzechami</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">199 kcal</span>
</div>
<div class="p-card__tags">jogurtu naturalnego, mieszanki orzechów</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="ananas chia jablko jogurt melon odzywka">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/owoce-z-jogurtem-roslinnym/">Owoce z jogurtem roślinnym</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">435 kcal</span>
</div>
<div class="p-card__tags">jogurtu roślinnego, melona, ananasa świeżego, jabłka, nasion chia…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="chleb maslo pomidor rzodkiewka serek-wiejski">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/serek-wiejski-z-rzodkiewka-pomidorem-i/">Serek wiejski z rzodkiewką, pomidorem i pieczywem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">451 kcal</span>
</div>
<div class="p-card__tags">serka wiejskiego, chleba żytniego, pomidora, rzodkiewki, masła</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="cebula czosnek kasza mleko oliwa platki-drozdzowe por siemie-lniane soczewica">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/pulpeciki-z-soczewicy-z-kasza-jeczmienna/">Pulpeciki z soczewicy z kaszą jęczmienną</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">368 kcal</span>
</div>
<div class="p-card__tags">suchej soczewicy zielonej, czosnku, cebuli, pora, mleka roślinnego…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="bulka cebula ketchup musztarda ogorki-kiszone oliwa papryka-konserwowa parowki">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/hot-dog-z-weganska-parowka/">Hot dog z wegańską parówką</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">456 kcal</span>
</div>
<div class="p-card__tags">bułki do hot dogów, parówek wegańskich Tarczyński, cebuli czerwonej…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="maka maliny mleko odzywka orzechy">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/budyn-waniliowy-na-mleku-roslinnym-z/">Budyń waniliowy na mleku roślinnym z sosem malinowym</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">463 kcal</span>
</div>
<div class="p-card__tags">mleka roślinnego, mąki ziemniaczanej, malin, wegańskiej odżywki białkowej…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="chleb jajka kielki losos oliwa pomidor szpinak">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/omlet-z-wedzonym-lososiem-szpinakiem-i/">Omlet z wędzonym łososiem, szpinakiem i pomidorkami koktajlowymi</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">469 kcal</span>
</div>
<div class="p-card__tags">łososia wędzonego, szpinaku, jajek kurzych, pomidorków koktajlowych…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="brokul cebula czosnek jajka makaron marchewka mleko mozzarella oliwa pomidor">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/zapiekanka-makaronowa-z-serem-mozzarella/">Zapiekanka makaronowa z serem mozzarella</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">372 kcal</span>
</div>
<div class="p-card__tags">makaronu penne, jajek kurzych, mleka roślinnego, marchwi, cebuli, czosnku…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="cukinia cytryna czosnek jajka jogurt majonez maka oliwa">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/placuszki-z-cukinii-z-dipem-czosnkowym/">Placuszki z cukinii z dipem czosnkowym</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">460 kcal</span>
</div>
<div class="p-card__tags">cukinii, mąki z ciecierzycy, jajek kurzych, czosnku, jogurtu naturalnego…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="banan jajka maka odzywka olej-kokosowy">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/chleb-bananowy/">Chleb bananowy</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">463 kcal</span>
</div>
<div class="p-card__tags">małego banana, mąki owsianej pełnoziarnistej, oleju kokosowego…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="chleb jajka pomidor serek-wiejski">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/pasta-jajeczna/">Pasta jajeczna</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">448 kcal</span>
</div>
<div class="p-card__tags">serka wiejskiego light, jajek kurzych, chleba żytniego razowego…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="awokado cukinia fasola kasza oliwa papryczka-chili platki-drozdzowe platki-owsiane pomidor pomidory-puszka salata slonecznik">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/burger-z-fasoli-z-awokado-i/">Burger z fasoli z awokado i grillowaną cukinią</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">359 kcal</span>
</div>
<div class="p-card__tags">kaszy jaglanej, fasoli czerwonej, koncentratu pomidorowego…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="banan czekolada fasola kakao maka mleko oliwa siemie-lniane wisnie">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/brownie-z-fasoli-z-wisniami-i/">Brownie z fasoli z wiśniami i bananem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">465 kcal</span>
</div>
<div class="p-card__tags">mąki pszennej pełnoziarnistej, oleju rzepakowego…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="gruszka mleko odzywka orzechy platki-jaglane">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/jaglanka-z-gruszka/">Jaglanka z gruszką</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">441 kcal</span>
</div>
<div class="p-card__tags">płatków jaglanych, napoju migdałowego, małej gruszki, orzechów włoskich…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="cebula chleb oliwa platki-drozdzowe pomidor tofu">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/tofucznica-z-cebulka-szczypiorkiem-i-pieczywem/">Tofucznica z cebulką, szczypiorkiem i pieczywem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">455 kcal</span>
</div>
<div class="p-card__tags">tofu naturalnego, cebuli, płatków drożdżowych, oleju rzepakowego…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="ciecierzyca cukinia cytryna czosnek jogurt marchewka oliwa papryka tortilla">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/tortilla-z-ciecierzyca-cukinia-papryka-i/">Tortilla z ciecierzycą, cukinią, papryką i sosem czosnkowym</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">378 kcal</span>
</div>
<div class="p-card__tags">tortilli pszennych, ciecierzycy konserwowej, cukinii, papryki czerwonej…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="jajka jogurt kakao maka marchewka oliwa orzechy">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/ciasto-marchewkowe-z-kakao/">Ciasto marchewkowe z kakao</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">474 kcal</span>
</div>
<div class="p-card__tags">marchwi, mąki pszennej pełnoziarnistej, oleju rzepakowego, jajka, kakao…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="jajka maka maliny mleko odzywka olej-kokosowy">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/fit-placuszki/">Fit Placuszki</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">473 kcal</span>
</div>
<div class="p-card__tags">jaja kurzego, mąki owsianej pełnoziarnistej, odżywki białkowej…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="cebula czosnek dynia fasola mleczko-kokosowe oliwa ziemniaki">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/krem-z-dyni/">Krem z dyni</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">375 kcal</span>
</div>
<div class="p-card__tags">dyni, czarnej fasoli konserwowej, cebuli, czosnku, mleczka kokosowego 12%…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="cebula ciecierzyca czosnek maka migdaly oliwa oliwki pomidory-puszka szpinak">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/wege-pizza/">Wege pizza</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">464 kcal</span>
</div>
<div class="p-card__tags">mąki orkiszowej, oliwy z oliwek, koncentratu pomidorowego, czosnku…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="jablko jogurt mleko orzechy ryz">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/ryz-z-jablkami/">Ryż z jabłkami</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">482 kcal</span>
</div>
<div class="p-card__tags">ryżu basmati, napoju roślinnego, małego jabłka, orzechów, jogurtu skyr</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="cebula chleb cytryna czosnek fasola kielki oliwa papryka rzodkiewka">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/kanapka-z-pasta-z-czerwonej-fasoli/">Kanapka z pastą z czerwonej fasoli</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">451 kcal</span>
</div>
<div class="p-card__tags">fasoli czerwonej konserwowej, czerwonej cebuli, czosnku, soku z cytryny…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="cebula czosnek makaron mozzarella oliwa papryka pomidor">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/makaron-z-pieczonymi-warzywami-i-serem/">Makaron z pieczonymi warzywami i serem mozzarella</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">370 kcal</span>
</div>
<div class="p-card__tags">papryki czerwonej, małej cebuli, czosnku, makaronu pełnoziarnistego penne…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="czekolada jablko jogurt orzechy platki-owsiane syrop-klonowy">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/jogurt-naturalny-z-domowa-granola-z/">Jogurt naturalny z domową granolą z orzechami i jabłkiem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">460 kcal</span>
</div>
<div class="p-card__tags">płatków owsianych górskich, orzechów włoskich, gorzkiej czekolady…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="czekolada kakao maslo-orzechowe mleko odzywka platki-owsiane">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/shake-snickers/">Shake snickers</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">460 kcal</span>
</div>
<div class="p-card__tags">napoju roślinnego, wegańskiej odżywki białkowej, kakao, masła orzechowego…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="bulka chrzan kielki losos ogorek serek-smietankowy">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/kanapka-z-wedzonym-lososiem/">Kanapka z wędzonym łososiem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">474 kcal</span>
</div>
<div class="p-card__tags">bułki grahamki, łososia wędzonego, serka śmietankowego, chrzanu…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="batat maslo-orzechowe oliwa ryz salata sos-sojowy tofu">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/buddha-bowl/">Buddha bowl</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">382 kcal</span>
</div>
<div class="p-card__tags">ryżu basmati, tofu naturalnego, batata, mieszanych sałat, sosu sojowego…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="bagietka cebula cukinia czosnek grana-padano marchewka oliwa pomidory-puszka por soczewica">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/bruschetta-z-soczewica-swiezymi-ziolami-i/">Bruschetta z soczewicą, świeżymi ziołami i serem grana padano</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">456 kcal</span>
</div>
<div class="p-card__tags">bagietki, soczewicy czerwonej, pora, cukinii, marchwi, cebuli, czosnku…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="czekolada jogurt maslo-orzechowe miod orzechy platki-owsiane">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/owsiane-batoniki-z-czekolada-orzechami-arachidowymi/">Owsiane batoniki z czekoladą, orzechami arachidowymi i miodem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">471 kcal</span>
</div>
<div class="p-card__tags">płatków owsianych górskich, orzeszków arachidowych, masła orzechowego…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="chleb maslo pomidor pomidory-suszone serek-smietankowy szpinak">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/pasta-z-twarozku-z-suszonymi-pomidorami/">Pasta z twarożku z suszonymi pomidorami, szczypiorkiem, liśćmi szpinaku, pomidorem i ciemnym pieczywem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">478 kcal</span>
</div>
<div class="p-card__tags">twarożku, szpinaku, pomidora, suszonych pomidorów, chleb żytniego razowego…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="cebula dorsz jablko kapusta marchewka oliwa ziemniaki">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/dorsz-z-ziemniakami-i-kiszona-kapusta/">Dorsz z ziemniakami i kiszoną kapustą</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">379 kcal</span>
</div>
<div class="p-card__tags">dorsza świeżego, ziemniaków, kapusty kwaszonej, jabłka, marchwi, cebuli…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="burak camembert chleb miod musztarda oliwa szpinak truskawki">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/salatka-ze-szpinakiem-serem-plesniowym-burakami/">Sałatka ze szpinakiem, serem pleśniowym, burakami i grzankami</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">455 kcal</span>
</div>
<div class="p-card__tags">chleb pszennego, truskawek, buraków, musztardy, miodu, sera camembert…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="banan mleko odzywka orzechy platki-inne platki-owsiane">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/owsianka-lion/">Owsianka Lion</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">451 kcal</span>
</div>
<div class="p-card__tags">płatków owsianych, mleka roślinnego, wegańskiej odżywki białkowej…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="chleb cukinia jajka oliwa pomidor">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/pieczony-omlet-z-cukinia/">Pieczony omlet z cukinią</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">473 kcal</span>
</div>
<div class="p-card__tags">jaj, małej cukinii, pomidorków koktajlowych, chleba żytniego razowego…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="burak feta grejpfrut makaron migdaly oliwa salata">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/salatka-z-makaronem-i-serem-feta/">Sałatka z makaronem i serem feta</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">386 kcal</span>
</div>
<div class="p-card__tags">rukoli, makaronu pełnoziarnistego, np. świderki, sera feta, małego buraka…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="banan czekolada jogurt migdaly wafle">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/serek-waniliowy-z-kawalkami-czekolady-i/">Serek waniliowy z kawałkami czekolady i bananem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">465 kcal</span>
</div>
<div class="p-card__tags">czekolady gorzkiej, banana, jogurtu skyr, wafli ryżowych, płatków migdałowych</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="banan cytryna kiwi migdaly mleko odzywka platki-owsiane">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/waniliowa-owsianka-z-bananem-i-kiwi/">Waniliowa owsianka z bananem i kiwi</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">443 kcal</span>
</div>
<div class="p-card__tags">napoju sojowego, płatków owsianych, banana, kiwi, soku z cytryny, migdałów…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="awokado chleb mozzarella pomidor">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/tost-z-awokado-i-mozzarella/">Tost z awokado i mozzarellą</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">463 kcal</span>
</div>
<div class="p-card__tags">chleba żytniego razowego, mozzarelli, awokado, małego pomidora</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="bulka-tarta burak cebula cytryna czosnek maka mleko oliwa pieczarki siemie-lniane soczewica ziemniaki">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/pieczone-kotlety-mielone-z-soczewicy-z/">Pieczone kotlety mielone z soczewicy z ziemniakami</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">386 kcal</span>
</div>
<div class="p-card__tags">soczewicy zielonej, cebuli, czosnku, pieczarek uprawnych…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="jablko maslo-orzechowe mleko odzywka orzechy platki-jaglane">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/jaglanka-z-jablkiem-i-cynamonem/">Jaglanka z jabłkiem i cynamonem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">460 kcal</span>
</div>
<div class="p-card__tags">płatków jaglanych, napoju roślinnego, małego jabłka, masła orzechowego…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="cytryna dorsz oliwa pomidor ziemniaki">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/ryba-grillowana-w-papilocie/">Ryba grillowana w papilocie</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">516 kcal</span>
</div>
<div class="p-card__tags">Dorsz, Ziemniaki, Pomidorki koktajlowe, Sok z cytryny, Oliwa z oliwek</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="cebula halloumi ogorek oliwki papryka pomidor salata tortilla">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/tortilla-pelnoziarnista-z-salatka-po-grecku/">Tortilla pełnoziarnista z sałatką po grecku i serem halloumi</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">514 kcal</span>
</div>
<div class="p-card__tags">Ser halloumi, Ogórek świeży, Papryka czerwona, Cebula, Pomidor…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="chleb hummus ogorek papryka plastry-wegan pomidor">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/kanapki-z-hummusem-wedlina-i-warzywami/">Kanapki z hummusem, wędliną i warzywami</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">593 kcal</span>
</div>
<div class="p-card__tags">Chleb żytni razowy, Plastry wegańskie z pistacjami Go Vege, Pomidor…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="cebula cukinia czosnek kasza marchewka oliwa papryka pomidory-puszka soczewica">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/gulasz-z-soczewicy-czerwonej/">Gulasz z soczewicy czerwonej</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">499 kcal</span>
</div>
<div class="p-card__tags">Papryka czerwona, Kasza jęczmienna pęczak, Cukinia, Cebula, Czosnek…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="ciasto-nalesniki daktyle jogurt kakao orzechy">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/nalesniki-z-kremem-czekoladowym/">Naleśniki z kremem czekoladowym</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">603 kcal</span>
</div>
<div class="p-card__tags">Ciasto do naleśników wegańskie, Orzechy laskowe, Daktyle, suszone…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="biszkopty czekolada pudding serek-proteinowy smietanka">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/warstwowy-deser-z-gorzka-czekolada/">Warstwowy deser z gorzką czekoladą</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">617 kcal</span>
</div>
<div class="p-card__tags">Serek proteinowy ze skyrem waniliowy Go Active, Biszkopty…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="cebula czosnek dynia feta kasza oliwa szpinak">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/peczak-z-dynia-i-serem-typu/">Pęczak z dynią i serem typu feta</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">487 kcal</span>
</div>
<div class="p-card__tags">Dynia świeża lub mrożona, Ser typu Feta, Kasza jęczmienna pęczak…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="jablko jajka jogurt miod mleko oliwa platki-owsiane">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/pieczona-owsianka-z-jablkiem-oraz-cynamonem/">Pieczona owsianka z jabłkiem oraz cynamonem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">603 kcal</span>
</div>
<div class="p-card__tags">Płatki owsiane górskie, Jajko kurze całe, Mleko roślinne niesłodzone, Miód…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="brokul cytryna losos miod musztarda oliwa ryz">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/losos-w-sosie-musztardowo-miodowym-z/">Łosoś w sosie musztardowo-miodowym z ryżem oraz brokułem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">495 kcal</span>
</div>
<div class="p-card__tags">Łosoś świeży, Ryż basmati, Brokuł, świeży lub mrożony, Miód, Musztarda…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="budyn jablko jajka jogurt kasza oliwa">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/placuszki-jablkowe/">Placuszki jabłkowe</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">599 kcal</span>
</div>
<div class="p-card__tags">Kasza jaglana, Jabłko, Budyń w proszku (z cukrem), Olej rzepakowy…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="chleb cytryna feta kukurydza oliwa pomidor salata">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/salatka-z-serem-i-kukurydza-konserwowa/">Sałatka z serem i kukurydzą konserwową</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">501 kcal</span>
</div>
<div class="p-card__tags">Miks sałat, Kukurydza konserwowa, Ser typu Feta, Pomidorki koktajlowe…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="chleb mozzarella plastry-wegan pomidor rzodkiewka serek-smietankowy">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/tost-z-szynka-serem-i-warzywami/">Tost z szynką, serem i warzywami</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">598 kcal</span>
</div>
<div class="p-card__tags">Chleb żytni razowy, Plastry wegańskie z pistacjami Go Vege…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="kakao maslo-orzechowe mleko odzywka platki-owsiane">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/czekoladowe-smoothie/">Czekoladowe smoothie</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">583 kcal</span>
</div>
<div class="p-card__tags">Mleko roślinne niesłodzone, Kakao 16%, Masło orzechowe, Odżywka białkowa…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="awokado bajgiel czosnek halloumi miod musztarda pomidor salata">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/bajgiel-z-kremowym-sosem/">Bajgiel z kremowym sosem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">602 kcal</span>
</div>
<div class="p-card__tags">Bajgiel z sezamem, Ser halloumi, Rukola, Pomidor, Awokado, Miód, Musztarda…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="cebula czosnek makaron mieso-wegan mozzarella oliwa papryka pomidor pomidory-puszka">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/lasagne-w-papryce/">Lasagne w papryce</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">509 kcal</span>
</div>
<div class="p-card__tags">Papryka czerwona, Oliwa z oliwek, Cebula, Czosnek…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="banan migdaly pomarancza serek-wiejski syrop-klonowy">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/serek-wiejski-z-owocami-i-syropem/">Serek wiejski z owocami i syropem klonowym</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">604 kcal</span>
</div>
<div class="p-card__tags">Serek wiejski naturalny, Banan, Pomarańcza, Syrop klonowy, Migdały</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="chleb jajka majonez ogorek plastry-wegan pomidor">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/kanapki-z-szynka-jajkiem-i-ogorkiem/">Kanapki z szynką, jajkiem i ogórkiem kiszonym</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">595 kcal</span>
</div>
<div class="p-card__tags">Chleb żytni razowy, Majonez wegański…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="borowki jajka maka oliwa twarog">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/syrniki-z-owocami/">Syrniki z owocami (liczba porcji: 3)</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">596 kcal</span>
</div>
<div class="p-card__tags">Ser twarogowy półtłusty, Jajko kurze całe, Mąka pszenna pełnoziarnista…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="biszkopty jogurt kakao kawa orzechy truskawki">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/tiramisu-z-truskawkami/">Tiramisu z truskawkami</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">596 kcal</span>
</div>
<div class="p-card__tags">Biszkopty, Jogurt skyr, Jogurt naturalny 2%, Kakao 16%…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="chleb gouda jajka ogorek oliwa plastry-wegan">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/tosty-francuskie-z-serem-gouda-oraz/">Tosty francuskie z serem gouda oraz plastrem wegańskim</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">604 kcal</span>
</div>
<div class="p-card__tags">Chleb żytni razowy, Jajko kurze całe, Ser gouda…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="banan czekolada maslo-orzechowe mleko odzywka orzechy platki-owsiane">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/owsianka-snickers/">Owsianka snickers</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">443 kcal</span>
</div>
<div class="p-card__tags">płatków owsianych, napoju roślinnego np. migdałowego, czekolady gorzkiej…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="bulka losos papryka pomidor">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/grahamka-z-lososiem-wedzonym-i-warzywami/">Grahamka z łososiem wędzonym i warzywami</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">440 kcal</span>
</div>
<div class="p-card__tags">bułki grahamki, pomidora, papryki czerwonej, łososia wędzonego</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="cebula cukinia makaron mozzarella oliwa papryka pesto salata">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/makaron-fusilli-z-czerwonym-pesto-i/">Makaron fusilli z czerwonym pesto i mozzarellą</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">366 kcal</span>
</div>
<div class="p-card__tags">pesto czerwonego, papryki czerwonej, cebuli, cukinii, mozzarelli, rukoli…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="banan borowki jajka maka oliwa twarog">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/placuszki-twarogowe/">Placuszki twarogowe</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">465 kcal</span>
</div>
<div class="p-card__tags">twarogu półtłustego, jajka kurzego, mąki orkiszowej pełnoziarnistej…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="banan jogurt maliny orzechy platki-owsiane">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/bananowa-owsianka-z-malinami/">Bananowa owsianka z malinami</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">465 kcal</span>
</div>
<div class="p-card__tags">płatków owsianych górskich, malin, banana, orzechów włoskich, jogurtu skyr</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="cebula maka mozzarella oliwa pieczarki pomidory-suszone">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/wege-omlet-z-mozzarella-i-suszonymi/">Wege omlet z mozzarellą i suszonymi pomidorami</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">461 kcal</span>
</div>
<div class="p-card__tags">mąki z ciecierzycy, suszonych pomidorów, pieczarek, cebuli…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="ananas awokado cytryna czosnek imbir miso ogorek oliwa pomidor soczewica sos-sojowy">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/buddha-bowl-z-awokado/">Buddha bowl z awokado</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">380 kcal</span>
</div>
<div class="p-card__tags">soczewicy czarnej, awokado, pomidorków koktajlowych, ogórka zielonego…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="chleb cytryna czosnek hummus imbir kielki marchewka ogorek olej-sezamowy sos-sojowy syrop-klonowy tofu">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/kanapka-z-grillowanym-tofu/">Kanapka z grillowanym tofu</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">475 kcal</span>
</div>
<div class="p-card__tags">tofu naturalnego, sosu sojowego, czosnku, imbiru, syropu klonowego…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="banan kakao maslo-orzechowe mleko odzywka">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/koktajl-czekoladowy/">Koktajl czekoladowy</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">469 kcal</span>
</div>
<div class="p-card__tags">banana, wegańskiej odżywki białkowej, kakao, masła orzechowego…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="chleb jajka pomidor rzodkiewka salata serek-smietankowy">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/kanapka-z-jajkiem/">Kanapka z jajkiem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">443 kcal</span>
</div>
<div class="p-card__tags">chleba żytniego, serka kanapkowego, jaj, pomidora, rzodkiewki, rukoli</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="cytryna czosnek imbir limonka losos oliwa ryz sezam sos-sojowy">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/losos-w-sezamie/">Łosoś w sezamie</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">379 kcal</span>
</div>
<div class="p-card__tags">świeżego łososia, ryżu basmati, cytryny, sezamu, sosu sojowego…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="chia jogurt orzechy platki-owsiane syrop-klonowy zurawina">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/domowa-granola-z-jogurtem/">Domowa granola z jogurtem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">466 kcal</span>
</div>
<div class="p-card__tags">płatków owsianych górskich, żurawiny suszonej, orzechów włoskich…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="jagody maka migdaly mleko odzywka">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/budyn-na-mleku-roslinnym-z-jagodami/">Budyń na mleku roślinnym z jagodami i płatkami migdałowymi</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">475 kcal</span>
</div>
<div class="p-card__tags">mleka roślinnego, mąki ziemniaczanej, płatków migdałowych, jagód…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="chleb maslo mleko ogorek papryka pomidor rzodkiewka salata twarog">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/pasta-z-twarozku-z-czarnuszka-z/">Pasta z twarożku z czarnuszką z warzywami</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">457 kcal</span>
</div>
<div class="p-card__tags">sera twarogowego półtłustego, mleka roślinnego, papryki, pomidora, ogórka…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="cebula cukinia czosnek feta kuskus oliwa papryka pomidor">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/cukinia-nadziewana-kasza-kuskus-z-warzywami/">Cukinia nadziewana kaszą kuskus z warzywami i serem feta</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">375 kcal</span>
</div>
<div class="p-card__tags">kaszy kuskus, cukinii, cebuli, czosnku, papryki żółtej, pomidora…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="bob cebula chleb cytryna czosnek odzywka oliwa pomidor szpinak">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/pasta-z-bobu-ze-szpinakiem-swiezymi/">Pasta z bobu ze szpinakiem, świeżymi pomidorami i pieczywem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">483 kcal</span>
</div>
<div class="p-card__tags">bobu, czosnku, cebuli, oliwy z oliwek, szpinaku, pomidora, chleba razowego…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="maliny mleko odzywka platki-jaglane wiorki">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/kokosowy-krem-jaglany-z-malinami/">Kokosowy krem jaglany z malinami</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">461 kcal</span>
</div>
<div class="p-card__tags">mleka roślinnego, płatków jaglanych, malin świeżych lub mrożonych…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="awokado chleb cytryna jajka pomidor">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/kanapka-z-pasta-z-jajka-i/">Kanapka z pastą z jajka i awokado</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">463 kcal</span>
</div>
<div class="p-card__tags">chleba żytniego razowego, jajek kurzych, awokado, soku z cytryny, pomidora</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="cebula czosnek fasola kakao kapusta kukurydza marchewka oliwa papryka pomidory-puszka ryz">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/weganskie-chilli-sin-carne/">Wegańskie chilli sin carne</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">372 kcal</span>
</div>
<div class="p-card__tags">kapusty białej, fasoli czarnej konserwowej, kukurydzy konserwowej…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="batat ciecierzyca oliwa pomidor salata tofu">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/salatka-z-pieczonych-batatow-i-ciecierzycy/">Sałatka z pieczonych batatów i ciecierzycy</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">498 kcal</span>
</div>
<div class="p-card__tags">małego batata, oliwy z oliwek, ciecierzycy konserwowej…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="jajka jogurt maka oliwa truskawki">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/placuszki-z-truskawkami/">Placuszki z truskawkami</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">466 kcal</span>
</div>
<div class="p-card__tags">mąki żytniej pełnoziarnistej, jogurtu greckiego/skyr, truskawek…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="bulka ogorek rzodkiewka serek-wiejski">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/pieczywo-z-wiosennym-serkiem-wiejskim-rzodkiewka/">Pieczywo z wiosennym serkiem wiejskim, rzodkiewką i ogórkiem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">468 kcal</span>
</div>
<div class="p-card__tags">serka wiejskiego, rzodkiewek, ogórka, bułki grahamki</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="cebula ciecierzyca cytryna kuskus ogorek oliwa papryka pomidor">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/tabbouleh-z-ogorkiem-i-pomidorem/">Tabbouleh z ogórkiem i pomidorem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">382 kcal</span>
</div>
<div class="p-card__tags">kuskusu, cebuli, papryki, ogórka zielonego, pomidora…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="bagietka cebula mozzarella oliwa pomidor slonecznik">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/zapiekanka-z-pomidorami-i-mozzarella/">Zapiekanka z pomidorami i mozzarellą</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">474 kcal</span>
</div>
<div class="p-card__tags">bagietki, małego pomidora, sera mozzarella, małej cebuli czerwonej…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="borowki jogurt orzechy platki-owsiane">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/jogurt-z-borowkami-i-orzechami/">Jogurt z borówkami i orzechami</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">468 kcal</span>
</div>
<div class="p-card__tags">borówek świeżych lub mrożonych, jogurtu, mieszanki orzechów, płatków owsianych</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="burak chleb ciecierzyca cytryna kielki maslo-orzechowe oliwa papryka szpinak">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/buraczany-hummus-z-warzywami-i-pieczywem/">Buraczany hummus z warzywami i pieczywem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">457 kcal</span>
</div>
<div class="p-card__tags">chleba żytniego razowego, ciecierzycy konserwowej…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="cebula chrzan jajka jogurt oliwa pieczarki platki-owsiane seler ziemniaki">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/zapiekane-pieczarki-portobello-z-farszem-z/">Zapiekane pieczarki portobello z farszem z jajek</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">363 kcal</span>
</div>
<div class="p-card__tags">pieczarek portobello, jajek kurzych, małej cebuli, płatków owsianych…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="kakao mleko odzywka platki-inne truskawki wiorki">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/pudding-czekoladowy-z-truskawkami/">Pudding czekoladowy z truskawkami</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">456 kcal</span>
</div>
<div class="p-card__tags">mleka roślinnego np. migdałowe, truskawek, kakao, płatków ryżowych…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="czekolada mleko odzywka platki-owsiane wiorki">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/owsianka-bounty/">Owsianka bounty</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">455 kcal</span>
</div>
<div class="p-card__tags">płatków owsianych, czekolady gorzkiej, wiórków kokosowych…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="chleb ogorek pomidor salata ser-zolty serek-smietankowy">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/kanapki-z-zoltym-serem-i-warzywami/">Kanapki z żółtym serem i warzywami</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">458 kcal</span>
</div>
<div class="p-card__tags">chleba żytniego razowego, małego pomidora, małego ogórka, rukoli…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="cebula cukinia feta marchewka oliwa papryka ziemniaki">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/zapiekanka-warzywna-z-serem-feta/">Zapiekanka warzywna z serem feta</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">364 kcal</span>
</div>
<div class="p-card__tags">cukinii, ziemniaków, sera feta, małej czerwonej cebuli, marchewki…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="chleb losos majonez ogorek olej-sezamowy por sos-ostry sos-sojowy">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/pasta-z-lososia-teriyaki-z-pieczywem/">Pasta z łososia teriyaki z pieczywem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">456 kcal</span>
</div>
<div class="p-card__tags">łososia świeżego, ogórka zielonego, pora, majonezu, sosu sojowego…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="chleb maslo-orzechowe twarog wisnie">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/kanapki-z-twarogiem-maslem-orzechowym-i/">Kanapki z twarogiem, masłem orzechowym i dżemem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">447 kcal</span>
</div>
<div class="p-card__tags">chleba żytniego, twarogu chudego, masła orzechowego…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="bulka mozzarella orzechy pomidor">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/mozzarella-pomidor-grahamka-i-orzechy/">Mozzarella, pomidor, grahamka i orzechy</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">469 kcal</span>
</div>
<div class="p-card__tags">bułki grahamki, sera mozzarella, orzechów włoskich, małego pomidora</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="awokado grana-padano makaron pomidor salata serek-smietankowy">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/makaron-penne-z-awokado-pomidorkami-koktajlowymi/">Makaron penne z awokado, pomidorkami koktajlowymi, rukolą, bazylią i serem grana padano</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">385 kcal</span>
</div>
<div class="p-card__tags">makaronu penne, awokado, serka śmietankowego, pomidorków koktajlowych…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="czekolada kakao migdaly mleko odzywka platki-jaglane porzeczki">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/czekoladowy-krem-jaglany-z-porzeczkami/">Czekoladowy krem jaglany z porzeczkami</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">451 kcal</span>
</div>
<div class="p-card__tags">mleka roślinnego, płatków jaglanych, porzeczek czarnych, kakao…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="jogurt maslo-orzechowe miod orzechy platki-owsiane">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/owsiane-batoniki-z-miodem-i-maslem/">Owsiane batoniki z miodem i masłem orzechowym</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">481 kcal</span>
</div>
<div class="p-card__tags">płatków owsianych, masła orzechowego, mieszanych orzechów, miodu, jogurtu skyr</div>
</div></article></li>
<li>
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="cebula chleb fasola jablko ogorki-kiszone oliwa">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/pasta-z-bialej-fasoli-z-ogorkiem/">Pasta z białej fasoli z ogórkiem kiszonym i pieczywem</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Śniadanie</span>
<span class="p-num">7:00-10:00</span>
<span class="p-num">458 kcal</span>
</div>
<div class="p-card__tags">chleba żytniego razowego, białej fasoli konserwowej, małej cebuli…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="cebula ciecierzyca czosnek marchewka oliwa pietruszka-korzen por tofu">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/zupa-krem-z-ciecierzycy-i-pieczonych/">Zupa krem z ciecierzycy i pieczonych warzyw</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">377 kcal</span>
</div>
<div class="p-card__tags">marchewki, ciecierzycy konserwowej, czosnku, małej cebuli, pora…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="losos ogorek rzodkiewka salata serek-smietankowy tortilla">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/tortilla-z-wedzonym-lososiem-i-warzywami/">Tortilla z wędzonym łososiem i warzywami</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">450 kcal</span>
</div>
<div class="p-card__tags">tortilii pełnoziarnistej, łososia wędzonego, serka śmietankowego…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="cebula czosnek dynia grana-padano marchewka oliwa ryz salata">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/risotto-z-dynia-i-serem-salatkowym/">Risotto z dynią i serem sałatkowym</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">362 kcal</span>
</div>
<div class="p-card__tags">ryżu, dyni, sera salatkowego, grana padano, rukoli, marchwi, cebuli…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="burak kapusta makaron marchewka ogorek papier-ryzowy sos-ostry sos-sojowy">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/warzywne-spring-rolls/">Warzywne spring rolls</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">460 kcal</span>
</div>
<div class="p-card__tags">ogórka, marchwi, kapusty, buraka, makaronu ryżowego, papieru ryżowego…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="3" data-slot-id="kolacja" data-tags="czekolada jogurt miod platki-inne platki-owsiane zurawina">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/owsiano-zytnie-batoniki-z-miodem-i/">Owsiano-żytnie batoniki z miodem i czekoladą</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Kolacja</span>
<span class="p-num">18:00-20:00</span>
<span class="p-num">456 kcal</span>
</div>
<div class="p-card__tags">płatków owsianych górskich, płatków żytnich, żurawiny suszonej…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="awokado cebula ciecierzyca cukinia czosnek odzywka oliwa pomidory-puszka tortilla">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/tortilla-z-ciecierzyca-cukinia-i-awokado/">Tortilla z ciecierzycą, cukinią i awokado + shake białkowy - przepis na 2 porcje</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">381 kcal</span>
</div>
<div class="p-card__tags">tortilli pełnoziarnistej, ciecierzycy konserwowej, awokado…</div>
</div></article></li>
<li>
<article class="p-card" data-slot="2" data-slot-id="obiad" data-tags="cebula ciecierzyca cukinia czosnek kasza marchewka oliwa papryka pietruszka-korzen">
<div class="p-card__band"></div>
<div class="p-card__body">
<a class="p-card__title" href="przepisy/vege-krupnik/">Vege krupnik</a>
<div class="p-card__meta">
<span class="p-card__slot"><span class="p-dot"></span>Obiad</span>
<span class="p-num">13:00-16:00</span>
<span class="p-num">363 kcal</span>
</div>
<div class="p-card__tags">cukinii, ciecierzycy konserwowej, kaszy jęczmiennej, papryki czerwonej…</div>
</div></article></li>
</ul>

<script>window.RECIPES = {"count": 280, "ingredients": [{"id": "oliwa", "label": "Oliwa / olej"}, {"id": "pomidor", "label": "Pomidor"}, {"id": "cebula", "label": "Cebula"}, {"id": "chleb", "label": "Chleb"}, {"id": "czosnek", "label": "Czosnek"}, {"id": "jogurt", "label": "Jogurt / skyr"}, {"id": "mleko", "label": "Mleko roślinne"}, {"id": "odzywka", "label": "Odżywka białkowa"}, {"id": "orzechy", "label": "Orzechy"}, {"id": "jajka", "label": "Jajka"}, {"id": "platki-owsiane", "label": "Płatki owsiane"}, {"id": "papryka", "label": "Papryka"}, {"id": "cytryna", "label": "Cytryna"}, {"id": "ogorek", "label": "Ogórek"}, {"id": "banan", "label": "Banan"}, {"id": "marchewka", "label": "Marchewka"}, {"id": "salata", "label": "Sałata / rukola / roszponka"}, {"id": "maka", "label": "Mąka"}, {"id": "pomidory-puszka", "label": "Pomidory z puszki / passata"}, {"id": "maslo-orzechowe", "label": "Masło orzechowe"}, {"id": "mozzarella", "label": "Mozzarella"}, {"id": "szpinak", "label": "Szpinak"}, {"id": "ryz", "label": "Ryż"}, {"id": "cukinia", "label": "Cukinia"}, {"id": "czekolada", "label": "Czekolada"}, {"id": "jablko", "label": "Jabłko"}, {"id": "kakao", "label": "Kakao"}, {"id": "makaron", "label": "Makaron"}, {"id": "fasola", "label": "Fasola"}, {"id": "tofu", "label": "Tofu"}, {"id": "losos", "label": "Łosoś"}, {"id": "ciecierzyca", "label": "Ciecierzyca"}, {"id": "migdaly", "label": "Migdały"}, {"id": "sos-sojowy", "label": "Sos sojowy"}, {"id": "awokado", "label": "Awokado"}, {"id": "bulka", "label": "Bułka"}, {"id": "soczewica", "label": "Soczewica"}, {"id": "kasza", "label": "Kasza"}, {"id": "rzodkiewka", "label": "Rzodkiewka"}, {"id": "seler", "label": "Seler"}, {"id": "twarog", "label": "Twaróg"}, {"id": "ziemniaki", "label": "Ziemniaki"}, {"id": "feta", "label": "Feta"}, {"id": "maliny", "label": "Maliny"}, {"id": "serek-smietankowy", "label": "Serek śmietankowy"}, {"id": "imbir", "label": "Imbir"}, {"id": "miod", "label": "Miód"}, {"id": "serek-wiejski", "label": "Serek wiejski"}, {"id": "tortilla", "label": "Tortilla"}, {"id": "syrop-klonowy", "label": "Syrop klonowy"}, {"id": "truskawki", "label": "Truskawki"}, {"id": "borowki", "label": "Borówki"}, {"id": "majonez", "label": "Majonez"}, {"id": "maslo", "label": "Masło / margaryna"}, {"id": "pieczarki", "label": "Pieczarki"}, {"id": "por", "label": "Por"}, {"id": "wiorki", "label": "Wiórki kokosowe"}, {"id": "ananas", "label": "Ananas"}, {"id": "brokul", "label": "Brokuł"}, {"id": "gruszka", "label": "Gruszka"}, {"id": "kielki", "label": "Kiełki"}, {"id": "mango", "label": "Mango"}, {"id": "musztarda", "label": "Musztarda"}, {"id": "oliwki", "label": "Oliwki"}, {"id": "platki-jaglane", "label": "Płatki jaglane"}, {"id": "dynia", "label": "Dynia"}, {"id": "grana-padano", "label": "Grana padano"}, {"id": "kapusta", "label": "Kapusta"}, {"id": "pietruszka-korzen", "label": "Pietruszka korzeń"}, {"id": "platki-drozdzowe", "label": "Płatki drożdżowe"}, {"id": "slonecznik", "label": "Słonecznik"}, {"id": "baton", "label": "Baton / przekąska"}, {"id": "burak", "label": "Burak"}, {"id": "gouda", "label": "Gouda"}, {"id": "halloumi", "label": "Halloumi"}, {"id": "hummus", "label": "Hummus"}, {"id": "limonka", "label": "Limonka"}, {"id": "mleczko-kokosowe", "label": "Mleczko kokosowe"}, {"id": "chia", "label": "Nasiona chia"}, {"id": "pomarancza", "label": "Pomarańcza"}, {"id": "pomidory-suszone", "label": "Pomidory suszone"}, {"id": "siemie-lniane", "label": "Siemię lniane"}, {"id": "bagietka", "label": "Bagietka"}, {"id": "batat", "label": "Batat"}, {"id": "daktyle", "label": "Daktyle"}, {"id": "kuskus", "label": "Kasza kuskus"}, {"id": "kukurydza", "label": "Kukurydza"}, {"id": "mandarynka", "label": "Mandarynka"}, {"id": "ogorki-kiszone", "label": "Ogórki kiszone"}, {"id": "papryczka-chili", "label": "Papryczka chili"}, {"id": "pesto", "label": "Pesto"}, {"id": "plastry-wegan", "label": "Plastry wegańskie"}, {"id": "platki-inne", "label": "Płatki inne"}, {"id": "smoothie", "label": "Smoothie / sok"}, {"id": "syrop-agawa", "label": "Syrop z agawy"}, {"id": "wafle", "label": "Wafle ryżowe"}, {"id": "chrzan", "label": "Chrzan"}, {"id": "ciasto-nalesniki", "label": "Ciasto na naleśniki"}, {"id": "dorsz", "label": "Dorsz"}, {"id": "kiwi", "label": "Kiwi"}, {"id": "olej-kokosowy", "label": "Olej kokosowy"}, {"id": "papryka-konserwowa", "label": "Papryka konserwowa"}, {"id": "sezam", "label": "Sezam"}, {"id": "sos-ostry", "label": "Sos ostry / rybny"}, {"id": "wisnie", "label": "Wiśnie"}, {"id": "zurawina", "label": "Żurawina"}, {"id": "biszkopty", "label": "Biszkopty"}, {"id": "budyn", "label": "Budyń"}, {"id": "camembert", "label": "Camembert"}, {"id": "jagody", "label": "Jagody"}, {"id": "ketchup", "label": "Ketchup"}, {"id": "olej-sezamowy", "label": "Olej sezamowy"}, {"id": "parowki", "label": "Parówki roślinne"}, {"id": "porzeczki", "label": "Porzeczki"}, {"id": "pstrag", "label": "Pstrąg"}, {"id": "pudding", "label": "Pudding proteinowy"}, {"id": "ser-plesniowy", "label": "Ser pleśniowy"}, {"id": "tahini", "label": "Tahini"}, {"id": "smietanka", "label": "Śmietanka"}, {"id": "bajgiel", "label": "Bajgiel"}, {"id": "bulka-tarta", "label": "Bułka tarta"}, {"id": "bob", "label": "Bób"}, {"id": "cheddar", "label": "Cheddar"}, {"id": "grejpfrut", "label": "Grejpfrut"}, {"id": "groszek", "label": "Groszek"}, {"id": "kabanosy", "label": "Kabanosy roślinne"}, {"id": "kaki", "label": "Kaki"}, {"id": "kaszanka", "label": "Kaszanka roślinna"}, {"id": "kawa", "label": "Kawa"}, {"id": "kielbaski", "label": "Kiełbaski roślinne"}, {"id": "komosa", "label": "Komosa ryżowa"}, {"id": "makrela", "label": "Makrela"}, {"id": "maslanka", "label": "Maślanka"}, {"id": "melon", "label": "Melon"}, {"id": "mintaj", "label": "Mintaj"}, {"id": "miso", "label": "Miso"}, {"id": "mieso-wegan", "label": "Mięso wegańskie"}, {"id": "owoce-mrozone", "label": "Owoce mrożone"}, {"id": "owsianka-instant", "label": "Owsianka instant"}, {"id": "papier-ryzowy", "label": "Papier ryżowy"}, {"id": "pasta-warzywna", "label": "Pasta warzywna"}, {"id": "gyoza", "label": "Pierożki gyoza"}, {"id": "pistacje", "label": "Pistacje"}, {"id": "ser-zolty", "label": "Ser żółty"}, {"id": "serek-proteinowy", "label": "Serek proteinowy"}, {"id": "sok", "label": "Sok"}, {"id": "zupa-gotowa", "label": "Zupa gotowa"}]};</script>
