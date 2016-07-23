# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0005_auto_20160717_0052'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='descuento',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
