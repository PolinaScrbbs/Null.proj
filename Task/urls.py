from django.conf import settings
from django.conf.urls.static import static

from django.urls import path

from .views import *

#Task
urlpatterns = [
    path('event:<str:event>/task:<str:task>/', event_task, name='event_task'),
    path('save_result/', save_result, name='save_task_result'),
]

#Code
urlpatterns += [
    path('run_code/', run_code, name='run_code'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)