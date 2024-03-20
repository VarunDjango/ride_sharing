from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets

from rides.models import Ride
from rides.permisssion import UserTypePermission
from rides.serializers import RideSerializer


class RideViewSet(viewsets.ModelViewSet):
    permission_classes = [UserTypePermission]
    http_method_names = ['get', 'post', 'put', 'patch']
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    
    def perform_create(self, serializer):
        serializer.save(rider=self.request.user)
        return super().perform_create(serializer)
    
    @action(detail=True, methods=['patch'])
    def update_ride_status(self, request, pk=None):
        ride = self.get_object()
        new_status = request.data.get('status', '').upper()
        
        if new_status not in dict(Ride.STATUS_CHOICES):
            return Response({'error': 'Invalid status'}, status=status.HTTP_400_BAD_REQUEST)
        
        if new_status == ride.status:
            return Response({'error': f'Ride is already in {new_status} status'}, status=status.HTTP_400_BAD_REQUEST)
        
        allowed_transitions = {
            'Requested': ['STARTED', 'CANCELLED'],
            'Started': ['COMPLETED'],
            'Completed': [],
            'Cancelled': []
        }
        if new_status not in allowed_transitions.get(ride.status, []):
            return Response({'error': f'Invalid status transition from {ride.status} to {new_status}'}, status=status.HTTP_400_BAD_REQUEST)
        
        ride.status = new_status
        ride.save()
        return Response({'message': f'Ride status updated to {new_status}'}, status=status.HTTP_200_OK)


    
    
