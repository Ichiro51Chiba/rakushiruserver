from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    _user_has_perm,
    PermissionsMixin
)
from django.core import validators
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from datetime import datetime
from api_user.models import Company



class UserManager(BaseUserManager):
    """
    ユーザーマネージャー
    """
    def create_user(self, email, password=None, **user_data):
        """
        ユーザーを作成
        """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            **user_data
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, **user_data):
        """
        スーパーユーザーを作成
        """
        return self.create_user(is_superuser=True, is_staff=True, username="Admin", **user_data)

class User(AbstractBaseUser, PermissionsMixin):
    """
    ユーザーモデル
    """
    id            = models.AutoField('ID', primary_key=True)
    username      = models.CharField('ニックネーム', max_length=255, null=False)
    email         = models.EmailField(verbose_name='email address', max_length=255, unique=True, null=False)
    companies     = models.ManyToManyField(Company, null=True, blank=True)
    birthday      = models.DateField('生年月日', null=True, blank=True)
    address       = models.CharField('現住所', max_length=140, null=True, blank=True)
    password      = models.CharField('パスワード', max_length=140, null=False)
    is_tmp_user   = models.BooleanField(default=False)
    is_staff      = models.BooleanField(default=False)
    is_superuser  = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    
    objects = UserManager()
    
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.username
    @property
    def age(self):
        if self.birthday==None:
            return -1
        year = self.birthday.year
        month = self.birthday.month
        day = self.birthday.day
        now = datetime.now()
        #今日の日付
        today_year  = now.year
        today_month = now.month
        today_day   = now.day
        #月が過ぎた場合
        if today_month > month :
            is_passed = True
        #月が同じ場合
        elif today_month == month :
            is_passed = today_day >= day
        else :
            is_passed = False
        if is_passed :
            age = today_year - year
        else :
            age = today_year - year - 1
        return age
# Create your models here.


class Settinguser(models.Model):
    # user設定画面
    
    set_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    #品目No
    set_no     = models.BooleanField(default=True)
    #勘定コード
    set_kanzyo = models.BooleanField(default=True)
    #品目名称
    set_name   = models.BooleanField(default=True)
    #規格コード
    set_code   = models.BooleanField(default=True)
    #評価単価
    set_price  = models.BooleanField(default=True)
    #新品/中古
    set_which  = models.BooleanField(default=True)
    #実残数
    set_number = models.BooleanField(default=True)
    #合計金額
    set_totalprice  = models.BooleanField(default=True)
    #備考
    set_remark = models.BooleanField(default=True)
    #写真
    set_pic    = models.BooleanField(default=True) 
    
    #def __str__(self):
    #  return self.set_user.__str__
    

