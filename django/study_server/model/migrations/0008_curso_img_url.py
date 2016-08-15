# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0007_auto_20160807_0121'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='img_url',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
