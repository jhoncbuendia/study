# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0016_auto_20160922_0310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='resume',
        ),
    ]
