# coding: utf-8
from django.contrib.auth.models import AbstractBaseUser, User, PermissionsMixin
from django.db import models


SEX_TYPE = (
    ('M', u'男'),
    ('F', u'女'),
    ('S', u'密码')
)


class User(AbstractBaseUser, PermissionsMixin):
    avatar = models.ImageField(upload_to='account/', max_length=255, verbose_name=u'头像', default='')
    sex = models.CharField(max_length=1, choices=SEX_TYPE, verbose_name=u'性别', default='S')
    declaration = models.CharField(max_length=200, verbose_name=u'个性签名', default='')