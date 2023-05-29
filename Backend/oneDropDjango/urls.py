"""
URL configuration for oneDropDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # importo include
from appOneDrop import views
from appOneDrop.views import LoginView , LogoutView

urlpatterns = [
    ########################
    path('api/auth/login/', LoginView.as_view() , name ='auth_login'),
    
    path('api/auth/logout/', LogoutView.as_view() , name ='auth_logout'),
    ########################
    path('api/',include('appOneDrop.urls')), #estas vienen del router api

    path('',views.home, name ='home'),
    path('signup/',views.signup, name ='signup'),
   # path('signin/',views.signin, name ='signin'),
    path('signout/',views.signout, name ='signout'),
    path('protegido/',views.protegido, name ='protegido'),

    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # EN TEORIA, SERIA PARA EVITAR QUE ENTREN A OTRAS RUTAS
    
]
