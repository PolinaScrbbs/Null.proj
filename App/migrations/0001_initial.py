# Generated by Django 3.2.23 on 2024-02-02 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, unique=True, verbose_name='Направление')),
            ],
            options={
                'verbose_name': 'Направление',
                'verbose_name_plural': 'Направления',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, upload_to='media/events', verbose_name='Аватар')),
                ('title', models.CharField(max_length=20, unique=True, verbose_name='Мероприятие')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('date', models.DateField(verbose_name='Дата мероприятия')),
            ],
            options={
                'verbose_name': 'Событие',
                'verbose_name_plural': 'События',
            },
        ),
        migrations.CreateModel(
            name='EventResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_completed', models.BooleanField(default=False)),
                ('score', models.PositiveIntegerField(default=0, verbose_name='Баллы')),
            ],
            options={
                'verbose_name': 'Результат события',
                'verbose_name_plural': 'Результаты события',
            },
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Участник',
                'verbose_name_plural': 'Участники',
            },
        ),
        migrations.CreateModel(
            name='ProgrammingLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='media/programming_languages', verbose_name='Иконка')),
                ('title', models.CharField(max_length=40, unique=True, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.TextField(verbose_name='Результат')),
                ('is_right', models.BooleanField(default=False, verbose_name='Правильность')),
            ],
            options={
                'verbose_name': 'Результат',
                'verbose_name_plural': 'Результаты',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, unique=True, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, unique=True, verbose_name='Заголовок')),
                ('condition', models.TextField(verbose_name='Условие')),
                ('note', models.TextField(verbose_name='Примечание')),
                ('answer_structure', models.TextField(default='#Введите ваш код здесь', verbose_name='Структура ответа')),
                ('answer', models.TextField(verbose_name='Ответ')),
            ],
            options={
                'verbose_name': 'Задание',
                'verbose_name_plural': 'Задания',
            },
        ),
        migrations.CreateModel(
            name='TaskComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Комментарий')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата комментария')),
                ('like', models.PositiveIntegerField(default=0, verbose_name='Количество лайков')),
            ],
            options={
                'verbose_name': 'Комментарий к заданию',
                'verbose_name_plural': 'Комментарии к заданям',
            },
        ),
        migrations.CreateModel(
            name='TestData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_data', models.TextField(verbose_name='Входные данные')),
                ('output_data', models.TextField(verbose_name='Выходные данные')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.task', verbose_name='Задание')),
            ],
            options={
                'verbose_name': 'Тестовые данные',
                'verbose_name_plural': 'Тестовые данные',
            },
        ),
        migrations.CreateModel(
            name='TaskReward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ponts', models.PositiveIntegerField(verbose_name='Поинты')),
                ('task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='App.task', verbose_name='Задание')),
            ],
            options={
                'verbose_name': 'Награда за задание',
                'verbose_name_plural': 'Награды за задания',
            },
        ),
    ]
