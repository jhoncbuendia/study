from rest_framework import generics, viewsets
from cursos.serializers import CursoListSerializer
from model.models import Curso
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

class CursoList(viewsets.ViewSet):
    #permission_classes = (IsAuthenticated,)

    def list(self, request):
        query = request.GET.get('q', False)

        if (query):
            queryset = Curso.objects.filter(Q( categoria__nombre__contains = request.GET.get('categoria', False) ) |
                                                 Q( nivel__nombre__contains = request.GET.get('nivel', False) ) |
                                                 Q( pais__nombre__contains = request.GET.get('pais', False) ) |
                                                 Q( precio__lte = request.GET.get('precio', False) ))

        else:
            queryset = Curso.objects.all()

        serializer = CursoListSerializer(queryset, many = True)
        return Response(serializer.data)

    
