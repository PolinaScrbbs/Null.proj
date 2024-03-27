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

//ФИЛЬТРАЦИЯ ПО СТАТУСАМ
document.addEventListener("DOMContentLoaded", function() {
    var allEvents = document.querySelectorAll(".eventCards__card");

    document.querySelectorAll(".events__status").forEach(function(status) {
        status.addEventListener("click", function() {
            var filter = this.textContent.trim();

            allEvents.forEach(function(event) {
                event.classList.remove("hidden");

                if (filter === "Зарегистрированные") {
                    var button = event.querySelector(".eventCards__btn button");
                    if (!button || button.textContent.trim() !== "Перейти") {
                        event.classList.add("hidden");
                    }
                } else if (filter === "Ближайшие") {
                    var eventDate = parseDate(event.querySelector(".eventCards__date").textContent.trim());
                    var today = new Date();
                    var threeDaysLater = new Date(today);
                    threeDaysLater.setDate(today.getDate() + 3);

                    if (eventDate < today || eventDate > threeDaysLater) {
                        event.classList.add("hidden");
                    }
                } else if (filter === "В этом месяце") {
                    var eventDate = parseDate(event.querySelector(".eventCards__date").textContent.trim());
                    var today = new Date();
                    var firstDayOfMonth = new Date(today.getFullYear(), today.getMonth(), 1);
                    var lastDayOfMonth = new Date(today.getFullYear(), today.getMonth() + 1, 0);

                    if (eventDate < firstDayOfMonth || eventDate > lastDayOfMonth) {
                        event.classList.add("hidden");
                    }
                }
            });
        });
    });
});

function parseDate(dateString) {
    var parts = dateString.split(' ');
    var day = parseInt(parts[0], 10);
    var month = parseMonth(parts[1]);
    var year = parseInt(parts[2], 10);
    var time = parts[4].split(':');
    var hour = parseInt(time[0], 10);
    var minute = parseInt(time[1], 10);

    return new Date(year, month, day, hour, minute);
}

function parseMonth(monthString) {
    var months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря'];
    return months.indexOf(monthString);
}
//ПОООИСК
document.addEventListener("DOMContentLoaded", function() {
    var allEvents = document.querySelectorAll(".eventCards__card");

    document.querySelector(".eventNav__input").addEventListener("input", function() {
        var searchTerm = this.value.trim().toLowerCase();

        allEvents.forEach(function(event) {
            var title = event.querySelector(".eventCards__title").textContent.trim().toLowerCase();
            var description = event.querySelector(".eventCards__description").textContent.trim().toLowerCase();
            var organizer = event.querySelector(".eventCards__role").textContent.trim().toLowerCase();

            if (title.indexOf(searchTerm) === -1 && description.indexOf(searchTerm) === -1 && organizer.indexOf(searchTerm) === -1) {
                event.classList.add("hidden");
            } else {
                event.classList.remove("hidden");
            }
        });
    });
});