from django.db import models
from datetime import date
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser , AbstractBaseUser

##############
# PROPUESTA ISPC
class CustomUser(AbstractUser):
    email = models.EmailField( max_length=150, default="", unique=True)
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = ['username','password']
    
##############

#  PACIENTE  #
class Paciente(models.Model):
    nombre_paciente = models.CharField(max_length=30 , blank=False)
    apellido_paciente = models.CharField(max_length=30 , blank=False )
    email_paciente = models.EmailField(max_length=100 , blank=False , default="", unique=True)
    contraseña_paciente = models.CharField(max_length=100 , blank=False)
    telefono_paciente = models.CharField(max_length=30 , blank=False)
    fecha_nacimiento = models.DateField(default=date.today , blank=False)
    sexo_paciente = models.CharField(max_length=30 , null=True, blank=True)

    class Meta:
        db_table = 'paciente'
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
    
    def __unicode__(self):
        return self.nombre_paciente    
    #este metodo luego se muestra o sirve, para que cuando vea la tabla de registros glucemia, la relacion se muestre en base a este string
    def __str__(self):
        return 'El paciente es ' + self.nombre_paciente +" "+ self.apellido_paciente
    


class Ficha_medica(models.Model):
    #tipo_diabetes
    TIPO_1 = 'tipo 1'
    TIPO_2 = 'tipo 2'
    GESTACIONAL = 'gestacional'
    choices_tipo_diabetes = (
         (TIPO_1, 'Tipo 1'),
         (TIPO_2, 'Tipo 2'),
         (GESTACIONAL, 'Gestacional'),
     )    
    #terapia_insulina
    TERAPIA_INSULINA_1 = 'tipo 1'
    TERAPIA_INSULINA_2 = 'tipo 2'
    choices_terapia_insulina = (
         (TERAPIA_INSULINA_1, 'Tipo 1'),
         (TERAPIA_INSULINA_2, 'Tipo 2'),
     )
    #terapia_pastillas
    TERAPIA_PASTILLAS_1 = 'tipo 1'
    TERAPIA_PASTILLAS_2 = 'tipo 2'
    choices_terapia_pastillas = (
         (TERAPIA_PASTILLAS_1, 'Tipo 1'),
         (TERAPIA_PASTILLAS_2, 'Tipo 2'),
     )
    #tipo_glucometro
    TIPO_GLUCOMETRO_1 = 'tipo 1'
    TIPO_GLUCOMETRO_2 = 'tipo 2'
    choices_tipo_glucometro = (
         (TIPO_GLUCOMETRO_1, 'Tipo 1'),
         (TIPO_GLUCOMETRO_2, 'Tipo 2'),
     )
    #tipo_sensor
    TIPO_SENSOR_1 = 'tipo 1'
    TIPO_SENSOR_2 = 'tipo 2'
    choices_tipo_sensor = (
         (TIPO_SENSOR_1, 'Tipo 1'),
         (TIPO_SENSOR_2, 'Tipo 2'),
     )
    tipo_diabetes = models.CharField(max_length=35 , choices = choices_tipo_diabetes) 
    terapia_insulina = models.CharField(max_length=30 , choices = choices_terapia_insulina)
    terapia_pastillas = models.CharField(max_length=30 , choices = choices_terapia_pastillas)
    tipo_glucometro = models.CharField(max_length=30 , choices = choices_tipo_glucometro)
    tipo_sensor = models.CharField(max_length=30 , choices = choices_tipo_sensor)
    comorbilidades = models.TextField(default="No")
    objetivo_glucosa = models.DecimalField(max_digits=3, decimal_places=2)
    paciente = models.OneToOneField(Paciente , null=False, blank=True ,  on_delete=models.CASCADE )

    class Meta:
        db_table = 'Ficha_medica'
        verbose_name = 'Ficha medica'
        verbose_name_plural = 'Fichas medicas'    

class Registro_glucemia(models.Model):
    fecha_registro = models.DateTimeField(default=now , blank=False)
    valor_glucemia = models.DecimalField(max_digits=3, decimal_places=2 , blank=False)
    comentario_registro = models.CharField(max_length=200 , null=True, blank=True)
    paciente = models.ForeignKey(Paciente , null=True, blank=True ,  on_delete=models.CASCADE )

    class Meta:
        db_table = 'Registro_glucemia'
        verbose_name = 'Registro glucemia'
        verbose_name_plural = 'Registros glucemia'    
    def __unicode__(self):
        return self.valor_glucemia    
    def __str__(self):
        return "El valor de glucemia es " + self.valor_glucemia + " , medido el " + self.fecha_registro
    
