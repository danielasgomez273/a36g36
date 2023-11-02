from .models import Paciente , Ficha_medica , Registro_glucemia , Prestador , Servicio , Carrito , Factura
from rest_framework import viewsets , permissions
from .serializers import PacienteSerializer , FichaMedicaSerializer , RegistroGlucemiaSerializer ,PrestadorSerializer , ServicioSerializer , CarritoSerializer , FacturaSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = PacienteSerializer 

class FichaMedicaViewSet(viewsets.ModelViewSet):
    queryset = Ficha_medica.objects.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = FichaMedicaSerializer 

class RegistroGlucemiaViewSet(viewsets.ModelViewSet):
    queryset = Registro_glucemia.objects.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = RegistroGlucemiaSerializer 

class PrestadorViewSet(viewsets.ModelViewSet):
    queryset = Prestador.objects.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = PrestadorSerializer 

class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = ServicioSerializer 

# class PaqueteViewSet(viewsets.ModelViewSet):
#     queryset = Paquete.objects.all()
#     permission_classes = [permissions.IsAdminUser]
#     serializer_class = PaqueteSerializer 

class CarritoViewSet(viewsets.ModelViewSet):
    queryset = Carrito.objects.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = CarritoSerializer 

class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = FacturaSerializer 
