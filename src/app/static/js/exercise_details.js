document.addEventListener("DOMContentLoaded", () => {
    const favoritesButton = document.getElementById('add-favorites-button')
    favoritesButton.addEventListener("click", (event) => {
        const exercise = favoritesButton.dataset.exercise;
        var req_rul = '/add_favorite_exercise'
        let data = new FormData();
        data.append('exercise', exercise);
        fetch(req_rul, {
            'method': 'POST',
            'body': data
        })
        .then(response => response.json())
        .then(result => {
            if (result.success){
                console.log('success')
                favoritesButton.dataset.selected = 'true';
            }
            else {
                console.log(result.message)
            }
        })
        .catch(error => {
            console.log(error);
        });
    });
});