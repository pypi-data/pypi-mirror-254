# 🌍 Regions, Districts &amp; Quarters Database

[![PyPI Version](https://img.shields.io/pypi/v/uzbekistan)](https://pypi.org/project/uzbekistan/)
[![Django Version](https://img.shields.io/badge/Django-5.x-green.svg)](https://www.djangoproject.com/)

Full Database of Uzbekistan Regions, Districts &amp; Quarters with
Latin, Cyrillic and Russian versions.

## Insights

Total Regions : 14 <br>
Total Regions/Cities : 205 <br>
Total Towns/Districts : 2,183+ <br>

Last Updated On : 5th June 2022

## Installation

You can install your app via pip:

```shell
pip install uzbekistan
```

Add it to your Django project's INSTALLED_APPS:

```python3

INSTALLED_APPS = [
    # ...
    'uzbekistan',
]
```

Configure views and models to which feature you want to use in your project.
You can enable/disable models and views for regions, districts and villages.

```python3
UZBEKISTAN = {
    'models': {
        'region': True,
        'district': True,
        'village': False,
    },
    'views': {
        'region': True,
        'district': True,
        'village': False,
    }
}
```

Include URL Configuration in the Project's urls.py

```python3
urlpatterns = [
    # ...
    path('', include('uzbekistan.urls'), name='uzbekistan'),
]
```

Load the data into your database

```shell
python3 manage.py loaddata regions
python3 manage.py loaddata districts
```

## Change logs

A new version available that includes many updates.

- Added **Villages** to the database
- Added Dynamic **URLs** for all models
- Added Dynamic **Views** for all models
- Added **Models** to Django Admin panel
- English translations added to **Region**

## Suggestions / Feedbacks

```
Suggestions & Feedbacks are Most Welcome
```

That's all Folks. Enjoy😊!