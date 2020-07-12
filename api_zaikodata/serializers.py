from rest_framework import serializers
from .models import Zaiko
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserSerializers(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id','username','password','email')
    extra_kwargs = {'password':{'write_only':True,'required':True}}
  
  def create(self,validated_data):
    user = User.objects.create_user(**validated_data)
    Token.objects.create(user=user)
    return user
  
class ZaikoSerializers(serializers.ModelSerializer):
  class Meta:
    model = Zaiko
    fields = ('kanzyo','code','price','status','number','name','total_price','remark','pic')
    read_only_fields = ('create_at','updated_at')
    