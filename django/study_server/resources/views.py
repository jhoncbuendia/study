from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from model import models
import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
import json
from django.db.models import Q
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
# Create your views here.




class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class Mail(APIView):

    def get(self, request):
        response = {}
        response['status'] = 200
        subject, from_email, to = 'Haz recibido una factura (0000) de Study', 'from@example.com', 'jhoncbuendia@gmail.com'
        text_content = ''
        html_content = """
    <!DOCTYPE html>
<html>
  <head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta charset="utf-8">

  </head>
  <body>
    <div style="width: 100%; display: block;">
      <div style="width: 49%; display: inline-block;">
          <p>Logo Study</p>
      </div>
      <div style="width: 49%; display: inline-block;">
          <img src="http://www.readwriteweb.es/wp-content/uploads/2016/06/PayPal-2.jpg" alt="" style="width: 120px;">
      </div>
    </div>
    <div style="width: 100%;">
      <div style="width: 90%; border-radius: 5px; margin: 10px auto 0; padding: 1em; border: 1px solid;">
        <p style="display: block;">
          Hola jhon,
        </p>
        <p style="display: block;">
          Study Limited te ha enviado una factura por $926.00 NZD.
        </p>
        <p style="display: block;">
          <strong>Resumen de la factura</strong>
        </p>

        <div>

          <div style="display: inline-block; width: 95%; margin: 0 auto; padding: 1em; border: 1px solid;">
            <div style="display: block; margin-bottom: 10px;">
              <strong>Enviado a:</strong>   Jhon Buendia
            </div>
            <div style="display: block; margin-bottom: 10px;">
              <strong>Enviado por:</strong> Study Limited
            </div>
            <div style="display: block; margin-bottom: 10px;">
              <strong>Numero de la factura:</strong> 0000
            </div>
            <div style="display: block; margin-bottom: 10px;">
              <strong>Fecha de vencimiento:</strong> Jul 20, 2016
            </div>
            <div style="display: block; margin-bottom: 10px;">
              <strong>Cantidad:</strong>   100 USD
            </div>
          </div>


        </div>
        <div>
          <div style="display: block; margin-top: 10px;">
            Please don't reply to this email. It'll just confuse the computer that sent it and you won't get a response.
          </div>
          <div style="display: block; margin-top: 10px;">
            Copyright  2016 PayPal, Inc. All rights reserved. PayPal is located at 2211 N. First St., San Jose, CA 95131.
          </div>
        </div>
      </div>


    </div>
  </body>
</html>


                        """

        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        subject, from_email, to = 'Haz recibido una factura (0000) de Study', 'from@example.com', 'jhoncbuendia@gmail.com'
        msg.send()

        return JSONResponse(response)

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
