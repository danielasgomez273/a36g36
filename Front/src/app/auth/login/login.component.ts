import { Component, OnInit } from '@angular/core';
import { FormBuilder,Validators } from '@angular/forms';
import { loginInterface } from 'src/app/servicios/interfaces/loginInterface';
import { LoginService } from 'src/app/servicios/login.service';

// SE USARAN FORMULARIOS REACTIVOS Y VALIDACIONES SINCRONICAS

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit{
  // SE CREA OBJETO TIPO formBuilder

  profileForm=this.formBuilder.group({
    email:["",[Validators.required,Validators.email]],
    pass:["",[Validators.required]]

  });

  // SE INYECTA FormBuilder               y   EL SERVICIO   LoginService
  constructor(private formBuilder:FormBuilder, private serv_login:LoginService){};


  // METODO DE VERIFICACION
  verificacionLogin(){

    if(this.profileForm.valid){

      this.serv_login.login(this.profileForm.value as loginInterface).subscribe({
          next:(userData) => {
            console.log(userData);
          },
          error: (errorData) => {
              console.error(errorData);
          },

          complete:() => {
           // alert("Validacion realizada correctamente");

          }

      });
      this.profileForm.reset(); // SI VALIDA CORRECTAMENTE SE REINICIAN LOS VALORES DE LOS CAMPOS
    } 
    else{

      // SI NO VALIDA TODOS LOS CAMPOS QUEDAN MARCADO EN ROJO
      this.profileForm.markAllAsTouched();
     //alert("No se ingresaron correctamente los datos")
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


