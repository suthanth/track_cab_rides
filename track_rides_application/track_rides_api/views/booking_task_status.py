from celery.result import AsyncResult
from rest_framework import generics, status
from rest_framework.response import Response
import logging

logger = logging.getLogger(__name__)

from track_rides_application.track_rides_api.models.booking_details import BookingDetails
from track_rides_application.track_rides_api.serializers.booking_serializer import BookingSerializer


class BookingTaskStatus(generics.RetrieveAPIView):
    queryset = BookingDetails.objects.all()
    serializer_class = BookingSerializer

    def get(self, request, *args, **kwargs):
        task_id = self.kwargs['task_id']
        if not task_id:
            data = {}
            data['message'] = 'Invalid task Id'
            return Response(
                data=data,
                status=status.HTTP_400_BAD_REQUEST
            )

        result = AsyncResult(task_id)
        if result.ready():
            result_id = result.result['app_id']
            logger.debug('mmmmmmmmmm%s', result_id)
            if result_id:
                booking_details = self.queryset.get(pk=result_id)
                data = {}
                data['booking_details'] = BookingSerializer(booking_details).data
                return Response(
                    data=data,
                    status=status.HTTP_201_CREATED
                )

            else:
                data = {}
                data['message'] = 'Failed to create Booking details '
                return Response(
                    data=data,
                    status=status.HTTP_400_BAD_REQUEST
                )

        else:
            data = {}
            data['task_details'] = task_id
            return Response(
                data=data,
                status=status.HTTP_200_OK
            )
