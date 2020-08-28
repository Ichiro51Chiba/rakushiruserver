from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from .models import Settinguser
from .serializers import Settinguserserializer
from rest_framework import viewsets
from api_user.models import Company
from api_user.serializers import CompanySerializers


# Create your views here.
# class UserViewSet(viewset.ModelViewSet):
  
  
#   def create(self, request):
#     print(request.data)
#     company_id = request.data.get("company_id", None)
#     email = request.data.get("email", None)
    
    
#     user_manager = UserManager()
#     user_manager.create_user(email, password, compnay=company)

  
  

class SettinguserViewSet(viewsets.ModelViewSet):
  queryset = Settinguser.objects.all()
  serializer_class = Settinguserserializer
  
  def list(self, request):
    setting = self.queryset.filter(set_user=request.user).first()
    
    if setting is None:
      return HttpResponse("NOT FOUND", 404)
    
    data = self.serializer_class(setting).data
    return Response(data)
  

