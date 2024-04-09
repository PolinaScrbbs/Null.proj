from django.db import models
from django.core.exceptions import ValidationError

from django.contrib.auth import get_user_model

from Subject.models import Organization

#СОЦ СЕТИ===============================================================================================>

#Социальные сети
class SocialNetwork(models.Model):
    title = models.CharField(max_length=40, unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Социальная сеть'
        verbose_name_plural = 'Социальные сети'

    def __str__(self):
        return self.title
   
#Ссылки на социальные сети субъектов 
class SubjectSocialNetwork(models.Model):
    social_network = models.ForeignKey(SocialNetwork, verbose_name='Социальная сеть', on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), verbose_name='Пользователь', on_delete=models.CASCADE, null=True, blank=True)
    organization = models.ForeignKey(Organization, verbose_name='Организация', on_delete=models.CASCADE, null=True, blank=True)
    url = models.URLField(verbose_name='Ссылка')
    
    def clean(self) -> None:
        if self.user and self.organization:
            raise ValidationError('Ссылка может принадлежать либо пользователю, либо организации, но не обоим одновременно.')

    class Meta:
        verbose_name = 'Социальная сеть'
        verbose_name_plural = 'Социальные сети'

    def __str__(self):
        if self.user:
            return f"{self.social_network} {self.user}'s: {self.url}"
        elif self.organization:
            return f"{self.social_network} {self.organization}'s: {self.url}"
        else:
            return f"{self.social_network}: {self.url}"




  




            