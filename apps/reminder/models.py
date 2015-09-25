# coding: utf-8
from django.db import models
from django.utils import timezone
from ..common.models import BaseModel


class Company(BaseModel):
    name = models.CharField(max_length=40, verbose_name=u'名称', default=u'其他')
    is_current = models.BooleanField(default=False, verbose_name=u'是否当前所在公司')

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'reminder'
        db_table = 'reminder_company'


class Reminder(BaseModel):
    company = models.ForeignKey(Company, verbose_name=u'公司')
    title = models.CharField(max_length=80, verbose_name=u'标题', default='')
    content = models.CharField(max_length=500, verbose_name=u'内容', default='')

    def __unicode__(self):
        return self.title

    class Meta:
        app_label = 'reminder'
        db_table = 'reminder_reminder'