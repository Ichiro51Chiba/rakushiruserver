from rest_framework import serializers
from .models import Company
from rest_framework.authtoken.models import Token

class CompanySerializers(serializers.ModelSerializer):
  class Meta:
    model = Company
    fields = ('company','tel_number','postal_code','address','res')
    read_only_fields = ('create_com','updated_com')
    
    
    