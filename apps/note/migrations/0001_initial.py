# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('type', models.CharField(default=b'LON', max_length=3, null=True, blank=True, choices=[(b'LON', '\u4e00\u8a00\u96be\u5c3d'), (b'SHO', '\u8a00\u7b80\u610f\u8d45')])),
                ('title', models.CharField(default=b'', max_length=400, verbose_name='\u6807\u9898')),
                ('content', models.TextField(default=b'', verbose_name='\u5185\u5bb9')),
            ],
            options={
                'db_table': 'note',
            },
        ),
        migrations.CreateModel(
            name='NoteCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('name', models.CharField(default='\u5176\u4ed6', max_length=40, verbose_name='\u540d\u79f0')),
            ],
            options={
                'db_table': 'note_category',
            },
        ),
        migrations.AddField(
            model_name='note',
            name='category',
            field=models.ForeignKey(verbose_name='\u76ee\u5f55', to='note.NoteCategory'),
        ),
    ]
