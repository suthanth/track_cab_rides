from django.db import models


class UserDetails:
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255)
    phone_number = models.PositiveIntegerField()
