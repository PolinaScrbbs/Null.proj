from django.db import models
from django.contrib.auth import get_user_model

class Tag(models.Model):
    title = models.CharField(max_length=40, unique=True, blank=False, verbose_name="Название")
    description = models.TextField(blank=False, verbose_name="Описание")

    def __str__(self):
        return self.title

class Direction(models.Model):
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='created_directions', verbose_name='Создатель')
    title = models.CharField(max_length=20, unique=True, verbose_name='Направление')

    def __str__(self):
        return self.title
    
class Event(models.Model):
    avatar = models.ImageField(upload_to='media/events', blank=True, verbose_name='Аватар')
    title = models.CharField(max_length=20, unique=True, verbose_name='Мероприятие')
    date = models.DateField(verbose_name='Дата мероприятия')
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE, verbose_name='Направление')

    def __str__(self):
        return self.title

class ProgrammingLanguage(models.Model):
    icon = models.ImageField(upload_to='media/programming_languages', blank=False, verbose_name='Иконка')
    title = models.CharField(max_length=40, unique=True, blank=False, verbose_name="Название")

    def __str__(self):
        return self.title

class TestData(models.Model):
    input_data = models.TextField(blank=False, verbose_name='Входные данные')
    output_data = models.TextField(blank=False, verbose_name='Выходные данные')

class Comment(models.Model):
    class Meta:
        abstract = True

    author = models.ForeignKey(get_user_model(),  on_delete=models.CASCADE, verbose_name='Автор')
    content = models.TextField(blank=False, verbose_name='Комментарий')
    date = models.DateTimeField(blank=False, auto_now_add=True, verbose_name='Дата комментария')
    like = models.PositiveIntegerField(default=0, verbose_name='Количество лайков')

class TaskComment(Comment):
    class Meta:
        db_table = 'task_comment'

class Task(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name='Событие')
    tag = models.ManyToManyField(Tag)
    title = models.CharField(max_length=40, unique=True, blank=False, verbose_name="Заголовок")
    programming_languages = models.ManyToManyField(ProgrammingLanguage, verbose_name="Доступные языки")
    condition = models.TextField(blank=False, verbose_name="Условие")
    note = models.TextField(blank=False, verbose_name="Примечание")
    test_data = models.ManyToManyField(TestData, blank=False, verbose_name='Тестовые данные')
    answer_structure = models.TextField(default='#Введите ваш код здесь', verbose_name='Структура ответа')  #Базовое поле кода
    answer = models.TextField(blank=False, verbose_name="Ответ")
    comment = models.ManyToManyField(TaskComment, default=None, verbose_name='Комментарии')

    def __str__(self):
        return self.title

class Participant(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name='Мероприятие', related_name='participant_event')
    participant =  models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Пользователь', related_name='participant')
