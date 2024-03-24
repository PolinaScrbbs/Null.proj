document.addEventListener('DOMContentLoaded', function () {
  var burgerMenuBtn = document.querySelector('.burger-menu-btn');
  var burgerMenu = document.querySelector('.burger-menu');

  burgerMenuBtn.addEventListener('click', function () {
    burgerMenu.style.display = 'block'; // Сначала делаем меню видимым
    setTimeout(function () {
      burgerMenu.classList.toggle('show');
    }, 0); // Запускаем анимацию прозрачности через setTimeout
  });

  burgerMenu.addEventListener('transitionend', function (event) {
    if (event.propertyName === 'opacity' && !burgerMenu.classList.contains('show')) {
      burgerMenu.classList.remove('hide');
      burgerMenu.style.display = 'none'; // После анимации прозрачности скрываем меню
    }
  });
});


document.addEventListener('DOMContentLoaded', function() {
  const tabs = document.querySelectorAll('.tablink');
  tabs.forEach(tab => {
      tab.addEventListener('click', function() {
          const tabName = this.dataset.tab;
          openTab(tabName);
      });
  });

  function openTab(tabName) {
      const tabContents = document.querySelectorAll('.tabcontent');
      tabContents.forEach(content => {
          content.style.display = 'none';
      });
      
      const tabLinks = document.querySelectorAll('.tablink');
      tabLinks.forEach(link => {
          link.classList.remove('active');
      });

      document.getElementById(tabName).style.display = 'block';
      event.currentTarget.classList.add('active');
  }
});


document.addEventListener('DOMContentLoaded', function() {
  const dropdownBtn = document.querySelector('.languages__btn');
  const dropdownContent = document.querySelector('.languages__content');

  dropdownBtn.addEventListener('click', function(event) {
      dropdownContent.classList.toggle('show');
      event.stopPropagation(); // Остановить всплытие события, чтобы не срабатывало закрытие меню
  });

  // Закрывать меню при клике вне области меню
  window.addEventListener('click', function(event) {
      if (!event.target.matches('.languages__btn')) {
          if (dropdownContent.classList.contains('show')) {
              dropdownContent.classList.remove('show');
          }
      }
  });

  // Обработчик клика для каждой опции языка
  const languageOptions = document.querySelectorAll('.languages__content button');
  languageOptions.forEach(option => {
      option.addEventListener('click', function() {
          dropdownContent.classList.remove('show'); // Закрыть меню
          dropdownBtn.textContent = this.textContent; // Отобразить выбранный язык в названии кнопки меню
      });
  });
});


