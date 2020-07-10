from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import ZaikoDataViewSet,UserViewSet

router = routers.DefaultRouter()

router.register('users',UserViewSet)
router.register('zaikodatas',ZaikoDataViewSet)

urlpatterns = [
  path('', include(router.urls)),
]
