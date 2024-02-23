import json
from django.http import JsonResponse

from django.shortcuts import render, redirect

from Auth.models import CustomUser, Role
from .models.models import Direction, Event, Participant, Task, TestData, Result
from .forms import EventForm, PhoneNumberForm

from .utils import execute_code

def index(request): 
    if request.user.is_authenticated:
        
        directions = Direction.objects.all()
        events = Event.objects.all()

        participant = Participant.objects.filter(participant = request.user)
        participate_in =  participant #Список ивентов в которых участвует юзер
        registered_events = participate_in.values_list('event__title', flat=True)

        context = { 
            'title': 'Главная страница', 
            'directions': directions, 
            'events': events,
            'registered_events': registered_events
        }

        return render(request, 'indexСтарый.html', context=context) 
    else: 
        return render(request, 'index.html')
    
def profile(request, username):
    user = CustomUser.objects.get(username=username)
    role = Role.objects.get(id=user.role_id)
    phone_number_form = PhoneNumberForm
    if request.method == 'POST':
        phone_number_form = PhoneNumberForm(request.POST)
        if phone_number_form.is_valid():
            phone_number = phone_number_form.cleaned_data['phone_number']
            CustomUser.objects.filter(id=user.id).update(phone_number=phone_number)
  
    context={
        'title': 'Профиль',
        'user': user,
        'role': role,
        'phone_number_form': phone_number_form
    }

    return render(request, 'profile.html', context=context)

def upload_avatar(request):
    if request.method == 'POST' and request.FILES.get('file'):
        user = CustomUser.objects.get(full_name=request.user)
        if user.is_authenticated:
            uploaded_file = request.FILES['file']
            user.photo = uploaded_file
            user.save()

            # Возвращаем JSON с URL новой фотографии
            response_data = {'url': user.photo.url}
            return JsonResponse(response_data)

    # Если что-то пошло не так, возвращаем ошибку
    return JsonResponse({'error': 'Invalid request'})

def event_info(request, event):
    try:
        Participant.objects.get(event=Event.objects.get(title=event), participant=CustomUser.objects.get(username=request.user))
        is_reg = True
    except:
        is_reg = False

    context = {
        'event': event,
        'is_reg': is_reg
    }

    return render(request, 'event/event_info.html', context)

def reg_event(request, event):
    user = CustomUser.objects.get(username=request.user)
    event = Event.objects.get(title=event)

    participant, created = Participant.objects.get_or_create(event=event, participant=user)
    if not created:
        tasks = Task.objects.filter(event=event)
        task = tasks.first().title
        return redirect('event_task', event = event.title, task = task)
    
    else:
        event.number_of_participants_update()
        return redirect('event_info', event = event.title)
    
def event_form(request):
    if request.method == 'POST':
        form = EventForm(request.user, request.POST)
        if form.is_valid():
            # Делаем что-то с формой, например, сохраняем событие
            event = form.save(commit=False)
            event.save()
            return redirect('index')
    else:
        form = EventForm(request.user)

    return render(request, 'event_form.html', {'form': form})

def event_task(request, event, task=None):
    event = Event.objects.get(title=event)
    tasks = Task.objects.filter(event=event)
    participant = Participant.objects.get(participant=request.user, event=event)

    try:
        results = Result.objects.filter(participant=participant, task__in=tasks)
    except Result.DoesNotExist:
        results = None

    result_titles = results.values_list('task__title', flat=True)

    is_last = False

    if tasks.count() - result_titles.count() <= 1:
        is_last = True

    if task == 'last':
        last_task = tasks.exclude(id__in=results.values('task')).first()
        task = last_task

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

    return render(request, 'event/event_task.html', context)

