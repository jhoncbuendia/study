# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0011_curso_puede_trabajar'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='agencia',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
