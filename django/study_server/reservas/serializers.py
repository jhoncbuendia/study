from rest_framework import serializers
from model.models import Reserva


class ReservaPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reserva
        fields = ( 'estudiante', 'tipo_visa', )

class ReservaListSerializer(serializers.ModelSerializer):
    estudiante = serializers.StringRelatedField( read_only = False )
    class Meta:
        model = Reserva
        fields = ( 'id', 'estudiante', 'tipo_visa', )

class ReservaDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Reserva
        fields = ( 'id', 'estudiante', 'tipo_visa', )
