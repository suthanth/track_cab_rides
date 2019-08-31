from rest_framework import generics, status
from rest_framework.response import Response

from track_rides_application.track_rides_api.models.vehicle_detaila import VehicleDetails
from track_rides_application.track_rides_api.serializers.vehicle_serializer import VehicleSerializer


class VehicleView(generics.ListCreateAPIView):
    queryset = VehicleDetails.objects.all()
    serializer_class = VehicleSerializer

    def post(self, request, *args, **kwargs):
        serializer = VehicleSerializer()
        application_data = serializer.create(request.data)
        return Response(
            data=VehicleSerializer(application_data).data,
            status=status.HTTP_201_CREATED
        )
