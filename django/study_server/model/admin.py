from django.contrib import admin
import models

# Register your models here.


class EscuelaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'resume', 'ubicacion_maps', 'fecha_creacion' )
    list_filter = ('fecha_creacion',)
    search_fields = ['nombre', 'fecha_creacion']
    #filter_horizontal = ()

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre','precio','numero_horas_total', 'numero_horas_semana', 'pais','escuela', 'fecha_creacion',  )
    list_filter = ( 'pais', 'ciudad',)
    search_fields = ['nombre', 'numero_horas_total', 'numero_horas_semana', 'pais   ', ]
    filter_horizontal = ('actividades', 'plan')

class AlojamientoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'costo', 'ubicacion', 'curso' )
    list_filter = ('curso',)
    search_fields = ['nombre', 'costo', 'curso',  ]
    #filter_horizontal = ('Actividades',)

class ActividadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion', 'fecha_creacion', )
    list_filter = ('fecha_creacion',)
    search_fields = ['nombre', 'ubicacion',  ]
    #filter_horizontal = ('Actividades',)

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'curso', 'fecha_creacion', )
    list_filter = ('fecha_creacion',)
    search_fields = ['titulo', 'curso',  ]
    #filter_horizontal = ('Actividades',)

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'numero_pasaporte', 'numero_identificacion', 'pais', 'fecha_creacion',)
    list_filter = ('fecha_creacion', 'pais', 'ciudad', )
    search_fields = ['nombres', 'apellidos', 'numero_identificacion', 'numero_pasaporte', 'pais', 'ciudad'  ]
    #filter_horizontal = ('Actividades',)

class AgenteAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'numero_pasaporte', 'numero_identificacion', 'pais', 'fecha_creacion',)
    list_filter = ('fecha_creacion', 'pais', 'ciudad', )
    search_fields = ['nombres', 'apellidos', 'numero_identificacion', 'numero_pasaporte', 'pais', 'ciudad'  ]
    #filter_horizontal = ('Actividades',)

class ReservaAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'curso', 'alojamiento', 'agente', 'fecha_creacion',)
    list_filter = ('fecha_creacion', 'curso', 'agente', )
    search_fields = ['estudiante', 'curso', 'alojamiento', 'agente',  ]
    #filter_horizontal = ('Actividades',)

class PagoAdmin(admin.ModelAdmin):
    list_display = ('reserva', 'estado', 'fecha_creacion',)
    list_filter = ('fecha_creacion', 'estado', )
    search_fields = ['reserva', 'estado' ]
    #filter_horizontal = ('Actividades',)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',  'fecha_creacion',)
    list_filter = ('fecha_creacion',  )
    search_fields = ['nombre',  ]
    #filter_horizontal = ('Actividades',)

class NivelAdmin(admin.ModelAdmin):
    list_display = ('nombre',  'fecha_creacion',)
    list_filter = ('fecha_creacion',  )
    search_fields = ['nombre',  ]
    #filter_horizontal = ('Actividades',)

class PaisAdmin(admin.ModelAdmin):
    list_display = ('nombre',  'fecha_creacion',)
    list_filter = ('fecha_creacion',  )
    search_fields = ['nombre',  ]
    #filter_horizontal = ('Actividades',)

class PlanAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'fecha_creacion', 'resume')
    list_filter = ('fecha_creacion',  )
    search_fields = ['nombre', 'precio' ]
    #filter_horizontal = ('Actividades',)

admin.site.register(models.Escuela, EscuelaAdmin)
admin.site.register(models.Curso, CursoAdmin)
admin.site.register(models.Alojamiento, AlojamientoAdmin)
admin.site.register(models.Actividad, ActividadAdmin)
admin.site.register(models.Comentario, ComentarioAdmin)
admin.site.register(models.Estudiante, EstudianteAdmin)
admin.site.register(models.Reserva, ReservaAdmin)
admin.site.register(models.Agente, AgenteAdmin)
admin.site.register(models.Pago, PagoAdmin)
admin.site.register(models.Categoria, CategoriaAdmin)
admin.site.register(models.Nivel, NivelAdmin)
admin.site.register(models.Pais, PaisAdmin)
admin.site.register(models.Plan, PlanAdmin)
