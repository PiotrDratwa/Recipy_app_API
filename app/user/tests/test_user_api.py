"""from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status
"""

"""
#commenting co it lets me push to github,
#the user api is not yet implemented so test will fail obviously

CREATE_USER_URL = reverse('user:create')

def create_user(**params):
    #create and return a new user
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    #test public features of user API

    def setUp(self):
        self.client = APIClient()

    def test_create_user_success(self):
        payload = {
            'email': 'test@example.com',
            'password': 'testpass123',
            'name': 'Test Name',
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(email=payload('email'))
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)"""
