from rest_framework import serializers

from track_rides_application.track_rides_api.models.area_details import AreaDetails
from track_rides_application.track_rides_api.models.booking_details import BookingDetails
from track_rides_application.track_rides_api.models.city_details import CityDetails
from track_rides_application.track_rides_api.models.user_details import UserDetails
from track_rides_application.track_rides_api.models.vehicle_detaila import VehicleDetails


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingDetails
        fields = ('id', 'user_id', 'vehicle_model_id', 'package_id', 'travel_type_id', 'from_area_id', 'to_area_id',
                  'from_city_id', 'to_city_id', 'from_date', 'to_date', 'online_booking', 'mobile_site_booking',
                  'booking_created', 'from_lat', 'from_long', 'to_lat', 'to_long', 'Car_Cancellation')

    def create(self, validated_data):
        user_id = UserDetails.objects.get(id=validated_data['user_id'])
        vehicle_model_id = VehicleDetails(id=validated_data['vehicle_model_id'])
        from_area_id = AreaDetails.objects.get(id=validated_data['from_area_id'])
        to_area_id = AreaDetails.objects.get(id=validated_data['to_area_id'])
        from_city_id = CityDetails.objects.get(id=validated_data['from_city_id'])
        to_city_id = CityDetails.objects.get(id=validated_data['to_city_id'])
        instance = BookingDetails.objects.create(
            user_id=user_id,
            vehicle_model_id=vehicle_model_id,
            package_id=validated_data['package_id'],
            travel_type_id=validated_data['travel_type_id'],
            from_area_id=from_area_id,
            to_area_id=to_area_id,
            from_city_id=from_city_id,
            to_city_id=to_city_id,
            from_date=validated_data['from_date'],
            to_date=validated_data['to_date'],
            online_booking=validated_data['online_booking'],
            mobile_site_booking=validated_data['mobile_site_booking'],
            booking_created=validated_data['booking_created'],
            from_lat=validated_data['from_lat'],
            from_long=validated_data['from_long'],
            to_lat=validated_data['to_lat'],
            to_long=validated_data['to_long'],
            Car_Cancellation=validated_data['Car_Cancellation'],
        )
        return instance

    def update(self, instance, validated_data):
        pass
