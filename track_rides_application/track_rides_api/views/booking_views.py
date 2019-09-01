from celery import uuid
from rest_framework import generics, status
from rest_framework.response import Response

from track_rides_application.track_rides_api.models.booking_details import BookingDetails
from track_rides_application.track_rides_api.serializers.booking_serializer import BookingSerializer
from track_rides_application.track_rides_api.tasks import create_booking_task


class BookingView(generics.ListCreateAPIView):
    queryset = BookingDetails.objects.all()
    serializer_class = BookingSerializer

    def post(self, request, *args, **kwargs):
        try:
            task_id = uuid()
            create_booking_task.apply_async([request.data], task_id=task_id)
            data = {}
            data['task_details'] = task_id
            return Response(
                data=data,
                status=status.HTTP_200_OK
            )

        except Exception as exception:
            data = {}
            data['message'] = 'Exception' + str(exception)
            return Response(
                data=data,
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
