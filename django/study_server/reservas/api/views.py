from rest_framework import generics, viewsets
from reservas.serializers import (
                            ReservaPostSerializer,
                            ReservaListSerializer,
                            ReservaDetailSerializer

                            )
from model.models import Reserva
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class ReservaList(viewsets.ViewSet):
    #permission_classes = (IsAuthenticated,)

    def create(self, request):
        queryset = Reserva.objects.all()

        print request.data
        serializer = ReservaPostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def list(self, request):
        queryset = Reserva.objects.all()
        serializer = ReservaListSerializer(queryset, many = True)
        return Response(serializer.data)


class ReservaDetail(viewsets.ViewSet):
    def update(self, request, pk=None):
        obj = Reserva.objects.get(pk=pk)
        serializer = ReservaDetailSerializer(obj, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
