# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0002_test'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Test',
        ),
    ]
