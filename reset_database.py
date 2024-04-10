import os
import django
from django.conf import settings

# Инициализация настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Null.settings')
django.setup()

from django.core.management import call_command
import shutil

def reset_database():
    # Удаление базы данных
    if os.path.exists('db.sqlite3'):
        os.remove('db.sqlite3')
    
    # Получение списка приложений
    apps = ['App', 'Subject', 'Event', 'Statistic']

    # Удаление и создание папок миграций в каждом приложении
    for app in apps:
        migrations_dir = os.path.join(app, 'migrations')
        if os.path.exists(migrations_dir):
            shutil.rmtree(migrations_dir)
        os.makedirs(migrations_dir, exist_ok=True)
        
        # Создание миграций для текущего приложения
        with open(os.path.join(migrations_dir, '__init__.py'), 'w'):
            pass  # Создаём пустой файл __init__.py в папке миграций
        os.chdir(app)  # Переходим в директорию приложения
        os.chdir('..')  # Возвращаемся в исходную директорию

    #Создаём миграции
    call_command('makemigrations', interactive=False)

    # Применение миграций
    call_command('migrate', interactive=False)

    # Загрузка фикстур
    fixture_path = os.path.join(settings.BASE_DIR, 'fixture', 'db.json')
    call_command('loaddata', fixture_path)

if __name__ == '__main__':
    reset_database()

