"""track_rides_application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from track_rides_application.track_rides_api.views.area_views import AreaView
from track_rides_application.track_rides_api.views.booking_task_status import BookingTaskStatus
from track_rides_application.track_rides_api.views.booking_views import BookingView
from track_rides_application.track_rides_api.views.city_views import CityView
from track_rides_application.track_rides_api.views.user_view import UserView
from track_rides_application.track_rides_api.views.vehicle_views import VehicleView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('booking/', BookingView.as_view(), name='booking'),
    path('area/', AreaView.as_view(), name='area'),
    path('city/', CityView.as_view(), name='city'),
    path('user/', UserView.as_view(), name='user'),
    path('vehicle/', VehicleView.as_view(), name='vehicle'),
    path('bookingStatus/<str:task_id>', BookingTaskStatus.as_view(), name='booking-status')
]
