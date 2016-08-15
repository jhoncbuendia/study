from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.nombre

class Nivel(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.nombre

class Pais(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.nombre


class Agente(models.Model):
    nombres = models.CharField(max_length=50, blank = True )
    apellidos = models.CharField(max_length=50, blank = True )
    numero_pasaporte = models.CharField(max_length=50, blank = True )
    correo = models.CharField(max_length=50, blank = True )
    numero_identificacion = models.CharField(max_length=50, blank = True )
    numero_telefono = models.CharField(max_length=50, blank = True )
    pais = models.CharField(max_length=50, blank = True )
    ciudad = models.CharField(max_length=50, blank = True )
    direccion = models.CharField(max_length=50, blank = True )
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.nombres

class Estudiante(models.Model):
    nombres = models.CharField(max_length=50, blank = True )
    apellidos = models.CharField(max_length=50, blank = True )
    numero_pasaporte = models.CharField(max_length=50, blank = True )
    correo = models.CharField(max_length=50, blank = True )
    numero_identificacion = models.CharField(max_length=50, blank = True )
    numero_telefono = models.CharField(max_length=50, blank = True )
    pais = models.CharField(max_length=50, blank = True )
    ciudad = models.CharField(max_length=50, blank = True )
    direccion = models.CharField(max_length=50, blank = True )
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.nombres

class Escuela(models.Model):
    nombre = models.CharField(max_length=50, blank = True )
    resume = models.TextField(max_length=100, blank = True )
    ubicacion_maps = models.CharField(max_length=10, blank = True )
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.nombre

class Curso(models.Model):

    nombre = models.CharField(max_length=50, blank = True )
    img_url = models.CharField(max_length=200, blank = True )
    categoria =  models.ForeignKey('Categoria', null = True,  blank = True)
    nivel =  models.ForeignKey('Nivel', null = True,  blank = True)
    pais =  models.ForeignKey('Pais', null = True,  blank = True)
    precio = models.IntegerField()
    numero_horas_total = models.CharField(max_length=10, blank = True )
    numero_horas_semana = models.CharField(max_length=10, blank = True )
    ciudad = models.CharField(max_length=20, blank = True)
    edad_minima = models.CharField(max_length=10, blank = True )
    nivel_ingles_requerido = models.CharField(max_length=10, blank = True )
    opcion_trabajo = models.CharField(max_length=10, blank = True )
    escuela =  models.ForeignKey('Escuela', null = True,  blank = True)
    actividades = models.ManyToManyField("Actividad", blank = True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    plan = models.ManyToManyField("Plan", blank = True)
    alojamiento = models.ManyToManyField("Alojamiento", blank = True)

    def __unicode__(self):
        return self.nombre

class Plan(models.Model):
    nombre = models.CharField( max_length = 50)
    precio = models.IntegerField()
    descuento = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    resume = models.TextField(max_length=100, blank = True )

    def __unicode__(self):
        return self.nombre


class Alojamiento(models.Model):
    nombre = models.CharField(max_length=50, blank = True )
    resume = models.TextField(max_length=100, blank = True )
    costo = models.CharField(max_length=10, blank = True )
    ubicacion = models.CharField(max_length=20, blank = True )


    def __unicode__(self):
        return self.nombre

class Actividad(models.Model):
    nombre = models.CharField(max_length=50, blank = True )
    resume = models.TextField(max_length=100, blank = True )
    ubicacion = models.CharField(max_length=20, blank = True )
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.nombre

class Comentario(models.Model):
    titulo = models.CharField(max_length=50, blank = True )
    resume = models.TextField(max_length=100, blank = True )
    curso =  models.ForeignKey('Curso', null = True,  blank = True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.titulo

class Reserva(models.Model):
    #estudiante =  models.ForeignKey('Estudiante')
    #curso =  models.ForeignKey('Curso', null = True,  blank = True)
    #alojamiento =  models.ForeignKey('Alojamiento', null = True,  blank = True)
    #agente =  models.ForeignKey('Agente', null = True,  blank = True)
    #tipo_visa = models.CharField(max_length=50, blank = True )
    #seguro = models.CharField(max_length=50, blank = True)
    #traslado_areopuerto = models.CharField(max_length=50, blank = True )
    nombre = models.CharField(max_length=50, blank = True )
    apellido = models.CharField(max_length=50, blank = True )
    correo = models.CharField(max_length=50, blank = True )
    pasaporte = models.CharField(max_length=50, blank = True )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    whatsapp = models.CharField(max_length=50, blank = True )
    plan = models.CharField(max_length=50, blank = True )
    alojamiento = models.CharField(max_length=50, blank = True )
    visa = models.CharField(max_length=50, blank = True )

    def __unicode__(self):
        return self.nombre

class Pago(models.Model):
    reserva =  models.ForeignKey('Reserva', null = True,  blank = True)
    estado =  models.BooleanField(blank = True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.reserva)
