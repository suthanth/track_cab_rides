
from rest_framework import generics, status
from rest_framework.response import Response

from track_rides_application.track_rides_api.models.booking_details import BookingDetails
from track_rides_application.track_rides_api.serializers.booking_serializer import BookingSerializer


class BookingView(generics.ListCreateAPIView):
    queryset = BookingDetails.objects.all()
    serializer_class = BookingSerializer

    def post(self, request, *args, **kwargs):
        serializer = BookingSerializer()
        application_data = serializer.create(request.data)
        return Response(
            data=BookingSerializer(application_data).data,
            status=status.HTTP_201_CREATED
        )
