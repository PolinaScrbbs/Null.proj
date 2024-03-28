from django.db import models
from django.contrib.auth import get_user_model

from .keys import Tag

from django.utils import timezone

class Direction(models.Model):
    class Meta:
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления' 
    
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='created_directions', verbose_name='Создатель')
    title = models.CharField(max_length=20, unique=True, verbose_name='Направление')

    def __str__(self):
        return self.title
    
class EventStatus(models.Model):
    class Meta:
        verbose_name = 'Статус события'
        verbose_name_plural = 'Статусы события'

    title = models.CharField(max_length=20, unique=True, verbose_name='Статус события')

    def __str__(self):
        return self.title
  
class Event(models.Model):
    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
    
    avatar = models.ImageField(upload_to='events', blank=True, verbose_name='Аватар')
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE, verbose_name='Направление')
    title = models.TextField( unique=True, verbose_name='Мероприятие')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    tag = models.ManyToManyField(Tag, verbose_name='Теги')
    number_of_participants = models.PositiveIntegerField(default=0, verbose_name='Количестов участников')
    status = models.ForeignKey(EventStatus, default=1, on_delete=models.CASCADE, verbose_name='Статус события')
    date = models.DateTimeField(verbose_name='Дата и время начала события')
    duration = models.DurationField(verbose_name='Длительность события')

    def number_of_participants_update(self):
        self.number_of_participants = Participant.objects.filter(event=self).count()
        self.save()

    def __str__(self):
        return self.title

class Participant(models.Model):
    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'
    
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name='Мероприятие', related_name='participant_event')
    user =  models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Участник', related_name='participant')
    
    def __str__(self):
        return self.user.username
    
class EventResult(models.Model):
    class Meta:
        verbose_name = 'Результат события'
        verbose_name_plural = 'Результаты события'
    
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE, verbose_name='Участник')
    # solved_count = models.PositiveSmallIntegerField(default=0, verbose_name='Количество решённых')
    is_completed = models.BooleanField(default=False)
    score = models.PositiveIntegerField(default=0, verbose_name='Баллы')

    # def get_time_before_event_start(self):
    #     return self.date - timezone.now()

    # def get_event_remaining_time(self):
    #     event_end_time = self.date + self.duration
    #     return event_end_time - timezone.now()

    # def event_status_update(self):
    #     time_to_start = self.get_time_before_event_start()
    #     if time_to_start < timezone.timedelta(0):
    #         self.status = EventStatus.objects.get(id=2)
    #     elif self.get_event_remaining_time() < timezone.timedelta(0):
    #         self.status = EventStatus.objects.get(id=3)
            
    # def save(self, *args, **kwargs):
    #     self.number_of_participants_update()
    #     self.event_status_update()
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    




            