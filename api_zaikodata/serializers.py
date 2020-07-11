from rest_framework import serializers
from .models import ZaikoData
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
  
class ZaikoDataSerializers(serializers.ModelSerializer):
  class Meta:
    model = ZaikoData
    fields = ('model_kanzyo','model_code','model_price','model_which','model_number','model_name','model_total_price','model_remark','model_pic')
    read_only_fields = ('model_create_at','model_updated_at')
    