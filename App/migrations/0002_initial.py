# Generated by Django 4.2.10 on 2024-02-29 05:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskcomment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='taskcomment',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.task', verbose_name='Задание'),
        ),
        migrations.AddField(
            model_name='task',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.event', verbose_name='Событие'),
        ),
        migrations.AddField(
            model_name='task',
            name='programming_languages',
            field=models.ManyToManyField(to='App.programminglanguage', verbose_name='Доступные языки'),
        ),
        migrations.AddField(
            model_name='result',
            name='participant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.participant', verbose_name='Участник'),
        ),
        migrations.AddField(
            model_name='result',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.task', verbose_name='Задание'),
        ),
        migrations.AddField(
            model_name='participant',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participant_event', to='App.event', verbose_name='Мероприятие'),
        ),
        migrations.AddField(
            model_name='participant',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participant', to=settings.AUTH_USER_MODEL, verbose_name='Участник'),
        ),
        migrations.AddField(
            model_name='eventresult',
            name='participant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.participant', verbose_name='Участник'),
        ),
        migrations.AddField(
            model_name='event',
            name='direction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.direction', verbose_name='Направление'),
        ),
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='App.eventstatus', verbose_name='Статус события'),
        ),
        migrations.AddField(
            model_name='event',
            name='tag',
            field=models.ManyToManyField(to='App.tag', verbose_name='Теги'),
        ),
        migrations.AddField(
            model_name='direction',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_directions', to=settings.AUTH_USER_MODEL, verbose_name='Создатель'),
        ),
    ]
