from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from Subject.models import User, UserRole
from Event.models import Event, Participant
from .forms import ProfileForm

# @login_required
def index(request):
    if request.user.is_authenticated:
        return redirect('catalog')
    context = {
        'title':'.Null'
    }
    return render(request, 'index.html', context)

def event_catalog(request):
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
        events = Event.objects.all()

        context = {
            'title': 'Мероприятия',
            'events': events,
        }

        return render(request, 'event_catalog.html', context=context)
        
#PROFILE==========================================================================================>

@login_required 
def profile(request, username):
    user = User.objects.get(username=username)
    role = UserRole.objects.get(id=user.role_id)
    events = Event.objects.all()
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
        'profile_form': profile_form,
        'events': events
    }

    return render(request, 'profile.html', context=context)

@login_required
def upload_avatar(request):
    if request.method == 'POST' and request.FILES.get('file'):
        print(request.user)
        user = User.objects.get(username=request.user)
        if user.is_authenticated:
            uploaded_file = request.FILES['file']
            user.avatar = uploaded_file
            user.save()

            response_data = {'url': user.avatar.url}
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