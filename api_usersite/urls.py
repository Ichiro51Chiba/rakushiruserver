from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import SettinguserViewSet

router = routers.DefaultRouter()

router.register('Settings',SettinguserViewSet)

urlpatterns = [
  path('', include(router.urls)),
]
