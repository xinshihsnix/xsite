# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0003_auto_20151213_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='favicon',
            field=models.ImageField(default=b'', upload_to=b'image/navigation/', null=True, verbose_name=b'\xe7\xbd\x91\xe7\xab\x99icon', blank=True),
        ),
    ]
