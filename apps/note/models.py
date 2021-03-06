# coding: utf-8
from django.db import models
from django.utils import timezone
from ..common.models import BaseModel
from ckeditor.fields import RichTextField


class NoteCategory(BaseModel):
    name = models.CharField(max_length=40, verbose_name=u'名称', default=u'其他')

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'note'
        db_table = 'note_category'

NOTE_TYPE = (
    ('LON', u'一言难尽'),
    ('SHO', u'言简意赅'),
)


class Note(BaseModel):
    type = models.CharField(max_length=3, choices=NOTE_TYPE, blank=True, null=True, default='LON')
    category = models.ForeignKey(NoteCategory, verbose_name=u'目录')
    title = models.CharField(max_length=400, verbose_name=u'标题', default='')
    # content = models.TextField(verbose_name=u'内容', default='')
    content = RichTextField(verbose_name=u'内容', default='')

    def __unicode__(self):
        return self.title

    class Meta:
        app_label = 'note'
        db_table = 'note_note'

