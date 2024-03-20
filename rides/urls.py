from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rides.views import RideViewSet

router = DefaultRouter()
router.register(r'rides', RideViewSet)

urlpatterns = [
    path('', include(router.urls)),
]