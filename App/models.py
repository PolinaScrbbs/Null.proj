from django.db import models
from django.core.exceptions import ValidationError

from django.contrib.auth import get_user_model

#ОРГАНИЗАЦИЯ===============================================================================================>

#Организации
class Organization(models.Model):
    avatar = models.ImageField(upload_to='organization_avatars', blank=True, null=True, verbose_name='Аватарка')
    owner = models.ForeignKey(get_user_model(), related_name='organizations_as_owner', verbose_name='Создатель', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True, blank=False, verbose_name='Уникальное название')
    full_title = models.CharField(max_length=100, blank=False, verbose_name='Полное название')
    description = models.TextField(blank=True, verbose_name='Описание')
    email = models.EmailField(unique=True, blank=False, verbose_name='E-mail')
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name='Номер телефона')
    members = models.ManyToManyField(get_user_model(), related_name='organizations_as_member', verbose_name='Участники')

    #Количество участников
    @property
    def members_number(self):
        return self.members.count()
    
    def save(self, *args, **kwargs):
        #Добавляем создателя организации в участники
        if not self.pk:
            self.members.add(self.owner)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации' 
    
    def __str__(self):
        return self.name

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




  




            