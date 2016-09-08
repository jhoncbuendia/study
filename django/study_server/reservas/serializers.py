from rest_framework import serializers
from model.models import Reserva


class ReservaPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ( 'nombre', )

class ReservaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ( 'nombre', )

class ReservaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ( 'nombre', )
