from django.db import models


class CityDetails(models.Model):
    id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=255)

    class Meta:
        ordering = ['id']
