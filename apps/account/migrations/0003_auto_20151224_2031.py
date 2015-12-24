# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='sex',
            field=models.CharField(default=b'S', max_length=1, verbose_name='\u6027\u522b', choices=[(b'M', '\u7537'), (b'F', '\u5973'), (b'S', '\u5bc6\u79d8')]),
        ),
    ]
