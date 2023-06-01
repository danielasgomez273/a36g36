import { Component, OnInit } from '@angular/core';
import { FormBuilder,FormGroup,Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { FormContactoService } from 'src/app/servicios/form-contacto.service';
import { loginInterface } from 'src/app/servicios/interfaces/loginInterface';
@Component({
  selector: 'app-contacto',
  templateUrl: './contacto.component.html',
  styleUrls: ['./contacto.component.css']
})
export class ContactoComponent implements OnInit {

  constructor(private formBuilder:FormBuilder,private router:Router , private serv_logincontact:FormContactoService){};
  profileForm=this.formBuilder.group({
    email:["",[Validators.required,Validators.email]],
    pass:["",[Validators.required,Validators.minLength(7)]]

  });

  ngOnInit(): void {}



// ////////////////////////////// METODO DE VERIFICACION USER ////////////////////////////
  verificacionLoginUser(){
// si el formulario es valido
    if(this.profileForm.valid){
      this.serv_logincontact.login(this.profileForm.value as loginInterface).subscribe({
          next:(userData) => {
            console.log(userData);
          this.router.navigateByUrl("/auth/dash_user")
          },
          error: (errorData) => {
              console.error(errorData);
          },
          complete:() => {
          //alert("Validacion realizada correctamente");
          }

      });
      //this.profileForm.reset(); // SI VALIDA CORRECTAMENTE SE REINICIAN LOS VALORES DE LOS CAMPOS
      //this.direccion="auth/dash_user"
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
  
        this.serv_logincontact.login(this.profileForm.value as loginInterface).subscribe({
            next:(userData) => {
            console.log(userData);
            this.router.navigateByUrl("/auth/dash_admin")

  
            },
            error: (errorData) => {
                console.error(errorData);
            },
  
            complete:() => {
            //alert("Validacion realizada correctamente");
  
  
            }
  
        });
        //this.profileForm.reset(); // SI VALIDA CORRECTAMENTE SE REINICIAN LOS VALORES DE LOS CAMPOS

      } 
      else{
        // SI NO VALIDA TODOS LOS CAMPOS QUEDAN MARCADO EN ROJO
        this.profileForm.markAllAsTouched();
        alert("No se ingresaron correctamente los datos o no se reconoce el usuario")

      }
    }


  ///// METODOS GET /////
  get email_GET(){
    return this.profileForm.controls['email'];
  }
  get pass_GET(){
    return this.profileForm.controls['pass'];
  }
}
