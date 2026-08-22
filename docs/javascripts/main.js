// Obsługa dynamicznych porcji, przeliczania, listy zakupów i kroków
let currentStep = 0;

function updatePortions() {
  const input = document.getElementById('persons-count');
  if (!input) return;

  const count = parseFloat(input.value) || 1;

  // 1. Aktualizacja nagłówka: Składniki (na X osób)
  const headers = document.querySelectorAll('h2, h3');
  headers.forEach(h => {
    if (h.textContent.includes('Składniki')) {
      let word = 'osób';
      if (count === 1) {
        word = 'osobę';
      } else if (count >= 2 && count <= 4) {
        word = 'osoby';
      }
      h.textContent = `Składniki (na ${count} ${word})`;
    }
  });

  // 2. Aktualizacja gramatury oraz przeliczanie miar w nawiasach
  const items = document.querySelectorAll('.ing-item');
  items.forEach(item => {
    const base = parseFloat(item.getAttribute('data-base'));
    const unit = item.getAttribute('data-unit') || 'g';
    const name = item.getAttribute('data-name') || '';

    const measureBase = item.getAttribute('data-measure-base');
    const measureUnit = item.getAttribute('data-measure-unit');

    if (!isNaN(base)) {
      const newBase = Math.round((base * count) * 100) / 100;
      let text = `${newBase} ${unit} ${name}`;

      if (measureBase && measureUnit) {
        const newMeasure = Math.round((parseFloat(measureBase) * count) * 100) / 100;
        text += ` (${newMeasure} ${measureUnit})`;
      }

      item.textContent = text;
    }
  });
}

function toggleShoppingList() {
  const list = document.getElementById('shopping-list-box');
  if (!list) return;
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
  const personsInput = document.getElementById('persons-count');
  const persons = personsInput ? personsInput.value : 1;
  const titleElem = document.querySelector('h1');
  const title = titleElem ? titleElem.innerText : 'Przepis';

  let printWindow = window.open('', '', 'width=600,height=600');
  printWindow.document.write(`<html><head><title>Lista Zakupów</title></head><body>`);
  printWindow.document.write(`<h2>Lista zakupów - ${title} (Osoby: ${persons})</h2><ul>`);

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
  if (indicator) indicator.innerText = `Krok ${index + 1} z ${steps.length}`;
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