from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.core.validators import RegexValidator



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
  pic = models.ImageField(upload_to=None,   height_field=None, width_field=None, max_length=100,null=True)
  # 作成日
  create_at = models.DateTimeField(auto_now_add=True)
  # 更新日
  updated_at = models.DateTimeField(null=True,blank=True)
  
  def __str__(self):
      return self.name




# class Company(models.Model):
#   # 会社名
#   company = models.CharField(max_length=50)
#   # 電話番号
#   tel_number_regex = RegexValidator(regex=r'^[0-9]+$', message = ("Tel Number must be entered in the format: '09012345678'. Up to 15 digits allowed."))
#   tel_number = models.CharField(validators=[tel_number_regex], max_length=15, verbose_name='電話番号')
#   # 郵便番号
#   postal_code_regex = RegexValidator(regex=r'^[0-9]+$', message = ("Postal Code must be entered in the format: '1234567'. Up to 7 digits allowed."))
#   postal_code = models.CharField(validators=[postal_code_regex], max_length=7, verbose_name='郵便番号') 
#   # 備考
#   res = models.CharField(max_length=50)
#     # 作成日
#   create_com = models.DateTimeField(auto_now_add=True)
#   # 更新日
#   updated_com = models.DateTimeField(null=True,blank=True)
  
#   def __str__(self):
#       return self.company
  
  




  




