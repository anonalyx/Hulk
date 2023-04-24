document.addEventListener("DOMContentLoaded", () => {
    const favoritesButtons = document.querySelectorAll("#favorites-button");
    const searchTableRows = document.getElementById("search-results-table-rows")

    searchTableRows.addEventListener("click", (event) => {
        const row = event.target.closest("tr");
        const exercise = row.dataset.selection;
    });

    favoritesButtons.forEach((button) => {
        button.addEventListener("click", (event) => {
            const exercise = event.target.closest("tr").dataset.selection;
            const isSelected = button.dataset.selected === 'true';

            if (!isSelected) {
                button.dataset.selected = 'true';
                // Add to favorites API CALL
            }
            else {
                button.dataset.selected = 'false';
                // Remove from favorites API CALL
            }
        });
    });
});