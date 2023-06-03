from django.contrib import admin
from django.urls import path, include # importo include
from appOneDrop import views
from rest_framework.authtoken import views as authtokenViews

urlpatterns = [
##############
# PROPUESTA ISPC
    #SESIONES Y LOGUEO
    path('api/auth/signup/', views.SignupView.as_view(), name='auth_signup'),
    
    path('api/auth/login/',views.LoginView.as_view(), name ='auth_login'),
    path('api/auth/logout/',views.LogoutView.as_view(), name ='auth_logout'),

    #SOLO ADMIN
    path('api/usuarios/', views.VerUsuarios.as_view(), name='ver_usuarios'),

    # METODO PARA ELIMINAR Y EDITAR PENDIENTE
    path('api/servicios/', views.CrudServicios.as_view(), name='crud_servicios'),
    

    #SOLO PACIENTE ------ pendienteeee
    path('api/paciente/', views.CrearPaciente.as_view(), name='crear_paciente'),
    #path('api/paciente/', views.VerPaciente.as_view(), name='ver_paciente'),
    #path('api/paciente/', views.EditarPaciente.as_view(), name='editar_paciente'),





    ##############
#    #NO FUNCIONA ESTE LOGIN
#    path('api/singUpDePostman',views.singUpDePostman , name ='singUpDePostman'),
#    path('api/singInDePostman',views.singInDePostman , name ='singInDePostman'),
    ##############

     path('api/',include('appOneDrop.urls')), #estas vienen del router api

#    path('',views.home, name ='home'),
#    path('signup/',views.signup, name ='signup'),
#    path('signin/',views.signin, name ='signin'),
#    path('signout/',views.signout, name ='signout'),
#    path('protegido/',views.protegido, name ='protegido'),
   
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # EN TEORIA, SERIA PARA EVITAR QUE ENTREN A OTRAS RUTAS
]
