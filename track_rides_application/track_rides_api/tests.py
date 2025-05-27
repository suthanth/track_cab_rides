from django.test import TestCase, override_settings
from django.urls import reverse

from track_rides_application.track_rides_api.models.area_details import AreaDetails


TEST_DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}


@override_settings(DATABASES=TEST_DATABASES)
class AreaViewTests(TestCase):
    def test_create_area(self):
        """POST to /area/ should create a new AreaDetails record."""
        url = reverse('area')
        data = {
            'area_name': 'Test Area',
            'area_address': '123 Test Street'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(AreaDetails.objects.count(), 1)
        area = AreaDetails.objects.first()
        self.assertEqual(area.area_name, data['area_name'])
        self.assertEqual(area.area_address, data['area_address'])

