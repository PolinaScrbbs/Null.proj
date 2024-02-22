from celery import shared_task
from datetime import datetime, time

@shared_task
def update_event_statuses_task(start_time):
    from .models import Event
    
    # Получаем текущую дату
    today = datetime.now().date()
    
    # Получаем события на сегодня с переданным временем начала
    events_to_update = Event.objects.filter(date=today, start_time=start_time)
    
    # Обновляем статусы для каждого события с переданным временем начала
    for event in events_to_update:
        event.event_status_update()
        event.save()

@shared_task
def schedule_update_event_statuses_task():
    from .models import Event

    # Получаем текущую дату
    today = datetime.now().date()
    
    # Получаем все события на сегодня
    events_today = Event.objects.filter(date=today)
    
    # Получаем время начала для каждого события
    start_times = [event.start_time for event in events_today]
    
    # Выбираем уникальные времена начала
    unique_start_times = set(start_times)
    
    # Запланировать выполнение задачи обновления статусов для каждого уникального времени начала
    for start_time in unique_start_times:
        # Запуск задачи в указанное время начала
        update_event_statuses_task.apply_async((start_time,), eta=start_time)

# Задаем время, когда нужно запустить задачу по планированию обновления статусов
scheduled_time = time(hour=12, minute=0)  # Например, в 12:00 PM