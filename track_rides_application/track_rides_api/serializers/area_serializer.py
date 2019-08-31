from rest_framework import serializers

from track_rides_application.track_rides_api.models.area_details import AreaDetails
from track_rides_application.track_rides_api.models.city_details import CityDetails


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaDetails
        fields =('id', 'area_name', 'area_address', 'city_id')

    def create(self, validated_data):
        city_id = CityDetails.objects.get(city_id=validated_data['city_id'])
        instance = AreaDetails.objects.create(
            area_name=validated_data['area_name'],
            area_address=validated_data['area_address'],
            city_id=city_id
        )
        return instance

    def update(self, instance, validated_data):
        pass
