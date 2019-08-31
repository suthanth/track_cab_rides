from django.db import models
from django.utils.timezone import now

from track_rides_application.track_rides_api.models.area_details import AreaDetails
from track_rides_application.track_rides_api.models.city_details import CityDetails
from track_rides_application.track_rides_api.models.user_details import UserDetails
from track_rides_application.track_rides_api.models.vehicle_detaila import VehicleDetails


class BookingDetails:
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE, null=True, blank=True)
    vehicle_model_id = models.ForeignKey(VehicleDetails, on_delete=models.CASCADE)
    package_id = models.PositiveIntegerField()
    travel_type_id = models.PositiveIntegerField()
    from_area_id = models.ForeignKey(AreaDetails, on_delete=models.CASCADE)
    to_area_id = models.ForeignKey(AreaDetails, on_delete=models.CASCADE)
    from_city_id = models.ForeignKey(CityDetails, on_delete=models.CASCADE)
    to_city_id = models.ForeignKey(CityDetails, on_delete=models.CASCADE)
    from_date = models.DateField(default=now, null=False)
    to_date = models.DateField(default=now, null=False)
    online_booking = models.BooleanField(default=False)
    mobile_site_booking = models.BooleanField(default=True)
    booking_created = models.DateTimeField(default=now(), null=False)
    from_lat = models.PositiveIntegerField()
    from_long = models.PositiveIntegerField()
    to_lat = models.PositiveIntegerField()
    to_long = models.PositiveIntegerField()
    Car_Cancellation = models.BooleanField(default=False)
