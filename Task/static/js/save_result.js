const result_btn = document.getElementById('resultBotton');

if (result_btn) {
    result_btn.addEventListener('click', () => {
        saveResult();
    });
}

function saveResult() {
    var code = editor.getValue();
    var save_result = "True";
    var event_title = "{{ event }}";
    var task_id = "{{ task.id }}";

    fetch('/save_result/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            code: code,
            save_result: save_result,
            event_title: event_title,
            task_id: task_id
        }),
    })
    .then(response => response.json())
    .then(data => {
        const event = data.event;
        const task = data.task
        const url = '/' + event + '/' + task + '/';
        window.location.href = url;
    })
    .catch(error => console.error('Ошибка:', error));
}