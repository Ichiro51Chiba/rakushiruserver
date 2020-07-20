from django.db import models
from django.core.validators import RegexValidator

class Company(models.Model):
  # 会社名
  company = models.CharField(max_length=50)
  # 電話番号
  tel_number_regex = RegexValidator(regex=r'^[0-9]+$', message = ("Tel Number must be entered in the format: '09012345678'. Up to 15 digits allowed."))
  tel_number = models.CharField(validators=[tel_number_regex], max_length=15, verbose_name='電話番号')
  # 郵便番号
  postal_code_regex = RegexValidator(regex=r'^[0-9]+$', message = ("Postal Code must be entered in the format: '1234567'. Up to 7 digits allowed."))
  postal_code = models.CharField(validators=[postal_code_regex], max_length=7, verbose_name='郵便番号') 
  # 住所
  address = models.CharField(max_length=50,null=True)
  # 備考
  res = models.CharField(max_length=50)
    # 作成日
  create_com = models.DateTimeField(auto_now_add=True)
  # 更新日
  updated_com = models.DateTimeField(null=True,blank=True)
  
  def __str__(self):
      return self.company
  
  
