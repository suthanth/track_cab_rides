from celery import shared_task
from django.db import transaction
import logging

logger = logging.getLogger(__name__)

from track_rides_application.track_rides_api.serializers.booking_serializer import BookingSerializer


@shared_task(name='booking-task')
def create_booking_task(booking_request):
    try:
        serializer = BookingSerializer()
        logger.debug("Inside task1")
        with transaction.atomic():
            application_data = serializer.create(booking_request)
        logger.debug("Inside task2")
        data={}
        data['app_id'] = application_data.id
        return data

    except Exception as exception:
        logger.exception(str(exception))
        data = {}
        data['app_id'] = 0
        return data
