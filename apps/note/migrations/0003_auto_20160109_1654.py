# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0002_auto_20150925_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='content',
            field=ckeditor.fields.RichTextField(default=b'', verbose_name='\u5185\u5bb9'),
        ),
    ]
