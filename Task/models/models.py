from django.db import models

from App.models.models import Event, EventResult, Participant
from .abstract import Comment, Reward
from .keys import ProgrammingLanguage

from Task.utils import test_task

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

class TaskComment(Comment):
    class Meta:
        verbose_name = 'Комментарий к заданию'
        verbose_name_plural = 'Комментарии к заданям'
    
    task = models.ForeignKey(Task, on_delete = models.CASCADE, verbose_name='Задание')

class Result(models.Model):
    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'
    
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE, verbose_name='Участник')
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
            event_result, created = EventResult.objects.get_or_create(participant=self.participant)

            # event_result.solved_count += 1
            event_result.score += reward_points
            event_result.save()