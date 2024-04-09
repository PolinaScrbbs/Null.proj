# Generated by Django 4.2.10 on 2024-04-09 07:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App', '0001_initial'),
        ('Subject', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjectsocialnetwork',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Subject.organization', verbose_name='Организация'),
        ),
        migrations.AddField(
            model_name='subjectsocialnetwork',
            name='social_network',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.socialnetwork', verbose_name='Социальная сеть'),
        ),
        migrations.AddField(
            model_name='subjectsocialnetwork',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
