from rest_framework import generics, viewsets
from cursos.serializers import CursoListSerializer
from model.models import Curso
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from django.http import HttpResponse
from pymongo import MongoClient
import json
from bson.json_util import dumps
from django.views.generic.base import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class CursoView(View):

    client = MongoClient('localhost', 27017)
    db = client.book2study

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(CursoView, self).dispatch(request, *args, **kwargs)

    def get(self, request):

        cursos = self.db.cursos
        cursos = dumps(cursos.find(), ensure_ascii=False)
        return HttpResponse(cursos, content_type='application/json')


    def put(self, request):
        #print request.body
        try:
            body = json.loads(request.body)
            self.db.cursos.find_one_and_update({'_id': body['_id']}, { "$set": json.loads(request.body) })
            return HttpResponse(json.dumps({'response': '200'}), content_type='application/json')
        except:
            return HttpResponse(json.dumps({'response': '400'}), content_type='application/json')



class CursoList(viewsets.ViewSet):
    #permission_classes = (IsAuthenticated,)

    def list(self, request):
        popular = request.GET.get('popular', False)
        if(popular):
            queryset = Curso.objects.all().order_by('-id')[:6]
            serializer = CursoListSerializer(queryset, many = True)
            return Response(serializer.data)
        else:
            query = request.GET.get('q', False)
            if (query):
                #todo add precio filter
                queryset = Curso.objects.filter(Q( categoria__nombre__contains = request.GET.get('categoria', False) ) |
                                                 Q( nivel__nombre__contains = request.GET.get('nivel', False) ) |
                                                 Q( pais__nombre__contains = request.GET.get('pais', False) ) )
                                                 #| Q( precio__lte = request.GET.get('precio', False) ))
            else:
                queryset = Curso.objects.all()

            serializer = CursoListSerializer(queryset, many = True)
            return Response(serializer.data)
