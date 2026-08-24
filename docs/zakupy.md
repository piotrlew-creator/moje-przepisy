---
title: Lista zakupów
hide:
  - toc
---

# Lista zakupów

Zaznacz dania, które planujesz w tym tygodniu, ustaw przy każdym liczbę porcji — a złożę z tego jedną listę i jeden PDF. Te same produkty z różnych przepisów sumują się.

<div class="p-koszyk" id="koszyk">
<div class="p-koszyk__pick">
<div class="p-searchrow">
<div class="p-search"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg><input type="search" id="z-search" inputmode="search" placeholder="Szukaj dania…" aria-label="Szukaj dania"><button type="button" class="p-search__x" id="z-search-clear" aria-label="Wyczyść wyszukiwanie" hidden>&times;</button></div>
</div>
<div class="p-slotbar" role="group" aria-label="Pora posiłku">
<button type="button" class="p-chip" data-z-slot="all" data-on="1" aria-pressed="true">Wszystkie</button>
<button type="button" class="p-chip p-chip--slot1" data-z-slot="sniadanie" aria-pressed="false"><span class="p-dot"></span>Śniadanie</button>
<button type="button" class="p-chip p-chip--slot2" data-z-slot="obiad" aria-pressed="false"><span class="p-dot"></span>Obiad</button>
<button type="button" class="p-chip p-chip--slot3" data-z-slot="kolacja" aria-pressed="false"><span class="p-dot"></span>Kolacja</button>
</div>
<p class="p-hint" id="z-hint">Wczytuję przepisy…</p>
<ul class="p-zlist" id="z-list"></ul>
</div>
<div class="p-koszyk__cart">
<div class="p-ings__head">
<h2 style="margin:0">Wybrane dania <span class="p-num" id="z-count"></span></h2>
<button type="button" class="p-btn p-btn--ghost" id="z-clear" style="min-height:auto;padding:6px 8px" hidden>Wyczyść</button>
</div>
<p class="p-empty" id="z-empty">Nic jeszcze nie wybrałeś. Dodaj dania z listy obok — lista zakupów złoży się sama.</p>
<ul class="p-zcart" id="z-cart"></ul>
<div class="p-actions" id="z-actions" hidden>
<button type="button" class="p-btn p-btn--block" id="z-reset">Odznacz kupione</button>
<button type="button" class="p-btn p-btn--primary p-btn--block" id="z-pdf">Wygeneruj PDF</button>
</div>
<div class="p-sheet__body" id="z-body"></div>
</div>
</div>
<div class="p-toast" id="toast" role="status" data-on="0"></div>

<noscript><p class="p-note">Zbiorcza lista zakupów wymaga JavaScriptu. Listę dla pojedynczego dania znajdziesz na stronie każdego przepisu.</p></noscript>

<script>window.UNITS = {"łyżka":["łyżka","łyżki","łyżek","łyżki"],"łyżeczka":["łyżeczka","łyżeczki","łyżeczek","łyżeczki"],"sztuka":["sztuka","sztuki","sztuk","sztuki"],"garść":["garść","garście","garści","garści"],"kromka":["kromka","kromki","kromek","kromki"],"plaster":["plaster","plastry","plastrów","plastra"],"szklanka":["szklanka","szklanki","szklanek","szklanki"],"opakowanie":["opakowanie","opakowania","opakowań","opakowania"],"ząbek":["ząbek","ząbki","ząbków","ząbka"],"szczypta":["szczypta","szczypty","szczypt","szczypty"],"porcja":["porcja","porcje","porcji","porcji"],"puszka":["puszka","puszki","puszek","puszki"],"kostka":["kostka","kostki","kostek","kostki"],"listek":["listek","listki","listków","listka"],"łodyga":["łodyga","łodygi","łodyg","łodygi"]};</script>
