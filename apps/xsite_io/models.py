# coding: utf-8
from django.db import models
from ..common.models import BaseModel
from django.utils import timezone
from django.conf import settings


class WebImage(BaseModel):
    """ web图片 """
    url = models.CharField(max_length=400, verbose_name=u'url', default='')
    image = models.ImageField(upload_to='image/io/', verbose_name='图片', default='', null=True, blank=True)

    class Meta:
        app_label = 'xsite_io'
        db_table = 'xsite_io_webimage'




