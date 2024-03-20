from django.test import TestCase
from rides.models import Ride
from user.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class RideAPITestCase(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create(username='test_user1', email='test_user1@example.com', user_type='rider')
        self.user2 = User.objects.create(username='test_user2', email='test_user2@example.com', user_type='rider')
        self.ride = Ride.objects.create(
            rider=self.user1,
            driver=self.user2,
            pickup_location='Location A',
            dropoff_location='Location B'
        )
        self.client.force_authenticate(user=self.user1)
        self.client.force_authenticate(user=self.user2)
    
    def test_get_rides(self):
        url = reverse('ride-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_ride(self):
        url = reverse('ride-list')
        data = {
            'driver': self.user2.id,
            'pickup_location': 'Location C',
            'dropoff_location': 'Location D'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_update_ride_status(self):
        url = reverse('ride-update-ride-status', kwargs={'pk': self.ride.id})
        data = {'status': 'STARTED'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)