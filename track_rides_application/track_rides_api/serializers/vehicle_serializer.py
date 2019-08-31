from rest_framework import serializers

from track_rides_application.track_rides_api.models.user_details import UserDetails
from track_rides_application.track_rides_api.models.vehicle_detaila import VehicleDetails


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleDetails
        fields = ('id', 'vehicle_name', 'vehicle_model_name')

    def create(self, validated_data):
        instance = VehicleDetails.objects.create(
            vehicle_name=validated_data['vehicle_name'],
            vehicle_model_name=validated_data['vehicle_model_name']
        )
        return instance

    def update(self, instance, validated_data):
        pass
