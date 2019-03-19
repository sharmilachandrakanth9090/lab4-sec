from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Pilot
from .serializers import PilotSerializer

# Create your tests here.


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_pilot(first_name='',
                     last_name=''
                     ):
        if first_name != '' and last_name != '':
            Pilot.objects.create(first_name=first_name, last_name=last_name)

    def setUp(self):
        # add test data
        self.create_pilot('Jon', 'Shallow')
        self.create_pilot('Amelia', 'Earhart')
        self.create_pilot('Chuck', 'Yeager')
        self.create_pilot('Buzz', 'Aldrin')


class GetAllPilotsTest(BaseViewTest):

    def test_get_all_pilots(self):
        """
        This test ensure that all pilots added in the setUp method
        exist when we make a GET request to the pilots/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("pilots-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Pilot.objects.all()
        serialized = PilotSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
