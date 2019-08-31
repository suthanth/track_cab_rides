from django.db import models


class VehicleDetails(models.Model):
    id = models.AutoField(primary_key=True)
    vehicle_name = models.CharField(max_length=255)
    vehicle_model_name = models.CharField(max_length=255)

    class Meta:
        ordering = ['id']
