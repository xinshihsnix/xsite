# coding: utf-8
from django.db import models
from django.utils import timezone
from ..common.models import BaseModel


class Domain(BaseModel):
    url = models.CharField(max_length=400, verbose_name=u'url', default='')
    title = models.CharField(max_length=400, verbose_name=u'标题', default='')
    description = models.CharField(max_length=400, verbose_name=u'描述', default='')

    def __unicode__(self):
        return self.url

    class Meta:
        app_label = 'navigation'
        db_table = 'domain'
