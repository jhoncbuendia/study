from rest_framework import serializers
from model.models import Curso, Plan, Alojamiento

class PlanesSerializer(serializers.ModelSerializer):

    class Meta:

        model = Plan
        fields = ('id', 'nombre', 'precio', 'descuento', 'fecha_creacion', 'resume')

class AlojamientoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Alojamiento
        fields = ('id', 'nombre', 'costo')

class CursoListSerializer(serializers.ModelSerializer):

    nivel = serializers.StringRelatedField(read_only = False)
    plan = PlanesSerializer(many = True, read_only = True)
    alojamiento = AlojamientoSerializer(many = True, read_only = True)
    escuela = serializers.StringRelatedField()
    pais = serializers.StringRelatedField()
    actividades = serializers.StringRelatedField(many=True)
    #planes = serializers.StringRelatedField(read_only = False)

    class Meta:
        model = Curso
        fields = ('id', 'img_url', 'nombre', 'actividades', 'categoria', 'nivel', 'plan', 'precio', 'alojamiento', 'pais', 'escuela')
