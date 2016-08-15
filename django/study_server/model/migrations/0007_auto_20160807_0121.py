# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0006_plan_descuento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alojamiento',
            name='curso',
        ),
        migrations.AddField(
            model_name='curso',
            name='alojamiento',
            field=models.ManyToManyField(to='model.Alojamiento', blank=True),
        ),
    ]
