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
                // Add to favorites API CALL
                var req_url = ADD_FAV_URL; // url_for('add_favorite_exercise') from head script
                // Create FormData to pass exercise
                let data = new FormData();
                data.append('exercise', exercise);
                // Send fetch request with FormData
                fetch(req_url, {
                    'method': 'POST',
                    'body': data
                })
                // Parse response to json
                .then(response => response.json())
                // Check if 'success' response is true
                .then(result => {
                    if (result.success){
                        console.log('success')
                        button.dataset.selected = 'true';
                    }
                    else {
                        console.log(result.message)
                    }
                })
                .catch(error => {
                    console.log(error);
                });

            }
            else {
                // Remove from favorites API CALL
                var req_url = REM_FAV_URL // url_for('remove_favorite_exercise') from head script
                // Create FormData to pass exercise
                let data = new FormData();
                data.append('exercise', exercise);
                fetch(req_url, {
                    'method': 'POST',
                    'body': data
                })
                // Parse response to json
                .then(response => response.json())
                // Check if 'success' response is true
                .then(result => {
                    if (result.success){
                        console.log('success')
                        button.dataset.selected = 'false';
                    }
                    else {
                        console.log(result.message)
                    }
                })
                .catch(error => {
                    console.log(error);
                });
            }
        });
    });
});
