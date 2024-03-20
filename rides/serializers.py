from rest_framework import serializers
from rides.models import Ride


class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = ['id', 'driver', 'pickup_location',
                  'dropoff_location', 'status', 'created_at', 'updated_at']
        
