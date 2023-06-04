import { Component, OnInit } from '@angular/core';
import { FormBuilder,Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { loginInterface } from 'src/app/servicios/interfaces/loginInterface';
import { LoginService } from 'src/app/servicios/login.service';

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
  constructor(private formBuilder:FormBuilder,private router:Router , private serv_login:LoginService){};

// METODO DE BORDES
  bordeOk(){
    this.borde_validacion="borde-validacion_ok"
  }


// ////////////////////////////// METODO DE VERIFICACION USER ////////////////////////////
  verificacionLoginUser(){
// si el formulario es valido
    if(this.profileForm.valid){
      alert("Ingreso exitoso")
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
            alert("Ingreso exitoso")
            this.router.navigateByUrl("/auth/dash_admin")         
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


