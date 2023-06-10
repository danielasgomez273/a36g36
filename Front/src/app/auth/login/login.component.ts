import { HttpBackend, HttpClient, HttpClientModule, HttpHeaderResponse, HttpResponse } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { FormBuilder,Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { loginInterface } from 'src/app/servicios/interfaces/loginInterface';
import { LoginService } from 'src/app/servicios/login.service';
import { HttpHeaders } from '@angular/common/http';

// SE USARAN FORMULARIOS REACTIVOS Y VALIDACIONES SINCRONICAS

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})

export class LoginComponent implements OnInit{

  borde_validacion:string=""


  // SE CREA OBJETO TIPO formBuilder 

  profileForm=this.formBuilder.group({
    email:["",[Validators.required,Validators.email]],
    pass:["",[Validators.required,Validators.minLength(7)]]

  });

  // SE INYECTA FormBuilder               y   EL SERVICIO   LoginService
  constructor(private formBuilder:FormBuilder,private router:Router , private serv_login:LoginService , private http : HttpClient){};

// METODO DE BORDES
  bordeOk(){
    this.borde_validacion="borde-validacion_ok"
  }


// ////////////////////////////// METODO DE VERIFICACION USER ////////////////////////////
  verificacionLoginUser(){
// si el formulario es valido
    if(this.profileForm.valid){
       // PARTE QUE CONSUME EL SERVICIO
       /*
       this.serv_login.login(this.profileForm.value as loginInterface).subscribe({

        next:(userData) => {
          console.log("----", userData)
        },
        error:(errorData) => {
          console.log(errorData)
        },
        complete:() => {

        }
      })
      */
/*
      this.serv_login.login(this.profileForm.value as loginInterface).subscribe((data)=>{
        console.log(data)
        //const csrftoken = HttpHeaderResponse.prototype.headers.get("csrftoken") //getAll("csrftoken")
        console.log("SE SUPONE QUE DEBERIA GUARDAR UNA COOKIE CON csrftoken")
        console.log("SE SUPONE QUE DEBERIA GUARDAR UNA COOKIE CON csrftoken")      
        //si no setea la cookie, deberia poder setearla manualmente.. pero no tengo acceso al token, como puedo obtenerlo desde los headers?
        //this.serv_login.setToken(data.token);
      })
      */
      
      this.serv_login.login(this.profileForm.value as loginInterface).subscribe((data)=>{
        console.log(data)
        //const csrftoken = HttpHeaderResponse.prototype.headers.get("csrftoken") //getAll("csrftoken")
        console.log("SE SUPONE QUE DEBERIA GUARDAR UNA COOKIE CON csrftoken")
        console.log("SE SUPONE QUE DEBERIA GUARDAR UNA COOKIE CON csrftoken")      
        //si no setea la cookie, deberia poder setearla manualmente.. pero no tengo acceso al token, como puedo obtenerlo desde los headers?
        //this.serv_login.setToken(data.token);
      })

  // CODIGO QUE VALIDA, ES APARTE AL CONSUMO DEL SERVICIO
          
  // ACA HAY QUE ESPERAR UNA RESPUESTA 200 SI SE logueo USUARIO, SINO ERROR.. El problema es que no se como acceder a la respuesta que envia el back.. el codigo lo envia pero no lo puedo acceder?? Una vez que acceda, puedo saber si la respuesta fue exitosa, reenviar al dashboard correspondiente..
  this.router.navigateByUrl("/auth/dash_user")
  
  this.profileForm.reset(); // SI VALIDA CORRECTAMENTE SE REINICIAN LOS VALORES DE LOS CAMPOS

    } 
    else{

      // SI NO VALIDA TODOS LOS CAMPOS QUEDAN MARCADO EN ROJO
      this.profileForm.markAllAsTouched();
      alert("No se ingresaron correctamente los datos o no se reconoce el usuario")
    
    }
  }


// /////////////////////////// METODO DE VERIFICACION ADMIN  ///////////////////////////
    verificacionLoginAdmin(){

      if(this.profileForm.valid){

        // PARTE QUE CONSUME EL SERVICIO
            this.serv_login.login(this.profileForm.value as loginInterface).subscribe({

              next:(userData) => {

              },
              error:(errorData) => {
                console.log(errorData)
              },
              complete:() => {
              }
            })

        // CODIGO QUE VALIDA, ES APARTE AL CONSUMO DEL SERVICIO

        
        // ACA HAY QUE ESPERAR UNA RESPUESTA 200 SI SE logueo USUARIO, SINO ERROR
        // ACA HAY QUE ESPERAR UNA RESPUESTA 200 SI SE logueo USUARIO, SINO ERROR
        // ACA HAY QUE ESPERAR UNA RESPUESTA 200 SI SE logueo USUARIO, SINO ERROR
        // ACA HAY QUE ESPERAR UNA RESPUESTA 200 SI SE logueo USUARIO, SINO ERROR
        // ACA HAY QUE ESPERAR UNA RESPUESTA 200 SI SE logueo USUARIO, SINO ERROR
        // ACA HAY QUE ESPERAR UNA RESPUESTA 200 SI SE logueo USUARIO, SINO ERROR
        // ACA HAY QUE ESPERAR UNA RESPUESTA 200 SI SE logueo USUARIO, SINO ERROR
        //    this.router.navigateByUrl("/auth/dash_admin")   
        
            

            this.profileForm.reset(); // SI VALIDA CORRECTAMENTE SE REINICIAN LOS VALORES DE LOS CAMPOS

      } 
      else{
  
        // SI NO VALIDA TODOS LOS CAMPOS QUEDAN MARCADO EN ROJO
        this.profileForm.markAllAsTouched();
        alert("No se ingresaron correctamente los datos o no se reconoce el usuario")

      }
    }


  ///// METODOS GET /////
  get email_GET(){
    return this.profileForm.controls.email;
  }
  get pass_GET(){
    return this.profileForm.controls.pass;
  }




  ngOnInit(): void {}
}


