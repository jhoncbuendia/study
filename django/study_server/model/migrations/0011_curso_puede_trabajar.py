# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0010_curso_documentacion_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='puede_trabajar',
            field=models.BooleanField(default=False),
        ),
    ]
