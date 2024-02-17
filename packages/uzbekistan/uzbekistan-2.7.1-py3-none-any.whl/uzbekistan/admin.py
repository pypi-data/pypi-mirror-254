from django.conf import settings
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from uzbekistan.models import Region, District, Village

if settings.UZBEKISTAN['models'].get('region', False):
    @admin.register(Region)
    class RegionAdmin(ModelAdmin):
        list_display = ('name_uz', 'name_oz', 'name_ru', 'name_en')
        search_fields = ('name_uz', 'name_oz', 'name_ru', 'name_en')
        sortable_by = ('name_uz', 'name_oz', 'name_ru', 'name_en')

if settings.UZBEKISTAN['models'].get('district', False):
    @admin.register(District)
    class DistrictAdmin(ModelAdmin):
        list_display = ('name_uz', 'name_oz', 'name_ru', 'name_en', 'get_region_name')
        search_fields = ('name_uz', 'name_oz', 'name_ru', 'name_en', 'get_region_name')
        sortable_by = ('name_uz', 'name_oz', 'name_ru', 'name_en', 'region')
        save_on_top = True

        def get_region_name(self, obj):
            return obj.region.name_uz

        get_region_name.short_description = 'Region'

if settings.UZBEKISTAN['models'].get('village', False):
    @admin.register(Village)
    class VillageAdmin(ModelAdmin):
        list_display = ('name_uz', 'name_oz', 'name_ru', 'get_district_name', 'get_region_name')
        search_fields = ('name_uz', 'name_oz', 'name_ru', 'get_district_name', 'get_region_name')
        sortable_by = ('name_uz', 'name_oz', 'name_ru', 'district')
        save_on_top = True

        def get_district_name(self, obj):
            return obj.district.name_uz

        get_district_name.short_description = 'District'

        def get_region_name(self, obj):
            return obj.district.region.name_uz

        get_region_name.short_description = 'Region'
