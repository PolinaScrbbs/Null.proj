from django.contrib import admin
from django.urls import path, include

#Administrations
urlpatterns = [
    path('admin/', admin.site.urls),
]

#includes
urlpatterns += [
    path('',include('Subject.urls')),
    path('',include('App.urls')),
    path('',include('Event.urls')),
]