from rest_framework import routers
from .api import PacienteViewSet , FichaMedicaViewSet , RegistroGlucemiaViewSet , PrestadorViewSet , ServicioViewSet , PaqueteViewSet , CarritoViewSet , FacturaViewSet

router = routers.DefaultRouter()
router.register('paciente', PacienteViewSet ,'Pacientes')
router.register('fichaMedica', FichaMedicaViewSet ,'Fichas Medicas' )
router.register('registroGlucemia', RegistroGlucemiaViewSet ,'Registros glucemia' )
router.register('prestador', PrestadorViewSet ,'Prestadores de salud' )
router.register('servicio', ServicioViewSet ,'servicios' )
router.register('paquete', PaqueteViewSet ,'Paquetes' )
router.register('carrito', CarritoViewSet ,'Carritos' )
router.register('factura', FacturaViewSet ,'Facturas' )

urlpatterns = router.urls
