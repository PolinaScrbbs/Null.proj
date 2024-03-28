from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from Auth.models import CustomUser, Role
from Task.models.models import Task

from .models.models import Direction, Event, Participant
from .forms import ProfileForm

# @login_required
def index(request): 
    if request.user.is_authenticated:
        events = Event.objects.all()

        participant = Participant.objects.filter(user = request.user)
        participate_in =  participant
        registered_events = participate_in.values_list('event__title', flat=True)

        context = {
            'title': 'Мероприятия',
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
    event = Event.objects.get(title=event)
    try:
        Participant.objects.get(event=event, user=CustomUser.objects.get(username=request.user))
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
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=user)
        if profile_form.is_valid():
            profile_form.save()
            
    initial_data= {
        'username': user.username,
        'full_name': user.full_name,
        'email': user.email,
        'phone_number': user.phone_number,
    }
    profile_form = ProfileForm(initial=initial_data)  

    context={
        'title': 'Профиль',
        'user': user,
        'role': role,
        'profile_form': profile_form
    }

    return render(request, 'profile.html', context=context)

@login_required
def upload_avatar(request):
    if request.method == 'POST' and request.FILES.get('file'):
        user = CustomUser.objects.get(username=request.user)
        if user.is_authenticated:
            uploaded_file = request.FILES['file']
            user.photo = uploaded_file
            user.save()

            response_data = {'url': user.photo.url}
            return JsonResponse(response_data)

    return JsonResponse({'error': 'Invalid request'})

# @login_required
# def update_profile(request):
#     if request.method == 'POST':
#         form = ProfileForm(request.POST)
#         if form.is_valid():
#             # Хеширование пароля перед сохранением пользователя
#             password = form.cleaned_data['password']
#             hashed_password = make_password(password)

#             user = form.save(commit=False)
#             user.password = hashed_password
#             user.save()

#             return redirect('profile')
#     else:
#         form = ProfileForm()