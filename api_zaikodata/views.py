from django.shortcuts import render
from .models import ZaikoData
from django.contrib.auth.models import User
from .serializers import ZaikoDataSerializers,UserSerializers
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializers

class ZaikoDataViewSet(viewsets.ModelViewSet):
  queryset = ZaikoData.objects.all()
  serializer_class = ZaikoDataSerializers