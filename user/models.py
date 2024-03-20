from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    STATUS_CHOICES = [
        ('DRIVER', 'driver'),
        ('RIDER', 'rider'),
    ]
    user_type = models.CharField(max_length=10, choices=STATUS_CHOICES,
                                default='rider')
