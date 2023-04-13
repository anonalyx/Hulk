document.addEventListener('DOMContentLoaded', function() {
    const home_search = document.getElementById('home_search_button')
    const home_login = document.getElementById('home_login_signup_button')
    const home_profile_button = document.getElementById('home_profile_button')
    const home_calcalc = document.getElementById('home_calcalc_button')

    home_login.addEventListener('click', () => {
        console.log('redirecting login')
        window.location.href = '/'
    })
    home_calcalc.addEventListener('click', () => {
        console.log('redirecting to calorie calculator')
        window.location.href = '/calcalc'
    })

    home_search.addEventListener('click', () => {
        console.log('redirecting search')
        window.location.href = '/search'
    })
});