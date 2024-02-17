from django.urls import path

from uzbekistan.dynamic_importer import import_conditional_classes

urlpatterns = []
for view in import_conditional_classes('uzbekistan.views', 'views'):
    url_path = f'{view.url_path}/<int:{view.url_relation}>/' if view.url_relation else f'{view.url_path}/'
    urlpatterns.append(path(url_path, view.as_view(), name=f'{view.url_name}'))
