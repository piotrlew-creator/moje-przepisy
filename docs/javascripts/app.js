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
  };

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
    if (!root || !window.RECIPES) return;

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

    var saved = LS.get("filters", { slot: "all", ings: [] });
    var state = { slot: saved.slot || "all", ings: saved.ings || [] };

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
        apply();
      });
    });

    ingChips.forEach(function (chip) {
      var input = chip.querySelector("input");
      input.checked = state.ings.indexOf(input.value) !== -1;
      chip.setAttribute("data-on", input.checked ? "1" : "0");
      input.addEventListener("change", function () {
        chip.setAttribute("data-on", input.checked ? "1" : "0");
        state.ings = ingChips
          .map(function (c) { return c.querySelector("input"); })
          .filter(function (i) { return i.checked; })
          .map(function (i) { return i.value; });
        apply();
      });
    });

    // Bez zapytania widać tylko kluczowe składniki plus te już zaznaczone;
    // z zapytaniem — wszystko, co pasuje, także mimo literówki.
    function renderChips() {
      var q = search ? search.value.trim() : "";
      var exact = 0, fuzzy = [];
      ingChips.forEach(function (chip) {
        var label = chip.getAttribute("data-label") || "";
        var checked = chip.querySelector("input").checked;
        if (!q) {
          chip.hidden = chip.getAttribute("data-rank") !== "top" && !checked;
          return;
        }
        var score = matchScore(label, q);
        chip.hidden = score === Infinity;
        if (score <= 0.5) exact++;
        else if (score < Infinity) fuzzy.push(label);
      });
      if (searchClear) searchClear.hidden = !q;
      if (hint) {
        if (!q) {
          hint.textContent = hintText;
        } else if (exact === 0 && fuzzy.length) {
          hint.textContent = "Nie znaleziono „" + q + "”. Może chodziło o: " +
            fuzzy.slice(0, 3).join(", ") + "?";
        } else if (exact === 0) {
          hint.textContent = "Brak składnika pasującego do „" + q + "”.";
        } else {
          hint.textContent = "";
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
      LS.set("filters", state);
    }

    if (panel && state.ings.length) panel.open = true;
    renderChips();
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

    var swapState = LS.get("swap:" + data.slug, {});

    /* ------------------------------------------------------ zamienniki ---- */

    function optionOf(ing, id) {
      var g = groups[ing.swap.group];
      for (var i = 0; i < g.options.length; i++) {
        if (g.options[i].id === id) return g.options[i];
      }
      return null;
    }

    // Zwraca nazwę i mnożnik gramatury dla wybranego wariantu składnika.
    // Owoce mają w PDF-ie różne wagi jednej sztuki, więc podmiana skaluje
    // gramaturę — 1 sztuka banana to nie to samo co 1 sztuka jabłka.
    function resolve(ing, idx) {
      if (!ing.swap) return { name: ing.name, ratio: 1, swapped: false };
      var chosen = swapState[idx];
      if (!chosen || chosen === ing.swap.self) {
        return { name: ing.name, ratio: 1, swapped: false };
      }
      var self = optionOf(ing, ing.swap.self);
      var opt = optionOf(ing, chosen);
      if (!opt) return { name: ing.name, ratio: 1, swapped: false };
      var ratio = (opt.equiv && self && self.equiv) ? opt.equiv / self.equiv : 1;
      var name = opt.formy[ing.swap.nameCase] || opt.formy.D || opt.formy.M;
      return { name: name, ratio: ratio, swapped: true };
    }

    var TOKEN = /«(\d+)\|([A-Za-z]+)\|([A-Za-z_]*)\|([^|]*)\|(U?)»/g;

    function renderStepText(step) {
      return step.replace(TOKEN, function (_, idx, kase, adj, infix, up) {
        var ing = data.ingredients[+idx];
        var opt = optionOf(ing, swapState[+idx] || ing.swap.self) ||
                  optionOf(ing, ing.swap.self);
        var w = opt.formy[kase] || opt.formy.M;
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
        unit: unit,
        name: r.name,
        grams: fmtGrams(f === 1 ? ing.grams * r.ratio : grams),
        swapped: r.swapped,
      };
    }

    function line(s) {
      return s.qty + " " + s.unit + " " + s.name;
    }

    function render() {
      num.textContent = servings;
      word.textContent = personWord(servings);
      minus.disabled = servings <= 1;
      plus.disabled = servings >= 12;
      heading.textContent = "Składniki na " + servings + " " +
        plural(servings, ["osobę", "osoby", "osób", "osoby"]);

      if (note) {
        note.hidden = (data.baseServings || 1) === 1;
        if (!note.hidden) {
          var total = (data.baseServings || 1) * servings;
          note.textContent =
            "W planie diety ten przepis jest opisany jako " + data.baseServings +
            " porcje i takie ilości podajemy dla jednej osoby — dokładnie jak w PDF-ie. " +
            "Dla " + servings + " " + plural(servings, ["osoby", "osób", "osób", "osoby"]) +
            " wyjdzie " + total + " " +
            plural(total, ["porcja", "porcje", "porcji", "porcji"]) + ".";
        }
      }

      // Same wiersze składników przepisujemy w miejscu, żeby nie gubić
      // otwartych list rozwijanych „Zamień na”.
      [].forEach.call(list.children, function (li, idx) {
        var s = scaled(data.ingredients[idx], idx);
        li.querySelector(".p-ing__q").textContent = s.qty + " " + s.unit;
        li.querySelector(".p-ing__n").textContent = s.name;
        li.querySelector(".p-ing__g").textContent = s.grams + " g";
        li.setAttribute("data-swapped", s.swapped ? "1" : "0");
      });

      if (stepsList) {
        [].forEach.call(stepsList.children, function (li, i) {
          li.textContent = renderStepText(data.steps[i]);
        });
      }

      var anySwap = Object.keys(swapState).some(function (k) {
        return swapState[k] && swapState[k] !== data.ingredients[+k].swap.self;
      });
      if (swapReset) swapReset.hidden = !anySwap;

      LS.set("servings:" + data.slug, servings);
      LS.set("swap:" + data.slug, swapState);
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

        items.forEach(function (it, n) {
          var s = scaled(it.ing, it.idx);
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
          txt.textContent = line(s);
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

    function openSheet() {
      renderShopping();
      sheet.setAttribute("data-open", "1");
      document.body.classList.add("p-cooking");
      closeBtn.focus();
    }

    function closeSheet() {
      sheet.setAttribute("data-open", "0");
      document.body.classList.remove("p-cooking");
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
        makePdf(data, servings, scaled, groupsForList(), boughtMap(), pdfBtn, line);
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

    function openCook() {
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
      cookNext.focus();
      if ("wakeLock" in navigator) {
        navigator.wakeLock.request("screen").then(function (l) { wakeLock = l; }, function () {});
      }
    }

    function closeCook() {
      cook.setAttribute("data-open", "0");
      document.body.classList.remove("p-cooking");
      if (wakeLock) { wakeLock.release().catch(function () {}); wakeLock = null; }
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
      } else if (sheet && sheet.getAttribute("data-open") === "1" && ev.key === "Escape") {
        closeSheet();
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
