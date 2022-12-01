from django.apps import AppConfig


class CurriculoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'curriculo'

    def ready(self):
        from . import signals

default_app_config = 'curriculo.apps.CurriculoConfig'