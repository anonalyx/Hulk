document.addEventListener('DOMContentLoaded', function() {

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
        const username = document.getElementById('username-input');
        const email = document.getElementById('email-input');

        const formData = new FormData();
        formData.append('username', username.value);
        formData.append('email', email.value);
        const requestOptions = {
            method: 'POST',
            body: formData
        };

        fetch(window.location.origin + endpoint, requestOptions)
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