from rest_framework import serializers
from .models import Settinguser

class Settinguserserializer(serializers.ModelSerializer):
  class Meta:
    model = Settinguser
    fields = ('pk', 'set_user','set_no','set_kanzyo','set_name','set_code','set_price','set_which','set_number','set_totalprice','set_remark','set_pic')