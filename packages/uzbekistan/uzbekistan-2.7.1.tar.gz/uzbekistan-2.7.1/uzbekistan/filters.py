from django.db.models import Q

from uzbekistan.models import Region, District, Village
from django_filters import CharFilter, DateFilter, ChoiceFilter, BooleanFilter, NumberFilter
from django_filters.rest_framework import FilterSet


class RegionFilterSet(FilterSet):
    name = CharFilter(method='filter_by_name')

    @staticmethod
    def filter_by_name(queryset, name, value):
        return queryset.filter(
            Q(name_uz__startswith=value) |
            Q(name_oz__startswith=value) |
            Q(name_ru__startswith=value)
        )

    class Meta:
        model = Region
        fields = ('name',)


class DistrictFilterSet(FilterSet):
    name = CharFilter(method='filter_by_name')

    @staticmethod
    def filter_by_name(queryset, name, value):
        return queryset.filter(
            Q(name_uz__startswith=value) |
            Q(name_oz__startswith=value) |
            Q(name_ru__startswith=value)
        )

    class Meta:
        model = District
        fields = ('name',)


class VillageFilterSet(FilterSet):
    name = CharFilter(method='filter_by_name')

    @staticmethod
    def filter_by_name(queryset, name, value):
        return queryset.filter(
            Q(name_uz__startswith=value) |
            Q(name_oz__startswith=value) |
            Q(name_ru__startswith=value)
        )

    class Meta:
        model = Village
        fields = ('name',)
