from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from model import models
import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
import json
from django.db.models import Q
# Create your views here.




class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)



class IndexList(APIView):
    def get(self, request):
        response = []

        categorias = models.Categoria.objects.all().values('nombre')
        niveles = models.Nivel.objects.all().values('nombre')
        paises = models.Pais.objects.all().values('nombre')
        cursos_populares = models.Curso.objects.all().order_by('-id')[:6]
        popular_countries = models.Pais.objects.all().order_by('-id')[:6].values('nombre')

        index = {}
        index['filter_content']= {}
        index['filter_content']['categories'] = categorias
        index['filter_content']['levels'] = niveles
        index['filter_content']['countries'] = paises



        index['popular_courses']= serializers.CursoSerializer(cursos_populares, many=True).data
        index['popular_countries']= popular_countries


        response.append(index)
        return JSONResponse(response)


class CursoList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):

        cursos = models.Curso.objects.all()
        if(cursos):
            serializer = serializers.CursoSerializer(cursos, many=True)
            return JSONResponse(serializer.data)
        else:
            response = {}
            response['data'] = 'course not found'
            return JSONResponse(response)

class CursoDetail(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, id):

        curso = models.Curso.objects.filter(id = id)
        if(curso):
            serializer = serializers.CursoSerializer(curso[0])
            #print json.dumps(curso[0])
            return JSONResponse(serializer.data)
        else:
            response = {}
            response['data'] = 'course not found'
            return JSONResponse(response)

class CursoFilter(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None, categoria = False, nivel = False, pais = False, precio_max = False ):

        cursos = models.Curso.objects.filter(Q( categoria__nombre__contains = categoria ) |
                                             Q( nivel__nombre__contains = nivel ) |
                                             Q( pais__nombre__contains = pais ) |
                                             Q( precio__lte = precio_max ))

        if(cursos):
            serializer = serializers.CursoSerializer(cursos, many=True)
            return JSONResponse(serializer.data)
        else:
            response = {}
            response['msg'] = 'course not found'
            response['code'] = '404'
            return JSONResponse(response)
