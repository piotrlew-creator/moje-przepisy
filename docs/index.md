---
hide:
  - toc
---

# Co dziś jesz?

Wybierz porę posiłku, zaznacz produkty, na które masz ochotę — albo po prostu przewiń wszystkie 40 przepisów z Twojego planu.

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
<label class="p-chip" data-rank="top" data-label="Jajka"><input type="checkbox" value="jajka">Jajka <span class="p-num" style="opacity:.55">4</span></label>
<label class="p-chip" data-rank="top" data-label="Makaron"><input type="checkbox" value="makaron">Makaron <span class="p-num" style="opacity:.55">4</span></label>
<label class="p-chip" data-rank="top" data-label="Ryż"><input type="checkbox" value="ryz">Ryż <span class="p-num" style="opacity:.55">3</span></label>
<label class="p-chip" data-rank="top" data-label="Kasza"><input type="checkbox" value="kasza">Kasza <span class="p-num" style="opacity:.55">2</span></label>
<label class="p-chip" data-rank="top" data-label="Płatki owsiane"><input type="checkbox" value="platki-owsiane">Płatki owsiane <span class="p-num" style="opacity:.55">3</span></label>
<label class="p-chip" data-rank="top" data-label="Chleb"><input type="checkbox" value="chleb">Chleb <span class="p-num" style="opacity:.55">10</span></label>
<label class="p-chip" data-rank="top" data-label="Banan"><input type="checkbox" value="banan">Banan <span class="p-num" style="opacity:.55">5</span></label>
<label class="p-chip" data-rank="top" data-label="Jabłko"><input type="checkbox" value="jablko">Jabłko <span class="p-num" style="opacity:.55">2</span></label>
<label class="p-chip" data-rank="top" data-label="Gruszka"><input type="checkbox" value="gruszka">Gruszka <span class="p-num" style="opacity:.55">3</span></label>
<label class="p-chip" data-rank="top" data-label="Pomidor"><input type="checkbox" value="pomidor">Pomidor <span class="p-num" style="opacity:.55">9</span></label>
<label class="p-chip" data-rank="top" data-label="Ogórek"><input type="checkbox" value="ogorek">Ogórek <span class="p-num" style="opacity:.55">6</span></label>
<label class="p-chip" data-rank="top" data-label="Papryka"><input type="checkbox" value="papryka">Papryka <span class="p-num" style="opacity:.55">3</span></label>
<label class="p-chip" data-rank="top" data-label="Szpinak"><input type="checkbox" value="szpinak">Szpinak <span class="p-num" style="opacity:.55">5</span></label>
<label class="p-chip" data-rank="top" data-label="Pieczarki"><input type="checkbox" value="pieczarki">Pieczarki <span class="p-num" style="opacity:.55">2</span></label>
<label class="p-chip" data-rank="top" data-label="Awokado"><input type="checkbox" value="awokado">Awokado <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="top" data-label="Mozzarella"><input type="checkbox" value="mozzarella">Mozzarella <span class="p-num" style="opacity:.55">4</span></label>
<label class="p-chip" data-rank="top" data-label="Serek wiejski"><input type="checkbox" value="serek-wiejski">Serek wiejski <span class="p-num" style="opacity:.55">2</span></label>
<label class="p-chip" data-rank="top" data-label="Tofu"><input type="checkbox" value="tofu">Tofu <span class="p-num" style="opacity:.55">3</span></label>
<label class="p-chip" data-rank="top" data-label="Orzechy"><input type="checkbox" value="orzechy">Orzechy <span class="p-num" style="opacity:.55">10</span></label>
<label class="p-chip" data-rank="top" data-label="Masło orzechowe"><input type="checkbox" value="maslo-orzechowe">Masło orzechowe <span class="p-num" style="opacity:.55">5</span></label>
<label class="p-chip" data-rank="rest" data-label="Oliwa / olej" hidden><input type="checkbox" value="oliwa">Oliwa / olej <span class="p-num" style="opacity:.55">9</span></label>
<label class="p-chip" data-rank="rest" data-label="Czosnek" hidden><input type="checkbox" value="czosnek">Czosnek <span class="p-num" style="opacity:.55">8</span></label>
<label class="p-chip" data-rank="rest" data-label="Odżywka białkowa" hidden><input type="checkbox" value="odzywka">Odżywka białkowa <span class="p-num" style="opacity:.55">8</span></label>
<label class="p-chip" data-rank="rest" data-label="Cebula" hidden><input type="checkbox" value="cebula">Cebula <span class="p-num" style="opacity:.55">7</span></label>
<label class="p-chip" data-rank="rest" data-label="Jogurt / skyr" hidden><input type="checkbox" value="jogurt">Jogurt / skyr <span class="p-num" style="opacity:.55">5</span></label>
<label class="p-chip" data-rank="rest" data-label="Marchewka" hidden><input type="checkbox" value="marchewka">Marchewka <span class="p-num" style="opacity:.55">5</span></label>
<label class="p-chip" data-rank="rest" data-label="Mleko roślinne" hidden><input type="checkbox" value="mleko">Mleko roślinne <span class="p-num" style="opacity:.55">5</span></label>
<label class="p-chip" data-rank="rest" data-label="Cytryna" hidden><input type="checkbox" value="cytryna">Cytryna <span class="p-num" style="opacity:.55">4</span></label>
<label class="p-chip" data-rank="rest" data-label="Sałata / rukola / roszponka" hidden><input type="checkbox" value="salata">Sałata / rukola / roszponka <span class="p-num" style="opacity:.55">4</span></label>
<label class="p-chip" data-rank="rest" data-label="Baton / przekąska" hidden><input type="checkbox" value="baton">Baton / przekąska <span class="p-num" style="opacity:.55">3</span></label>
<label class="p-chip" data-rank="rest" data-label="Bułka / grahamka" hidden><input type="checkbox" value="bulka">Bułka / grahamka <span class="p-num" style="opacity:.55">3</span></label>
<label class="p-chip" data-rank="rest" data-label="Grana padano" hidden><input type="checkbox" value="grana-padano">Grana padano <span class="p-num" style="opacity:.55">3</span></label>
<label class="p-chip" data-rank="rest" data-label="Pomidory z puszki / passata" hidden><input type="checkbox" value="pomidory-puszka">Pomidory z puszki / passata <span class="p-num" style="opacity:.55">3</span></label>
<label class="p-chip" data-rank="rest" data-label="Smoothie / sok" hidden><input type="checkbox" value="smoothie">Smoothie / sok <span class="p-num" style="opacity:.55">3</span></label>
<label class="p-chip" data-rank="rest" data-label="Brokuł" hidden><input type="checkbox" value="brokul">Brokuł <span class="p-num" style="opacity:.55">2</span></label>
<label class="p-chip" data-rank="rest" data-label="Ciecierzyca" hidden><input type="checkbox" value="ciecierzyca">Ciecierzyca <span class="p-num" style="opacity:.55">2</span></label>
<label class="p-chip" data-rank="rest" data-label="Daktyle" hidden><input type="checkbox" value="daktyle">Daktyle <span class="p-num" style="opacity:.55">2</span></label>
<label class="p-chip" data-rank="rest" data-label="Kakao" hidden><input type="checkbox" value="kakao">Kakao <span class="p-num" style="opacity:.55">2</span></label>
<label class="p-chip" data-rank="rest" data-label="Majonez" hidden><input type="checkbox" value="majonez">Majonez <span class="p-num" style="opacity:.55">2</span></label>
<label class="p-chip" data-rank="rest" data-label="Mandarynka" hidden><input type="checkbox" value="mandarynka">Mandarynka <span class="p-num" style="opacity:.55">2</span></label>
<label class="p-chip" data-rank="rest" data-label="Masło / margaryna" hidden><input type="checkbox" value="maslo">Masło / margaryna <span class="p-num" style="opacity:.55">2</span></label>
<label class="p-chip" data-rank="rest" data-label="Mleczko kokosowe" hidden><input type="checkbox" value="mleczko-kokosowe">Mleczko kokosowe <span class="p-num" style="opacity:.55">2</span></label>
<label class="p-chip" data-rank="rest" data-label="Mąka" hidden><input type="checkbox" value="maka">Mąka <span class="p-num" style="opacity:.55">2</span></label>
<label class="p-chip" data-rank="rest" data-label="Rzodkiewka" hidden><input type="checkbox" value="rzodkiewka">Rzodkiewka <span class="p-num" style="opacity:.55">2</span></label>
<label class="p-chip" data-rank="rest" data-label="Seler naciowy" hidden><input type="checkbox" value="seler">Seler naciowy <span class="p-num" style="opacity:.55">2</span></label>
<label class="p-chip" data-rank="rest" data-label="Serek śmietankowy" hidden><input type="checkbox" value="serek-smietankowy">Serek śmietankowy <span class="p-num" style="opacity:.55">2</span></label>
<label class="p-chip" data-rank="rest" data-label="Syrop z agawy" hidden><input type="checkbox" value="syrop-agawa">Syrop z agawy <span class="p-num" style="opacity:.55">2</span></label>
<label class="p-chip" data-rank="rest" data-label="Twaróg" hidden><input type="checkbox" value="twarog">Twaróg <span class="p-num" style="opacity:.55">2</span></label>
<label class="p-chip" data-rank="rest" data-label="Wafle ryżowe" hidden><input type="checkbox" value="wafle">Wafle ryżowe <span class="p-num" style="opacity:.55">2</span></label>
<label class="p-chip" data-rank="rest" data-label="Ziemniaki" hidden><input type="checkbox" value="ziemniaki">Ziemniaki <span class="p-num" style="opacity:.55">2</span></label>
<label class="p-chip" data-rank="rest" data-label="Ananas" hidden><input type="checkbox" value="ananas">Ananas <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Bagietka" hidden><input type="checkbox" value="bagietka">Bagietka <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Czekolada gorzka" hidden><input type="checkbox" value="czekolada">Czekolada gorzka <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Dynia" hidden><input type="checkbox" value="dynia">Dynia <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Feta" hidden><input type="checkbox" value="feta">Feta <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Gouda" hidden><input type="checkbox" value="gouda">Gouda <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Hummus" hidden><input type="checkbox" value="hummus">Hummus <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Kabanosy roślinne" hidden><input type="checkbox" value="kabanosy">Kabanosy roślinne <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Kaki" hidden><input type="checkbox" value="kaki">Kaki <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Kaszanka roślinna" hidden><input type="checkbox" value="kaszanka">Kaszanka roślinna <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Kiełki" hidden><input type="checkbox" value="kielki">Kiełki <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Kukurydza" hidden><input type="checkbox" value="kukurydza">Kukurydza <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Miód" hidden><input type="checkbox" value="miod">Miód <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Nasiona chia" hidden><input type="checkbox" value="chia">Nasiona chia <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Ogórki kiszone" hidden><input type="checkbox" value="ogorki-kiszone">Ogórki kiszone <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Oliwki" hidden><input type="checkbox" value="oliwki">Oliwki <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Owsianka instant" hidden><input type="checkbox" value="owsianka-instant">Owsianka instant <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Pasta warzywna" hidden><input type="checkbox" value="pasta-warzywna">Pasta warzywna <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Pesto" hidden><input type="checkbox" value="pesto">Pesto <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Pierożki gyoza" hidden><input type="checkbox" value="gyoza">Pierożki gyoza <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Pomidory suszone" hidden><input type="checkbox" value="pomidory-suszone">Pomidory suszone <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Pstrąg wędzony" hidden><input type="checkbox" value="pstrag">Pstrąg wędzony <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Płatki jaglane" hidden><input type="checkbox" value="platki-jaglane">Płatki jaglane <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Soczewica" hidden><input type="checkbox" value="soczewica">Soczewica <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Sos sojowy" hidden><input type="checkbox" value="sos-sojowy">Sos sojowy <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Słonecznik" hidden><input type="checkbox" value="slonecznik">Słonecznik <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Tahini" hidden><input type="checkbox" value="tahini">Tahini <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Wiórki kokosowe" hidden><input type="checkbox" value="wiorki">Wiórki kokosowe <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Zupa gotowa" hidden><input type="checkbox" value="zupa-gotowa">Zupa gotowa <span class="p-num" style="opacity:.55">1</span></label>
<label class="p-chip" data-rank="rest" data-label="Śmietanka" hidden><input type="checkbox" value="smietanka">Śmietanka <span class="p-num" style="opacity:.55">1</span></label>
</div>
<p class="p-hint" id="ing-hint">Widzisz 20 najczęstszych składników. Pozostałe 60 znajdziesz przez wyszukiwanie.</p>
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
<article class="p-card" data-slot="1" data-slot-id="sniadanie" data-tags="baton kabanosy pomidor">
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
</ul>

