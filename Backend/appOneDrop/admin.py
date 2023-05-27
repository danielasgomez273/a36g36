from django.contrib import admin
from .models import Paciente
from .models import Ficha_medica
from .models import Registro_glucemia
from .models import Prestador
from .models import Servicio
from .models import Paquete
from .models import Carrito
from .models import Factura

# Register your models here.
#     admin.site.register(Paciente)
#     admin.site.register(Ficha_medica)
#     admin.site.register(Registro_glucemia)
#     admin.site.register(Prestador)
#     admin.site.register(Servicio)
#     admin.site.register(Paquete)
#     admin.site.register(Carrito)


#esta clase perimite mostrar la tabla de pacientes con esta estructura y estos campos, es opcional
class PacienteAdmin(admin.ModelAdmin):
    list_display = ( "nombre_paciente" , "apellido_paciente" , "email_paciente" , "telefono_paciente" , "fecha_nacimiento" ,"sexo_paciente")

class Ficha_medicaAdmin(admin.ModelAdmin):
    list_display = ( "tipo_diabetes" , "terapia_insulina" , "terapia_pastillas" , "tipo_glucometro" , "tipo_sensor" , "comorbilidades" , "objetivo_glucosa" , "paciente"  )

class Registro_glucemiaAdmin(admin.ModelAdmin):
    list_display = ( "fecha_registro" , "valor_glucemia" , "comentario_registro" , "paciente" )

class PrestadorAdmin(admin.ModelAdmin):
    list_display = ( "email_prestador" , "nombre_usuario_prestador" , "sede_prestador" , "telefono_prestador" , "informacion_extra_prestador")

class ServicioAdmin(admin.ModelAdmin):
    list_display = ( "nombre_servicio" , "descripcion_servicio" , "sede_servicio" , "precio_servicio" , "comentarios_servicio" , "duracion_servicio" , "prestador")

class PaqueteAdmin(admin.ModelAdmin):
    list_display = ( "nombre_paquete" , "duracion_total" , "precio_total" , "sede_paquete" , "fecha_seleccionada")

class CarritoAdmin(admin.ModelAdmin):
    list_display = ( "estado_carrito" , "paciente")

class FacturaAdmin(admin.ModelAdmin):
    list_display = ( "fecha_completa_factura" , "concepto_factura" , "valor_factura" , "medio_pago_factura", "estado_pago" , "carrito")


admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Ficha_medica,Ficha_medicaAdmin)
admin.site.register(Registro_glucemia, Registro_glucemiaAdmin)
admin.site.register(Prestador,PrestadorAdmin)
admin.site.register(Servicio,ServicioAdmin)
admin.site.register(Paquete,PaqueteAdmin)
admin.site.register(Carrito,CarritoAdmin)
admin.site.register(Factura,FacturaAdmin)