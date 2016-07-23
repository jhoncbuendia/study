# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0004_auto_20160626_0029'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('resume', models.TextField(max_length=100, blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='reserva',
            name='estudiante',
            field=models.ForeignKey(to='model.Estudiante'),
        ),
        migrations.AddField(
            model_name='curso',
            name='plan',
            field=models.ManyToManyField(to='model.Plan', blank=True),
        ),
    ]
