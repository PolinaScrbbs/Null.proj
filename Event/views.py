import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from App.models import *
from Auth.models import User

from .models import *
from .functions import *
from .utils import *

#EVENT==========================================================================================>

@login_required
def event_info(request, event):
    event = Event.objects.get(title=event)
    try:
        Participant.objects.get(event=event, user=User.objects.get(username=request.user))
        is_reg = True
    except:
        is_reg = False

    context = {
        'event': event,
        'is_reg': is_reg
    }

    return render(request, 'event_info.html', context)

@login_required
def reg_event(request, event):
    user = User.objects.get(username=request.user)
    event = Event.objects.get(title=event)

    participant, created = Participant.objects.get_or_create(event=event, user=user)
    if created:
        event.number_of_participants_update()
    
    tasks = Task.objects.filter(event=event)
    task = tasks.first().title
    return redirect('event_task', event = event.title, task = task)

#TASK==========================================================================================>

@login_required
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

@login_required
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

@login_required
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
