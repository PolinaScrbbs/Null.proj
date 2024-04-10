from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from Event.models import Event
from .models import UserStatistic, EventStatistic

@receiver(post_save, sender=get_user_model())
def create_user_statistic(sender, instance, created, **kwargs):
    if created:
        UserStatistic.objects.create(user=instance)
        
@receiver(post_save, sender=Event)
def create_user_statistic(sender, instance, created, **kwargs):
    if created:
        EventStatistic.objects.create(event=instance)