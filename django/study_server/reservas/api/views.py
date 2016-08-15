from rest_framework import generics, viewsets
from model.models import Reserva
import json
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from reservas.serializers import (
                            ReservaPostSerializer,
                            ReservaListSerializer,
                            ReservaDetailSerializer

                            )
from model.models import Reserva
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


def sendMail(email):
    response = {}
    response['status'] = 200
    subject, from_email, to = 'Haz recibido una factura (0000) de Study', 'info@study.com', email
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
    try:
        msg.send()
    except:
        pass


class ReservaList(viewsets.ViewSet):
    #permission_classes = (IsAuthenticated,)

    def create(self, request):
        queryset = Reserva.objects.all()
        data = json.loads(request.data['data'])
        #print data
        print data['informacion_personal']['nombre']

        reserva = Reserva()
        reserva.nombre = data['informacion_personal']['nombre']
        reserva.apellido = data['informacion_personal']['apellido']
        reserva.correo = data['informacion_personal']['correo']
        reserva.pasaporte = data['informacion_personal']['pasaporte']
        reserva.whatsapp = data['informacion_personal']['whatsapp']
        reserva.plan = data['plan']['nombre']
        reserva.alojamiento = data['alojamiento']
        reserva.visa = data['visa']
        reserva.save()
        sendMail(data['informacion_personal']['correo'])
        return Response({})

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
