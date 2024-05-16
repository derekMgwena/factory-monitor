from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DeviceViewSet, ParameterViewSet

router = DefaultRouter()
router.register(r'devices', DeviceViewSet)
router.register(r'parameters', ParameterViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
