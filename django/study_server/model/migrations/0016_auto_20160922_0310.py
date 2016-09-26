# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0015_auto_20160920_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='resume_es',
            field=models.TextField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='plan',
            name='resume_ing',
            field=models.TextField(max_length=100, blank=True),
        ),
    ]
