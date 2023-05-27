from rest_framework import routers
from .api import PacienteViewSet , FichaMedicaViewSet , RegistroGlucemiaViewSet , PrestadorViewSet , ServicioViewSet , PaqueteViewSet , CarritoViewSet , FacturaViewSet

#debo iniciar el router y luego registro los distintos endpoints 
router = routers.DefaultRouter()
# ruta, wiewset en el que estara basado y otro nombre de ruta, ROUTER CREARA EL CRUD COMPLETO DE ESTA RUTA, osea get, post, put, delete
router.register('api/paciente', PacienteViewSet ,'Pacientes' )
router.register('api/fichaMedica', FichaMedicaViewSet ,'Fichas Medicas' )
router.register('api/registroGlucemia', RegistroGlucemiaViewSet ,'Registros glucemia' )
router.register('api/prestador', PrestadorViewSet ,'Prestadores de salud' )
router.register('api/servicio', ServicioViewSet ,'servicios' )
router.register('api/paquete', PaqueteViewSet ,'Paquetes' )
router.register('api/carrito', CarritoViewSet ,'Carritos' )
router.register('api/factura', FacturaViewSet ,'Facturas' )
#Sirve para exportar urls registradas en router
urlpatterns = router.urls
