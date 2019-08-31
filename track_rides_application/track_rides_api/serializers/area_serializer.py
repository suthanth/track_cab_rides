from rest_framework import serializers

from track_rides_application.track_rides_api.models.area_details import AreaDetails


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaDetails
        fields =('id', 'area_name', 'area_address')

    def create(self, validated_data):
        instance = AreaDetails.objects.create(
            area_name=validated_data['area_name'],
            area_address=validated_data['area_address'],
        )
        return instance

    def update(self, instance, validated_data):
        pass
