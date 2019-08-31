from rest_framework import serializers

from track_rides_application.track_rides_api.models.user_details import UserDetails


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ('id', 'user_name', 'phone_number')

    def create(self, validated_data):
        instance = UserDetails.objects.create(
            user_name=validated_data['user_name'],
            phone_number=validated_data['phone_number']
        )
        return instance

    def update(self, instance, validated_data):
        pass
