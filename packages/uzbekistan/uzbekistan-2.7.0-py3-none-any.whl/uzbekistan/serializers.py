from rest_framework.serializers import ModelSerializer

from uzbekistan.models import Region, District, Village


class RegionModelSerializer(ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class DistrictModelSerializer(ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'


class VillageModelSerializer(ModelSerializer):
    class Meta:
        model = Village
        fields = '__all__'
