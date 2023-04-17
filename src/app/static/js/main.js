document.addEventListener("DOMContentLoaded", function() {
    fetch('navbar.html')
      .then(response => response.text())
      .then(data => {
        document.querySelector('#navbar-container').innerHTML = data;
        addNavbarEventListeners();
      })
      .catch(error => {
        console.error('Error loading navbar:', error);
      });
});

function addNavbarEventListeners() {
    const brand_image = document.getElementById('brand-image');
    const brand = document.getElementById('brand')
    const nav_search_button = document.getElementById('nav_search_button')
    const nav_calcalc_button = document.getElementById('nav_calcalc_button')
    const nav_profile_button = document.getElementById('nav_profile_button')

    brand.addEventListener('click', () => {
        console.log('redirecting home')
        window.location.href = '/home';
    });
    brand_image.addEventListener('click', () => {
        console.log('redirecting home')
        window.location.href = '/home';
    })
    nav_search_button.addEventListener('click', () => {
        console.log('redirecting home')
        window.location.href = '/search';
    });
    nav_calcalc_button.addEventListener('click', () => {
        console.log('redirecting home')
        window.location.href = '/calculator';
    })
    nav_profile_button.addEventListener('click', () => {
        console.log('redirecting home')
        window.location.href = '/profile';
    });
}
