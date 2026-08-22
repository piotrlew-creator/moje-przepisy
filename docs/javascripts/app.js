/* ==========================================================================
   Przepisy Dietetyczne — logika strony
   --------------------------------------------------------------------------
   Trzy niezależne kawałki, wszystkie inicjowane przez boot():
     1. wyszukiwarka na stronie głównej (pora dnia + składniki),
     2. przepis (przelicznik porcji, lista zakupów, PDF),
     3. tryb gotowania (jeden krok na ekran).

   Stan (liczba osób, odhaczone zakupy, numer kroku, filtry) trzymamy w
   localStorage, żeby przypadkowe odświeżenie w trakcie gotowania niczego nie
   gubiło.
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
    if (Number.isInteger(r)) return String(r);
    return String(parseFloat(r.toFixed(2)));
  }

  function fmtGrams(n) {
    if (n < 10) return String(parseFloat((Math.round(n * 10) / 10).toFixed(1)));
    return String(Math.round(n));
  }

  function unitFor(qty, ing, units) {
    var forms = ing.unitLemma && units ? units[ing.unitLemma] : null;
    if (!forms) return ing.unit;
    return plural(qty, forms);
  }

  /* --------------------------------------------------- składniki przepisu -- */

  function scaleIngredient(ing, factor, units) {
    var qty = ing.qty * factor;
    var grams = ing.grams * factor;
    if (factor === 1) {
      return { qty: fmtQty(ing.qty), unit: ing.unit, name: ing.name, grams: fmtGrams(ing.grams) };
    }
    return { qty: fmtQty(qty), unit: unitFor(qty, ing, units), name: ing.name, grams: fmtGrams(grams) };
  }

  function ingredientLine(s) {
    return s.qty + " " + s.unit + " " + s.name;
  }

  /* ================================================== STRONA GŁÓWNA ======== */

  function initFinder() {
    var root = document.getElementById("finder");
    if (!root || !window.RECIPES) return;

    var cards = Array.prototype.slice.call(document.querySelectorAll("#recipes .p-card"));
    var slotChips = Array.prototype.slice.call(root.querySelectorAll("[data-slot-filter]"));
    var ingWrap = document.getElementById("ing-chips");
    var ingChips = Array.prototype.slice.call(ingWrap.querySelectorAll(".p-chip"));
    var search = document.getElementById("ing-search");
    var toggleAll = document.getElementById("ing-toggle");
    var countEl = document.getElementById("result-count");
    var clearEl = document.getElementById("clear-filters");
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

    if (search) {
      search.addEventListener("input", function () {
        var q = search.value.trim().toLowerCase();
        var anyHidden = false;
        ingChips.forEach(function (chip) {
          var label = chip.getAttribute("data-label") || "";
          var hit = !q || label.toLowerCase().indexOf(q) !== -1;
          chip.style.display = hit ? "" : "none";
          if (!hit) anyHidden = true;
        });
        // przy szukaniu pokazujemy wszystkie pasujące, nie tylko popularne
        ingWrap.setAttribute("data-collapsed", q ? "0" : collapsed ? "1" : "0");
        if (anyHidden) { /* nic — tylko czytelność warunku wyżej */ }
      });
    }

    var collapsed = true;
    if (toggleAll) {
      toggleAll.addEventListener("click", function () {
        collapsed = !collapsed;
        ingWrap.setAttribute("data-collapsed", collapsed ? "1" : "0");
        toggleAll.textContent = collapsed
          ? "Pokaż wszystkie (" + ingChips.length + ")"
          : "Pokaż mniej";
      });
      toggleAll.textContent = "Pokaż wszystkie (" + ingChips.length + ")";
    }

    if (clearEl) {
      clearEl.addEventListener("click", function () {
        state.slot = "all";
        state.ings = [];
        slotChips.forEach(function (c) {
          var sel = c.getAttribute("data-slot-filter") === "all";
          c.setAttribute("data-on", sel ? "1" : "0");
          c.setAttribute("aria-pressed", sel ? "true" : "false");
        });
        ingChips.forEach(function (c) {
          c.querySelector("input").checked = false;
          c.setAttribute("data-on", "0");
        });
        if (search) search.value = "";
        ingChips.forEach(function (c) { c.style.display = ""; });
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

      countEl.textContent = shown + " " + plural(shown, ["przepis", "przepisy", "przepisów", "przepisu"]);
      var filtering = state.slot !== "all" || state.ings.length > 0;
      clearEl.hidden = !filtering;
      emptyEl.hidden = shown !== 0;

      if (stateEl) {
        var n = state.ings.length;
        stateEl.textContent = n
          ? n + " " + plural(n, ["wybrany", "wybrane", "wybranych", "wybranego"])
          : "wybierz składniki";
        stateEl.setAttribute("data-active", n ? "1" : "0");
      }

      LS.set("filters", state);
    }

    // Jeśli wracasz z zaznaczonymi składnikami, panel otwiera się sam —
    // inaczej filtr działałby niewidocznie.
    if (panel && state.ings.length) panel.open = true;

    apply();
  }

  /* ======================================================= PRZEPIS ========= */

  function initRecipe() {
    var data = window.RECIPE;
    if (!data) return;

    var units = window.UNITS || {};
    var minus = document.getElementById("srv-minus");
    var plus = document.getElementById("srv-plus");
    var num = document.getElementById("srv-num");
    var word = document.getElementById("srv-word");
    var list = document.getElementById("ing-list");
    var heading = document.getElementById("ing-heading");
    var note = document.getElementById("srv-note");

    var servings = LS.get("servings:" + data.slug, 1);
    if (!(servings >= 1)) servings = 1;
    servings = Math.min(12, Math.round(servings));

    // Jedna osoba = dokładnie te ilości, które są w planie diety — także wtedy,
    // gdy przepis jest tam opisany jako wieloporcjowy. Nic nie dzielimy, bo
    // dzielenie dawałoby „0.33 opakowania” i rozjeżdżałoby się ze źródłem.
    function factor() {
      return servings;
    }

    function render() {
      num.textContent = servings;
      word.textContent = personWord(servings);
      minus.disabled = servings <= 1;
      plus.disabled = servings >= 12;
      heading.textContent = "Składniki na " + servings + " " + plural(servings, ["osobę", "osoby", "osób", "osoby"]);

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

      list.innerHTML = "";
      var f = factor();
      data.ingredients.forEach(function (ing) {
        var s = scaleIngredient(ing, f, units);
        var li = document.createElement("li");
        if (ing.pantry) li.setAttribute("data-pantry", "1");
        var q = document.createElement("span");
        q.className = "p-ing__q";
        q.textContent = s.qty + " " + s.unit;
        var n = document.createElement("span");
        n.textContent = s.name;
        var g = document.createElement("span");
        g.className = "p-ing__g";
        g.textContent = s.grams + " g";
        li.appendChild(q);
        li.appendChild(n);
        li.appendChild(g);
        list.appendChild(li);
      });

      LS.set("servings:" + data.slug, servings);
      if (sheet && sheet.getAttribute("data-open") === "1") renderShopping();
    }

    minus.addEventListener("click", function () {
      if (servings > 1) { servings--; render(); }
    });
    plus.addEventListener("click", function () {
      if (servings < 12) { servings++; render(); }
    });

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

    function renderShopping() {
      var bought = boughtMap();
      var f = factor();
      sheetBody.innerHTML = "";

      [
        { key: "buy", label: "Do kupienia", pantry: false },
        { key: "pantry", label: "Przyprawy i podstawy", pantry: true },
      ].forEach(function (group) {
        var items = data.ingredients.filter(function (i) { return !!i.pantry === group.pantry; });
        if (!items.length) return;
        var h = document.createElement("p");
        h.className = "p-group";
        h.textContent = group.label;
        sheetBody.appendChild(h);

        items.forEach(function (ing, idx) {
          var s = scaleIngredient(ing, f, units);
          var id = group.key + ":" + idx;
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
          txt.textContent = ingredientLine(s);
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
        makePdf(data, servings, factor(), units, boughtMap(), pdfBtn);
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
      cookText.textContent = data.steps[step];
      cookPrev.disabled = step === 0;
      cookNext.textContent = step === data.steps.length - 1 ? "Gotowe · Smacznego!" : "Następny krok";
      Array.prototype.forEach.call(cookProgress.children, function (seg, i) {
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

    document.addEventListener("keydown", function (e) {
      if (cook && cook.getAttribute("data-open") === "1") {
        if (e.key === "Escape") closeCook();
        if (e.key === "ArrowRight") cookNext.click();
        if (e.key === "ArrowLeft") cookPrev.click();
      } else if (sheet && sheet.getAttribute("data-open") === "1" && e.key === "Escape") {
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

  function makePdf(data, servings, factor, units, bought, btn) {
    var old = btn.textContent;
    btn.textContent = "Tworzę PDF…";
    btn.disabled = true;

    ensurePdf().then(function () {
      var jsPDF = window.jspdf.jsPDF;
      var doc = new jsPDF({ unit: "mm", format: "a4" });

      // Wbudowane kroje jsPDF nie mają polskich znaków — dokładamy własny.
      doc.addFileToVFS("DejaVu.ttf", window.PRZEPISY_FONT.regular);
      doc.addFont("DejaVu.ttf", "DejaVu", "normal");
      doc.addFileToVFS("DejaVu-Bold.ttf", window.PRZEPISY_FONT.bold);
      doc.addFont("DejaVu-Bold.ttf", "DejaVu", "bold");

      var M = 18;
      var W = 210 - M * 2;
      var y = M;

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
      doc.text(
        servings + " " + plural(servings, ["osoba", "osoby", "osób", "osoby"]) +
        "  ·  " + data.slotLabel + " " + data.time +
        "  ·  Dzień " + data.day,
        M, y
      );
      y += 8;
      doc.setDrawColor(210);
      doc.line(M, y, M + W, y);
      y += 8;

      [
        { label: "Do kupienia", pantry: false, key: "buy" },
        { label: "Przyprawy i podstawy", pantry: true, key: "pantry" },
      ].forEach(function (group) {
        var items = data.ingredients.filter(function (i) { return !!i.pantry === group.pantry; });
        if (!items.length) return;

        if (y > 250) { doc.addPage(); y = M; }
        doc.setFont("DejaVu", "bold");
        doc.setFontSize(9);
        doc.setTextColor(120);
        doc.text(group.label.toUpperCase(), M, y);
        y += 7;

        doc.setFont("DejaVu", "normal");
        doc.setFontSize(11);
        items.forEach(function (ing, idx) {
          if (y > 275) { doc.addPage(); y = M; }
          var s = scaleIngredient(ing, factor, units);
          var done = !!bought[group.key + ":" + idx];

          doc.setDrawColor(done ? 60 : 150);
          doc.setLineWidth(0.3);
          doc.rect(M, y - 3.6, 4, 4);
          if (done) {
            doc.setLineWidth(0.6);
            doc.line(M + 0.8, y - 1.6, M + 1.8, y - 0.4);
            doc.line(M + 1.8, y - 0.4, M + 3.3, y - 3);
          }

          doc.setTextColor(done ? 140 : 25);
          var line = ingredientLine(s);
          var wrapped = doc.splitTextToSize(line, W - 30);
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
      doc.text(
        "Przepisy Dietetyczne · wygenerowano " + new Date().toLocaleDateString("pl-PL"),
        M, 287
      );

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
