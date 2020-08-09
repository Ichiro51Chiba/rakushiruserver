from rest_framework import serializers
from .models import Zaiko
from api_usersite.models import User
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
    fields = ('pk','kanzyo','code','price','status','number','name','total_price','remark','pic')
    read_only_fields = ('create_at','updated_at')
    
    

# class UserSerializers(serializers.ModelSerializer):
  
#     token = serializers.SerializerMethodField()
#     password = serializers.CharField(write_only=True)

#     def get_token(self, obj):
#         jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
#         jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

#         payload = jwt_payload_handler(obj)
#         token = jwt_encode_handler(payload)
#         return token

#     def create(self, validated_data):
#         password = validated_data.pop('password', None)
#         instance = self.Meta.model(**validated_data)
#         if password is not None:
#             instance.set_password(password)
#         instance.save()
#         return instance

#     class Meta:
#         model = User
#         fields = ('token', 'username', 'password','email')

  

      