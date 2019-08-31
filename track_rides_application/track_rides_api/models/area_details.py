from django.db import models


class AreaDetails(models.Model):
    id = models.AutoField(primary_key=True)
    area_name = models.CharField(max_length=255)
    area_address = models.CharField(max_length=255)

    class Meta:
        ordering = ['id']
