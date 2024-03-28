from django.urls import path
from .views import index, profile, upload_avatar

urlpatterns = [
    path('', index, name='index'),
]

#Profile
urlpatterns += [
    path('@<str:username>/', profile, name='profile'),
    path('upload_avatar/', upload_avatar, name='upload_avatar' )
]
