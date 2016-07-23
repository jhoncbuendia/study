# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='categoria',
            field=models.ForeignKey(blank=True, to='model.Categoria', null=True),
        ),
    ]
