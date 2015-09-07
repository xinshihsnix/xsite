# coding: utf-8
from django.db import models
from django.utils import timezone
from ..common.models import BaseModel


DOMAIN_TYPE = (
    ('LEA', u'学习'),
    ('REL', u'娱乐'),
    ('COM', u'公司'),
)


class Domain(BaseModel):
    type = models.CharField(max_length=3, choices=DOMAIN_TYPE, blank=True, null=True, default='REL')
    url = models.CharField(max_length=400, verbose_name=u'url', default='')
    title = models.CharField(max_length=400, verbose_name=u'标题', blank=True, default='')
    description = models.CharField(max_length=400, verbose_name=u'描述', blank=True, default='')
    # icon = models.ImageField(upload_to='img/navigation/', verbose_name='网站icon', default='')

    def __unicode__(self):
        return self.url

    class Meta:
        app_label = 'navigation'
        db_table = 'domain'
