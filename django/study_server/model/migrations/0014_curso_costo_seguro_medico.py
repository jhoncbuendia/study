# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0013_reserva_seguro'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='costo_seguro_medico',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]
