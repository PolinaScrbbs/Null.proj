from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import profile, index, base_event, reg_event, upload_avatar, event_form, task, task_result

urlpatterns = [
    path('', index, name='index'),
    path('<str:title>', base_event, name='base_event'),
    path('reg_event/<str:title>', reg_event, name='reg_event' ),
    path('event_form', event_form, name="event_form"),
]

urlpatterns += [
    path('<str:event>/<str:task>', task, name='task'),
    path('result/<str:event>/<str:task>', task_result, name='task_result')
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