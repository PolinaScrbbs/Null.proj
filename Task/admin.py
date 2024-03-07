from django.contrib import admin

from .models.keys import *
from .models.models import *

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
    search_fields = ('task',)

@admin.register(TaskComment)
class TaskCommentAdmin(admin.ModelAdmin):
    list_display = ('task', 'author', 'content', 'date')
    search_fields = ('task', 'author', 'content', 'date')

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'task', 'is_right')
    search_fields = ('user', 'task', 'is_right')

