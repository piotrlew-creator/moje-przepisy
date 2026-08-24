/* ==========================================================================
   Gotuj z Lewym — logika strony
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

  /* ---------------------------------------------------------- minutnik ---- */

  // Jeden minutnik na raz — dwa naraz w kuchni i tak nie mają sensu, a jeden
  // upraszcza wszystko: nie trzeba pilnować, który przycisk co odlicza.
  var minutnik = {
    krok: null,      // numer kroku albo null
    koniec: 0,       // znacznik czasu zakończenia
    tik: null,
    sluchacze: [],
  };

  function mmss(sek) {
    sek = Math.max(0, Math.round(sek));
    return Math.floor(sek / 60) + ":" + String(sek % 60).padStart(2, "0");
  }

  function zostalo() {
    return Math.max(0, (minutnik.koniec - Date.now()) / 1000);
  }

  function ogloszMinutnik() {
    minutnik.sluchacze.forEach(function (f) { f(); });
  }

  function dzwiek() {
    try {
      var Ctx = window.AudioContext || window.webkitAudioContext;
      if (!Ctx) return;
      var ctx = new Ctx();
      [0, 0.28, 0.56].forEach(function (t) {
        var o = ctx.createOscillator(), g = ctx.createGain();
        o.type = "sine";
        o.frequency.value = 880;
        g.gain.setValueAtTime(0.0001, ctx.currentTime + t);
        g.gain.exponentialRampToValueAtTime(0.25, ctx.currentTime + t + 0.02);
        g.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + t + 0.22);
        o.connect(g); g.connect(ctx.destination);
        o.start(ctx.currentTime + t);
        o.stop(ctx.currentTime + t + 0.24);
      });
      setTimeout(function () { ctx.close(); }, 1500);
    } catch (e) {
      /* przeglądarka bez dźwięku albo bez zgody — zostaje wibracja i napis */
    }
  }

  function stopMinutnik() {
    clearInterval(minutnik.tik);
    minutnik.tik = null;
    minutnik.krok = null;
    ogloszMinutnik();
  }

  function startMinutnik(krok, sekundy) {
    clearInterval(minutnik.tik);
    minutnik.krok = krok;
    minutnik.koniec = Date.now() + sekundy * 1000;
    minutnik.tik = setInterval(function () {
      if (zostalo() > 0) return ogloszMinutnik();
      clearInterval(minutnik.tik);
      minutnik.tik = null;
      minutnik.krok = null;
      ogloszMinutnik();
      dzwiek();
      if (navigator.vibrate) navigator.vibrate([250, 120, 250]);
      toast("Minutnik: czas minął");
    }, 250);
    ogloszMinutnik();
  }

  /* ------------------------------------------ ulubione i „ugotowane” ------ */

  // Jedno miejsce na oba zbiory, żeby strona główna i strona przepisu nie
  // rozjechały się co do formatu zapisu.
  function ulubione() {
    var v = LS.get("fav", []);
    return Array.isArray(v) ? v : [];
  }

  function ustawUlubiony(slug, on) {
    var lista = ulubione().filter(function (x) { return x !== slug; });
    if (on) lista.push(slug);
    remember("fav", lista, lista.length > 0);
    return lista;
  }

  function ugotowane() {
    var v = LS.get("cooked", {});
    return v && typeof v === "object" ? v : {};
  }

  function oznaczUgotowane(slug) {
    var m = ugotowane();
    m[slug] = new Date().toISOString().slice(0, 10);
    remember("cooked", m, true);
    return m;
  }

  /* ------------------------------------------- składnik: zapis i skalowanie */

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

  // Starsze plany zapisują składnik w dopełniaczu („ryżu basmati”), nowsze
  // w mianowniku („Ryż basmati”). Żeby zbiorcza lista zakupów nie wypisywała
  // tego samego dwa razy, porównujemy nazwy po obciętych końcówkach.
  // To heurystyka, nie odmiana — dlatego scalamy tylko w obrębie tej samej
  // kategorii składnika, a przy pozycji pokazujemy, z ilu przepisów pochodzi.
  var KONCOWKI = /(ami|ach|owi|ego|emu|ów|om|em|ie|ia|y|a|u|e|i|ą|ę)$/;

  function rdzen(nazwa) {
    return norm(nazwa).split(/\s+/).map(function (w) {
      return w.length > 4 ? w.replace(KONCOWKI, "") : w;
    }).join(" ");
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

  // Przeliczenie składnika na wybraną liczbę porcji. `podmiana` jest opcjonalna
  // — strona zakupów nie zna zamienników, strona przepisu podaje je z resolve().
  function skaluj(ing, f, units, podmiana) {
    var r = podmiana || { name: ing.name, ratio: 1, swapped: false, hidePieces: false };
    var qty = ing.qty * f;
    var unit = ing.unit;
    if (f !== 1 && ing.unitLemma && units && units[ing.unitLemma]) {
      unit = plural(qty, units[ing.unitLemma]);
    }
    return {
      qty: fmtQty(f === 1 ? ing.qty : qty),
      unit: skrot(unit),
      name: r.name,
      grams: fmtGrams(ing.grams * f * r.ratio),
      gramsNum: ing.grams * f * r.ratio,
      swapped: r.swapped,
      nameFirst: !!ing.nameFirst,
      // zamiennik bez znanej wagi sztuki pokazujemy jak składnik wagowy
      weightOnly: !!ing.weightOnly || r.hidePieces,
      section: ing.section || null,
    };
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
      q: "",
      fav: false,
      cooked: false,
      fridge: false,
    };

    var etykiety = window.SKLADNIKI || {};

    // Tekst, po którym szukamy: nazwa dania plus etykiety jego składników.
    // Dzięki temu „owsianka” trafia w danie, a „jajka” w każdy przepis z jajkami.
    var szukajTekst = {};
    cards.forEach(function (card) {
      var slug = card.getAttribute("data-slug");
      var tagi = (card.getAttribute("data-tags") || "").split(" ")
        .map(function (t) { return etykiety[t] || t; }).join(" ");
      szukajTekst[slug] = (card.getAttribute("data-title") || "") + " " + tagi;
    });

    var favBtn = document.getElementById("mode-fav");
    var cookedBtn = document.getElementById("mode-cooked");
    var fridgeBtn = document.getElementById("mode-fridge");
    var favCount = document.getElementById("fav-count");
    var cookedCount = document.getElementById("cooked-count");
    var fridgeHint = document.getElementById("fridge-hint");

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
      var q = state.q;
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
          hint.textContent = "Żaden składnik nie nazywa się „" + q + "”. " +
            "Może chodziło o: " + fuzzy.slice(0, 3).join(", ") + "?";
        } else if (q && exact === 0) {
          hint.textContent = "Szukam „" + q + "” wśród nazw dań. " +
            "Żaden składnik tak się nie nazywa.";
        } else if (q) {
          hint.textContent = exact + " " +
            plural(exact, ["składnik pasuje", "składniki pasują", "składników pasuje",
                           "składnika pasuje"]) +
            " do „" + q + "” — zaznacz, żeby zawęzić.";
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
      // Pole szuka dwóch rzeczy naraz: zawęża listę dań po nazwie i składnikach,
      // a jednocześnie filtruje kafelki składników w panelu.
      search.addEventListener("input", function () {
        state.q = search.value.trim();
        apply();
      });
    }
    if (searchClear) {
      searchClear.addEventListener("click", function () {
        search.value = "";
        state.q = "";
        apply();
        search.focus();
      });
    }

    if (clearEl) {
      clearEl.addEventListener("click", function () {
        state.ings = [];
        state.q = "";
        state.fav = state.cooked = state.fridge = false;
        ingChips.forEach(function (c) {
          c.querySelector("input").checked = false;
          c.setAttribute("data-on", "0");
        });
        [favBtn, cookedBtn, fridgeBtn].forEach(function (b) {
          if (!b) return;
          b.setAttribute("data-on", "0");
          b.setAttribute("aria-pressed", "false");
        });
        if (fridgeHint) fridgeHint.hidden = true;
        if (search) search.value = "";
        apply();
      });
    }

    // Pora dnia zawęża, składniki poszerzają: przepis pasuje, gdy jest we
    // właściwym posiłku ORAZ zawiera CHOĆ JEDEN z zaznaczonych składników.
    // Ile z zaznaczonych składników brakuje w danym przepisie. Produkty
    // spiżarniane nie mają kategorii, więc z definicji nie liczą się jako brak.
    function braki(card) {
      var tags = (card.getAttribute("data-tags") || "").split(" ");
      var mam = state.ings;
      return tags.filter(function (t) {
        return t && mam.indexOf(t) === -1;
      });
    }

    function apply() {
      var shown = 0;
      var doPosortowania = [];

      cards.forEach(function (card) {
        var li = card.parentElement;
        var slug = card.getAttribute("data-slug");
        var tags = (card.getAttribute("data-tags") || "").split(" ");

        var slotOk = state.slot === "all" || card.getAttribute("data-slot-id") === state.slot;
        // W trybie „mam w lodówce” składniki nie odsiewają, tylko układają
        // kolejność — inaczej wybranie trzech rzeczy dawałoby pustą stronę.
        var ingOk = state.fridge || state.ings.length === 0 ||
          state.ings.some(function (t) { return tags.indexOf(t) !== -1; });
        var textOk = !state.q || matchScore(szukajTekst[slug] || "", state.q) < Infinity;
        var favOk = !state.fav || fav.indexOf(slug) !== -1;
        var cookedOk = !state.cooked || !!cooked[slug];

        var ok = slotOk && ingOk && textOk && favOk && cookedOk;
        li.hidden = !ok;

        var miss = card.querySelector(".p-card__miss");
        if (ok && state.fridge && state.ings.length) {
          var brak = braki(card);
          // Przy równej liczbie braków wyżej stoi przepis, który zużywa więcej
          // z tego, co masz — inaczej na górze lądują dania dwuskładnikowe,
          // bo im z definicji brakuje najmniej.
          var mam = tags.length - brak.length;
          doPosortowania.push({ li: li, n: brak.length, mam: mam });
          if (miss) {
            miss.hidden = false;
            miss.textContent = brak.length === 0
              ? "Masz wszystko"
              : "Brakuje " + brak.length + ": " +
                brak.slice(0, 3).map(function (t) { return etykiety[t] || t; }).join(", ") +
                (brak.length > 3 ? "…" : "");
            miss.setAttribute("data-none", brak.length === 0 ? "1" : "0");
          }
        } else if (miss) {
          miss.hidden = true;
        }
        if (ok) shown++;
      });

      // Kafelki leżą w siatce, więc kolejność zmieniamy właściwością `order`
      // zamiast przestawiać węzły — 263 elementy bez ruszania drzewa.
      if (doPosortowania.length) {
        doPosortowania.sort(function (a, b) { return a.n - b.n || b.mam - a.mam; });
        doPosortowania.forEach(function (x, i) { x.li.style.order = i; });
      } else {
        cards.forEach(function (c) { c.parentElement.style.order = ""; });
      }

      countEl.textContent = shown + " " +
        plural(shown, ["przepis", "przepisy", "przepisów", "przepisu"]);
      emptyEl.hidden = shown !== 0;

      var n = state.ings.length;
      // „Mam w lodówce” to tryb pokazywania, nie filtr — nie doliczamy go,
      // żeby licznik nie mówił „(4)” przy trzech zaznaczonych składnikach.
      var aktywne = n + (state.q ? 1 : 0) + (state.fav ? 1 : 0) + (state.cooked ? 1 : 0);
      if (!aktywne && state.fridge) aktywne = 0;
      if (clearEl) {
        clearEl.hidden = aktywne === 0 && !state.fridge;
        if (clearCount) clearCount.textContent = aktywne ? "(" + aktywne + ")" : "";
      }
      if (stateEl) {
        stateEl.textContent = n
          ? n + " " + plural(n, ["wybrany", "wybrane", "wybranych", "wybranego"])
          : "wybierz składniki";
        stateEl.setAttribute("data-active", n ? "1" : "0");
      }
      // Zapisujemy tylko składniki — pora posiłku, szukanie i tryby zawsze
      // startują od zera.
      remember("filters", { ings: state.ings }, state.ings.length > 0);
      renderChips();
    }

    /* --------------------------------------- ulubione, ugotowane, lodówka -- */

    var fav = ulubione();
    var cooked = ugotowane();

    function odswiezSerca() {
      [].forEach.call(document.querySelectorAll("[data-fav]"), function (btn) {
        var on = fav.indexOf(btn.getAttribute("data-fav")) !== -1;
        btn.setAttribute("aria-pressed", on ? "true" : "false");
        btn.firstChild.textContent = on ? "\u2665" : "\u2661";
      });
      cards.forEach(function (card) {
        card.setAttribute("data-cooked", cooked[card.getAttribute("data-slug")] ? "1" : "0");
      });
      if (favCount) favCount.textContent = fav.length || "";
      if (cookedCount) cookedCount.textContent = Object.keys(cooked).length || "";
      if (favBtn) favBtn.disabled = fav.length === 0 && !state.fav;
      if (cookedBtn) cookedBtn.disabled = Object.keys(cooked).length === 0 && !state.cooked;
    }

    document.addEventListener("click", function (ev) {
      var btn = ev.target.closest && ev.target.closest("[data-fav]");
      if (!btn) return;
      ev.preventDefault();
      var slug = btn.getAttribute("data-fav");
      fav = ustawUlubiony(slug, fav.indexOf(slug) === -1);
      odswiezSerca();
      if (state.fav) apply();
    });

    function trybPrzelacz(btn, klucz) {
      if (!btn) return;
      btn.addEventListener("click", function () {
        state[klucz] = !state[klucz];
        btn.setAttribute("data-on", state[klucz] ? "1" : "0");
        btn.setAttribute("aria-pressed", state[klucz] ? "true" : "false");
        if (klucz === "fridge") {
          if (fridgeHint) fridgeHint.hidden = !state.fridge;
          if (state.fridge && panel) panel.open = true;
        }
        apply();
      });
    }

    trybPrzelacz(favBtn, "fav");
    trybPrzelacz(cookedBtn, "cooked");
    trybPrzelacz(fridgeBtn, "fridge");

    odswiezSerca();
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

    function scaled(ing, idx) {
      return skaluj(ing, factor(), units, resolve(ing, idx));
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
        // Podmieniamy sam tekst kroku, nie całe <li> — obok niego stoi jeszcze
        // przycisk minutnika i nadpisanie textContent by go skasowało.
        [].forEach.call(stepsList.children, function (li, i) {
          var txt = li.querySelector(".p-step__text") || li;
          txt.textContent = renderStepText(data.steps[i]);
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

    // Na telefonie gest cofania to podstawowy sposób zamykania nakładek.
    // Bez wpisu w historii „wstecz” wyrzucał ze strony przepisu na listę —
    // w środku gotowania. Otwarcie okna dokłada wpis, zamknięcie go zdejmuje.
    var zamykaHistoria = false;

    function pchnijHistorie(nazwa) {
      try {
        history.pushState({ pModal: nazwa }, "");
      } catch (e) {
        /* przeglądarka bez pushState — okno działa dalej, tylko bez „wstecz” */
      }
    }

    function zdejmijHistorie(nazwa) {
      if (zamykaHistoria) return;
      if (history.state && history.state.pModal === nazwa) history.back();
    }

    window.addEventListener("popstate", function () {
      zamykaHistoria = true;
      if (cook && cook.getAttribute("data-open") === "1") closeCook();
      else if (sheet && sheet.getAttribute("data-open") === "1") closeSheet();
      zamykaHistoria = false;
    });

    function openSheet() {
      if (sheet.getAttribute("data-open") === "1") return;
      renderShopping();
      sheet.setAttribute("data-open", "1");
      document.body.classList.add("p-cooking");
      zablokujTlo(sheet);
      pchnijHistorie("shopping");
      closeBtn.focus();
    }

    function closeSheet() {
      sheet.setAttribute("data-open", "0");
      document.body.classList.remove("p-cooking");
      odblokujTlo();
      openBtn.focus();
      zdejmijHistorie("shopping");
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
        var bought = boughtMap();
        var jednostka = wieloporcjowy
          ? plural(servings, ["porcja", "porcje", "porcji", "porcji"]) + " z planu"
          : plural(servings, ["osoba", "osoby", "osób", "osoby"]);
        makePdf({
          btn: pdfBtn,
          tytul: data.title,
          podtytul: servings + " " + jednostka + "  ·  " + data.slotLabel + " " + data.time,
          plik: "lista-zakupow-" + data.slug + "-" + servings +
                (wieloporcjowy ? "porcji" : "os") + ".pdf",
          sekcje: groupsForList().map(function (group) {
            var pozycje = [];
            data.ingredients.forEach(function (ing, idx) {
              if (!!ing.pantry !== group.pantry) return;
              var s = scaled(ing, idx);
              pozycje.push({
                tekst: lineShort(s),
                gramy: s.grams,
                odhaczone: !!bought[group.key + ":" + pozycje.length],
                uwaga: s.swapped ? "zamiennik" : "",
              });
            });
            return { label: group.label, pozycje: pozycje };
          }),
        });
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
      var cookTimerBtn = document.getElementById("cook-timer");
      if (cookTimerBtn) {
        var sek = (data.times || [])[step];
        cookTimerBtn.hidden = !sek;
        if (sek) {
          cookTimerBtn.textContent = minutnik.krok === step
            ? "\u23F1 " + mmss(zostalo()) + " · zatrzymaj"
            : "\u23F1 " + mmss(sek);
          cookTimerBtn.setAttribute("data-running", minutnik.krok === step ? "1" : "0");
        }
      }
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
      pchnijHistorie("cook");
      cookNext.focus();
      trzymajEkran();
    }

    function closeCook() {
      cook.setAttribute("data-open", "0");
      document.body.classList.remove("p-cooking");
      odblokujTlo();
      pusćEkran();
      cookStart.focus();
      zdejmijHistorie("cook");
    }

    if (cookStart) cookStart.addEventListener("click", openCook);
    if (cookClose) cookClose.addEventListener("click", closeCook);
    if (cookPrev) cookPrev.addEventListener("click", function () {
      if (step > 0) { step--; renderStep(); }
    });
    if (cookNext) cookNext.addEventListener("click", function () {
      if (step < data.steps.length - 1) { step++; renderStep(); }
      else {
        LS.set("step:" + data.slug, 0);
        oznaczUgotowane(data.slug);
        odswiezUgotowane();
        closeCook();
        toast("Smacznego! Oznaczyłem przepis jako ugotowany.");
      }
    });

    /* --------------------------------- ulubione, ugotowane, minutnik ------ */

    function odswiezSerce() {
      var on = ulubione().indexOf(data.slug) !== -1;
      [].forEach.call(document.querySelectorAll("[data-fav]"), function (btn) {
        btn.setAttribute("aria-pressed", on ? "true" : "false");
        btn.firstChild.textContent = on ? "\u2665" : "\u2661";
        btn.setAttribute("aria-label", on ? "Usuń z ulubionych" : "Dodaj do ulubionych");
      });
    }

    [].forEach.call(document.querySelectorAll("[data-fav]"), function (btn) {
      btn.addEventListener("click", function () {
        var teraz = ulubione().indexOf(data.slug) === -1;
        ustawUlubiony(data.slug, teraz);
        odswiezSerce();
        toast(teraz ? "Dodano do ulubionych" : "Usunięto z ulubionych");
      });
    });
    odswiezSerce();

    var cookedNote = document.getElementById("cooked-note");
    function odswiezUgotowane() {
      if (!cookedNote) return;
      var kiedy = ugotowane()[data.slug];
      cookedNote.hidden = !kiedy;
      if (kiedy) {
        var d = kiedy.split("-");
        cookedNote.textContent = "\u2713 Ugotowane " + d[2] + "." + d[1] + "." + d[0];
      }
    }
    odswiezUgotowane();

    // Minutnik. Czasy wyłapał generator z treści kroków, więc przycisk pojawia
    // się tylko tam, gdzie w przepisie naprawdę stoi określenie czasu.
    var czasy = data.times || [];
    var cookTimer = document.getElementById("cook-timer");

    function tekstMinutnika(krok, sek) {
      if (minutnik.krok === krok) return "\u23F1 " + mmss(zostalo()) + " · zatrzymaj";
      return "\u23F1 " + mmss(sek);
    }

    function podepnijMinutnik(btn, krok, sek) {
      btn.addEventListener("click", function () {
        if (minutnik.krok === krok) stopMinutnik();
        else startMinutnik(krok, sek);
      });
    }

    var przyciskiMinutnika = [].slice.call(document.querySelectorAll("[data-timer]"));
    przyciskiMinutnika.forEach(function (btn) {
      var krok = +btn.getAttribute("data-timer");
      podepnijMinutnik(btn, krok, czasy[krok] || 60);
    });

    if (cookTimer) {
      cookTimer.addEventListener("click", function () {
        if (minutnik.krok === step) stopMinutnik();
        else startMinutnik(step, czasy[step] || 60);
      });
    }

    minutnik.sluchacze.push(function () {
      przyciskiMinutnika.forEach(function (btn) {
        var krok = +btn.getAttribute("data-timer");
        btn.textContent = tekstMinutnika(krok, czasy[krok] || 60);
        btn.setAttribute("data-running", minutnik.krok === krok ? "1" : "0");
      });
      if (cookTimer && !cookTimer.hidden) {
        cookTimer.textContent = tekstMinutnika(step, czasy[step] || 60);
        cookTimer.setAttribute("data-running", minutnik.krok === step ? "1" : "0");
      }
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

  /* ================================================ ZBIORCZE ZAKUPY ======== */

  function initShopping() {
    var root = document.getElementById("koszyk");
    if (!root) return;

    var units = window.UNITS || {};
    var lista = document.getElementById("z-list");
    var hint = document.getElementById("z-hint");
    var search = document.getElementById("z-search");
    var searchClear = document.getElementById("z-search-clear");
    var cartEl = document.getElementById("z-cart");
    var countEl = document.getElementById("z-count");
    var emptyEl = document.getElementById("z-empty");
    var bodyEl = document.getElementById("z-body");
    var actions = document.getElementById("z-actions");
    var clearBtn = document.getElementById("z-clear");
    var resetBtn = document.getElementById("z-reset");
    var pdfBtn = document.getElementById("z-pdf");
    var slotChips = [].slice.call(root.querySelectorAll("[data-z-slot]"));

    var przepisy = [];
    var poSlugu = {};
    var koszyk = LS.get("koszyk", {});
    if (!koszyk || typeof koszyk !== "object") koszyk = {};
    var stan = { slot: "all", q: "" };

    /* ------------------------------------------------------- wczytanie --- */

    fetch(BASE + "dane/zakupy.json")
      .then(function (r) { return r.json(); })
      .then(function (d) {
        przepisy = d.recipes || [];
        przepisy.forEach(function (r) { poSlugu[r.s] = r; });
        // Zapisany koszyk mógł wskazywać przepis, którego już nie ma.
        Object.keys(koszyk).forEach(function (slug) {
          if (!poSlugu[slug]) delete koszyk[slug];
        });
        rysujListe();
        rysujKoszyk();
      })
      .catch(function () {
        if (hint) hint.textContent =
          "Nie udało się wczytać listy przepisów. Odśwież stronę.";
      });

    /* --------------------------------------------------- wybór przepisów - */

    function rysujListe() {
      var widoczne = przepisy.filter(function (r) {
        if (stan.slot !== "all" && r.sid !== stan.slot) return false;
        if (stan.q && matchScore(r.t, stan.q) === Infinity) return false;
        return true;
      });

      lista.innerHTML = "";
      widoczne.slice(0, 60).forEach(function (r) {
        var li = document.createElement("li");
        li.className = "p-zitem";
        li.setAttribute("data-in", koszyk[r.s] ? "1" : "0");

        var txt = document.createElement("span");
        txt.className = "p-zitem__t";
        txt.textContent = r.t;

        var meta = document.createElement("span");
        meta.className = "p-zitem__m p-num";
        meta.textContent = r.l + " · " + r.k + " kcal";

        var btn = document.createElement("button");
        btn.type = "button";
        btn.className = "p-zitem__b";
        btn.textContent = koszyk[r.s] ? "\u2713" : "+";
        btn.setAttribute("aria-label",
          (koszyk[r.s] ? "Usuń z listy: " : "Dodaj do listy: ") + r.t);
        btn.addEventListener("click", function () {
          if (koszyk[r.s]) delete koszyk[r.s];
          else koszyk[r.s] = 1;
          zapiszKoszyk();
          rysujListe();
          rysujKoszyk();
        });

        li.appendChild(txt);
        li.appendChild(meta);
        li.appendChild(btn);
        lista.appendChild(li);
      });

      if (hint) {
        hint.textContent = widoczne.length > 60
          ? "Pokazuję 60 z " + widoczne.length + " dań — dopisz coś do wyszukiwania."
          : widoczne.length + " " +
            plural(widoczne.length, ["danie", "dania", "dań", "dania"]);
      }
      if (searchClear) searchClear.hidden = !stan.q;
    }

    slotChips.forEach(function (chip) {
      chip.addEventListener("click", function () {
        stan.slot = chip.getAttribute("data-z-slot");
        slotChips.forEach(function (c) {
          var sel = c === chip;
          c.setAttribute("data-on", sel ? "1" : "0");
          c.setAttribute("aria-pressed", sel ? "true" : "false");
        });
        rysujListe();
      });
    });

    if (search) {
      search.addEventListener("input", function () {
        stan.q = search.value.trim();
        rysujListe();
      });
    }
    if (searchClear) {
      searchClear.addEventListener("click", function () {
        search.value = "";
        stan.q = "";
        rysujListe();
        search.focus();
      });
    }

    function zapiszKoszyk() {
      remember("koszyk", koszyk, Object.keys(koszyk).length > 0);
    }

    /* -------------------------------------------------------- scalanie --- */

    // Klucz scalania: kategoria składnika + rdzeń nazwy + jednostka. Sam rdzeń
    // to za mało (scaliłby chleb żytni z bezglutenowym), sama kategoria też
    // (to samo). Razem łączą „Ryż basmati” z „ryżu basmati” i nic ponadto.
    function zloz() {
      var poz = {};
      Object.keys(koszyk).forEach(function (slug) {
        var r = poSlugu[slug];
        if (!r) return;
        var f = koszyk[slug];
        r.i.forEach(function (a) {
          var ing = {
            qty: a[0], unit: a[1], unitLemma: a[2] || null, name: a[3],
            grams: a[4], pantry: !!a[5], tag: a[6] || "",
          };
          var lemat = ing.unitLemma || ing.unit;
          var klucz = ing.tag + "|" + rdzen(ing.name) + "|" + lemat;
          if (!poz[klucz]) {
            poz[klucz] = {
              qty: 0, grams: 0, unitLemma: ing.unitLemma, unit: ing.unit,
              name: ing.name, pantry: ing.pantry, zrodla: [],
              weightOnly: ing.unit === "g",
            };
          }
          var p = poz[klucz];
          p.qty += ing.qty * f;
          p.grams += ing.grams * f;
          if (p.zrodla.indexOf(r.t) === -1) p.zrodla.push(r.t);
        });
      });

      return Object.keys(poz).map(function (k) {
        var p = poz[k];
        var unit = p.unit;
        if (p.unitLemma && units[p.unitLemma]) unit = plural(p.qty, units[p.unitLemma]);
        return {
          tekst: p.weightOnly ? p.name
            : fmtQty(p.qty) + " " + skrot(unit) + " " + p.name,
          gramy: fmtGrams(p.grams),
          pantry: p.pantry,
          zrodla: p.zrodla,
          sort: norm(p.name),
        };
      }).sort(function (a, b) { return a.sort < b.sort ? -1 : 1; });
    }

    /* ---------------------------------------------------------- koszyk --- */

    function boughtMap() {
      var v = LS.get("bought:zakupy", {});
      return v && typeof v === "object" ? v : {};
    }

    function rysujKoszyk() {
      var slugi = Object.keys(koszyk);
      countEl.textContent = slugi.length ? "(" + slugi.length + ")" : "";
      emptyEl.hidden = slugi.length > 0;
      if (clearBtn) clearBtn.hidden = slugi.length === 0;
      if (actions) actions.hidden = slugi.length === 0;

      cartEl.innerHTML = "";
      slugi.forEach(function (slug) {
        var r = poSlugu[slug];
        if (!r) return;
        var li = document.createElement("li");
        li.className = "p-zcart__i";

        var a = document.createElement("a");
        a.href = BASE + "przepisy/" + slug + "/";
        a.className = "p-zcart__t";
        a.textContent = r.t;

        var st = document.createElement("div");
        st.className = "p-stepper p-stepper--sm";
        var minus = document.createElement("button");
        minus.type = "button";
        minus.className = "p-stepper__btn";
        minus.innerHTML = "&minus;";
        minus.setAttribute("aria-label", "Mniej porcji: " + r.t);
        var val = document.createElement("span");
        val.className = "p-num";
        val.textContent = koszyk[slug];
        var plus = document.createElement("button");
        plus.type = "button";
        plus.className = "p-stepper__btn";
        plus.textContent = "+";
        plus.setAttribute("aria-label", "Więcej porcji: " + r.t);
        minus.disabled = koszyk[slug] <= 1;
        minus.addEventListener("click", function () {
          if (koszyk[slug] > 1) { koszyk[slug]--; zapiszKoszyk(); rysujKoszyk(); }
        });
        plus.addEventListener("click", function () {
          if (koszyk[slug] < 12) { koszyk[slug]++; zapiszKoszyk(); rysujKoszyk(); }
        });
        st.appendChild(minus); st.appendChild(val); st.appendChild(plus);

        var usun = document.createElement("button");
        usun.type = "button";
        usun.className = "p-iconbtn";
        usun.innerHTML = "&times;";
        usun.setAttribute("aria-label", "Usuń z listy: " + r.t);
        usun.addEventListener("click", function () {
          delete koszyk[slug];
          zapiszKoszyk();
          rysujListe();
          rysujKoszyk();
        });

        li.appendChild(a);
        li.appendChild(st);
        li.appendChild(usun);
        cartEl.appendChild(li);
      });

      rysujListeZakupow();
    }

    function grupy() {
      return [
        { key: "buy", label: "Do kupienia", pantry: false },
        { key: "have", label: "Zwykle masz w kuchni", pantry: true },
      ];
    }

    function rysujListeZakupow() {
      bodyEl.innerHTML = "";
      if (!Object.keys(koszyk).length) return;
      var pozycje = zloz();
      var bought = boughtMap();

      grupy().forEach(function (g) {
        var swoje = pozycje.filter(function (p) { return p.pantry === g.pantry; });
        if (!swoje.length) return;

        var h = document.createElement("p");
        h.className = "p-group";
        h.textContent = g.label;
        bodyEl.appendChild(h);

        swoje.forEach(function (p, n) {
          var id = g.key + ":" + n;
          var label = document.createElement("label");
          label.className = "p-check";
          var cb = document.createElement("input");
          cb.type = "checkbox";
          cb.checked = !!bought[id];
          cb.addEventListener("change", function () {
            var b = boughtMap();
            if (cb.checked) b[id] = true; else delete b[id];
            remember("bought:zakupy", b, Object.keys(b).length > 0);
          });
          var txt = document.createElement("span");
          txt.className = "p-check__text";
          txt.textContent = p.tekst;
          if (p.zrodla.length > 1) {
            var zn = document.createElement("span");
            zn.className = "p-zfrom";
            zn.textContent = "z " + p.zrodla.length + " dań";
            zn.title = p.zrodla.join(" · ");
            txt.appendChild(document.createTextNode(" "));
            txt.appendChild(zn);
          }
          var gr = document.createElement("span");
          gr.className = "p-check__g";
          gr.textContent = p.gramy + " g";
          label.appendChild(cb);
          label.appendChild(txt);
          label.appendChild(gr);
          bodyEl.appendChild(label);
        });
      });
    }

    if (clearBtn) {
      clearBtn.addEventListener("click", function () {
        koszyk = {};
        zapiszKoszyk();
        rysujListe();
        rysujKoszyk();
        toast("Wyczyszczono listę");
      });
    }
    if (resetBtn) {
      resetBtn.addEventListener("click", function () {
        remember("bought:zakupy", {}, false);
        rysujListeZakupow();
        toast("Odznaczono wszystko");
      });
    }
    if (pdfBtn) {
      pdfBtn.addEventListener("click", function () {
        var pozycje = zloz();
        var bought = boughtMap();
        var dania = Object.keys(koszyk).length;
        var porcje = Object.keys(koszyk).reduce(function (a, k) { return a + koszyk[k]; }, 0);
        makePdf({
          btn: pdfBtn,
          tytul: "Zakupy na " + dania + " " +
                 plural(dania, ["danie", "dania", "dań", "dania"]),
          podtytul: porcje + " " +
                    plural(porcje, ["porcja", "porcje", "porcji", "porcji"]) +
                    " łącznie  ·  " +
                    Object.keys(koszyk).map(function (k) {
                      return poSlugu[k] ? poSlugu[k].t : k;
                    }).join(", "),
          plik: "zakupy-" + dania + "-dan.pdf",
          sekcje: grupy().map(function (g) {
            return {
              label: g.label,
              pozycje: pozycje.filter(function (p) { return p.pantry === g.pantry; })
                .map(function (p, n) {
                  return {
                    tekst: p.tekst,
                    gramy: p.gramy,
                    odhaczone: !!bought[g.key + ":" + n],
                    uwaga: p.zrodla.length > 1 ? "z " + p.zrodla.length + " dań" : "",
                  };
                }),
            };
          }),
        });
      });
    }
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

  // Generator PDF-u nie wie nic o przepisach — dostaje gotowy opis dokumentu.
  // Dzięki temu obsługuje i listę dla jednego dania, i zbiorczą listę na kilka.
  //
  //   opts = {
  //     tytul, podtytul, plik, btn,
  //     sekcje: [{ label, pozycje: [{ tekst, gramy, odhaczone, uwaga }] }]
  //   }
  function makePdf(opts) {
    var btn = opts.btn;
    var old = btn.textContent;
    btn.textContent = "Tworzę PDF…";
    btn.disabled = true;

    return ensurePdf().then(function () {
      var doc = new window.jspdf.jsPDF({ unit: "mm", format: "a4" });

      // Wbudowane kroje jsPDF nie mają polskich znaków — dokładamy własny.
      doc.addFileToVFS("DejaVu.ttf", window.PRZEPISY_FONT.regular);
      doc.addFont("DejaVu.ttf", "DejaVu", "normal");
      doc.addFileToVFS("DejaVu-Bold.ttf", window.PRZEPISY_FONT.bold);
      doc.addFont("DejaVu-Bold.ttf", "DejaVu", "bold");

      var M = 18, W = 210 - M * 2, y = M;

      function naglowekGrupy(label) {
        doc.setFont("DejaVu", "bold");
        doc.setFontSize(9);
        doc.setTextColor(120);
        doc.text(label.toUpperCase(), M, y);
        y += 7;
        doc.setFont("DejaVu", "normal");
        doc.setFontSize(11);
      }

      doc.setFont("DejaVu", "bold");
      doc.setFontSize(9);
      doc.setTextColor(120);
      doc.text("LISTA ZAKUPÓW", M, y);
      y += 8;

      doc.setFontSize(16);
      doc.setTextColor(20);
      var tytul = doc.splitTextToSize(opts.tytul, W);
      doc.text(tytul, M, y);
      y += tytul.length * 7 + 2;

      doc.setFont("DejaVu", "normal");
      doc.setFontSize(10);
      doc.setTextColor(110);
      var pod = doc.splitTextToSize(opts.podtytul || "", W);
      doc.text(pod, M, y);
      y += pod.length * 5 + 3;
      doc.setDrawColor(210);
      doc.line(M, y, M + W, y);
      y += 8;

      opts.sekcje.forEach(function (sek) {
        if (!sek.pozycje.length) return;
        if (y > 250) { doc.addPage(); y = M; }
        naglowekGrupy(sek.label);

        sek.pozycje.forEach(function (poz) {
          if (y > 275) {
            doc.addPage();
            y = M;
            // Po łamaniu strony powtarzamy nagłówek grupy — inaczej druga
            // strona zaczyna się od produktów bez żadnego kontekstu.
            naglowekGrupy(sek.label + " (ciąg dalszy)");
          }
          var done = !!poz.odhaczone;

          doc.setDrawColor(done ? 60 : 150);
          doc.setLineWidth(0.3);
          doc.rect(M, y - 3.6, 4, 4);
          if (done) {
            doc.setLineWidth(0.6);
            doc.line(M + 0.8, y - 1.6, M + 1.8, y - 0.4);
            doc.line(M + 1.8, y - 0.4, M + 3.3, y - 3);
          }

          doc.setTextColor(done ? 140 : 25);
          var tekst = poz.tekst + (poz.uwaga ? "  (" + poz.uwaga + ")" : "");
          var wrapped = doc.splitTextToSize(tekst, W - 30);
          doc.text(wrapped, M + 7, y);
          doc.setTextColor(150);
          doc.text(poz.gramy + " g", M + W, y, { align: "right" });
          y += wrapped.length * 5.6 + 2.4;
        });
        y += 4;
      });

      doc.setFont("DejaVu", "normal");
      doc.setFontSize(8);
      doc.setTextColor(150);
      doc.text("Gotuj z Lewym · wygenerowano " +
               new Date().toLocaleDateString("pl-PL"), M, 287);

      doc.save(opts.plik);
      toast("Zapisano " + opts.plik);
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
    initShopping();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
