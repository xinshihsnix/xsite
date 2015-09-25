# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('name', models.CharField(default='\u5176\u4ed6', max_length=40, verbose_name='\u540d\u79f0')),
                ('is_current', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5f53\u524d\u6240\u5728\u516c\u53f8')),
            ],
            options={
                'db_table': 'reminder_company',
            },
        ),
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('title', models.CharField(default=b'', max_length=80, verbose_name='\u6807\u9898')),
                ('content', models.CharField(default=b'', max_length=500, verbose_name='\u5185\u5bb9')),
                ('company', models.ForeignKey(verbose_name='\u516c\u53f8', to='reminder.Company')),
            ],
            options={
                'db_table': 'reminder_reminder',
            },
        ),
    ]
