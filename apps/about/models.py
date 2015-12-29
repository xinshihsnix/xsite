# coding: utf-8
from django.db import models
from django.utils import timezone
from ..common.models import BaseModel
from ..account.models import User


class LeaveMessage(BaseModel):
    message = models.ForeignKey('self', verbose_name=u'回复的留言', null=True)
    user = models.ForeignKey(User, verbose_name=u'留言用户', null=True)
    content =  models.CharField(max_length=500, verbose_name=u'内容')
    ip = models.IPAddressField(verbose_name=u'ip地址')

    class Meta:
        app_label = 'about'
        db_table = 'about_leavemessage'
