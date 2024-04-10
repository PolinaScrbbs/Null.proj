document.addEventListener('DOMContentLoaded', function () {
  var burgerMenuBtn = document.querySelector('.burger-menu-btn');
  var burgerMenu = document.querySelector('.burger-menu');

  burgerMenuBtn.addEventListener('click', function () {
    burgerMenu.style.display = 'block'; 
    document.body.style.overflowY = "hidden"
    setTimeout(function () {
      burgerMenu.classList.toggle('show');
    }, 0); 
  });

  burgerMenu.addEventListener('transitionend', function (event) {
    if (event.propertyName === 'opacity' && !burgerMenu.classList.contains('show')) {
      burgerMenu.classList.remove('hide');
      document.body.style.overflowY = "auto"
      burgerMenu.style.display = 'none'; 
    }
  });
});


