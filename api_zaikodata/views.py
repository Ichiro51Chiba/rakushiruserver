from django.shortcuts import render
from .models import Zaiko
from api_usersite.models import User
from .serializers import ZaikoSerializers,UserSerializers
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import permissions, status #追加
from rest_framework_jwt.authentication import JSONWebTokenAuthentication 
from rest_framework import generics
from rest_framework.decorators import action
from api_user.serializers import CompanySerializers
from api_user.models import Company

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializers
  permission_classes = []
  
  # def list(self, request):
    
  #   company = request.GET.get("company", "")
  #   companies = self.queryset.filter(id = request.user.company.id)
  #   if company != "":
  #     companies = companies.filter(company__contains = company)
    
  #   data = self.serializer_class(companies, many=True).data
  #   return Response(data)
  

  
  # /users/companies/ [GET]
  # /users/companies/ [POST]
  @action(detail=False, methods=['get', 'post'])

  def companies(self, request):
    if request.method == 'GET':
      user = request.user
      companies = user.companies.all()
      data = CompanySerializers(companies, many=True).data
      # return Response(data)
      company = request.GET.get("company", "")
      # companies = self.queryset.filter(id = request.user.company.id)
      if company != "":
        companies = companies.filter(company__contains = company)
      
      data = CompanySerializers(companies, many=True).data
      return Response(data)
    
    if request.method == 'POST':
      user = request.user
      
      company = Company.objects.create(**request.data)
      user.companies.add(company)
      user.save()
      data = CompanySerializers(company).data
      return Response(data)



  
  

class ZaikoViewSet(viewsets.ModelViewSet):
  queryset = Zaiko.objects.all()
  serializer_class = ZaikoSerializers
  # authentication_classes = (TokenAuthentication,)
  # permission_classes = (IsAuthenticated,)
  def list(self, request):
            
    name = request.GET.get("name", "")
    queryset = self.queryset.filter(user=request.user)
    
    if name != "":
      queryset = queryset.filter(name__contains = name)
    # else:
    #   queryset = self.queryset.filter(name__contains = name)
      
    data = self.serializer_class(queryset, many=True).data
    return Response(data)
  
  

 

  
  
