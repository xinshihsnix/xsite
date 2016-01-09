# coding: utf-8
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.shortcuts import get_object_or_404, _get_queryset, Http404

class BaseModel(models.Model):
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        abstract = True

    @property
    def crate_time_str(self):
        """
        datetime.datetime(xxx) -> '2015-11-11 11:11:11'
        """
        return self.create_time.strftime(settings.DATETIME_FORMAT)

    @classmethod
    def get_by_str_id(cls, str):
        queryset = _get_queryset(cls)
        try:
            id = int(str)
        except cls.model.DoesNotExist:
            raise Http404('No %s matches the given query.' % queryset.model._meta.object_name)

        return get_object_or_404(cls, pk=id)


