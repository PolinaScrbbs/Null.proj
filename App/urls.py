from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import profile, index, event, reg_event, upload_avatar, event_form, import_file_form, import_file

urlpatterns = [
    path('', index, name='index'),
    path('event/<str:title>', event, name='event'),
    path('reg_event/<int:event_id>', reg_event, name='reg_event' ),
    path('event_form', event_form, name="event_form"),
]

urlpatterns += [
    path('profile/', profile, name='profile'),
    path('upload_avatar/', upload_avatar, name='upload_avatar' )
]

urlpatterns +=[
    path('import_file_form/', import_file_form, name="import_file_form"),
    path('import_file/', import_file, name='import_file')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)