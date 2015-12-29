# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('content', models.CharField(max_length=500, verbose_name='\u5185\u5bb9')),
                ('ip', models.IPAddressField(verbose_name='ip\u5730\u5740')),
                ('user', models.ForeignKey(verbose_name='\u7559\u8a00\u7528\u6237', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'db_table': 'about_leavemessage',
            },
        ),
    ]
