from django.shortcuts import render
from .models import Zaiko
from django.contrib.auth.models import User
from .serializers import ZaikoSerializers,UserSerializers
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializers
  # authentication_classes = (TokenAuthentication,)
  # permission_classes = (IsAuthenticated,)
  

class ZaikoViewSet(viewsets.ModelViewSet):
  # permission_classes = (IsAuthenticated,)
  queryset = Zaiko.objects.all()
  serializer_class = ZaikoSerializers
  # authentication_classes = (TokenAuthentication,)
  
  
