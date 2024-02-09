from django.db import models
from django.contrib.auth import get_user_model

class Tag(models.Model):
    title = models.CharField(max_length=40, unique=True, blank=False, verbose_name="Название")
    description = models.TextField(blank=False, verbose_name="Описание")

    def __str__(self):
        return self.title
    
# class EventReward(Reward):
#     pass


    
    
    