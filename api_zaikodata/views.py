from django.shortcuts import render
from .models import ZaikoData
from django.contrib.auth.models import User
from .serializers import ZaikoDataSerializers,UserSerializers
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializers

class ZaikoDataViewSet(viewsets.ModelViewSet):
  queryset = ZaikoData.objects.all()
  serializer_class = ZaikoDataSerializers
  authentication_classes = (TokenAuthentication,)
  permission_classes = (IsAuthenticated,)
  
  # view閲覧制限追加