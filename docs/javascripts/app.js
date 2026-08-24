/* ==========================================================================
   Przepisy Dietetyczne — logika strony
   --------------------------------------------------------------------------
   Trzy niezależne kawałki, wszystkie inicjowane przez boot():
     1. wyszukiwarka na stronie głównej (pora dnia + składniki),
     2. przepis (przelicznik porcji, zamienniki, lista zakupów, PDF),
     3. tryb gotowania (jeden krok na ekran).

   Stan (liczba osób, wybrane zamienniki, odhaczone zakupy, numer kroku,
   filtry) trzymamy w localStorage, żeby przypadkowe odświeżenie w trakcie
   gotowania niczego nie gubiło.
   ========================================================================== */
(function () {
  "use strict";

  var BASE = (function () {
    var s = document.currentScript && document.currentScript.src;
    return s ? s.replace(/javascripts\/app\.js.*$/, "") : "/";
  })();

  var LS = {
    get: function (k, fb) {
      try {
        var v = localStorage.getItem("przepisy:" + k);
        return v === null ? fb : JSON.parse(v);
      } catch (e) {
        return fb;
      }
    },
    set: function (k, v) {
      try {
        localStorage.setItem("przepisy:" + k, JSON.stringify(v));
      } catch (e) {
        /* tryb prywatny albo brak miejsca — działamy dalej bez zapisu */
      }
    },
    del: function (k) {
      try {
        localStorage.removeItem("przepisy:" + k);
      } catch (e) {
        /* jw. */
      }
    },
  };

  // Zapisuje albo kasuje klucz — żeby wartości domyślne nie zaśmiecały pamięci.
  function remember(key, value, worthKeeping) {
    if (worthKeeping) LS.set(key, value);
    else LS.del(key);
  }

  /* ---------------------------------------------------------- liczebniki -- */

  // Polski wybiera trzy formy: 1 łyżka, 2–4 łyżki, 5+ łyżek — z wyjątkiem
  // nastek (12 łyżek, nie „12 łyżki”). Ułamki biorą dopełniacz: 0.5 łyżki.
  function plural(n, forms) {
    if (!Number.isInteger(n)) return forms[3] || forms[1];
    if (n === 1) return forms[0];
    var last1 = Math.abs(n) % 10;
    var last2 = Math.abs(n) % 100;
    if (last1 >= 2 && last1 <= 4 && !(last2 >= 12 && last2 <= 14)) return forms[1];
    return forms[2];
  }

  function personWord(n) {
    return plural(n, ["osoba", "osoby", "osób", "osoby"]);
  }

  function fmtQty(n) {
    var r = Math.round(n * 100) / 100;
    return Number.isInteger(r) ? String(r) : String(parseFloat(r.toFixed(2)));
  }

  function fmtGrams(n) {
    if (n < 10) return String(parseFloat((Math.round(n * 10) / 10).toFixed(1)));
    return String(Math.round(n));
  }

  /* ------------------------------------------------ dopasowanie przybliżone */

  function norm(s) {
    return s.toLowerCase()
      .normalize("NFD").replace(/[̀-ͯ]/g, "")
      .replace(/ł/g, "l");
  }

  // Odległość Levenshteina — pozwala podpowiedzieć „Pomidor” na „pomdor”.
  function distance(a, b) {
    var prev = [], cur = [], i, j;
    for (j = 0; j <= b.length; j++) prev[j] = j;
    for (i = 1; i <= a.length; i++) {
      cur[0] = i;
      for (j = 1; j <= b.length; j++) {
        cur[j] = Math.min(
          prev[j] + 1,
          cur[j - 1] + 1,
          prev[j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1)
        );
      }
      prev = cur.slice();
    }
    return prev[b.length];
  }

  // 0 = trafienie dosłowne, 1..n = literówka, Infinity = nie pasuje.
  function matchScore(label, query) {
    var l = norm(label), q = norm(query);
    if (!q) return 0;
    var at = l.indexOf(q);
    if (at === 0) return 0;
    // Przy jednym–dwóch znakach szukamy tylko na początku słowa i bez
    // tolerancji literówek. Inaczej „a” pasowało do 97 etykiet, czyli po
    // wpisaniu pierwszego znaku lista robiła się dłuższa, nie krótsza.
    if (q.length <= 2) {
      var naPoczatku = l.split(/[\s/]+/).some(function (word) {
        return word.indexOf(q) === 0;
      });
      return naPoczatku ? 0.5 : Infinity;
    }
    if (at > 0) return 0.5;
    var tolerance = q.length <= 3 ? 1 : q.length <= 6 ? 2 : 3;
    var best = Infinity;
    l.split(/[\s/]+/).forEach(function (word) {
      // porównujemy z początkiem słowa o długości zapytania (±1 znak),
      // żeby „pomdor” trafiło w „pomidor”, a nie w całą etykietę
      for (var len = Math.max(1, q.length - 1); len <= q.length + 1; len++) {
        var d = distance(word.slice(0, len), q);
        if (d < best) best = d;
      }
    });
    return best <= tolerance ? 1 + best : Infinity;
  }

  /* ================================================== STRONA GŁÓWNA ======== */

  function initFinder() {
    var root = document.getElementById("finder");
    if (!root) return;

    var cards = [].slice.call(document.querySelectorAll("#recipes .p-card"));
    var slotChips = [].slice.call(root.querySelectorAll("[data-slot-filter]"));
    var ingChips = [].slice.call(document.querySelectorAll("#ing-chips .p-chip"));
    var search = document.getElementById("ing-search");
    var searchClear = document.getElementById("search-clear");
    var hint = document.getElementById("ing-hint");
    var hintText = hint ? hint.textContent : "";
    var countEl = document.getElementById("result-count");
    var clearEl = document.getElementById("clear-filters");
    var clearCount = document.getElementById("clear-count");
    var emptyEl = document.getElementById("empty-state");
    var panel = document.getElementById("ing-panel");
    var stateEl = document.getElementById("ing-state");

    // Pora posiłku startuje zawsze na „Wszystkie” — zawężenie do śniadania,
    // obiadu czy kolacji ma być świadomym wyborem, a nie stanem odziedziczonym
    // po poprzedniej wizycie. Zaznaczone składniki pamiętamy dalej.
    // Zapisany składnik, którego już nie ma w danych (bo zmienił się plan),
    // dawał „0 przepisów” i licznik „Wyczyść (1)” przy żadnym zaznaczonym
    // kafelku — ślepy zaułek bez widocznej przyczyny. Odsiewamy je.
    var znane = {};
    ingChips.forEach(function (c) { znane[c.querySelector("input").value] = true; });
    var saved = LS.get("filters", { ings: [] });
    var state = {
      slot: "all",
      ings: (saved.ings || []).filter(function (id) { return znane[id]; }),
    };

    // Ile przepisów w danej porze posiłku zawiera dany składnik.
    var countsBySlot = { all: {} };
    cards.forEach(function (card) {
      var slot = card.getAttribute("data-slot-id");
      countsBySlot[slot] = countsBySlot[slot] || {};
      (card.getAttribute("data-tags") || "").split(" ").forEach(function (t) {
        if (!t) return;
        countsBySlot.all[t] = (countsBySlot.all[t] || 0) + 1;
        countsBySlot[slot][t] = (countsBySlot[slot][t] || 0) + 1;
      });
    });

    function countFor(tag) {
      return (countsBySlot[state.slot] || {})[tag] || 0;
    }

    slotChips.forEach(function (chip) {
      var on = chip.getAttribute("data-slot-filter") === state.slot;
      chip.setAttribute("data-on", on ? "1" : "0");
      chip.setAttribute("aria-pressed", on ? "true" : "false");
      chip.addEventListener("click", function () {
        state.slot = chip.getAttribute("data-slot-filter");
        slotChips.forEach(function (c) {
          var sel = c === chip;
          c.setAttribute("data-on", sel ? "1" : "0");
          c.setAttribute("aria-pressed", sel ? "true" : "false");
        });
        // Składnik, którego nie ma w wybranej porze posiłku, zostaje
        // odznaczony — inaczej wynik byłby pusty bez widocznej przyczyny.
        ingChips.forEach(function (c) {
          var input = c.querySelector("input");
          if (input.checked && countFor(input.value) === 0) {
            input.checked = false;
            c.setAttribute("data-on", "0");
          }
        });
        state.ings = checkedIngredients();
        apply();
      });
    });

    function checkedIngredients() {
      return ingChips
        .map(function (c) { return c.querySelector("input"); })
        .filter(function (i) { return i.checked; })
        .map(function (i) { return i.value; });
    }

    ingChips.forEach(function (chip) {
      var input = chip.querySelector("input");
      input.checked = state.ings.indexOf(input.value) !== -1;
      chip.setAttribute("data-on", input.checked ? "1" : "0");
      input.addEventListener("change", function () {
        chip.setAttribute("data-on", input.checked ? "1" : "0");
        state.ings = checkedIngredients();
        apply();
      });
    });

    // Widoczność kafelka składnika zależy od dwóch rzeczy: czy występuje
    // w wybranej porze posiłku i czy pasuje do wpisanego zapytania.
    // Bez zapytania pokazujemy kluczowe składniki plus już zaznaczone.
    function renderChips() {
      var q = search ? search.value.trim() : "";
      var exact = 0, fuzzy = [], available = 0;
      ingChips.forEach(function (chip) {
        var input = chip.querySelector("input");
        var label = chip.getAttribute("data-label") || "";
        var n = countFor(input.value);
        var badge = chip.querySelector(".p-num");
        if (badge) badge.textContent = n;

        if (n === 0) {
          chip.hidden = true;
          return;
        }
        available++;
        if (!q) {
          chip.hidden = chip.getAttribute("data-rank") !== "top" && !input.checked;
          return;
        }
        var score = matchScore(label, q);
        chip.hidden = score === Infinity;
        if (score <= 0.5) exact++;
        else if (score < Infinity) fuzzy.push(label);
      });

      if (searchClear) searchClear.hidden = !q;
      if (hint) {
        if (q && exact === 0 && fuzzy.length) {
          hint.textContent = "Nie znaleziono „" + q + "”. Może chodziło o: " +
            fuzzy.slice(0, 3).join(", ") + "?";
        } else if (q && exact === 0) {
          hint.textContent = "Brak składnika pasującego do „" + q + "”.";
        } else if (q) {
          hint.textContent = "";
        } else if (state.slot === "all") {
          hint.textContent = hintText;
        } else {
          var meal = document.querySelector('[data-slot-filter="' + state.slot + '"]');
          var mealName = meal ? (meal.getAttribute("data-slot-label") || "") : "";
          hint.textContent = available + " " +
            plural(available, ["składnik", "składniki", "składników", "składnika"]) +
            " występujących w kategorii " + mealName +
            ". Resztę zobaczysz po powrocie do „Wszystkie”.";
        }
      }
    }

    if (search) {
      search.addEventListener("input", renderChips);
    }
    if (searchClear) {
      searchClear.addEventListener("click", function () {
        search.value = "";
        renderChips();
        search.focus();
      });
    }

    if (clearEl) {
      clearEl.addEventListener("click", function () {
        state.ings = [];
        ingChips.forEach(function (c) {
          c.querySelector("input").checked = false;
          c.setAttribute("data-on", "0");
        });
        if (search) search.value = "";
        renderChips();
        apply();
      });
    }

    // Pora dnia zawęża, składniki poszerzają: przepis pasuje, gdy jest we
    // właściwym posiłku ORAZ zawiera CHOĆ JEDEN z zaznaczonych składników.
    function apply() {
      var shown = 0;
      cards.forEach(function (card) {
        var slotOk = state.slot === "all" || card.getAttribute("data-slot-id") === state.slot;
        var tags = (card.getAttribute("data-tags") || "").split(" ");
        var ingOk = state.ings.length === 0 || state.ings.some(function (t) {
          return tags.indexOf(t) !== -1;
        });
        var ok = slotOk && ingOk;
        card.parentElement.hidden = !ok;
        if (ok) shown++;
      });

      countEl.textContent = shown + " " +
        plural(shown, ["przepis", "przepisy", "przepisów", "przepisu"]);
      emptyEl.hidden = shown !== 0;

      var n = state.ings.length;
      if (clearEl) {
        clearEl.hidden = n === 0;
        if (clearCount) clearCount.textContent = n ? "(" + n + ")" : "";
      }
      if (stateEl) {
        stateEl.textContent = n
          ? n + " " + plural(n, ["wybrany", "wybrane", "wybranych", "wybranego"])
          : "wybierz składniki";
        stateEl.setAttribute("data-active", n ? "1" : "0");
      }
      // Zapisujemy tylko składniki — pora posiłku zawsze startuje od
      // „Wszystkie”.
      LS.set("filters", { ings: state.ings });
      renderChips();
    }

    if (panel && state.ings.length) panel.open = true;
    apply();
  }

  /* ======================================================= PRZEPIS ========= */

  function initRecipe() {
    var data = window.RECIPE;
    if (!data) return;

    var units = window.UNITS || {};
    var groups = window.SWAPS || {};
    var adjectives = window.SWAP_ADJ || {};
    var minus = document.getElementById("srv-minus");
    var plus = document.getElementById("srv-plus");
    var num = document.getElementById("srv-num");
    var word = document.getElementById("srv-word");
    var list = document.getElementById("ing-list");
    var heading = document.getElementById("ing-heading");
    var note = document.getElementById("srv-note");
    var stepsList = document.getElementById("steps-list");
    var swapReset = document.getElementById("swap-reset");

    var servings = LS.get("servings:" + data.slug, 1);
    if (!(servings >= 1)) servings = 1;
    servings = Math.min(12, Math.round(servings));

    // Zapisany wybór zamienników jest kluczowany numerem składnika, więc po
    // dodaniu nowego planu (inna kolejność albo liczba składników w tym samym
    // przepisie) stary klucz wskazywałby w pustkę i render przerywałby się
    // wyjątkiem — po cichu, bo z ekranu nic nie znika. Odsiewamy takie klucze
    // przy wczytaniu.
    var swapState = (function () {
      var zapis = LS.get("swap:" + data.slug, {}), czyste = {};
      Object.keys(zapis || {}).forEach(function (k) {
        var ing = data.ingredients[+k];
        if (ing && ing.swap && optionOf(ing, zapis[k])) czyste[k] = zapis[k];
      });
      return czyste;
    })();

    /* ------------------------------------------------------ zamienniki ---- */

    function optionOf(ing, id) {
      var g = groups[ing.swap.group];
      for (var i = 0; i < g.options.length; i++) {
        if (g.options[i].id === id) return g.options[i];
      }
      return null;
    }

    // Biernik potoczny („pokrój pomidora”) mają tylko rzeczowniki męskie
    // odmieniane jak żywotne. Dla żeńskich i nijakich poprawny jest zwykły
    // biernik — bez tego po zamianie wychodziło „Papryka pokrój w plastry”.
    var ZAPAS = { Bpot: "B", Bpl: "B", Mpl: "M", Dpl: "D", Npl: "N", Mspl: "Ms" };

    function forma(opt, kase) {
      return opt.formy[kase] || opt.formy[ZAPAS[kase] || "M"] || opt.formy.M;
    }

    // Zwraca nazwę i gramaturę dla wybranego wariantu składnika.
    //
    // Owoce mają w „Liście wymienników” podaną wagę jednej sztuki (`equiv`),
    // więc przy jednostce sztukowej liczymy wagę wprost: sztuki × waga sztuki.
    // Warzywa takiej tabeli w PDF-ie nie mają, a jedna sztuka dyni to nie to
    // samo co jedna sztuka pomidora — wtedy zostawiamy gramaturę z planu
    // (dietetyk podaje właśnie wagę) i chowamy mylącą liczbę sztuk.
    function resolve(ing, idx) {
      var nic = { name: ing.name, ratio: 1, swapped: false, hidePieces: false };
      if (!ing.swap) return nic;
      var chosen = swapState[idx];
      if (!chosen || chosen === ing.swap.self) return nic;
      var opt = optionOf(ing, chosen);
      if (!opt) return nic;

      var sztukowa = ing.unitLemma === "sztuka";
      var ratio = 1;
      var hidePieces = false;
      if (sztukowa) {
        if (opt.equiv && ing.grams > 0) ratio = (ing.qty * opt.equiv) / ing.grams;
        else hidePieces = true;
      }
      return {
        name: forma(opt, ing.swap.nameCase) || opt.formy.D || opt.formy.M,
        ratio: ratio,
        swapped: true,
        hidePieces: hidePieces,
      };
    }

    var TOKEN = /«(\d+)\|([A-Za-z]+)\|([A-Za-z_]*)\|([^|]*)\|(U?)»/g;

    function renderStepText(step) {
      return step.replace(TOKEN, function (_, idx, kase, adj, infix, up) {
        var ing = data.ingredients[+idx];
        var opt = optionOf(ing, swapState[+idx] || ing.swap.self) ||
                  optionOf(ing, ing.swap.self);
        var w = forma(opt, kase);
        if (adj) {
          var rodz = (adj.slice(-2) === "_B" && kase === "Bpot")
            ? (opt.rodzajB || opt.rodzaj) : opt.rodzaj;
          w = adjectives[adj][rodz] + " " + (infix ? infix + " " : "") + w;
        }
        return up ? w.charAt(0).toUpperCase() + w.slice(1) : w;
      });
    }

    /* ---------------------------------------------------------- porcje ---- */

    // Jedna osoba = dokładnie te ilości, które są w planie diety — także wtedy,
    // gdy przepis jest tam opisany jako wieloporcjowy.
    function factor() {
      return servings;
    }

    // Skróty jednostek. Działają wyłącznie przy wyświetlaniu — w recipes.json
    // zostaje pełny zapis z PDF-u, dzięki czemu verify_against_pdf.py nadal
    // porównuje dane ze źródłem znak w znak. Ta sama tabela jest w
    // generate_site.py (SKROTY) — zmieniasz jedno, zmień drugie.
    var SKROTY = {
      "sztuka": "szt.", "sztuki": "szt.", "sztuk": "szt.",
      "opakowanie": "op.", "opakowania": "op.", "opakowań": "op.",
      "szczypta": "szcz.", "szczypty": "szcz.", "szczypt": "szcz."
    };

    function skrot(u) {
      return Object.prototype.hasOwnProperty.call(SKROTY, u) ? SKROTY[u] : u;
    }

    function scaled(ing, idx) {
      var r = resolve(ing, idx);
      var f = factor();
      var qty = ing.qty * f;
      var grams = ing.grams * f * r.ratio;
      var unit = ing.unit;
      if (f !== 1 && ing.unitLemma && units[ing.unitLemma]) {
        unit = plural(qty, units[ing.unitLemma]);
      }
      return {
        qty: fmtQty(f === 1 ? ing.qty : qty),
        unit: skrot(unit),
        name: r.name,
        grams: fmtGrams(f === 1 ? ing.grams * r.ratio : grams),
        swapped: r.swapped,
        nameFirst: !!ing.nameFirst,
        // zamiennik bez znanej wagi sztuki pokazujemy jak składnik wagowy
        weightOnly: !!ing.weightOnly || r.hidePieces,
        section: ing.section || null,
      };
    }

    // Zapis zgodny ze źródłem: starsze plany podają najpierw ilość
    // („2 łyżki ryżu basmati”), nowsze najpierw nazwę („Papryka – 0.5 sztuki”),
    // a część składników ma tylko gramaturę („50 g kaszy kuskus”).
    function line(s) {
      if (s.weightOnly) return s.grams + " g " + s.name;
      if (s.nameFirst) return s.name + " – " + s.qty + " " + s.unit;
      return s.qty + " " + s.unit + " " + s.name;
    }

    // Lista zakupów i PDF mają gramaturę w osobnej kolumnie po prawej, więc
    // dla składników wagowych nie powtarzamy jej jeszcze raz w nazwie.
    function lineShort(s) {
      return s.weightOnly ? s.name : line(s);
    }

    // Pięć przepisów jest w planie opisanych jako wieloporcjowe, a ilości
    // zostawiamy dokładnie takie jak w PDF-ie. Liczymy więc dla nich porcje
    // z planu, nie osoby — inaczej „1 osoba” dawała trzy porcje zupy przy
    // deklarowanych 404 kcal.
    var wieloporcjowy = (data.baseServings || 1) > 1;

    function render() {
      num.textContent = servings;
      word.textContent = wieloporcjowy
        ? plural(servings, ["porcja", "porcje", "porcji", "porcji"])
        : personWord(servings);
      minus.disabled = servings <= 1;
      plus.disabled = servings >= 12;
      heading.textContent = "Składniki na " + servings + " " + (wieloporcjowy
        ? plural(servings, ["porcję", "porcje", "porcji", "porcji"]) + " z planu"
        : plural(servings, ["osobę", "osoby", "osób", "osoby"]));

      if (note) {
        note.hidden = !wieloporcjowy;
        if (!note.hidden) {
          var total = data.baseServings * servings;
          note.textContent =
            "Jedna porcja z planu to " + data.baseServings + " " +
            plural(data.baseServings, ["porcja", "porcje", "porcji", "porcji"]) +
            " gotowego dania — tak opisał to dietetyk i takich ilości nie " +
            "zmieniamy. Przy " + servings + " " +
            plural(servings, ["porcji", "porcjach", "porcjach", "porcjach"]) +
            " z planu wyjdzie " + total + " " +
            plural(total, ["porcja", "porcje", "porcji", "porcji"]) +
            ", czyli " + (data.kcal * servings) + " kcal łącznie.";
        }
      }

      // Same wiersze składników przepisujemy w miejscu, żeby nie gubić
      // otwartych list rozwijanych „Zamień na”.
      var idx = 0;
      [].forEach.call(list.children, function (li) {
        if (li.classList.contains("p-ings__sec")) return;  // nagłówek sekcji
        var s = scaled(data.ingredients[idx], idx);
        li.querySelector(".p-ing__q").textContent = s.weightOnly ? "" : s.qty + " " + s.unit;
        li.querySelector(".p-ing__n").textContent = s.name;
        li.querySelector(".p-ing__g").textContent = s.grams + " g";
        li.setAttribute("data-swapped", s.swapped ? "1" : "0");
        idx++;
      });

      if (stepsList) {
        [].forEach.call(stepsList.children, function (li, i) {
          li.textContent = renderStepText(data.steps[i]);
        });
      }

      var anySwap = Object.keys(swapState).some(function (k) {
        var ing = data.ingredients[+k];
        return ing && ing.swap && swapState[k] && swapState[k] !== ing.swap.self;
      });
      if (swapReset) swapReset.hidden = !anySwap;

      // Zapisujemy tylko to, co użytkownik faktycznie zmienił. Bez tego samo
      // przejrzenie przepisów zostawiało po sobie tysiąc kluczy z wartościami
      // domyślnymi, których nikt nigdy nie sprząta.
      remember("servings:" + data.slug, servings, servings !== 1);
      remember("swap:" + data.slug, swapState, anySwap);
      if (sheet && sheet.getAttribute("data-open") === "1") renderShopping();
      if (cook && cook.getAttribute("data-open") === "1") renderStep();
    }

    minus.addEventListener("click", function () {
      if (servings > 1) { servings--; render(); }
    });
    plus.addEventListener("click", function () {
      if (servings < 12) { servings++; render(); }
    });

    [].forEach.call(document.querySelectorAll(".p-select[data-ing]"), function (sel) {
      sel.value = swapState[sel.getAttribute("data-ing")] ||
                  data.ingredients[+sel.getAttribute("data-ing")].swap.self;
      sel.addEventListener("change", function () {
        swapState[sel.getAttribute("data-ing")] = sel.value;
        render();
      });
    });

    if (swapReset) {
      swapReset.addEventListener("click", function () {
        swapState = {};
        [].forEach.call(document.querySelectorAll(".p-select[data-ing]"), function (sel) {
          sel.value = data.ingredients[+sel.getAttribute("data-ing")].swap.self;
        });
        render();
        toast("Przywrócono składniki z przepisu");
      });
    }

    /* ------------------------------------------------- lista zakupów ------ */

    var sheet = document.getElementById("shopping");
    var sheetBody = document.getElementById("shopping-body");
    var openBtn = document.getElementById("open-shopping");
    var closeBtn = document.getElementById("close-shopping");
    var scrim = document.getElementById("shopping-scrim");
    var pdfBtn = document.getElementById("pdf-btn");
    var resetBtn = document.getElementById("reset-shopping");

    function boughtMap() {
      return LS.get("bought:" + data.slug, {});
    }

    function groupsForList() {
      return [
        { key: "buy", label: "Do kupienia", pantry: false },
        { key: "pantry", label: "Przyprawy i podstawy", pantry: true },
      ];
    }

    function renderShopping() {
      var bought = boughtMap();
      sheetBody.innerHTML = "";
      groupsForList().forEach(function (group) {
        var items = [];
        data.ingredients.forEach(function (ing, idx) {
          if (!!ing.pantry === group.pantry) items.push({ ing: ing, idx: idx });
        });
        if (!items.length) return;
        var h = document.createElement("p");
        h.className = "p-group";
        h.textContent = group.label;
        sheetBody.appendChild(h);

        var sekcja = null;
        items.forEach(function (it, n) {
          var s = scaled(it.ing, it.idx);
          if (s.section !== sekcja) {
            sekcja = s.section;
            if (sekcja) {
              var sh = document.createElement("p");
              sh.className = "p-group p-group--sub";
              sh.textContent = sekcja;
              sheetBody.appendChild(sh);
            }
          }
          var id = group.key + ":" + n;
          var label = document.createElement("label");
          label.className = "p-check";
          var cb = document.createElement("input");
          cb.type = "checkbox";
          cb.checked = !!bought[id];
          cb.addEventListener("change", function () {
            var b = boughtMap();
            if (cb.checked) b[id] = true; else delete b[id];
            LS.set("bought:" + data.slug, b);
          });
          var txt = document.createElement("span");
          txt.className = "p-check__text";
          txt.textContent = lineShort(s);
          if (s.swapped) {
            var tag = document.createElement("span");
            tag.className = "p-swapped";
            tag.textContent = "zamiennik";
            txt.appendChild(document.createTextNode(" "));
            txt.appendChild(tag);
          }
          var g = document.createElement("span");
          g.className = "p-check__g";
          g.textContent = s.grams + " g";
          label.appendChild(cb);
          label.appendChild(txt);
          label.appendChild(g);
          sheetBody.appendChild(label);
        });
      });
    }

    // Okno modalne ma trzymać fokus u siebie. Bez tego jeden Tab wyprowadzał
    // klawiaturę na zasłoniętą treść — dawało się dojść do niewidocznego
    // „Gotujmy” i uruchomić tryb gotowania drugi raz.
    var FOKUSOWALNE = 'a[href], button:not([disabled]), input:not([disabled]),' +
      ' select:not([disabled]), textarea:not([disabled]), [tabindex]:not([tabindex="-1"])';
    // Okno leży głęboko w drzewie Material for MkDocs, więc idziemy od niego
    // w górę i na każdym piętrze wyłączamy rodzeństwo. Wyłączenie samych
    // dzieci kontenera zostawiało dostępną całą treść strony pod spodem.
    function zablokujTlo(okno) {
      for (var el = okno; el && el !== document.body; el = el.parentElement) {
        [].forEach.call(el.parentElement.children, function (rodzenstwo) {
          if (rodzenstwo !== el) rodzenstwo.setAttribute("inert", "");
        });
      }
    }

    function odblokujTlo() {
      [].forEach.call(document.querySelectorAll("[inert]"), function (el) {
        el.removeAttribute("inert");
      });
    }

    function zapetlFokus(okno, ev) {
      var f = [].slice.call(okno.querySelectorAll(FOKUSOWALNE))
        .filter(function (el) { return el.offsetParent !== null; });
      if (!f.length) return;
      var pierwszy = f[0], ostatni = f[f.length - 1];
      if (ev.shiftKey && document.activeElement === pierwszy) {
        ev.preventDefault();
        ostatni.focus();
      } else if (!ev.shiftKey && document.activeElement === ostatni) {
        ev.preventDefault();
        pierwszy.focus();
      }
    }

    function openSheet() {
      if (sheet.getAttribute("data-open") === "1") return;
      renderShopping();
      sheet.setAttribute("data-open", "1");
      document.body.classList.add("p-cooking");
      zablokujTlo(sheet);
      closeBtn.focus();
    }

    function closeSheet() {
      sheet.setAttribute("data-open", "0");
      document.body.classList.remove("p-cooking");
      odblokujTlo();
      openBtn.focus();
    }

    if (openBtn) openBtn.addEventListener("click", openSheet);
    if (closeBtn) closeBtn.addEventListener("click", closeSheet);
    if (scrim) scrim.addEventListener("click", closeSheet);
    if (resetBtn) {
      resetBtn.addEventListener("click", function () {
        LS.set("bought:" + data.slug, {});
        renderShopping();
        toast("Odznaczono wszystko");
      });
    }
    if (pdfBtn) {
      pdfBtn.addEventListener("click", function () {
        makePdf(data, servings, scaled, groupsForList(), boughtMap(), pdfBtn, lineShort);
      });
    }

    /* ------------------------------------------------ tryb gotowania ------ */

    var cook = document.getElementById("cook");
    var cookStart = document.getElementById("cook-start");
    var cookClose = document.getElementById("cook-close");
    var cookPrev = document.getElementById("cook-prev");
    var cookNext = document.getElementById("cook-next");
    var cookText = document.getElementById("cook-text");
    var cookLabel = document.getElementById("cook-label");
    var cookProgress = document.getElementById("cook-progress");
    var step = 0;
    var wakeLock = null;

    function renderStep() {
      cookLabel.textContent = "Krok " + (step + 1) + " z " + data.steps.length;
      cookText.textContent = renderStepText(data.steps[step]);
      cookPrev.disabled = step === 0;
      cookNext.textContent = step === data.steps.length - 1
        ? "Gotowe · Smacznego!" : "Następny krok";
      [].forEach.call(cookProgress.children, function (seg, i) {
        seg.setAttribute("data-done", i <= step ? "1" : "0");
      });
      cook.querySelector(".p-cook__body").scrollTop = 0;
      LS.set("step:" + data.slug, step);
    }

    // Przeglądarka zwalnia blokadę wygaszania ekranu, gdy karta znika z oczu.
    // Trzeba ją założyć ponownie po powrocie, bo inaczej ekran gaśnie w połowie
    // gotowania — dokładnie wtedy, gdy sprawdziłeś coś w innej aplikacji.
    function trzymajEkran() {
      if (!("wakeLock" in navigator) || wakeLock) return;
      navigator.wakeLock.request("screen").then(function (l) {
        wakeLock = l;
        l.addEventListener("release", function () { wakeLock = null; });
      }, function () {});
    }

    function pusćEkran() {
      if (!wakeLock) return;
      var l = wakeLock;
      wakeLock = null;
      l.release().catch(function () {});
    }

    document.addEventListener("visibilitychange", function () {
      if (document.visibilityState !== "visible") return;
      if (cook && cook.getAttribute("data-open") === "1") trzymajEkran();
    });

    function openCook() {
      if (cook.getAttribute("data-open") === "1") return;
      step = Math.min(LS.get("step:" + data.slug, 0), data.steps.length - 1);
      if (!(step >= 0)) step = 0;
      cookProgress.innerHTML = "";
      data.steps.forEach(function () {
        var seg = document.createElement("span");
        seg.className = "p-progress__seg";
        cookProgress.appendChild(seg);
      });
      renderStep();
      cook.setAttribute("data-open", "1");
      document.body.classList.add("p-cooking");
      zablokujTlo(cook);
      cookNext.focus();
      trzymajEkran();
    }

    function closeCook() {
      cook.setAttribute("data-open", "0");
      document.body.classList.remove("p-cooking");
      odblokujTlo();
      pusćEkran();
      cookStart.focus();
    }

    if (cookStart) cookStart.addEventListener("click", openCook);
    if (cookClose) cookClose.addEventListener("click", closeCook);
    if (cookPrev) cookPrev.addEventListener("click", function () {
      if (step > 0) { step--; renderStep(); }
    });
    if (cookNext) cookNext.addEventListener("click", function () {
      if (step < data.steps.length - 1) { step++; renderStep(); }
      else { LS.set("step:" + data.slug, 0); closeCook(); }
    });

    document.addEventListener("keydown", function (ev) {
      if (cook && cook.getAttribute("data-open") === "1") {
        if (ev.key === "Escape") closeCook();
        if (ev.key === "ArrowRight") cookNext.click();
        if (ev.key === "ArrowLeft") cookPrev.click();
        if (ev.key === "Tab") zapetlFokus(cook, ev);
      } else if (sheet && sheet.getAttribute("data-open") === "1") {
        if (ev.key === "Escape") closeSheet();
        if (ev.key === "Tab") zapetlFokus(sheet, ev);
      }
    });

    render();
  }

  /* ============================================================ PDF ======== */

  function loadScript(src) {
    return new Promise(function (resolve, reject) {
      var s = document.createElement("script");
      s.src = src;
      s.onload = resolve;
      s.onerror = function () { reject(new Error(src)); };
      document.head.appendChild(s);
    });
  }

  var pdfReady = null;
  function ensurePdf() {
    if (!pdfReady) {
      pdfReady = loadScript(BASE + "javascripts/vendor/jspdf.umd.min.js")
        .then(function () { return loadScript(BASE + "javascripts/vendor/pdf-font.js"); });
    }
    return pdfReady;
  }

  function toast(msg) {
    var el = document.getElementById("toast");
    if (!el) return;
    el.textContent = msg;
    el.setAttribute("data-on", "1");
    clearTimeout(el._t);
    el._t = setTimeout(function () { el.setAttribute("data-on", "0"); }, 2600);
  }

  function makePdf(data, servings, scaled, groups, bought, btn, line) {
    var old = btn.textContent;
    btn.textContent = "Tworzę PDF…";
    btn.disabled = true;

    ensurePdf().then(function () {
      var doc = new window.jspdf.jsPDF({ unit: "mm", format: "a4" });

      // Wbudowane kroje jsPDF nie mają polskich znaków — dokładamy własny.
      doc.addFileToVFS("DejaVu.ttf", window.PRZEPISY_FONT.regular);
      doc.addFont("DejaVu.ttf", "DejaVu", "normal");
      doc.addFileToVFS("DejaVu-Bold.ttf", window.PRZEPISY_FONT.bold);
      doc.addFont("DejaVu-Bold.ttf", "DejaVu", "bold");

      var M = 18, W = 210 - M * 2, y = M;

      doc.setFont("DejaVu", "bold");
      doc.setFontSize(9);
      doc.setTextColor(120);
      doc.text("LISTA ZAKUPÓW", M, y);
      y += 8;

      doc.setFontSize(16);
      doc.setTextColor(20);
      var title = doc.splitTextToSize(data.title, W);
      doc.text(title, M, y);
      y += title.length * 7 + 2;

      doc.setFont("DejaVu", "normal");
      doc.setFontSize(10);
      doc.setTextColor(110);
      doc.text(servings + " " + plural(servings, ["osoba", "osoby", "osób", "osoby"]) +
               "  ·  " + data.slotLabel + " " + data.time, M, y);
      y += 8;
      doc.setDrawColor(210);
      doc.line(M, y, M + W, y);
      y += 8;

      groups.forEach(function (group) {
        var items = [];
        data.ingredients.forEach(function (ing, idx) {
          if (!!ing.pantry === group.pantry) items.push({ ing: ing, idx: idx });
        });
        if (!items.length) return;

        if (y > 250) { doc.addPage(); y = M; }
        doc.setFont("DejaVu", "bold");
        doc.setFontSize(9);
        doc.setTextColor(120);
        doc.text(group.label.toUpperCase(), M, y);
        y += 7;

        doc.setFont("DejaVu", "normal");
        doc.setFontSize(11);
        items.forEach(function (it, n) {
          if (y > 275) { doc.addPage(); y = M; }
          var s = scaled(it.ing, it.idx);
          var done = !!bought[group.key + ":" + n];

          doc.setDrawColor(done ? 60 : 150);
          doc.setLineWidth(0.3);
          doc.rect(M, y - 3.6, 4, 4);
          if (done) {
            doc.setLineWidth(0.6);
            doc.line(M + 0.8, y - 1.6, M + 1.8, y - 0.4);
            doc.line(M + 1.8, y - 0.4, M + 3.3, y - 3);
          }

          doc.setTextColor(done ? 140 : 25);
          var wrapped = doc.splitTextToSize(line(s) + (s.swapped ? "  (zamiennik)" : ""), W - 30);
          doc.text(wrapped, M + 7, y);
          doc.setTextColor(150);
          doc.text(s.grams + " g", M + W, y, { align: "right" });
          y += wrapped.length * 5.6 + 2.4;
        });
        y += 4;
      });

      doc.setFont("DejaVu", "normal");
      doc.setFontSize(8);
      doc.setTextColor(150);
      doc.text("Przepisy Dietetyczne · wygenerowano " +
               new Date().toLocaleDateString("pl-PL"), M, 287);

      var name = "lista-zakupow-" + data.slug + "-" + servings + "os.pdf";
      doc.save(name);
      toast("Zapisano " + name);
    }).catch(function () {
      toast("Nie udało się utworzyć PDF-u. Sprawdź połączenie i spróbuj ponownie.");
    }).then(function () {
      btn.textContent = old;
      btn.disabled = false;
    });
  }

  /* =========================================================== start ====== */

  function boot() {
    initFinder();
    initRecipe();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
