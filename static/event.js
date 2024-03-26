//статусы
const statusElements = document.querySelectorAll('.events__status');

statusElements.forEach(function(status) {
    status.addEventListener('click', function() {
        statusElements.forEach(function(s) {
            s.classList.remove('active-status');
        });

        status.classList.add('active-status');
    });
});