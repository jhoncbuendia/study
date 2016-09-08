# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0012_reserva_agencia'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='seguro',
            field=models.CharField(max_length=10, blank=True),
        ),
    ]
