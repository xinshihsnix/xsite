# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('type', models.CharField(default=b'REL', max_length=3, null=True, blank=True, choices=[(b'LEA', '\u5b66\u4e60'), (b'REL', '\u5a31\u4e50'), (b'COM', '\u516c\u53f8')])),
                ('url', models.CharField(default=b'', max_length=400, verbose_name='url')),
                ('title', models.CharField(default=b'', max_length=400, verbose_name='\u6807\u9898', blank=True)),
                ('description', models.CharField(default=b'', max_length=400, verbose_name='\u63cf\u8ff0', blank=True)),
                ('favicon', models.ImageField(default=b'', upload_to=b'image/navigation/favicon/', verbose_name=b'\xe7\xbd\x91\xe7\xab\x99icon')),
            ],
            options={
                'db_table': 'domain',
            },
        ),
    ]
