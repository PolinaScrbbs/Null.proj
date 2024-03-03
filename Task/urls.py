from django.urls import path

from .views import *

#Task
urlpatterns = [
    path('<str:event>/<str:task>/', event_task, name='event_task'),
    path('save_result/', save_result, name='save_task_result'),
]

#Code
urlpatterns += [
    path('run_code/', run_code, name='run_code'),
]