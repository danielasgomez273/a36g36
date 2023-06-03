from rest_framework import routers
from .api import PacienteViewSet , FichaMedicaViewSet , RegistroGlucemiaViewSet , PrestadorViewSet , ServicioViewSet , PaqueteViewSet , CarritoViewSet , FacturaViewSet


#debo iniciar el router y luego registro los distintos endpoints 
router = routers.DefaultRouter()
# ruta, wiewset en el que estara basado y otro nombre de ruta, ROUTER CREARA EL CRUD COMPLETO DE ESTA RUTA, osea get, post, put, delete
router.register('paciente', PacienteViewSet ,'Pacientes')
router.register('fichaMedica', FichaMedicaViewSet ,'Fichas Medicas' )
router.register('registroGlucemia', RegistroGlucemiaViewSet ,'Registros glucemia' )
router.register('prestador', PrestadorViewSet ,'Prestadores de salud' )
router.register('servicio', ServicioViewSet ,'servicios' )
router.register('paquete', PaqueteViewSet ,'Paquetes' )
router.register('carrito', CarritoViewSet ,'Carritos' )
router.register('factura', FacturaViewSet ,'Facturas' )


#Sirve para exportar urls registradas en router

urlpatterns = router.urls
