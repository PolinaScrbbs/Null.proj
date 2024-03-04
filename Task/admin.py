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
    list_display = ('input_data', 'output_data')

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

