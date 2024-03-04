from django.contrib import admin

from .models.keys import *
from .models.models import *

@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator')
    search_fields = ('title', 'creatorfull__name', 'creator__email')

@admin.register(EventStatus)
class EventStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'direction')
    search_fields = ('title', 'direction__title')

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('event', 'user')
    search_fields = ('event__title', 'user__full_name', 'user__email')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(EventResult)
class EventResultAdmin(admin.ModelAdmin):
    search_fields = ('participant', 'is_completed')