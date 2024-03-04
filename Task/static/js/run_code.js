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