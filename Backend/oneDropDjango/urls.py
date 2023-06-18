from django.contrib import admin
from django.urls import path, include # importo include
from appOneDrop import views
from rest_framework.authtoken import views as authtokenViews

urlpatterns = [
#SESIONES Y LOGUEO
    path('api/auth/signup/', views.SignupView.as_view(), name='auth_signup'),    
    path('api/auth/login/',views.LoginView.as_view(), name ='auth_login'),
    path('api/auth/logout/',views.LogoutView.as_view(), name ='auth_logout'),

#SOLO USUARIOS------------
    path('api/verPerfil/', views.VerPerfil.as_view(), name='ver_perfil'),

##SOLO ADMIN------------
    path('api/admin/usuarios/', views.VerUsuarios.as_view(), name='ver_usuarios'),

    #METODO PARA ELIMINAR Y EDITAR PENDIENTE => SERVICIOS Y PAQUETES
    path('api/admin/servicios/', views.CrudServicios.as_view(), name='crud_servicios'),
    path('api/admin/servicios/<int:servicio_pk>', views.CrudServiciosById.as_view(),name='crud_Servicios_by_id'),
#   path('api/admin/paquetes/', views.CrudPaquetes.as_view(), name='crud_paquetes'),    
    path('api/admin/carritos/', views.VerCarritos.as_view(), name='ver_carritos'),
    path('api/admin/facturas/', views.VerFacturas.as_view(), name='ver_facturas'),

##SOLO PACIENTE------------
    #METODO PARA EDITAR PENDIENTE y eliminar????
    path('api/paciente/', views.CrudPaciente.as_view(), name='crud_paciente'),
    path('api/paciente/registros_glucemia/', views.CrudRegistrosGlucemia.as_view(), name='crud_registros_glucemia'),
    path('api/paciente/registros_glucemia/<int:registro_pk>', views.CrudRegistrosGlucemiaById.as_view(),name='crud_registros_glucemia_by_id'),
    path('api/paciente/ficha_medica/', views.CrudFichaMedica.as_view(), name='crud_ficha_medica'),
    path('api/paciente/carrito/', views.CrudCarrito.as_view(), name='crud_carrito'),    
    path('api/paciente/carrito/servicio/<int:servicio_pk>/', views.CrudServicioToCarrito.as_view(), name='crud_servicio_to_carrito'),
##SIN AUTH
    path('api/paciente/servicios/', views.VerServicios.as_view(), name='ver_servicios'),
#    path('api/paciente/paquetes/', views.VerPaquetes.as_view(), name='ver_paquetes'),
#    path('api/paciente/ver_todos/', views.VerTodos.as_view(), name='ver_todo'),

# que usuario pueda ver todos los paquetes

####### arreglar logica para que pueda agregar productos al carrito!!!!




##REVISAAAAR
    path('api/router/',include('appOneDrop.urls')), #estas vienen del router api
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # EN TEORIA, SERIA PARA EVITAR QUE ENTREN A OTRAS RUTAS


    ##############
#    #NO FUNCIONA ESTE LOGIN
#    path('api/singUpDePostman',views.singUpDePostman , name ='singUpDePostman'),
#    path('api/singInDePostman',views.singInDePostman , name ='singInDePostman'),
    ##############

#    path('',views.home, name ='home'),
#    path('signup/',views.signup, name ='signup'),
#    path('signin/',views.signin, name ='signin'),
#    path('signout/',views.signout, name ='signout'),
#    path('protegido/',views.protegido, name ='protegido'),
   
]
