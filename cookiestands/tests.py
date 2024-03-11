from django.test import TestCase

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import CookieStand

# class CookieStandsTests(TestCase):
#     # TODO: test your app
#     def test_your_app(self):
#         self.assertEqual("I have many tests", "I have no tests")

class CookieStandTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_cookiestand = CookieStand.objects.create(
            location="123 Main St",
            owner=testuser1,
            description="free parking",
            hourly_sales=20,
        )
        test_cookiestand.save()

    def setUp(self):
        self.client.login(username="testuser1", password="pass")

    def test_cookiestands_model(self):
        cookiestand = CookieStand.objects.get(id=1)
        actual_owner = str(cookiestand.owner)
        actual_location = str(cookiestand.location)
        actual_description = str(cookiestand.description)
        actual_hourly_sales = int(cookiestand.hourly_sales)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_location, "123 Main St")
        self.assertEqual(actual_description, "free parking")
        self.assertEqual(actual_hourly_sales, 20)

    def test_get_cookiestand_list(self):
        url = reverse("cookiestand_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        cookiestands = response.data
        self.assertEqual(len(cookiestands), 1)
        self.assertEqual(cookiestands[0]["location"], "123 Main St")

    def test_get_cookiestand_by_id(self):
        url = reverse("cookiestand_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        cookiestand = response.data
        self.assertEqual(cookiestand["location"], "123 Main St")

    def test_create_cookiestand(self):
        url = reverse("cookiestand_list")
        data = {"owner": 1, "location": "456 1st Ave", "description": "free wifi", "hourly_sales": 30}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        cookiestands = CookieStand.objects.all()
        self.assertEqual(len(cookiestands), 2)
        self.assertEqual(CookieStand.objects.get(id=2).location, "456 1st Ave")

    def test_update_cookiestand(self):
        url = reverse("cookiestand_detail", args=(1,))
        data = {
            "owner": 1,
            "location": "123 Main St",
            "description": "free parking",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        cookiestand = CookieStand.objects.get(id=1)
        self.assertEqual(cookiestand.location, data["location"])
        self.assertEqual(cookiestand.owner.id, data["owner"])
        self.assertEqual(cookiestand.description, data["description"])

    def test_delete_cookiestand(self):
        url = reverse("cookiestand_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        cookiestands = CookieStand.objects.all()
        self.assertEqual(len(cookiestands), 0)

    def test_authentication_required(self):
        self.client.logout()
        url = reverse("cookiestand_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
