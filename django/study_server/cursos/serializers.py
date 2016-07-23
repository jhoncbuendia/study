from rest_framework import serializers
from model.models import Curso, Plan

class PlanesSerializer(serializers.ModelSerializer):

    class Meta:

        model = Plan
        fields = ('id', 'nombre', 'precio', 'descuento', 'fecha_creacion', 'resume')

class CursoListSerializer(serializers.ModelSerializer):

    nivel = serializers.StringRelatedField(read_only = False)
    plan = PlanesSerializer(many = True, read_only = True)
    #planes = serializers.StringRelatedField(read_only = False)

    class Meta:
        model = Curso
        fields = ('id', 'nombre', 'categoria', 'nivel', 'plan')
