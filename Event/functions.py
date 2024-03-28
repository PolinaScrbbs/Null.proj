def get_next_task(current_task_id):
    from .models import Task, Result
    tasks_without_results = Task.objects.exclude(id__in=Result.objects.values_list('task_id', flat=True))

    if not tasks_without_results.exists():
        return Task.objects.first()

    next_task = tasks_without_results.filter(id__gt=current_task_id).first()

    if not next_task:
        return tasks_without_results.first()

    return next_task