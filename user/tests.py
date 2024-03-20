from django.test import TestCase
from user.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class UserModelTestCase(TestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpassword',
            'first_name': 'Test',
            'last_name': 'User',
            'user_type': 'driver'
        }

    def test_create_user(self):
        user = User.objects.create_user(**self.user_data)
        self.assertEqual(user.username, self.user_data['username'])
        self.assertEqual(user.email, self.user_data['email'])
        self.assertTrue(user.check_password(self.user_data['password']))
        self.assertEqual(user.first_name, self.user_data['first_name'])
        self.assertEqual(user.last_name, self.user_data['last_name'])
        self.assertEqual(user.user_type, self.user_data['user_type'])

    def test_user_str_representation(self):
        user = User.objects.create_user(**self.user_data)
        self.assertEqual(str(user), self.user_data['username'])


class UserAPITestCase(APITestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpassword',
            'first_name': 'Test',
            'last_name': 'User',
            'user_type': 'driver'
        }
        self.user = User.objects.create_user(**self.user_data)

    def test_user_creation(self):
        url = reverse('user-list')
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword',
            'first_name': 'New',
            'last_name': 'User',
            'user_type': 'RIDER'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.last().username, 'newuser')
