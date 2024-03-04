from django.db import models

#Языки програмирования, доступные для решения задания
class ProgrammingLanguage(models.Model):
    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'

    icon = models.ImageField(upload_to='media/programming_languages', blank=False, verbose_name='Иконка')
    title = models.CharField(max_length=40, unique=True, blank=False, verbose_name="Название")

    def __str__(self):
        return self.title
   