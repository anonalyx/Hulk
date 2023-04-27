document.addEventListener("DOMContentLoaded", () => {
    const deleteButtons = document.querySelectorAll("#delete-button");

    deleteButtons.forEach((button) => {
        button.addEventListener("click", (event) => {
            row = event.target.closest("tr");
            const exercise = row.dataset.selection;
            // Remove from favorites API CALL

            row.remove();
        });
    });
});
