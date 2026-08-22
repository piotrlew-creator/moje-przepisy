document.addEventListener("DOMContentLoaded", function() {
    // 1. Obsługa przeliczania porcji
    const personsInput = document.getElementById("persons-count");
    if (personsInput) {
        personsInput.addEventListener("input", function() {
            const factor = parseFloat(this.value) || 1;
            document.querySelectorAll(".ingredient").forEach(el => {
                const baseQty = parseFloat(el.getAttribute("data-base-qty"));
                const unit = el.getAttribute("data-unit") || "";
                if (!isNaN(baseQty)) {
                    const newQty = (baseQty * factor).toFixed(baseQty % 1 === 0 ? 0 : 1);
                    el.querySelector(".qty-value").innerText = newQty;
                }
            });
        });
    }

    // 2. Obsługa przełączania kroków (Wizzard)
    const steps = document.querySelectorAll(".step-card");
    let currentStep = 0;

    window.nextStep = function() {
        if (currentStep < steps.length - 1) {
            steps[currentStep].classList.remove("active");
            currentStep++;
            steps[currentStep].classList.add("active");
        }
    };

    window.prevStep = function() {
        if (currentStep > 0) {
            steps[currentStep].classList.remove("active");
            currentStep--;
            steps[currentStep].classList.add("active");
        }
    };

    // 3. Obsługa listy zakupów
    window.toggleShoppingList = function() {
        const modal = document.getElementById("shopping-list-container");
        if (!modal) return;
        
        if (modal.style.display === "none" || modal.style.display === "") {
            generateShoppingList();
            modal.style.display = "block";
        } else {
            modal.style.display = "none";
        }
    };

    function generateShoppingList() {
        const listItemsContainer = document.getElementById("shopping-list-items");
        listItemsContainer.innerHTML = "";
        
        document.querySelectorAll(".ingredient-item").forEach(item => {
            const name = item.querySelector(".ing-name").innerText;
            const qty = item.querySelector(".qty-value") ? item.querySelector(".qty-value").innerText : "";
            const unit = item.querySelector(".ing-unit") ? item.querySelector(".ing-unit").innerText : "";

            const label = document.createElement("label");
            label.className = "shopping-list-item";
            
            const checkbox = document.createElement("input");
            checkbox.type = "checkbox";
            checkbox.style.marginRight = "8px";
            checkbox.addEventListener("change", function() {
                label.classList.toggle("bought", this.checked);
            });

            label.appendChild(checkbox);
            label.appendChild(document.createTextNode(`${name} - ${qty} ${unit}`));
            listItemsContainer.appendChild(label);
        });
    }

    // 4. Generowanie PDF listy zakupów
    window.downloadPDF = function() {
        const element = document.getElementById("pdf-area");
        const recipeTitle = document.querySelector("h1") ? document.querySelector("h1").innerText : "Przepis";
        
        const opt = {
          margin:       10,
          filename:     `Lista_zakupow_${recipeTitle.replace(/\s+/g, '_')}.pdf`,
          image:        { type: 'jpeg', quality: 0.98 },
          html2canvas:  { scale: 2 },
          jsPDF:        { unit: 'mm', format: 'a4', orientation: 'portrait' }
        };

        html2pdf().set(opt).from(element).save();
    };
});