<script>window.RECIPES = {"count": 40, "ingredients": [{"id": "chleb", "label": "Chleb"}, {"id": "orzechy", "label": "Orzechy"}, {"id": "oliwa", "label": "Oliwa / olej"}, {"id": "pomidor", "label": "Pomidor"}, {"id": "czosnek", "label": "Czosnek"}, {"id": "odzywka", "label": "Odżywka białkowa"}, {"id": "cebula", "label": "Cebula"}, {"id": "ogorek", "label": "Ogórek"}, {"id": "banan", "label": "Banan"}, {"id": "jogurt", "label": "Jogurt / skyr"}, {"id": "marchewka", "label": "Marchewka"}, {"id": "maslo-orzechowe", "label": "Masło orzechowe"}, {"id": "mleko", "label": "Mleko roślinne"}, {"id": "szpinak", "label": "Szpinak"}, {"id": "cytryna", "label": "Cytryna"}, {"id": "jajka", "label": "Jajka"}, {"id": "makaron", "label": "Makaron"}, {"id": "mozzarella", "label": "Mozzarella"}, {"id": "salata", "label": "Sałata / rukola / roszponka"}, {"id": "baton", "label": "Baton / przekąska"}, {"id": "bulka", "label": "Bułka / grahamka"}, {"id": "grana-padano", "label": "Grana padano"}, {"id": "gruszka", "label": "Gruszka"}, {"id": "papryka", "label": "Papryka"}, {"id": "pomidory-puszka", "label": "Pomidory z puszki / passata"}, {"id": "platki-owsiane", "label": "Płatki owsiane"}, {"id": "ryz", "label": "Ryż"}, {"id": "smoothie", "label": "Smoothie / sok"}, {"id": "tofu", "label": "Tofu"}, {"id": "brokul", "label": "Brokuł"}, {"id": "ciecierzyca", "label": "Ciecierzyca"}, {"id": "daktyle", "label": "Daktyle"}, {"id": "jablko", "label": "Jabłko"}, {"id": "kakao", "label": "Kakao"}, {"id": "kasza", "label": "Kasza"}, {"id": "majonez", "label": "Majonez"}, {"id": "mandarynka", "label": "Mandarynka"}, {"id": "maslo", "label": "Masło / margaryna"}, {"id": "mleczko-kokosowe", "label": "Mleczko kokosowe"}, {"id": "maka", "label": "Mąka"}, {"id": "pieczarki", "label": "Pieczarki"}, {"id": "rzodkiewka", "label": "Rzodkiewka"}, {"id": "seler", "label": "Seler naciowy"}, {"id": "serek-wiejski", "label": "Serek wiejski"}, {"id": "serek-smietankowy", "label": "Serek śmietankowy"}, {"id": "syrop-agawa", "label": "Syrop z agawy"}, {"id": "twarog", "label": "Twaróg"}, {"id": "wafle", "label": "Wafle ryżowe"}, {"id": "ziemniaki", "label": "Ziemniaki"}, {"id": "ananas", "label": "Ananas"}, {"id": "awokado", "label": "Awokado"}, {"id": "bagietka", "label": "Bagietka"}, {"id": "czekolada", "label": "Czekolada gorzka"}, {"id": "dynia", "label": "Dynia"}, {"id": "feta", "label": "Feta"}, {"id": "gouda", "label": "Gouda"}, {"id": "hummus", "label": "Hummus"}, {"id": "kabanosy", "label": "Kabanosy roślinne"}, {"id": "kaki", "label": "Kaki"}, {"id": "kaszanka", "label": "Kaszanka roślinna"}, {"id": "kielki", "label": "Kiełki"}, {"id": "kukurydza", "label": "Kukurydza"}, {"id": "miod", "label": "Miód"}, {"id": "chia", "label": "Nasiona chia"}, {"id": "ogorki-kiszone", "label": "Ogórki kiszone"}, {"id": "oliwki", "label": "Oliwki"}, {"id": "owsianka-instant", "label": "Owsianka instant"}, {"id": "pasta-warzywna", "label": "Pasta warzywna"}, {"id": "pesto", "label": "Pesto"}, {"id": "gyoza", "label": "Pierożki gyoza"}, {"id": "pomidory-suszone", "label": "Pomidory suszone"}, {"id": "pstrag", "label": "Pstrąg wędzony"}, {"id": "platki-jaglane", "label": "Płatki jaglane"}, {"id": "soczewica", "label": "Soczewica"}, {"id": "sos-sojowy", "label": "Sos sojowy"}, {"id": "slonecznik", "label": "Słonecznik"}, {"id": "tahini", "label": "Tahini"}, {"id": "wiorki", "label": "Wiórki kokosowe"}, {"id": "zupa-gotowa", "label": "Zupa gotowa"}, {"id": "smietanka", "label": "Śmietanka"}]};</script>
