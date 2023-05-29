from .models import Paciente , Ficha_medica , Registro_glucemia , Prestador , Servicio , Paquete , Carrito , Factura
from rest_framework import viewsets , permissions
from .serializers import PacienteSerializer , FichaMedicaSerializer , RegistroGlucemiaSerializer ,PrestadorSerializer , ServicioSerializer , PaqueteSerializer , CarritoSerializer , FacturaSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    #consultas que se podran hacer
    # ej consultando el modelo paciente, consultaremos todos los pacientes
    #este metodo consulta todos los datos de una tabla
    queryset = Paciente.objects.all()
    #permission necesarios para ver, solo permitido para.. en este caso permitido a cualquiera (aca iria authentication)
    permission_classes = [permissions.IsAuthenticated]
    #indica el serializer que usara para convertir los datos
    serializer_class = PacienteSerializer 

class FichaMedicaViewSet(viewsets.ModelViewSet):
    queryset = Ficha_medica.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = FichaMedicaSerializer 

class RegistroGlucemiaViewSet(viewsets.ModelViewSet):
    queryset = Registro_glucemia.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegistroGlucemiaSerializer 

class PrestadorViewSet(viewsets.ModelViewSet):
    queryset = Prestador.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PrestadorSerializer 

class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ServicioSerializer 

class PaqueteViewSet(viewsets.ModelViewSet):
    queryset = Paquete.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PaqueteSerializer 

class CarritoViewSet(viewsets.ModelViewSet):
    queryset = Carrito.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CarritoSerializer 

class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = FacturaSerializer 
