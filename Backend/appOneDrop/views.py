from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login , logout , authenticate
from django.db import IntegrityError
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status , generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from .models import Paciente , Ficha_medica , Registro_glucemia , Prestador , Servicio , Paquete , Carrito , Factura

from .serializers import UserSerializer, PacienteSerializer , FichaMedicaSerializer , RegistroGlucemiaSerializer ,PrestadorSerializer , ServicioSerializer , PaqueteSerializer , CarritoSerializer , FacturaSerializer
from .models import CustomUser
from rest_framework.permissions import IsAdminUser , AllowAny
from rest_framework import permissions


##############
# PROPUESTA ISPC
class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = authenticate (email = email , password = password)        
        if user:
            login(request, user)
            return Response(
                UserSerializer(user).data,
                status=status.HTTP_200_OK)
        return Response (status=status.HTTP_404_NOT_FOUND)
    
class LogoutView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        logout(request)
        return Response (status=status.HTTP_200_OK)
    
class SignupView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer


##############

#SOLO ADMIN
class VerUsuarios(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get']
    permission_classes = [permissions.IsAdminUser]
    def listUsers (self, request):
        queryset = self.get_queryset()
        serializer = UserSerializer( queryset , many=True)
        if self.request.user.is_authenticated:
            return Response (serializer.data)

#CRUD SERVICIOS
class CrudServicios(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get (self, request):
        queryset = Servicio.objects.all()
        serializer = ServicioSerializer(queryset, many=True)
        if self.request.user.is_authenticated:
            return Response (serializer.data)
        return Response(status= status.HTTP_400_BAD_REQUEST)
    
    def post (self, request, format = None):
        serializer = ServicioSerializer (data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    


#SOLO PACIENTE
class CrearPaciente(APIView):
    ''' 
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get']
    permission_classes = [permissions.IsAdminUser]
    def listUsers (self, request):
        queryset = self.get_queryset()
        serializer = UserSerializer( queryset , many=True)
        if self.request.user.is_authenticated:
            return Response (serializer.data)
    ''' 
    pass
# # # # # # # # # # # # # # 


''' 
@csrf_exempt
def singInDePostman(request):
    # debe ser un POST SI O SI
    pass


@csrf_exempt
def singUpDePostman(request):
    
#ESTE REGISTRO DE USUARIO NO FUNCIONA, NO PUEDO ACCEDER AL request.POST
#    if request.POST['password1'] == request.POST['password2']:
#        try:
#            #register user,luego save user en bd, guardar usuario en session y luego redireccionar
#            userCreado = User.objects.create_user( username = request.POST['username'] , password = request.POST['password1'])
#            userCreado.save() 
#            login(request,userCreado) #guardar usuario en session 
#            # EN ESTE CASO, NO REDIRIGO, SOLO CODIGO OK return redirect('protegido')
#            print("SUPUESTA CREACION DE USUARIO CORRECTA.. AHORA BIEN, SE LOGUE USUARIO¿??????")
#            return Response (status=status.HTTP_201_CREATED)
#        except IntegrityError:
#            print("error de integridad en bd... solucionar respeusta")
#            return Response (status=status.HTTP_400_BAD_REQUEST)
#    else:
#        print("ERROR DE PASS SONSO")
#        return Response (status=status.HTTP_400_BAD_REQUEST)
    
# # # # # # # # # # # # # # 

    pass

def home(request):
    return render(request,'plantilla/home.html')


@csrf_exempt
def signup(request):
    if request.method == 'GET':
        return render(request,'plantilla/signup.html', {
        'form' : UserCreationForm,
        'authForm' : AuthenticationForm
    })
    else:
        print("ME ESTA LLEGANDOOOO request.POST")
        print(request.POST)
        print("ME LLEGO")
        if 'password' in request.POST:
            user = authenticate(request , username = request.POST['username'], password = request.POST['password'])
            if user is None:
                return render(request,'plantilla/signup.html', {
                    'form' : UserCreationForm,
                    'authForm' : AuthenticationForm,
                    'error' : 'Credenciallllles no vaalalalalidadsd'
                }) 
            else:        
                login(request,user) #guardar usuario en session 
                return redirect('protegido') 
        elif 'password1' in request.POST:   
            if request.POST['password1'] == request.POST['password2']:
                try:
                    #register user,luego save user en bd, guardar usuario en session y luego redireccionar
                    userCreado = User.objects.create_user( username = request.POST['username'] , password = request.POST['password1'])
                    userCreado.save() 
                    login(request,userCreado) #guardar usuario en session 
                    return redirect('protegido')
                except IntegrityError:
                    return render(request,'plantilla/signup.html', {
                        'form' : UserCreationForm,
                        'error' : 'User ya existeeeeee IntegrityError'
                    })          
            else:
                return render(request,'plantilla/signup.html', {
                    'form' : UserCreationForm,
                    'error' : 'Passss no coinciden sonsooo'
                })  

@login_required
def protegido(request):
    return render(request,'plantilla/protegido.html')

def signout(request):
    logout(request)
    return redirect('home')

'''