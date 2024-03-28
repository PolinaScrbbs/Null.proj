import json
from django.http import JsonResponse
from django.shortcuts import render, redirect

from App.models.models import Event, Participant

from .models.models import Task, TestData, Result
from .functions import *
from .utils import *

#TASK==========================================================================================>

def event_task(request, event, task):
    event = Event.objects.get(title=event)
    tasks = Task.objects.filter(event=event)
    participant = Participant.objects.get(user=request.user, event=event)

    try:
        results = Result.objects.filter(user=participant, task__in=tasks)
    except Result.DoesNotExist:
        results = None

    result_titles = results.values_list('task__title', flat=True)

    is_last = None

    try:
        if tasks.count() - result_titles.count() <= 1:
            is_last = True
    except:
        is_last = False

    if task == 'None':
        task = get_next_task(0)

        context = {
            'event': event,
            'tasks': tasks,
            'task': task,
            'programming_languages': task.programming_languages.all(),
            'results': result_titles,
            'is_last': is_last
        }

        return redirect('event_task', event.title, task.title)
    else:
        task = Task.objects.get(title=task)

    context = {
        'event': event,
        'tasks': tasks,
        'task': task,
        'programming_languages': task.programming_languages.all(),
        'results': result_titles,
        'is_last': is_last
    }

    return render(request, 'event_task.html', context)

def save_result(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        event_title = data.get('event_title')
        task_id = data.get('task_id', None)
        code = data.get('code', '')

        task = Task.objects.get(id = int(task_id))

        if not Result.objects.filter(task=task).exists():
                participant = Participant.objects.get(user=request.user)
                result = Result.objects.create(user=participant, task=task, result=code)
                result.right_check()

        task_title = get_next_task(current_task_id = task_id).title
        return JsonResponse({'redirect': 'event_task', 'event': event_title, 'task': task_title})
    return JsonResponse({'error': 'Метод запроса не поддерживается'})

#CODE==========================================================================================>

def run_code(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        task_id = data.get('task_id', None)
        task = Task.objects.get(id = int(task_id))
        code = data.get('code', '')
        
        test_data_list = TestData.objects.filter(task=task)
        input_data_list = [data.input_data for data in test_data_list]
        output_data_list = [data.output_data for data in test_data_list]

        run_result , success = test_task(code, input_data_list, output_data_list)
        
        if success and not Result.objects.filter(task=task).exists():
            event_id = data.get('event_id', None)
            event = Event.objects.get(id=event_id)
            participant = Participant.objects.get(user=request.user, event=event)
            result = Result.objects.create(user=participant, task=task, result=code)
            result.right_check()
        
        return JsonResponse({'CodeResult': run_result})
    return JsonResponse({'error': 'Метод запроса не поддерживается'})
