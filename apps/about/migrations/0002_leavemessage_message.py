# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='leavemessage',
            name='message',
            field=models.ForeignKey(verbose_name='\u56de\u590d\u7684\u7559\u8a00', to='about.LeaveMessage', null=True),
        ),
    ]
