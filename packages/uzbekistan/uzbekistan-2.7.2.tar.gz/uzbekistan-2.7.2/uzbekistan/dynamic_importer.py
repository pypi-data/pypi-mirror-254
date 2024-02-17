from importlib import import_module

from django.conf import settings


def import_conditional_classes(module_name, class_type):
    module = import_module(module_name)
    for class_name, is_enabled in settings.UZBEKISTAN.get(class_type, {}).items():
        if is_enabled and settings.UZBEKISTAN['models'].get(class_name.lower(), False):
            yield getattr(module, f'{class_name.title()}ListAPIView')
