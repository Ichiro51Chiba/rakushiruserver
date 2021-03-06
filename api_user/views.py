from django.shortcuts import render
from .models import Company
from .serializers import CompanySerializers
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from api_usersite.models import User
from rest_framework.response import Response
from rest_framework import generics

class CompanyViewSet(viewsets.ModelViewSet):
  queryset = Company.objects.all()
  serializer_class = CompanySerializers
  # authentication_classes = (TokenAuthentication,)
  # permission_classes = (IsAuthenticated,)
  def list(self, request):
    
    company = request.GET.get("company", "")
    companies = self.queryset.filter(id = request.user.company.id)
    
    if company != "":
      companies = companies.filter(company__contains = company)
    
    data = self.serializer_class(companies, many=True).data
    return Response(data)



  def create(self, request):
    company = Company.objects.create(**request.data)

    print("="*100)
    print('company', company)
    user = request.user
    user.company = company
    user.save()
    
    return Response()
  
