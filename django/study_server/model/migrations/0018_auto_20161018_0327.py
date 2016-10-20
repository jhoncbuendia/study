# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0017_remove_plan_resume'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='precio_cop',
            new_name='precio_colombia',
        ),
        migrations.RenameField(
            model_name='curso',
            old_name='precio_usd',
            new_name='precio_newzealand',
        ),
    ]
