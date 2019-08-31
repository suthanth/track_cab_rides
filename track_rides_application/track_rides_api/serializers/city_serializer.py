from rest_framework import serializers

from track_rides_application.track_rides_api.models.city_details import CityDetails


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CityDetails
        fields = ('id', 'city_name')

    def create(self, validated_data):
        instance = CityDetails.objects.create(
            city_name=validated_data['city_name']
        )
        return instance

    def update(self, instance, validated_data):
        pass
