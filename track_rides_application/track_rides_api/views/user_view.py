from rest_framework import generics, status
from rest_framework.response import Response

from track_rides_application.track_rides_api.models.user_details import UserDetails
from track_rides_application.track_rides_api.serializers.user_serializer import UserSerializer


class UserView(generics.ListCreateAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer()
        application_data = serializer.create(request.data)
        return Response(
            data=UserSerializer(application_data).data,
            status=status.HTTP_201_CREATED
        )
