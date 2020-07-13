from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator



class Zaiko(models.Model):
  STATUS = (
    ('1','新品'),
    ('2','中古'),
  )
  
  # 勘定コード
  kanzyo = models.IntegerField(validators=  [MinValueValidator(0)])
  # model_no = models.AutoField
  # 規格コード
  code = models.IntegerField(validators=  [MinValueValidator(0)])
  # 評価単価
  price = models.IntegerField(validators=  [MinValueValidator(0)])
  # 新品/中古
  status = models.CharField(max_length=40,choices=STATUS,  default=1)
  # 実残数
  number = models.IntegerField(validators=  [MinValueValidator(0)])
  # 品目名称
  name = models.CharField(max_length=50)
  # 合計金額
  total_price = models.IntegerField(validators=  [MinValueValidator(0)])
  # 備考
  remark = models.CharField(max_length=70)
  # 写真
  pic = models.ImageField(upload_to=None,   height_field=None, width_field=None, max_length=100)
  # 作成日
  create_at = models.DateTimeField(auto_now_add=True)
  # 更新日
  updated_at = models.DateTimeField(null=True,blank=True)
  
  def __str__(self):
      return self.name



  




