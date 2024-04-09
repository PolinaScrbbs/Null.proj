from django.urls import path
from .views import index, event_catalog, profile, upload_avatar

urlpatterns = [
    path('', index, name='index'),
    path('catalog/', event_catalog, name='catalog')
]

#Profile
urlpatterns += [
    path('@<str:username>/', profile, name='profile'),
    path('upload_avatar/', upload_avatar, name='upload_avatar' )
]
