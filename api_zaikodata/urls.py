from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import ZaikoViewSet,UserViewSet

router = routers.DefaultRouter()

router.register('users',UserViewSet)
router.register('Zaikos',ZaikoViewSet)

urlpatterns = [
  path('', include(router.urls)),
]
