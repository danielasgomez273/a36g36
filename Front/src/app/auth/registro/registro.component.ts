import { Component, OnInit } from '@angular/core';
import { FormBuilder,Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { loginInterface } from 'src/app/servicios/interfaces/loginInterface';
import { LoginService } from 'src/app/servicios/login.service';

// SE USARAN FORMULARIOS REACTIVOS Y VALIDACIONES SINCRONICAS

@Component({
  selector: 'app-registro',
  templateUrl: './registro.component.html',
  styleUrls: ['./registro.component.css']
})

export class RegistroComponent implements OnInit{

  borde_validacion:string=""


  // SE CREA OBJETO TIPO formBuilder 

  profileForm=this.formBuilder.group({
    email:["",[Validators.required,Validators.email]],
    pass:["",[Validators.required,Validators.minLength(7)]],
    name:["",[Validators.required]],
    last_name:["",[Validators.required]],
    phone:["",[Validators.required]],
    birthday:["",[Validators.required]],
    sex:["",[Validators.required]],
    

  });


///// METODOS GET /////
  get email_GET(){
    return this.profileForm.controls.email;
  }
  get pass_GET(){
    return this.profileForm.controls.pass;
  }
  get name_GET(){
    return this.profileForm.controls.name;
  }
  get last_name_GET(){
    return this.profileForm.controls.last_name;
  }
  get birthday_GET(){
    return this.profileForm.controls.birthday;
  }
  get sex_GET(){
    return this.profileForm.controls.sex;
  }
  get phone_GET(){
    return this.profileForm.controls.phone;
  }

  
  // SE INYECTA FormBuilder               y   EL SERVICIO   LoginService
  constructor(private formBuilder:FormBuilder,private router:Router , private serv_login:LoginService){};

// METODO DE BORDES
  bordeOk(){
    this.borde_validacion="borde-validacion_ok"
  }


// ////////////////////////////// METODO DE VERIFICACION USER ////////////////////////////
  verificacionRegistroUser(){
// si el formulario es valido
if(this.profileForm.valid){
  // CODIGO QUE CONSUME EL SERVICIO
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
 this.router.navigateByUrl("/auth/dash_user")
 this.profileForm.reset(); // SI VALIDA CORRECTAMENTE SE REINICIAN LOS VALORES DE LOS CAMPOS

    } 
    else{

      // SI NO VALIDA TODOS LOS CAMPOS QUEDAN MARCADO EN ROJO
      this.profileForm.markAllAsTouched();
      alert("No se ingresaron correctamente los datos")
    
    }
  }



  



  ngOnInit(): void {}
}


