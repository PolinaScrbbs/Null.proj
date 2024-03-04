# import os
# from celery import Celery

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Null.settings')

# app = Celery('Null')
# app.config_from_object('django.conf:settings', namespace='CELERY')
# app.conf.broker_url = 'amqp://guest:guest@localhost'

# app.autodiscover_tasks()