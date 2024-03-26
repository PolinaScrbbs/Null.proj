document.addEventListener('DOMContentLoaded', function () {
  var burgerMenuBtn = document.querySelector('.burger-menu-btn');
  var burgerMenu = document.querySelector('.burger-menu');

  burgerMenuBtn.addEventListener('click', function () {
    burgerMenu.style.display = 'block'; // Сначала делаем меню видимым
    document.body.style.overflowY = "hidden"
    setTimeout(function () {
      burgerMenu.classList.toggle('show');
    }, 0); // Запускаем анимацию прозрачности через setTimeout
  });

  burgerMenu.addEventListener('transitionend', function (event) {
    if (event.propertyName === 'opacity' && !burgerMenu.classList.contains('show')) {
      burgerMenu.classList.remove('hide');
      document.body.style.overflowY = "auto"
      burgerMenu.style.display = 'none'; // После анимации прозрачности скрываем меню
    }
  });
});


