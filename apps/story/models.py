# coding: utf-8
from django.db import models
from django.utils import timezone
from ..common.models import BaseModel


class Story(BaseModel):
    title = models.CharField(max_length=400, verbose_name=u'标题', default='')
    content = models.TextField(verbose_name=u'内容', default='')

    def __unicode__(self):
        return self.title

    class Meta:
        app_label = 'story'
        db_table = 'story'