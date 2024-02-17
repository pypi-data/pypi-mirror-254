from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView

from uzbekistan.models import Region, District, Village, check_model
from uzbekistan.serializers import RegionModelSerializer, DistrictModelSerializer
from uzbekistan.filters import RegionFilterSet, DistrictFilterSet, VillageFilterSet


class RegionListAPIView(ListAPIView):
    serializer_class = RegionModelSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RegionFilterSet
    pagination_class = None
    url_path = 'regions'
    url_name = 'region-list'
    url_relation = None

    def get_queryset(self):
        check_model(Region)
        return Region.objects.all()


class DistrictListAPIView(ListAPIView):
    serializer_class = DistrictModelSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = DistrictFilterSet
    pagination_class = None
    url_path = 'districts'
    url_name = 'district-list'
    url_relation = 'region_id'

    def get_queryset(self):
        check_model(District)
        return District.objects.filter(region_id=self.kwargs['region_id'])


class VillageListAPIView(ListAPIView):
    serializer_class = DistrictModelSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = VillageFilterSet
    pagination_class = None
    url_path = 'villages'
    url_name = 'village-list'
    url_relation = 'district_id'

    def get_queryset(self):
        check_model(Village)
        return Village.objects.filter(district_id=self.kwargs['district_id'])
