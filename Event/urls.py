from django.conf import settings
from django.conf.urls.static import static

from django.urls import path

from .views import event_info, reg_event, event_task, run_code, save_result

#Event
urlpatterns = [
    path('#<str:event>/', event_info, name='event_info'),
    path('reg_event/<str:event>/', reg_event, name='reg_event'),

]

#Task
urlpatterns += [
    path('event:<str:event>/task:<str:task>/', event_task, name='event_task'),
    
]

#Code
urlpatterns += [
    path('run_code/', run_code, name='run_code'),
]

#Result
urlpatterns += [
    path('save_result/', save_result, name='save_task_result'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)