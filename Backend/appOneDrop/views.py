from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login , logout , authenticate
from django.db import IntegrityError
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
#############################
#ispc apiview

class LoginView(APIView):
    def post(self, request):
        # email = request.data.get('email', None)
        # password = request.data.get('password', None)
        # email = authenticate (email = email , password = password)
        print("request.body")
        splitttt = request.body.split()
        
        print(request.body)        
        print(list(splitttt)['username'])

        user = authenticate(request , username = request.POST['username'], password = request.POST['password'])
        if user:
            print("TEORICAMENTE ME LOGUE")
            login(request,user)
            return Response(status=status.HTTP_200_OK)
        
        return Response(status=status.HTTP_404_NOT_FOUND) 

class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


#############################
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

