from rest_framework import serializers
from model import models

class PlanesSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.Plan
        fields = ('id', 'nombre', 'precio', 'descuento', 'fecha_creacion', 'resume')

class AlojamientoSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.Alojamiento
        fields = ('id', 'nombre', 'costo')

class CursoSerializer(serializers.ModelSerializer):
    actividades = serializers.StringRelatedField(many=True)
    plan = PlanesSerializer(many = True, read_only = True)
    alojamiento = AlojamientoSerializer(many = True, read_only = True)
    escuela = serializers.StringRelatedField()
    pais = serializers.StringRelatedField()
    class Meta:
        model = models.Curso
        fields = ('id', 'img_url', 'nombre','precio', 'plan', 'numero_horas_total', 'numero_horas_semana',  'pais','escuela', 'actividades', 'fecha_creacion', 'alojamiento')
