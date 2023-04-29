document.addEventListener("DOMContentLoaded", () => {
    const favoritesButtons = document.querySelectorAll("#favorites-button");
    const searchTableRows = document.getElementById("search-results-table-rows")

    searchTableRows.addEventListener("click", (event) => {
        const row = event.target.closest("tr");
        const exercise = row.dataset.selection;
    });

    favoritesButtons.forEach((button) => {
        button.addEventListener("click", (event) => {
            const trElements = event.target.closest("tr");
            let thElements = trElements.getElementsByTagName('th');
            let exercise = thElements[1].innerText
            const isSelected = button.dataset.selected === 'true';

            if (!isSelected) {
                button.dataset.selected = 'true';
                // Add to favorites API CALL
                var req_url = '/add_favorite_exercise'
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
                button.dataset.selected = 'false';
                // Remove from favorites API CALL
                var req_url = '/remove_favorite_exercise'
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