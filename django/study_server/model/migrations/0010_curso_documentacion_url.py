# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0009_auto_20160814_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='documentacion_url',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
