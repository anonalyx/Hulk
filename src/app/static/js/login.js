document.addEventListener('DOMContentLoaded', function() {

    const form = document.getElementById('user-form');
    const login_button= document.getElementById('login-button');
    const signup_button= document.getElementById('signup-button');
    login_button.addEventListener('click', function(event) {
        event.preventDefault();
        console.log('login button clicked')

        submitFormToEndpoint('/auth');
    });
    signup_button.addEventListener('click', function(event) {
        event.preventDefault();
        submitFormToEndpoint('/signup');
    });
    function submitFormToEndpoint(endpoint) {
        const formData = new FormData(form);
        const requestOptions = {
            method: 'POST',
            body: formData
        };

        fetch(endpoint, requestOptions)
            .then(response => {
                if (response.redirected) {
                    window.location.href = response.url;
                } else {
                    return response.json();
                }
            })
            .then(data => {
                console.log('Success:', data);
                // Handle the response data
            })
            .catch(error => {
                console.error('Error:', error);
                // Handle the error

            });
    }

});