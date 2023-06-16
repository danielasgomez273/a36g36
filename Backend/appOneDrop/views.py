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

# LOGUEO Y SESSIONES
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
        print(request)
        logout(request)
        return Response (status=status.HTTP_200_OK)
    
class SignupView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

#SOLO USUARIOS
class VerPerfil(APIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get']
    permission_classes = [permissions.IsAuthenticated]
    def get (self, request):   
        queryset = CustomUser.objects.filter(id=self.request.user.id)
        serializer = UserSerializer( queryset , many=True)
        if self.request.user.is_authenticated:
            return Response (serializer.data)

####################################### ADMIN #######################################
#SOLO ADMIN - VER USUARIOS
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
        
#SOLO ADMIN - VER CARRITOS
class VerCarritos(generics.ListCreateAPIView):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer
    http_method_names = ['get']
    permission_classes = [permissions.IsAdminUser]
    def verCarritos (self, request):
        queryset = self.get_queryset()
        serializer = CarritoSerializer( queryset , many=True)
        if self.request.user.is_authenticated:
            return Response (serializer.data)

#SOLO ADMIN - VER FACTURAS
class VerFacturas(generics.ListCreateAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer
    http_method_names = ['get']
    permission_classes = [permissions.IsAdminUser]
    def verFacturas (self, request):
        queryset = self.get_queryset()
        serializer = FacturaSerializer( queryset , many=True)
        if self.request.user.is_authenticated:
            return Response (serializer.data)
        
#SOLO ADMIN - CRUD SERVICIOS
class CrudServicios(APIView):
    permission_classes = [permissions.IsAdminUser]
    
    def get (self, request):
        queryset = Servicio.objects.all()
        serializer = ServicioSerializer(queryset, many=True)
        if self.request.user.is_authenticated:
            return Response (serializer.data)
        return Response(status= status.HTTP_400_BAD_REQUEST)
    
    def post (self, request, format = None):
        userAdmin = Prestador.objects.filter(usuario_id = self.request.user.id).get()
        userAdminPk = userAdmin.pk
        nuevoServicio ={
            'nombre_servicio' : request.data["nombre_servicio"] , 
            'descripcion_servicio' : request.data["descripcion_servicio"] , 
            'sede_servicio' : request.data["sede_servicio"] , 
            'precio_servicio' : request.data["precio_servicio"] ,
            'comentarios_servicio' : request.data["comentarios_servicio"] , 
            'prestador' : userAdminPk
        }

        serializer = ServicioSerializer (data = nuevoServicio)
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
#SOLO ADMIN - CRUD PAQUETES
class CrudPaquetes(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get (self, request):
        queryset = Paquete.objects.all()
        serializer = PaqueteSerializer(queryset, many=True)
        if self.request.user.is_authenticated:
            return Response (serializer.data)
        return Response(status= status.HTTP_400_BAD_REQUEST)
    
    def post (self, request, format = None):
        serializer = PaqueteSerializer (data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

####################################### PACIENTE #######################################
#SOLO PACIENTE - CRUD PACIENTE
class CrudPaciente(APIView): 
    http_method_names = ['get' , 'post']
    permission_classes = [permissions.IsAuthenticated]

    def get (self, request):  
        queryset = Paciente.objects.filter(usuario=self.request.user.id)
        serializer = PacienteSerializer(queryset, many=True)
        if self.request.user.is_authenticated:
            return Response (serializer.data)
        return Response(status= status.HTTP_400_BAD_REQUEST)
    
    def post (self, request, format = None):        
        usuarioId = self.request.user.id
        print( "························· id usuario PARA POST PACIENTE ··················· ")
        print(usuarioId)

        nuevoPaciente = {
            "nombre_paciente" : request.data["nombre_paciente"] ,
            "apellido_paciente" : request.data["apellido_paciente"] ,
            "telefono_paciente" : request.data["telefono_paciente"] ,
            "fecha_nacimiento" : request.data["fecha_nacimiento"] ,
            "sexo_paciente" : request.data["sexo_paciente"] ,
            "usuario" : usuarioId
        }        

        serializer = PacienteSerializer (data = nuevoPaciente)
        if serializer.is_valid():
            serializer.save()
            print("************ ID del nuevo PACIENTE ************")   
            print(serializer.data["id"]) 
            return Response( serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

#SOLO PACIENTE - CRUD REGISTROS            
class CrudRegistrosGlucemia(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get (self, request):  
        print("ID USUARIO=>")
        print(self.request.user.id)
        paciente = Paciente.objects.filter(usuario=self.request.user.id).get()
        queryset = Registro_glucemia.objects.filter(paciente_id = paciente.pk)
        serializer = RegistroGlucemiaSerializer(queryset, many=True)
        if self.request.user.is_authenticated:
            return Response (serializer.data)
        return Response(status= status.HTTP_401_UNAUTHORIZED)
    
    def post (self, request, format = None):
        print("ID USUARIO para registro glucemia=>")
        print(self.request.user.id)
        paciente = Paciente.objects.filter(usuario = self.request.user.id).get()
        paciente = paciente.pk

        nuevoRegistroGlucemia = {
            "fecha_registro" : request.data["fecha_registro"] ,
            "valor_glucemia" : request.data["valor_glucemia"] ,
            "comentario_registro" : request.data["comentario_registro"],
            "paciente" : paciente
        }
        serializer = RegistroGlucemiaSerializer (data = nuevoRegistroGlucemia)
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    












class CrudRegistrosGlucemiaById(generics.DestroyAPIView):  # revisar si funciona, antes estuve usando Apiview en vez de destroy

    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['delete', 'update']
    lookup_field = 'registro_pk'
    serializer_class = RegistroGlucemiaSerializer

    def delete (self, request, registro_pk):
        print(">>>>>>>>>>>>>>>>>>> entre a metodo DELETE >>>>>>>>>>>>>>>>>>>>>>")
        if self.request.user.is_authenticated:            
            print("ID USUARIO=>")
            print(self.request.user.id)

            # debo saber si el usuario actual quiere eliminar sino no puede
            paciente = Paciente.objects.filter(usuario=self.request.user.id).get()
            idPaciente = paciente.pk
            print("idPaciente=>")
            print(idPaciente)

            queryset = Registro_glucemia.objects.filter(id = registro_pk)
            
            print("idPaciente es igual a id dueño del registro??")
            print(idPaciente == queryset.get().paciente)

            if(idPaciente == queryset.get().paciente):
                print("SIII EL PTE AUTEHNTICADO ES EL DUEÑO DEL REGISTRO")
                #aca puedo eliminar o editar
                queryset.get().delete()
                print("SUPUESSSSTAMENTE YA ELIMINE EL REGISTRO==========> REVISAR BASE DE DATOS")
                return Response (status=204)
        return Response(status= status.HTTP_401_UNAUTHORIZED)
    
    def put (self, request, registro_pk):               
        print("/*/*/*/*/*/*/*/ entre a metodo UPDATE /*/*/*/*/*/*/*/>>>")

        print("METODO UPDATE EN PROCESOOOOOO")
        if self.request.user.is_authenticated:            
            print("ID USUARIO=>")
            print(self.request.user.id)
            paciente = Paciente.objects.filter(usuario=self.request.user.id).get()
            idPaciente = paciente.pk
            print("idPaciente=>")
            print(idPaciente)

            queryset = Registro_glucemia.objects.filter(id = registro_pk)
            
            print("idPaciente es igual a id dueño del registro??")
            print(idPaciente == queryset.get().paciente)

            if(idPaciente == queryset.get().paciente):
                print("SIII EL PTE AUTEHNTICADO ES EL DUEÑO DEL REGISTRO")
                
                
                
                #aca puedo eliminar o editar
                queryset.get().delete()

                registroEditado = {
                    "fecha_registro" : request.data["fecha_registro"] ,
                    "valor_glucemia" : request.data["valor_glucemia"] ,
                    "comentario_registro" : request.data["comentario_registro"],
                    "paciente" : paciente
                }

                serializer = RegistroGlucemiaSerializer (data = registroEditado)
                if serializer.is_valid():

                    #aca podria hacer un if de si cambio algun valor, pero seria mas facil pasar al fron toda la info y que el usuasroi solo cambie lo que quiera, y volver a recibir toda la info directamente
                    queryset.get().fecha_registro = request.data["fecha_registro"] 
                    queryset.get().valor_glucemia = request.data["valor_glucemia"] 
                    queryset.get().comentario_registro = request.data["comentario_registro"]


                    # aca debo revisar cual de los dos metodos me guarda el valor de manera correcta...
                    # aca debo revisar cual de los dos metodos me guarda el valor de manera correcta...
                    serializer.save() 
                    queryset.get().save()
                    # aca debo revisar cual de los dos metodos me guarda el valor de manera correcta...
                    # aca debo revisar cual de los dos metodos me guarda el valor de manera correcta...


                    print("SUPUESSSSTAMENTE YA EDITE EL REGISTRO==========> REVISAR BASE DE DATOS")

                    return Response(status= status.HTTP_200_OK)
        return Response(status= status.HTTP_401_UNAUTHORIZED)











#SOLO PACIENTE - CRUD FICHA MEDICA
class CrudFichaMedica(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get (self, request):  
        paciente = Paciente.objects.filter(usuario=self.request.user.id)       
        idPaciente = paciente.get().pk
        queryset = Ficha_medica.objects.filter(paciente_id = idPaciente)
        serializer = FichaMedicaSerializer(queryset, many=True)
        if self.request.user.is_authenticated:
            return Response (serializer.data)
        return Response(status= status.HTTP_401_UNAUTHORIZED)
    
    def post (self, request, format = None):
        print("ID USUARIO para ficha medica=>")
        print(self.request.user.id)

        paciente = Paciente.objects.filter(usuario = self.request.user.id).get()
        pacienteId = paciente.pk     

        print("ID PACIENTE para ficha medica=>")
        print(pacienteId)

        nuevaFichaMedica = {
            "tipo_diabetes" : request.data["tipo_diabetes"] ,
            "terapia_insulina" : request.data["terapia_insulina"] ,
            "terapia_pastillas" : request.data["terapia_pastillas"] ,
            "tipo_glucometro" : request.data["tipo_glucometro"] ,
            "tipo_sensor" : request.data["tipo_sensor"] ,
            "objetivo_glucosa" : request.data["objetivo_glucosa"] ,
            "comorbilidades" : request.data["comorbilidades"] ,
            "paciente" : pacienteId
        }
        print("nuevaFichaMedica=>")
        print(nuevaFichaMedica)

        serializer = FichaMedicaSerializer(data = nuevaFichaMedica)
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

#SOLO PACIENTE - CRUD CARRITO
class CrudCarrito(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get (self, request):  
        paciente = Paciente.objects.filter(usuario=self.request.user.id)       
        idPaciente = paciente.get().pk
        queryset = Carrito.objects.filter(paciente_id = idPaciente)
        serializer = CarritoSerializer(queryset, many=True)
        if self.request.user.is_authenticated:
            return Response (serializer.data)
        return Response(status= status.HTTP_400_BAD_REQUEST)
    
    def post (self, request, format = None):
        serializer = CarritoSerializer (data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

#SOLO PACIENTE - AGREGAR A CARRITO
class CrudServicioToCarrito(APIView):
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get']
    lookup_field = 'servicio_pk'
    serializer_class = ServicioSerializer

    def get (self, request, servicio_pk):  
        #Obtener el servicio a agregar..
        querysetServicio = Servicio.objects.filter(id=servicio_pk)
        serializerServicio = ServicioSerializer( querysetServicio , many=True)

        #Obtener el paciente que va a agregar..
        paciente = Paciente.objects.filter(usuario=self.request.user.id)    
        idPaciente = paciente.get().pk

        #Obtener el listado de servicios o paquetes que ya tiene 
        carrito = Carrito.objects.get(paciente = idPaciente)
        serviciosEnCarrito = carrito.servicio.get()
        #HASSTA AQUI TENGO LOS PAQUETES O SERVICIOS.. DEBERIA VER COMO SEGUIR INGRESANDO
        # DEBERIA POPULAR O ALGO?
        # SERIA MAS FACIL BORRAR LOS PAQUETES...
        print(serviciosEnCarrito)
        
        serviciosEnCarrito.append(servicio_pk)
        print(serviciosEnCarrito)
        carrito.servicio.set(serviciosEnCarrito)
        carrito.save()

        print(carrito)
        #carrito.append(servicio_pk)
        #querysetCarrito.save()
        serializerCarrito = CarritoSerializer(carrito, many=True)

        if self.request.user.is_authenticated:
            return Response (serializerCarrito.data)
        return Response(status= status.HTTP_400_BAD_REQUEST)
    '''
    def post (self, request, format = None):
        serializer = CarritoSerializer (data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    '''




####################################### SIN AUTH #######################################
#SIN AUTH - VER SERVICIOS
class VerServicios(generics.ListCreateAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer
    http_method_names = ['get']
    permission_classes = [permissions.AllowAny]
    def verServicios (self, request):
        queryset = self.get_queryset()
        serializer = ServicioSerializer( queryset , many=True)
        if self.request.user.is_authenticated:
            return Response (serializer.data)
        
#SIN AUTH - VER PAQUETES
class VerPaquetes(generics.ListCreateAPIView):
    queryset = Paquete.objects.all()
    serializer_class = PaqueteSerializer
    http_method_names = ['get']
    permission_classes = [permissions.AllowAny]
    def verPaquetes (self, request):
        queryset = self.get_queryset()
        serializer = PaqueteSerializer( queryset , many=True)
        if self.request.user.is_authenticated:
            return Response (serializer.data)
#SIN AUTH - VER TODOO => ERROR NO ESTA MOSDTRANDO TODOO
class VerTodos(generics.ListCreateAPIView):
    queryset = Paquete.objects.all()
    serializer_class = PaqueteSerializer
    http_method_names = ['get']
    permission_classes = [permissions.AllowAny]
    def verPaquetes (self, request):
        queryset = self.get_queryset()
        querysetServicio = Servicio.objects.all()
        serializer = PaqueteSerializer( queryset , many=True)
        serializerServicio = ServicioSerializer( querysetServicio , many=True)
        if self.request.user.is_authenticated:
            resp = {
                'servicios': serializerServicio.data ,
                'paquetes':serializer.data 
            }
            print("resp")
            print(resp)
            return Response(resp, status=status.HTTP_200_OK)
# # # # # # # # # # # # # # 

