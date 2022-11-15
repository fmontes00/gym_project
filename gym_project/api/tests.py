from unicodedata import name
from urllib import response
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from gym.models import Equipment


class APITest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.equipment = Equipment.objects.create(
            name="equipment_test",
            description="description_test",
        )

    def test_api_listview(self):
        response = self.client.get(reverse("equipment_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Equipment.objects.count(), 1)
        self.assertContains(response, self.equipment)


# Create your tests here.
