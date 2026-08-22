document.addEventListener("DOMContentLoaded", function() {
    const mealFilter = document.getElementById("meal-type-filter");
    const ingredientBoxes = document.querySelectorAll(".ingredient-checkbox");
    const recipeCards = document.querySelectorAll(".recipe-card");

    if (!mealFilter && ingredientBoxes.length === 0) return;

    function filterRecipes() {
        const selectedMeal = mealFilter ? mealFilter.value : "all";
        const selectedIngredients = Array.from(ingredientBoxes)
            .filter(cb => cb.checked)
            .map(cb => cb.value.toLowerCase());

        recipeCards.forEach(card => {
            const cardMeal = card.getAttribute("data-meal-type");
            const cardIngredients = card.getAttribute("data-ingredients").toLowerCase().split(",");

            const matchesMeal = (selectedMeal === "all" || cardMeal === selectedMeal);
            const matchesIngredients = selectedIngredients.every(ing => 
                cardIngredients.some(cIng => cIng.trim().includes(ing.trim()))
            );

            if (matchesMeal && matchesIngredients) {
                card.style.display = "block";
            } else {
                card.style.display = "none";
            }
        });
    }

    if (mealFilter) mealFilter.addEventListener("change", filterRecipes);
    ingredientBoxes.forEach(cb => cb.addEventListener("change", filterRecipes));
});