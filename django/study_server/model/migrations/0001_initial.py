# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, blank=True)),
                ('resume', models.TextField(max_length=100, blank=True)),
                ('ubicacion', models.CharField(max_length=20, blank=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Agente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=50, blank=True)),
                ('apellidos', models.CharField(max_length=50, blank=True)),
                ('numero_pasaporte', models.CharField(max_length=50, blank=True)),
                ('correo', models.CharField(max_length=50, blank=True)),
                ('numero_identificacion', models.CharField(max_length=50, blank=True)),
                ('numero_telefono', models.CharField(max_length=50, blank=True)),
                ('pais', models.CharField(max_length=50, blank=True)),
                ('ciudad', models.CharField(max_length=50, blank=True)),
                ('direccion', models.CharField(max_length=50, blank=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Alojamiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, blank=True)),
                ('resume', models.TextField(max_length=100, blank=True)),
                ('costo', models.CharField(max_length=10, blank=True)),
                ('ubicacion', models.CharField(max_length=20, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=50, blank=True)),
                ('resume', models.TextField(max_length=100, blank=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, blank=True)),
                ('precio', models.IntegerField()),
                ('numero_horas_total', models.CharField(max_length=10, blank=True)),
                ('numero_horas_semana', models.CharField(max_length=10, blank=True)),
                ('pais', models.CharField(max_length=20, blank=True)),
                ('ciudad', models.CharField(max_length=20, blank=True)),
                ('edad_minima', models.CharField(max_length=10, blank=True)),
                ('nivel_ingles_requerido', models.CharField(max_length=10, blank=True)),
                ('opcion_trabajo', models.CharField(max_length=10, blank=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('actividades', models.ManyToManyField(to='model.Actividad', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Escuela',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, blank=True)),
                ('resume', models.TextField(max_length=100, blank=True)),
                ('ubicacion_maps', models.CharField(max_length=10, blank=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=50, blank=True)),
                ('apellidos', models.CharField(max_length=50, blank=True)),
                ('numero_pasaporte', models.CharField(max_length=50, blank=True)),
                ('correo', models.CharField(max_length=50, blank=True)),
                ('numero_identificacion', models.CharField(max_length=50, blank=True)),
                ('numero_telefono', models.CharField(max_length=50, blank=True)),
                ('pais', models.CharField(max_length=50, blank=True)),
                ('ciudad', models.CharField(max_length=50, blank=True)),
                ('direccion', models.CharField(max_length=50, blank=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado', models.BooleanField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_visa', models.CharField(max_length=50, blank=True)),
                ('seguro', models.CharField(max_length=50, blank=True)),
                ('traslado_areopuerto', models.CharField(max_length=50, blank=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('agente', models.ForeignKey(blank=True, to='model.Agente', null=True)),
                ('alojamiento', models.ForeignKey(blank=True, to='model.Alojamiento', null=True)),
                ('curso', models.ForeignKey(blank=True, to='model.Curso', null=True)),
                ('estudiante', models.ForeignKey(blank=True, to='model.Estudiante', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='pago',
            name='reserva',
            field=models.ForeignKey(blank=True, to='model.Reserva', null=True),
        ),
        migrations.AddField(
            model_name='curso',
            name='escuela',
            field=models.ForeignKey(blank=True, to='model.Escuela', null=True),
        ),
        migrations.AddField(
            model_name='comentario',
            name='curso',
            field=models.ForeignKey(blank=True, to='model.Curso', null=True),
        ),
        migrations.AddField(
            model_name='alojamiento',
            name='curso',
            field=models.ForeignKey(blank=True, to='model.Curso', null=True),
        ),
    ]
