from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from Auth.models import CustomUser, Role
from Task.models.models import Task

from .models.models import Direction, Event, Participant

from .forms import PhoneNumberForm

# @login_required
def index(request): 
    if request.user.is_authenticated:
        directions = Direction.objects.all()
        events = Event.objects.all()

        participant = Participant.objects.filter(user = request.user)
        participate_in =  participant #Список ивентов в которых участвует юзер
        registered_events = participate_in.values_list('event__title', flat=True)

        context = {
            'title': 'Главная страница', 
            'directions': directions, 
            'events': events,
            'registered_events': registered_events
        }

        return render(request, 'event_catalog.html', context=context) 
    else:
        context = {
            'title':'.Null'
        }
        return render(request, 'index.html', context)

#EVENT==========================================================================================>

@login_required
def event_info(request, event):
    try:
        Participant.objects.get(event=Event.objects.get(title=event), user=CustomUser.objects.get(username=request.user))
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
    user = CustomUser.objects.get(username=request.user)
    event = Event.objects.get(title=event)

    participant, created = Participant.objects.get_or_create(event=event, user=user)
    if not created:
        tasks = Task.objects.filter(event=event)
        task = tasks.first().title
        return redirect('event_task', event = event.title, task = task)
    
    else:
        event.number_of_participants_update()
        return redirect('event_info', event = event.title)

#PROFILE==========================================================================================>

@login_required 
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

@login_required
def upload_avatar(request):
    if request.method == 'POST' and request.FILES.get('file'):
        user = CustomUser.objects.get(full_name=request.user)
        if user.is_authenticated:
            uploaded_file = request.FILES['file']
            user.photo = uploaded_file
            user.save()

            response_data = {'url': user.photo.url}
            return JsonResponse(response_data)

    return JsonResponse({'error': 'Invalid request'})