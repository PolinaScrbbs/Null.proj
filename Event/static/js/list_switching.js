const btn_task = document.getElementById('btn_task');
    const btn_output_data = document.getElementById('btn_output_data');
    const btn_tasks = document.getElementById('btn_tasks');
    const label = document.getElementById('label');
    const resOutput = document.getElementById('output')
    const buttonList = document.getElementById('buttonList');

    btn_task.addEventListener('click', () => {
        label.style.display = 'block';
        buttonList.style.display = 'none';
        resOutput.style.display = 'none';

        btn_task.classList.add('btn', 'btn-primary');

        btn_tasks.classList.remove('btn-primary');
        btn_output_data.classList.remove('btn-primary');

        btn_tasks.classList.add('btn');
        btn_output_data.classList.add('btn');
    });

    btn_output_data.addEventListener('click', () => {
        resOutput.style.display = 'block'
        label.style.display = 'none';
        buttonList.style.display = 'none';

        btn_output_data.classList.add('btn', 'btn-primary');

        btn_task.classList.remove('btn-primary');
        btn_tasks.classList.remove('btn-primary');

        btn_task.classList.add('btn');
        btn_tasks.classList.add('btn');

    });

    btn_tasks.addEventListener('click', () => {
        label.style.display = 'none';
        resOutput.style.display = 'none';
        buttonList.style.display = 'block';

        btn_tasks.classList.add('btn', 'btn-primary');

        btn_task.classList.remove('btn-primary');
        btn_output_data.classList.remove('btn-primary');

        btn_task.classList.add('btn');
        btn_output_data.classList.add('btn');
    });