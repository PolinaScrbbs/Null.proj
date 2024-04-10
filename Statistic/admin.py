from django.contrib import admin

from .models import Level, UserStatistic, EventStatistic

@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('title', 'needed_exp')

@admin.register(UserStatistic)
class UserStatisticAdmin(admin.ModelAdmin):
    list_display = ('user', 'level')
    
@admin.register(EventStatistic)
class EventStatisticAdmin(admin.ModelAdmin):
    list_display = (
                    'event', 'total_number_of_participant', 
                    'total_number_of_participants_who_completed_event',
                    'total_number_of_completed_tasks',
                    'total_number_of_completed_exp', 'total_number_of_participant_points'
                )