def run_code(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        task_id = data.get('task_id')
        task = Task.objects.get(id = int(task_id))
        code = data.get('code', '')

        test_data_list = TestData.objects.filter(task=task).first()
        input_data = [x.strip() for x in test_data_list.input_data.split(", ")]
        
        run_result, success = execute_code(code, input_data)

        save_result = data.get('save_result', None)  # Извлекаем параметр из данных запроса
        if save_result is not None:
            event_title = data.get('event_title')
            participant = Participant.objects.get(participant=request.user)
            if success:
                result = Result.objects.create(participant=participant, task=task, result=code)
                result.right_check()
                return JsonResponse({'redirect': 'event_last_task', 'event': event_title})
            else:
                return JsonResponse({'error': run_result})
        return JsonResponse({'CodeResult': run_result})
    return JsonResponse({'error': 'Метод запроса не поддерживается'})

# def save_task_result(request, event, task):
#     if request.method == 'POST':
#         # Получите данные из формы
#         result = request.POST.get('result')
        
#         event = Event.objects.get(title=event)
#         participant = Participant.objects.get(participant=request.user, event=event)
#         task = Task.objects.get(title=task)

#         Result.objects.get_or_create(
#             participant = participant,
#             task = task,
#             result = result,
#         )
        
#         result = Result.objects.get(participant = participant, task = task)

#         Result.right_check(result)

#         tasks = Task.objects.filter(event=event)

#         try:
#             results = Result.objects.filter(participant=participant, task__in=tasks)
#         except:
#             results = None
        
#         task = tasks.exclude(id__in=results.values('task')).first() #Первое задание, которого нет в результатах

#         return redirect('event', event, task)
            

# def import_file_form(request):
#     context = {
#         'title': 'Импорт'
#     }
    
#     return render(request, 'import.html', context)

# def add_event(sheet,row_num,  start_column):

#     # Цикл для чтения данных до окончания данных в первом столбце
#     while sheet.cell(row=row_num, column=start_column).value:
#         # Создаем объект Event, используя данные из текущей строки
#         data = {
#             'title': sheet.cell(row=row_num, column=1).value,
#             'date': sheet.cell(row=row_num, column=2).value,
#             'direction': Direction.objects.get(id = sheet.cell(row=row_num, column=3).value)
#         }
                
#         Event.objects.create(**data)

#         # Переходим к следующей строке
#         row_num += 1
                
# def add_user(sheet, row_num,  start_column):

#     # Цикл для чтения данных до окончания данных в первом столбце
#     while sheet.cell(row=row_num, column=start_column).value:
#         # Создаем объект Event, используя данные из текущей строки
#         data = {
#             'full_name': sheet.cell(row=row_num, column=1).value,
#             'password': sheet.cell(row=row_num, column=2).value,
#             'is_superuser': False,
#             'email': sheet.cell(row=row_num, column=3).value,
#             'phone_number':  sheet.cell(row=row_num, column=4).value,
#             'photo': None,
#             'is_active': True,
#             'is_staff': True,
#             'role_id': 3
#         }
                
#         CustomUser.objects.create(**data)

#         # Переходим к следующей строке
#         row_num += 1
        
# def import_file(request):
#     if request.method == 'POST' and request.FILES.get('file'):
#         uploaded_file = request.FILES['file']
#         model = request.POST.get('dropdown')

#         try:
#             # Загружаем книгу Excel
#             workbook = load_workbook(uploaded_file, data_only=True)

#             # Получаем активный лист
#             sheet = workbook.active

#             # Указываем диапазон столбцов для чтения
#             start_column = 1  # с первого столбца

#             # Указываем переменные для цикла
#             row_num = 1  # начиная с первой строки

#             if model == 'CustomUser':
#                 add_user(sheet, row_num, start_column)
#             else:
#                 add_event(sheet, row_num, start_column)
                
#             return redirect('import_file_form')

#         except Exception as e:
#             print(f"Error processing Excel file: {e}")
#             return JsonResponse({'status': 'error', 'message': 'Error processing Excel file'})

#     return JsonResponse({'status': 'error', 'message': 'Invalid request'})