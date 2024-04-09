from django.db import models
from django.contrib.auth import get_user_model

#Абстрактный комментарий
class Comment(models.Model):
    class Meta:
        abstract = True

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Автор')
    content = models.TextField(blank=False, verbose_name='Комментарий')
    date = models.DateTimeField(blank=False, auto_now_add=True, verbose_name='Дата комментария')
    like = models.PositiveIntegerField(default=0, verbose_name='Количество лайков')

# #Тип награды
# class RewardType(models.Model):
#     title = models.CharField(max_length=40, blank=False, verbose_name='Тип')

#Абстрактная награда
class Reward(models.Model):
    class Meta:
        abstract = True
    
    exp = models.PositiveIntegerField(blank=False, verbose_name="Опыт")
    points = models.PositiveIntegerField(blank=False, verbose_name="Поинты")
