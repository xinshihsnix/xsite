# coding: utf-8
from Crypto.Cipher import AES

from django.contrib.auth.models import AbstractBaseUser, User, PermissionsMixin, BaseUserManager
from django.db import models
from ..common.models import BaseModel
from django.utils import timezone
from django.conf import settings


SEX_TYPE = (
    ('M', u'男'),
    ('F', u'女'),
    ('S', u'密码')
)


class UserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError('The given username must be set')

        email = UserManager.normalize_email(email)
        user = self.model(username=username, email=email,
                          is_staff=False, is_active=True, is_superuser=False,
                          last_login=now, raw_password=password, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        u = self.create_user(username, email, password, **extra_fields)
        u.is_staff = True
        u.is_active = True
        u.is_superuser = True
        u.save(using=self._db)
        return u


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=128, verbose_name=u'用户名', unique=True)
    raw_password = models.CharField(max_length=128, verbose_name=u'原始密码')     # 原始密码, 为找回密码
    email = models.EmailField(unique = True, verbose_name='Email', null=True)

    class Meta:
        app_label = 'account'
        db_table = 'account_user'

    USERNAME_FIELD = 'username'    # 作为用户登录认证用的字段，可以usename，或者email等，但必须是唯一的。
    REQUIRED_FIELDS = []  # 使用createsuperuser命令创建超级用户时提示操作者输入的字段

    is_staff = models.BooleanField('staff status', default=False,
        help_text='Designates whether the user can log into this admin site.')

    is_active = models.BooleanField('active', default=True,
        help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()


    def get_short_name(self):
        return self.first_name

    def set_raw_password(self, raw_password):
        d = AES.new(settings.AES_PWD)
        x_content = raw_password + (16 - len(raw_password)%16)*'u'    # 被加密字符串要是16的倍数，所以不够的用u填充
        encrypted_content = d.encrypt(x_content)
        self.raw_password = encrypted_content

    objects = UserManager()


class Profile(BaseModel):
    user = models.OneToOneField(User, verbose_name=u'用户')

    sex = models.CharField(max_length=1, choices=SEX_TYPE, verbose_name=u'性别', default='S')
    declaration = models.CharField(max_length=200, verbose_name=u'个性签名', default='')
    avatar = models.ImageField(upload_to='account/', max_length=255, verbose_name=u'头像', default='')

    class Meta:
        app_label = 'account'
        db_table = 'account_profile'