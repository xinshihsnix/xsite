# coding: utf-8
from django.db import models
from django.utils import timezone
from ..common.models import BaseModel


class AuthBase(BaseModel):
    username = models.CharField(max_length=40, verbose_name=u'姓名', blank=False, null=False)
    password = models.CharField(max_length=128, verbose_name=u'密码', blank=False, null=False)

    def __unicode__(self):
        return self.username

    class Meta:
        abstract = True
        app_label = 'management'
        db_table = 'management_auth_base'

SEX_TYPE = (
    ('M', u'男'),
    ('F', u'女'),
    ('S', u'秘密')
)


class User(AuthBase):
    sex = models.CharField(max_length=2, verbose_name=u'性别', choices=SEX_TYPE, default='S')
    statement = models.CharField(max_length=200, verbose_name=u'个性宣言', default='')

    class Meta:
        app_label = 'management'
        db_table = 'management_user'