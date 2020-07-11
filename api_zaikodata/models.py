from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

# 日付
class ZaikoData(models.Model):
  STATUS = (
    ('1','新品'),
    ('2','中古'),
  )
  

  model_kanzyo = models.IntegerField(validators=  [MinValueValidator(0)])
  # model_no = models.AutoField
  model_code = models.IntegerField(validators=  [MinValueValidator(0)])
  model_price = models.IntegerField(validators=  [MinValueValidator(0)])
  model_which = models.CharField(max_length=40,choices=STATUS,  default=1)
  model_number = models.IntegerField(validators=  [MinValueValidator(0)])
  model_name = models.CharField(max_length=50)
  model_total_price = models.IntegerField(validators=  [MinValueValidator(0)])
  model_remark = models.CharField(max_length=70)
  model_pic = models.ImageField(upload_to=None,   height_field=None, width_field=None, max_length=100)
  model_create_at = models.DateTimeField(auto_now_add=True)
  model_updated_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
      return self.model_name
  




