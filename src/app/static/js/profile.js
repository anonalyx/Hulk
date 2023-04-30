document.addEventListener("DOMContentLoaded", () => {
    const deleteButtons = document.querySelectorAll("#delete-button");

    deleteButtons.forEach((button) => {
        button.addEventListener("click", (event) => {
            // Remove from favorites API CALL
            const trElements = event.target.closest("tr");
            let thElements = trElements.getElementsByTagName('th');
            let exercise = thElements[1].innerText
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
            trElements.remove();
        });
    });
});
