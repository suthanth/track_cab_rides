from rest_framework import generics, status
from rest_framework.response import Response

from track_rides_application.track_rides_api.models.area_details import AreaDetails
from track_rides_application.track_rides_api.serializers.area_serializer import AreaSerializer


class AreaView(generics.ListCreateAPIView):
    queryset = AreaDetails.objects.all()
    serializer_class = AreaSerializer

    def post(self, request, *args, **kwargs):
        serializer = AreaSerializer()
        application_data = serializer.create(request.data)
        return Response(
            data=AreaSerializer(application_data).data,
            status=status.HTTP_201_CREATED
        )
