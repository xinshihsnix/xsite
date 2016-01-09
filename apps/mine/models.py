# coding: utf-8
from django.db import models
from ..common.models import BaseModel
from django.utils import timezone
from django.conf import settings


class Log(BaseModel):
    """ 我的日志 """
    is_private = models.BooleanField(default=True, verbose_name=u'隐私否?')
    content = models.CharField(max_length=10000, verbose_name=u'内容')

    class Meta:
        app_label = 'mine'
        db_table = 'mine_log'




