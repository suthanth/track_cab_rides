from __future__ import absolute_import
from celery import Celery
from django.conf import settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'track_rides_application.settings')

app = Celery('track_rides_application',
             backend='rpc://',
             broker='amqp://guest:guest@127.0.0.1/'
             )

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))



