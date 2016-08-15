# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0008_curso_img_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reserva',
            old_name='seguro',
            new_name='apellido',
        ),
        migrations.RenameField(
            model_name='reserva',
            old_name='tipo_visa',
            new_name='correo',
        ),
        migrations.RenameField(
            model_name='reserva',
            old_name='traslado_areopuerto',
            new_name='nombre',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='agente',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='curso',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='estudiante',
        ),
        migrations.AddField(
            model_name='reserva',
            name='pasaporte',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='reserva',
            name='plan',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='reserva',
            name='visa',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='reserva',
            name='whatsapp',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='img_url',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='alojamiento',
            field=models.CharField(default=0, max_length=50, blank=True),
            preserve_default=False,
        ),
    ]
