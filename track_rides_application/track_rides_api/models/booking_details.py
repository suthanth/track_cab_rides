from django.db import models
from django.utils.timezone import now

from track_rides_application.track_rides_api.models.area_details import AreaDetails
from track_rides_application.track_rides_api.models.city_details import CityDetails
from track_rides_application.track_rides_api.models.user_details import UserDetails
from track_rides_application.track_rides_api.models.vehicle_detaila import VehicleDetails


class BookingDetails(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE, null=True, blank=True)
    vehicle_model_id = models.ForeignKey(VehicleDetails, on_delete=models.CASCADE)
    package_id = models.PositiveIntegerField()
    travel_type_id = models.PositiveIntegerField()
    from_area_id = models.ForeignKey(AreaDetails, related_name='from_area', on_delete=models.CASCADE)
    to_area_id = models.ForeignKey(AreaDetails, related_name='to_area', on_delete=models.CASCADE)
    from_city_id = models.ForeignKey(CityDetails, related_name='from_city', on_delete=models.CASCADE)
    to_city_id = models.ForeignKey(CityDetails, related_name='to_city', on_delete=models.CASCADE)
    from_date = models.DateTimeField(default=now, null=False)
    to_date = models.DateTimeField(default=now, null=False)
    online_booking = models.BooleanField(default=False)
    mobile_site_booking = models.BooleanField(default=True)
    booking_created = models.DateTimeField(default=now, null=False)
    from_lat = models.FloatField()
    from_long = models.FloatField()
    to_lat = models.FloatField()
    to_long = models.FloatField()
    Car_Cancellation = models.BooleanField(default=False)

    class Meta:
        ordering = ['id']
