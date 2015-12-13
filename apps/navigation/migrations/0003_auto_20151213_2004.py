# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0002_auto_20150925_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='favicon',
            field=models.ImageField(default=b'', upload_to=b'image/navigation/favicon/', null=True, verbose_name=b'\xe7\xbd\x91\xe7\xab\x99icon', blank=True),
        ),
    ]
