from django.db import models
from user.models import User


class Ride(models.Model):
    STATUS_CHOICES = [
        ('REQUESTED', 'Requested'),
        ('STARTED', 'Started'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled')
    ]
    rider = models.ForeignKey(User, related_name='driver_as',
                              on_delete=models.CASCADE)
    driver = models.ForeignKey(User, related_name='rider_As',
                               on_delete=models.CASCADE)
    pickup_location = models.CharField(max_length=100)
    dropoff_location = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,
                              default='Requested')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
