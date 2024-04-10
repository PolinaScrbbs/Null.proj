from django.db import models
from django.contrib.auth import get_user_model
from Event.models import Event

class Level(models.Model):
    title = models.CharField(max_length=40, unique=True, verbose_name='Титульник')
    needed_exp = models.PositiveIntegerField(verbose_name='Необходимое количество опыта')
    
    class Meta:
        verbose_name = 'Уровень'
        verbose_name_plural = 'Уровни'

    def __str__(self):
        return self.title

class UserStatistic(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Пользователь')
    level = models.ForeignKey(Level, default = 1, on_delete=models.CASCADE, verbose_name='Уровень')
    exp = models.PositiveIntegerField(verbose_name='Опыт', default = 0)
    points = models.PositiveIntegerField(verbose_name='Очки', default = 0)
    completed_events = models.ManyToManyField(Event, verbose_name='Завершённые события', blank=True, default = None)
    
    def completed_events_count(self):
        return self.completed_events.count()
    
    class Meta:
        verbose_name = 'Статистика пользователя'
        verbose_name_plural = 'Статистики пользователей'

    def __str__(self):
        return f'Статистика {self.user}'
    
class EventStatistic(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name='Событие')
    total_number_of_participant = models.PositiveIntegerField(default=0, verbose_name='Общее количество участников')
    total_number_of_participants_who_completed_event = models.PositiveIntegerField(default=0, verbose_name='Общее количество участников, завершивших событие')
    total_number_of_completed_tasks = models.PositiveIntegerField(default=0, verbose_name='Общее количество решённых заданий')
    total_number_of_completed_exp= models.PositiveIntegerField(default=0, verbose_name='Общее количество полученного опыта')
    total_number_of_participant_points = models.PositiveIntegerField(default=0, verbose_name='Общее количество полученных очков')
    
    class Meta:
        verbose_name = 'Статистика события'
        verbose_name_plural = 'Статистики событий'
        
    def __str__(self):
        return f'Статистика {self.event}'
