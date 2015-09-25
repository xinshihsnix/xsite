# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('title', models.CharField(default=b'', max_length=400, verbose_name='\u6807\u9898')),
                ('content', models.TextField(default=b'', verbose_name='\u5185\u5bb9')),
            ],
            options={
                'db_table': 'story',
            },
        ),
    ]
