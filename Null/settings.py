import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# # Добавьте ваши настройки Celery
# CELERY_BROKER_URL = 'amqp://guest:guest@localhost'  # URL для вашего брокера сообщений (RabbitMQ)
# CELERY_RESULT_BACKEND = 'rpc://'  # URL для бекенда результатов задач

# # Определите список приложений, содержащих задачи Celery
# CELERY_IMPORTS = (
#     'App.tasks',  # Замените 'App' на имя вашего приложения
# )

# # Настройки Celery
# CELERY_TASK_TRACK_STARTED = True
# CELERY_TASK_TIME_LIMIT = 30 * 60  # Ограничение времени выполнения задачи (в секундах), если нужно

# # Задайте список принятых форматов контента
# CELERY_ACCEPT_CONTENT = ['json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-k=s58ugb@@w=fih5nql$a8gs9=2e%*2xfc^1z^r8zs^3gfho)v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'Subject',
    'Statistic',
    'App',
    'Event'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Null.urls'

WSGI_APPLICATION = 'Null.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    'default': {
        # "ENGINE": "django.db.backends.postgresql",
        # 'NAME': 'Null',
        # 'USER': 'postgres',
        # 'PASSWORD': '111',
        # 'HOST': 'localhost',  # Или IP-адрес вашего сервера PostgreSQL
        # 'PORT': '5432',       # Порт PostgreSQL
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  
    }
}

AUTH_USER_MODEL = 'Subject.User'

#Настройка аутентификации по usermane или email
AUTHENTICATION_BACKENDS = [
    'Subject.backends.EmailOrUsernameModelBackend',
]

#Backend для восстановления пароля
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' #Backend
EMAIL_HOST = 'smtp.gmail.com' #Почта gmail
EMAIL_PORT = 587 #Порт gmail
EMAIL_USE_TLS = True #Использовать защищенное соединение
EMAIL_HOST_USER = 'polinascaraboobs@gmail.com'
EMAIL_HOST_PASSWORD = 'auqt begs eumx ttqo'

# # Настройки Celery
# CELERY_BROKER_URL = 'amqp://localhost'  # URL для подключения к RabbitMQ
# CELERY_RESULT_BACKEND = 'rpc://'  # URL для хранения результатов выполнения задач

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

#Перенаправление после логина
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'catalog'
LOGOUT_REDIRECT_URL = 'login'

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

#Установка русского языка для полей восстановления пароля
LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#TEMPLATES, STATIC, MEDIA===============================================================================>
MY_APPS = [
    'Subject',
    'App',
    'Task'
]

TEMPLATES_URL = '/templates/'

TEMPLATES = [ 
    { 
        'BACKEND': 'django.template.backends.django.DjangoTemplates', 
        'DIRS': [
            os.path.join(BASE_DIR, "templates"),
            *[os.path.join(BASE_DIR, app, 'templates') for app in MY_APPS], 
        ], 
        'APP_DIRS': True, 
        'OPTIONS': { 
            'context_processors': [ 
                'django.template.context_processors.debug', 
                'django.template.context_processors.request', 
                'django.contrib.auth.context_processors.auth', 
                'django.contrib.messages.context_processors.messages', 
            ], 
        }, 
    }, 
]
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    *[os.path.join(BASE_DIR, app, 'static') for app in MY_APPS]
    ]

MEDIA_URL = '/media/' 
 
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

