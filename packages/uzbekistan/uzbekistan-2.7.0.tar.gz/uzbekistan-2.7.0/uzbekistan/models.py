from django.conf import settings
from django.db.models import Model, CharField, ForeignKey, CASCADE


class Region(Model):
    name_uz = CharField(max_length=255, unique=True)
    name_oz = CharField(max_length=255, unique=True)
    name_ru = CharField(max_length=255, unique=True)
    name_en = CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'regions'

    def __str__(self):
        return self.name_uz


class District(Model):
    name_uz = CharField(max_length=255)
    name_oz = CharField(max_length=255)
    name_ru = CharField(max_length=255)
    name_en = CharField(max_length=255, null=True, blank=True)
    region = ForeignKey('uzbekistan.Region', on_delete=CASCADE)

    class Meta:
        db_table = 'districts'
        unique_together = ('name_uz', 'name_oz', 'name_ru', 'region')

    def __str__(self):
        return self.name_uz


class Village(Model):
    name_uz = CharField(max_length=255)
    name_oz = CharField(max_length=255)
    name_ru = CharField(max_length=255)
    district = ForeignKey('uzbekistan.District', on_delete=CASCADE)

    class Meta:
        db_table = 'villages'
        unique_together = ('name_uz', 'name_oz', 'name_ru', 'district')

    def __str__(self):
        return self.name_uz


def check_model(model):
    if model._meta.manged or not settings.UZBEKISTAN['models'].get(model.__name__.lower(), False):
        raise NotImplementedError(
            f"The model '{model}' is not enabled in the current configuration. "
            "Please check that this model is set to True in the 'models' dictionary "
            "of the UZBEKISTAN setting in your settings.py file."

        )
    if model == District and not settings.UZBEKISTAN['models'].get('region', False):
        raise NotImplementedError(
            "The 'District' model requires the 'Region' model to be enabled. "
            "Please ensure that 'Region' is set to True in the 'models' dictionary "
            "of the UZBEKISTAN setting in your settings.py file."
        )

    if model == Village:
        if not settings.UZBEKISTAN['models'].get('region', False):
            raise NotImplementedError(
                "The 'Village' model requires the 'Region' model to be enabled. "
                "Please ensure that 'Region' is set to True in the 'models' dictionary "
                "of the UZBEKISTAN setting in your settings.py file."
            )
        if not settings.UZBEKISTAN['models'].get('district', False):
            raise NotImplementedError(
                "The 'Village' model requires both 'Region' and 'District' models to be enabled. "
                "Please ensure that both are set to True in the 'models' dictionary "
                "of the UZBEKISTAN setting in your settings.py file."
            )
