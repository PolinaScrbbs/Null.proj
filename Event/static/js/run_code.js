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

const csrftoken = getCSRFToken(); 
const run_btn = document.getElementById('runButton');

run_btn.addEventListener('click', () => {
    runCode();
});

function runCode() {
    var code = editor.getValue();
    var task_id = "{{ task.id }}";

    fetch('/run_code/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({ 
            code: code, 
            task_id: task_id
        }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('output').innerText = data.CodeResult;
        document.getElementById('btn_output_data').click();
    })
    .catch(error => console.error('Ошибка:', error));
}