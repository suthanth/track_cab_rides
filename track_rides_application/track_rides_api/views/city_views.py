from rest_framework import generics, status
from rest_framework.response import Response

from track_rides_application.track_rides_api.models.city_details import CityDetails
from track_rides_application.track_rides_api.serializers.city_serializer import CitySerializer


class CityView(generics.ListCreateAPIView):
    queryset = CityDetails.objects.all()
    serializer_class = CitySerializer

    def post(self, request, *args, **kwargs):
        serializer = CitySerializer()
        application_data = serializer.create(request.data)
        return Response(
            data=CitySerializer(application_data).data,
            status=status.HTTP_201_CREATED
        )
