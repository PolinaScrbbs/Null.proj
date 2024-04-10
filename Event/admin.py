from django.contrib import admin
from .models import *

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

@admin.register(ProgrammingLanguage)
class ProgrammingLanguageAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('event', 'title')
    search_fields = ('event', 'title')

@admin.register(TestData)
class TestDataAdmin(admin.ModelAdmin):
    list_display = ('id','task', 'get_task_condition', 'input_data', 'output_data')

    def get_task_condition(self, obj):
        return obj.task.condition

    get_task_condition.short_description = 'Условие'

@admin.register(TaskReward)
class TaskRewardAdmin(admin.ModelAdmin):
    list_display = ('task', 'exp', 'points')
    search_fields = ('task', 'exp', 'points')

@admin.register(TaskComment)
class TaskCommentAdmin(admin.ModelAdmin):
    list_display = ('task', 'author', 'content', 'date')
    search_fields = ('task', 'author', 'content', 'date')

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'task', 'is_right')
    search_fields = ('user', 'task', 'is_right')

