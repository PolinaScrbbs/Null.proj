from django.contrib import admin
from .models import Direction, Event, Participant, Tag, ProgrammingLanguage, TestData, TaskComment, Task

@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator')
    search_fields = ('title', 'creatorfull__name', 'creator__email')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'direction')
    search_fields = ('title', 'direction__title')

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('event', 'participant')
    search_fields = ('event__title', 'participant__full_name', 'participant__email')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(ProgrammingLanguage)
class ProgrammingLanguageAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(TestData)
class TestDataAdmin(admin.ModelAdmin):
    list_display = ('input_data', 'output_data')

@admin.register(TaskComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'date')
    search_fields = ('author', 'date')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('event', 'title')
    search_fields = ('event', 'title')
