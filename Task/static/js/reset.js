const btn_reset = document.getElementById('btn_reset')

btn_reset.addEventListener('click', () => {
    editor.setValue('{{ task.answer_structure }}');
})