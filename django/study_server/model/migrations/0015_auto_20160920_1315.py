# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0014_curso_costo_seguro_medico'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='precio',
            new_name='precio_cop',
        ),
        migrations.AddField(
            model_name='curso',
            name='precio_usd',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
