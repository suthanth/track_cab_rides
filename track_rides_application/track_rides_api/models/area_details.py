from django.db import models

from track_rides_application.track_rides_api.models.city_details import CityDetails


class AreaDetails:
    id = models.AutoField(primary_key=True)
    area_name = models.CharField(max_length=255)
    area_address = models.CharField(max_length=255)
    city_id = models.ForeignKey(CityDetails, on_delete=models.CASCADE)
