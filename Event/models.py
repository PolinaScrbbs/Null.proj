from django.db import models
from django.contrib.auth import get_user_model
# from django.utils import timezone

from .abstract import Comment, Reward
from .utils import test_task

#EVENT==========================================================================================================================================>

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

class Tag(models.Model):
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    title = models.CharField(max_length=40, unique=True, blank=False, verbose_name="Название")
    description = models.TextField(blank=False, verbose_name="Описание")

    def __str__(self):
        return self.title
    
class Event(models.Model):
    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
    
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Создатель')
    avatar = models.ImageField(upload_to='events', blank=True, verbose_name='Аватар')
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE, verbose_name='Направление')
    title = models.TextField( unique=True, verbose_name='Мероприятие')
    description = models.TextField(verbose_name='Описание')
    used_skills = models.TextField(blank=True, null=True, verbose_name='Испольщующиеся навыки')
    detailed = models.TextField(blank=True, null=True, verbose_name='Подробнее')
    tag = models.ManyToManyField(Tag, verbose_name='Теги')
    number_of_participants = models.PositiveIntegerField(default=0, verbose_name='Количестов участников')
    status = models.ForeignKey(EventStatus, default=1, on_delete=models.CASCADE, verbose_name='Статус события')
    date = models.DateTimeField(verbose_name='Дата и время начала события')
    duration = models.DurationField(verbose_name='Длительность события')

    def number_of_participants_update(self):
        self.number_of_participants = Participant.objects.filter(event=self).count()
        self.save()

    #Количество заданий
    @property
    def task_count(self):
        return Task.objects.filter(event__title=self.title).count()
    
    #Количество опыта
    @property
    def exp(self):
        exp = sum(TaskReward.objects.filter(task__event=self).values_list('exp', flat=True))
        return exp
    
    #Количество очков
    @property
    def points(self):
        points = sum(TaskReward.objects.filter(task__event=self).values_list('points', flat=True))
        return points
    
    # @property
    # def get_detailed(self):
    #     points = sum(TaskReward.objects.filter(task__event=self).values_list('points', flat=True))
    #     return points

    def __str__(self):
        return self.title

#PARTICIPANT==========================================================================================================================================>

class Participant(models.Model):
    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'
    
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name='Мероприятие', related_name='participant_event')
    user =  models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Участник', related_name='participant')
    
    def __str__(self):
        return self.user.username
    
#TASK==========================================================================================================================================>

#Языки програмирования, доступные для решения задания
class ProgrammingLanguage(models.Model):
    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'

    icon = models.ImageField(upload_to='programming_languages', blank=False, verbose_name='Иконка')
    title = models.CharField(max_length=40, unique=True, blank=False, verbose_name="Название")

    def __str__(self):
        return self.title

class Task(models.Model):
    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
    
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name='Событие')
    title = models.CharField(max_length=40, unique=True, blank=False, verbose_name="Заголовок")
    programming_languages = models.ManyToManyField(ProgrammingLanguage, verbose_name="Доступные языки")
    condition = models.TextField(blank=False, verbose_name="Условие")
    note = models.TextField(blank=True, verbose_name="Примечание")
    answer_structure = models.TextField(default='#Введите ваш код здесь', blank=True, verbose_name='Структура ответа')  #Базовое поле кода

    def __str__(self):
        return self.title

class TestData(models.Model):
    class Meta:
        verbose_name = 'Тестовые данные'
        verbose_name_plural = 'Тестовые данные'
    
    task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name='Задание')
    input_data = models.TextField(blank=False, verbose_name='Входные данные')
    output_data = models.TextField(blank=False, verbose_name='Выходные данные')
    
class TaskReward(Reward):
    class Meta:
        verbose_name = 'Награда за задание'
        verbose_name_plural = 'Награды за задания'
    
    task = models.OneToOneField(Task, on_delete=models.CASCADE, verbose_name='Задание')
    
    def __str__(self):
        return self.task

class TaskComment(Comment):
    class Meta:
        verbose_name = 'Комментарий к заданию'
        verbose_name_plural = 'Комментарии к заданям'
    
    task = models.ForeignKey(Task, on_delete = models.CASCADE, verbose_name='Задание')

#RESULT==========================================================================================================================================>

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

class Result(models.Model):
    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'
    
    user = models.ForeignKey(Participant, on_delete=models.CASCADE, verbose_name='Участник')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name='Задание')
    result = models.TextField(blank=False, verbose_name='Результат')
    is_right = models.BooleanField(default=False, verbose_name='Правильность')
    
    def right_check(self):
        test_data = TestData.objects.filter(task=self.task)
        input_data_list = [data.input_data for data in test_data]
        output_data_list = [data.output_data for data in test_data]

        result, success = test_task(self.result, input_data_list, output_data_list)

        if success:
            self.is_right = True
            self.save()
        
        if self.is_right:
            reward_points = TaskReward.objects.get(task=self.task).ponts

            # Проверка на существование результатов участника, если нет, то создаём
            event_result, created = EventResult.objects.get_or_create(participant=self.user)

            # event_result.solved_count += 1
            event_result.score += reward_points
            event_result.save()