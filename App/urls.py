from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import index, profile, upload_avatar, event_info, reg_event, event_task, save_task_result, event_form 

urlpatterns = [
    path('', index, name='index'),
    path('event_form', event_form, name="event_form"),
]

urlpatterns += [
    path('#<str:event>', event_info, name='event_info'),
    path('reg_event/<str:event>', reg_event, name='reg_event'),
    path('<str:event>/<str:task>', event_task, name='event_task'),
    path('result/<str:event>/<str:task>', save_task_result, name='save_task_result')
]

urlpatterns += [
    path('@<str:username>', profile, name='profile'),
    path('upload_avatar/', upload_avatar, name='upload_avatar' )
]

# urlpatterns +=[
#     path('import_file_form/', import_file_form, name="import_file_form"),
#     path('import_file/', import_file, name='import_file')
# ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)