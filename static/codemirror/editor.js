 var editor = CodeMirror.fromTextArea(document.getElementById('code'), {
    theme: 'null',
    mode: 'python',
    indentUnit: 4, //Tab
    lineNumbers: true, //Циферки
    hintOptions: { // Параметры для автодополнения
        hint: CodeMirror.hint.python, // Функция автодополнения для Python
        completeSingle: false // Показывать автодополнение даже при вводе одиночного символа
    }
});


editor.on("change", function(cm, change) {
    if (change.text.length === 1 && /^[a-zA-Z0-9_]$/.test(change.text[0])) {
        cm.showHint(); 
    }
});

// Добавляем функциональность поиска
var searchCursor = editor.getSearchCursor('искомый текст', null, true);

function search() {
  if (searchCursor.findNext()) {
    // Найдено совпадение, делаем что-то с ним
    // Например, можем выделить найденный текст
    editor.setSelection(searchCursor.from(), searchCursor.to());
  } else {
    // Совпадения не найдены
    alert('Совпадения не найдены');
  }
}

// Обработчик для кнопки поиска
document.getElementById('searchButton').addEventListener('click', function() {
  search();
});

function getCSRFToken() {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Ищем CSRF токен по имени "csrftoken"
            if (cookie.substring(0, 10) === 'csrftoken=') {
                cookieValue = decodeURIComponent(cookie.substring(10));
                break;
            }
        }
    }
    return cookieValue;
}
    
const run_btn = document.getElementById('runButton')

run_btn.addEventListener('click', () => {
    var csrftoken = getCSRFToken();
    var code = editor.getValue()
    console.log('КОД ' + code)

    fetch('/run_code/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,  // Добавляем CSRF токен в заголовок запроса
        },
        body: JSON.stringify({ code: code }),
    })
        .then(response => response.json())
        .then(data => {
            // Отображение результата
            document.getElementById('output').innerText = data.CodeResult;
            document.getElementById('btn_output_data').click();
        })
            .catch(error => console.error('Ошибка:', error));

})


 function changeMode(language) {
    language = language.toLowerCase();
    console.log(language)
    // Обновляем режим в соответствии с выбранным языком
    editor.setOption("mode", language);
}

const btn_reset = document.getElementById('btn_reset')

btn_reset.addEventListener('click', () => {
    editor.setValue('{{ task.answer_structure }}');
})


