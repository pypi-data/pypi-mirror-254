from django.apps import AppConfig
from django.conf import settings


class UzbekistanConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'uzbekistan'

    def ready(self):
        if not settings.UZBEKISTAN.get('models') or not settings.UZBEKISTAN.get('views'):
            raise Exception('UZBEKISTAN settings is not configured properly.')

        for model_name, is_enabled in settings.UZBEKISTAN['models'].items():
            if not is_enabled:
                model_name = model_name.title()
                self.get_model(model_name)._meta.managed = False
                self.get_model(model_name)._meta.abstract = True
