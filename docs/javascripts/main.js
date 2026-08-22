// Obsługa dynamicznych porcji, przeliczania, listy zakupów i kroków
let currentStep = 0;

function updatePortions() {
    const persons = parseInt(document.getElementById('persons-count').value) || 1;
    
    // Przeliczanie składników
    document.querySelectorAll('.ing-item').forEach(el => {
        const baseAmount = parseFloat(el.getAttribute('data-base'));
        const unit = el.getAttribute('data-unit') || '';
        const name = el.getAttribute('data-name');
        
        if (!isNaN(baseAmount)) {
            const total = (baseAmount * persons).toFixed(baseAmount % 1 === 0 ? 0 : 1);
            el.innerText = `${total} ${unit}${name}`;
            el.setAttribute('data-current-amount', total);
        }
    });

    // Aktualizacja w usuniętej/otwartej liście zakupów
    renderShoppingList();
}

function toggleShoppingList() {
    const list = document.getElementById('shopping-list-box');
    if (list.style.display === 'none' || !list.style.display) {
        renderShoppingList();
        list.style.display = 'block';
    } else {
        list.style.display = 'none';
    }
}

function renderShoppingList() {
    const container = document.getElementById('shopping-list-items');
    if (!container) return;
    
    container.innerHTML = '';
    document.querySelectorAll('.ing-item').forEach(el => {
        const text = el.innerText;
        const li = document.createElement('li');
        li.innerHTML = `<label><input type="checkbox"> ${text}</label>`;
        container.appendChild(li);
    });
}

function printShoppingList() {
    const persons = document.getElementById('persons-count').value;
    const title = document.querySelector('h1').innerText;
    let printWindow = window.open('', '', 'width=600,height=600');
    printWindow.document.write(`<html><head><title>Lista Zakupów</title></head><body>`);
    printWindow.document.write(`<h2>Lista zakupów - ${title} (Osoby:${persons})</h2><ul>`);
    
    document.querySelectorAll('#shopping-list-items li').forEach(li => {
        const checked = li.querySelector('input').checked ? '[X] ' : '[ ] ';
        printWindow.document.write(`<li>${checked}${li.innerText}</li>`);
    });
    
    printWindow.document.write(`</ul></body></html>`);
    printWindow.document.close();
    printWindow.focus();
    printWindow.print();
    printWindow.close();
}

function showStep(index) {
    const steps = document.querySelectorAll('.step-card');
    if (steps.length === 0) return;

    steps.forEach((step, i) => {
        step.classList.toggle('active', i === index);
    });

    currentStep = index;
    const prevBtn = document.getElementById('btn-prev');
    const nextBtn = document.getElementById('btn-next');
    const indicator = document.getElementById('step-indicator');

    if (prevBtn) prevBtn.disabled = (index === 0);
    if (nextBtn) nextBtn.disabled = (index === steps.length - 1);
    if (indicator) indicator.innerText = `Krok ${index + 1} z${steps.length}`;
}

function nextStep() {
    const steps = document.querySelectorAll('.step-card');
    if (currentStep < steps.length - 1) {
        showStep(currentStep + 1);
    }
}

function prevStep() {
    if (currentStep > 0) {
        showStep(currentStep - 1);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    showStep(0);
});