from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login

def registration(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Хеширование пароля перед сохранением пользователя
            password = form.cleaned_data['password']
            hashed_password = make_password(password)

            user = form.save(commit=False)
            user.password = hashed_password
            user.save()

            login(request, user)

            return redirect('index')
    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})