#  PRESTADOR  #
class Prestador(models.Model):
    email_prestador = models.EmailField(max_length=100 , blank=False , default="", unique=True)
    contraseña_prestador = models.CharField(max_length=50 , blank=False)
    sede_prestador = models.CharField(max_length=50 , blank=False)
    telefono_prestador = models.CharField(max_length=50 , blank=False)
    informacion_extra_prestador = models.CharField(max_length=200 , null=True, blank=True)
    nombre_usuario_prestador = models.CharField(max_length=100 ,default="Prestador", blank=False)

    class Meta:
        db_table = 'Prestador'
        verbose_name = 'Prestador'
        verbose_name_plural = 'Prestadores'    
    def __unicode__(self):
        return self.nombre_usuario_prestador    
    def __str__(self):
        return 'El prestador es ' + self.nombre_usuario_prestador
    
#  SERVICIOS  #
class Servicio(models.Model):
    nombre_servicio = models.CharField(max_length=50 , blank=False)
    descripcion_servicio = models.TextField()
    sede_servicio = models.CharField(max_length=50 , blank=False)
    precio_servicio = models.DecimalField(max_digits=8, decimal_places=2)
    comentarios_servicio = models.CharField(max_length=200, null=True , blank= True)
    duracion_servicio = models.CharField(max_length=50 , blank=False)
    prestador = models.ForeignKey(Prestador, null=True , blank= True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Servicio'
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'    
    def __unicode__(self):
        return self.nombre_servicio    
    def __str__(self):
        return 'El servicio es ' + self.nombre_servicio
   
#  PAQUETES  #
class Paquete(models.Model):
    nombre_paquete = models.CharField(max_length=50 ,default="paquete" ,blank=False)
    duracion_total = models.CharField(max_length=50 , blank=False)
    precio_total = models.CharField(max_length=50 , blank=False)
    sede_paquete = models.CharField(max_length=50 , blank=False)
    fecha_seleccionada = models.DateTimeField(default=now , blank=False) # auto_now_add=True
    servicio = models.ManyToManyField(Servicio)
    
    class Meta:
        db_table = 'Paquete'
        verbose_name = 'Paquete'
        verbose_name_plural = 'Paquetes'    
    def __unicode__(self):
        return self.nombre_paquete    
    def __str__(self):
        return 'El paquete es ' + self.nombre_paquete   

#  CARRITO  #
class Carrito(models.Model):
    COMPRADO = 'comprado'
    PAGO_PENDIENTE = 'pago pendiente'
    ELIMINADO = 'eliminado'
    choices_estado_carrito = (
         (COMPRADO, 'Comprado'),
         (PAGO_PENDIENTE, 'Pago pendiente'),
         (ELIMINADO, 'Eliminado'),
     )
    estado_carrito = models.CharField(max_length=30 , choices = choices_estado_carrito)
    paciente = models.ForeignKey(Paciente, null=True , blank= True, on_delete=models.CASCADE)
    servicio = models.ManyToManyField(Paquete)

    class Meta:
        db_table = 'Carrito'
        verbose_name = 'Carrito'
        verbose_name_plural = 'Carritos'    
    def __str__(self):
        return 'De' + self.paciente.email_paciente
    
#  FACTURA  #
class Factura(models.Model):
    EFECTIVO = 'EFECTIVO'
    DEBITO = 'DEBITO'
    CREDITO = 'CREDITO'
    OTROS = 'OTROS'
    choices_medio_pago_factura = (
         (EFECTIVO, 'EFECTIVO'),
         (DEBITO, 'DEBITO'),
         (CREDITO, 'CREDITO'),
         (OTROS, 'OTROS'),
     )
    fecha_completa_factura = models.DateTimeField(default=now , blank=False)
    concepto_factura = models.CharField(max_length=50 , blank=False) # deberia ser un enum?
    valor_factura = models.DecimalField(max_digits=8, decimal_places=2)
    medio_pago_factura = models.CharField(max_length=30 , choices = choices_medio_pago_factura)
    estado_pago = models.CharField(max_length=50 , blank=False) # deberia ser un enum?    
    carrito = models.OneToOneField(Carrito , null=True, blank=True ,  on_delete=models.CASCADE )

    class Meta:
        db_table = 'Factura'
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'    
    def __str__(self):
        return 'De' + self.carrito