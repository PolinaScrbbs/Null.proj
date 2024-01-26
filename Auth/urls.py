from django.urls import path
from .views import registration
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from .forms import RegistrationForm

form = RegistrationForm()

urlpatterns = [
    path('registration/', registration, name='registration'),
    path('login/', LoginView.as_view(template_name='auth/login.html'), {'extra_context': {'form': form}}, name='login'),
    path('logout', LogoutView.as_view(), name='logout')
]

urlpatterns += [
    path('reset_password/', auth_views.PasswordResetView.as_view(),
         name ='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(),
         name ='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(),
          name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(),
         name ='password_reset_complete'),
]
