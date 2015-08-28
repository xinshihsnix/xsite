# coding: utf-8
from django.db import models
from django.utils import timezone
from django.conf import settings


class BaseModel(models.Model):
    create_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now, auto_now_add=True)

    class Meta:
        abstract = True

    @property
    def crate_time_str(self):
        """
        datetime.datetime(xxx) -> '2015-11-11 11:11:11'
        """
        return self.create_time.strftime(settings.DATETIME_FORMAT)