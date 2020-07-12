from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator



class Zaiko(models.Model):
  STATUS = (
    ('1','新品'),
    ('2','中古'),
  )
  

  kanzyo = models.IntegerField(validators=  [MinValueValidator(0)])
  # model_no = models.AutoField
  code = models.IntegerField(validators=  [MinValueValidator(0)])
  price = models.IntegerField(validators=  [MinValueValidator(0)])
  status = models.CharField(max_length=40,choices=STATUS,  default=1)
  number = models.IntegerField(validators=  [MinValueValidator(0)])
  name = models.CharField(max_length=50)
  total_price = models.IntegerField(validators=  [MinValueValidator(0)])
  remark = models.CharField(max_length=70)
  pic = models.ImageField(upload_to=None,   height_field=None, width_field=None, max_length=100)
  create_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(null=True,blank=True)
  
  def __str__(self):
      return self.name



  




