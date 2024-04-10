from django.apps import AppConfig


class StatisticConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Statistic'

    def ready(self) -> None:
        import Statistic.signals