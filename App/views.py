from django.shortcuts import render, redirect
from Auth.models import CustomUser, Role
from .models.models import Direction, Event, Participant, Task, Result
from .forms import EventForm, PhoneNumberForm, CodeForm
from django.http import JsonResponse
import sys
import io
import json
from django.templatetags.static import static

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

    context = {
        'event': event,
    }
    
    return render(request, 'event/event_info.html', context)

def reg_event(request, event):
    user = request.user
    event = Event.objects.get(title=event)

    try:
        participant = Participant.objects.get(event=event, participant=user)
        tasks = Task.objects.filter(event=event)

        results = Result.objects.filter(participant=participant, task__in=tasks)
        task = tasks.exclude(id__in=results.values('task')).first() #Первое задание, которого нет в результатах
        
        return redirect('task', event, task)
    except Participant.DoesNotExist:
        Participant.objects.create(event=event, participant=user)
        return redirect('event', event)
    
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

def event_task(request, event, task):

    if task == 'first':
        event = Event.objects.get(title=event)
        task = Task.objects.filter(event=event).first() 

    event = Event.objects.get(title=event)
    tasks = Task.objects.filter(event=event)
 
    participant = Participant.objects.get(participant=request.user, event=event)
    results = Result.objects.filter(participant=participant, task__in=tasks)
    results = results.values_list('task__title', flat=True)
    
    task = Task.objects.get(title = task)
    
    next_task = None
    try:
        for listTask in tasks.exclude(id__in=results.values('task')):
            if listTask.id > task.id:
                next_task = Task.objects.get(title=listTask.title)
                break  
    except:
        next_task = None
        
    context = {
        'event' : event,
        'tasks' : tasks,
        'task' : task,
        'next_task': next_task,
        'codeForm': CodeForm(),
        'programming_languages': task.programming_languages.all(),
        'results': results
    }
        
    return render(request, 'event/event_task.html', context)

def run_code(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        code = data.get('code', '')

        # Создаем объект для перехвата вывода
        stdout = io.StringIO()
        sys.stdout = stdout  # Перенаправляем стандартный вывод в объект

        try:
            exec(code)  # Выполняем код
            result = stdout.getvalue()  # Получаем результат из перехваченного вывода
            sys.stdout = sys.__stdout__  # Возвращаем стандартный вывод
            return JsonResponse({'CodeResult': result})
        
        except Exception as e:
            sys.stdout = sys.__stdout__  # Возвращаем стандартный вывод в случае исключения
            return JsonResponse({'CodeResult': str(e)})
    return JsonResponse({'error': 'Метод запроса не поддерживается'})

def save_task_result(request, event, task):
    if request.method == 'POST':
        # Получите данные из формы
        result = request.POST.get('result')
        
        event = Event.objects.get(title=event)
        participant = Participant.objects.get(participant=request.user, event=event)
        task = Task.objects.get(title=task)

        Result.objects.get_or_create(
            participant = participant,
            task = task,
            result = result,
        )
        
        result = Result.objects.get(participant = participant, task = task)

        Result.right_check(result)

        tasks = Task.objects.filter(event=event)

        try:
            results = Result.objects.filter(participant=participant, task__in=tasks)
        except:
            results = None
        
        task = tasks.exclude(id__in=results.values('task')).first() #Первое задание, которого нет в результатах

        return redirect('event', event, task)
            

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