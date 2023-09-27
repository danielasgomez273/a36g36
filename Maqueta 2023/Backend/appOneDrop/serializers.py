from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from .models import Paciente , Ficha_medica , Registro_glucemia , Prestador , Servicio , Carrito , Factura #refiere a que creare el serializer en base a un modelo existente   


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True)
    username = serializers.CharField(
        required=True)
    password = serializers.CharField(
        min_length=8 , write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password')
    
    def validate_password(self, value):
        return make_password(value)
    

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente    
        #campos de la tabla que van a ser consultados
        fields = ('id', 'nombre_paciente', 'apellido_paciente', 'telefono_paciente', 'fecha_nacimiento', 'sexo_paciente', 'usuario') #'email_paciente', 'contraseña_paciente', 
        # fiels = '__all__'
        
        #read_only_fields = ('email_paciente',) # indica que estos campos no pueden ser modificados, solo lectura, el problema es que en los posteos no deja cargar el atributo en el formulario...

class FichaMedicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ficha_medica    
        fields = ('id', 'tipo_diabetes', 'terapia_insulina', 'terapia_pastillas', 'tipo_glucometro', 'tipo_sensor', 'objetivo_glucosa','comorbilidades' , 'paciente')

class RegistroGlucemiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registro_glucemia    
        fields = ('id', 'fecha_registro', 'valor_glucemia', 'comentario_registro', 'paciente')

class PrestadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestador    
        fields = ('id',  'sede_prestador', 'telefono_prestador', 'informacion_extra_prestador', 'nombre_usuario_prestador', 'usuario_id')
        #'email_prestador', 'contraseña_prestador',

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio    
        fields = ('id', 'nombre_servicio', 'descripcion_servicio', 'precio_servicio', 'comentarios_servicio', 'prestador')

# class PaqueteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Paquete    
#         fields = ('id', 'nombre_paquete', 'duracion_total', 'precio_total', 'sede_paquete', 'fecha_seleccionada', 'servicio')

class CarritoSerializer(serializers.ModelSerializer):
    # servicio = serializers.PrimaryKeyRelatedField (many=True, queryset = Servicio.objects.all())
    servicio = ServicioSerializer(many=True, read_only=True) 
    class Meta:
        model = Carrito    
        fields = ('id', 'estado_carrito', 'paciente', 'servicio') # __all__

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura    
        fields = ('id', 'fecha_completa_factura', 'concepto_factura', 'valor_factura', 'medio_pago_factura', 'estado_pago', 'carrito')

