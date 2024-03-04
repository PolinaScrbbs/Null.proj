from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import index, event_info, reg_event, profile, upload_avatar

urlpatterns = [
    path('', index, name='index'),
]

#Event
urlpatterns += [
    path('#<str:event>/', event_info, name='event_info'),
    path('reg_event/<str:event>/', reg_event, name='reg_event'),

]

#Profile
urlpatterns += [
    path('@<str:username>/', profile, name='profile'),
    path('upload_avatar/', upload_avatar, name='upload_avatar' )
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)