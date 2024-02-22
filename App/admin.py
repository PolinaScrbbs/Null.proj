from django.contrib import admin
from .models.models import Direction, EventStatus, Event, Participant, TaskComment, Task, EventResult, TestData, TaskReward, Result
from .models.Keys.event import Tag
from .models.Keys.task import ProgrammingLanguage


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
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('event', 'title')
    search_fields = ('event', 'title')
    
@admin.register(EventResult)
class EventResultAdmin(admin.ModelAdmin):
    search_fields = ('participant', 'is_completed')
    
@admin.register(TaskReward)
class TaskRewardAdmin(admin.ModelAdmin):
    search_fields = ('task',)
    
@admin.register(TaskComment)
class TaskCommentAdmin(admin.ModelAdmin):
    list_display = ('task', 'author', 'content', 'date')
    search_fields = ('task', 'author', 'content', 'date')

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('participant', 'task', 'is_right')
    search_fields = ('participant', 'task', 'is_right')