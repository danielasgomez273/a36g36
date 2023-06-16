import { Component, OnInit } from '@angular/core';
import { FormBuilder,FormGroup,Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/servicios/auth.service';

// SE USARAN FORMULARIOS REACTIVOS Y VALIDACIONES SINCRONICAS

@Component({
  selector: 'app-registro',
  templateUrl: './registro.component.html',
  styleUrls: ['./registro.component.css']
})

export class RegistroComponent implements OnInit{

////////////////////////////////////////////////////////////////////////
  formPOSTRegistroUsuario: FormGroup | any;

  
//////////////////////////////////////////////////////////////////////
  ngOnInit(): void {
    
    this.formPOSTRegistroUsuario= this.formBuilder.group({
      id:[],
      email:["",[Validators.required,Validators.email]],
      pass:["",[Validators.required,Validators.minLength(9)]],
      username:["",[Validators.required]]
    })

  }

  ///////////////////////////////////////////////////////////////////////           
    constructor(
      private formBuilder:FormBuilder,
      private router:Router,
      private serv_registro:AuthService){};


  //////////// METODOS GET ///////////
  get email_GET(){
    return this.formPOSTRegistroUsuario.controls['email'];
  }
  get pass_GET(){
    return this.formPOSTRegistroUsuario.controls['pass'];
  }
  get username_GET(){
    return this.formPOSTRegistroUsuario.controls['username'];
  }



  //////////// METODO POST //////////////
  enviarDatosRegistroInicial(){
    // SI EL FORMULARIO CUMPLE CON LA VALIDACION
      if(this.formPOSTRegistroUsuario.valid){

            // Envia los datos
            //this.serv_registro.POST( 'http://localhost:3000/REGISTRO_INICIAL',
            this.serv_registro.POST( 'http://127.0.0.1:8000/api/auth/signup/',
            {
              // INFORMACION QUE VAMOS A PASAR  
              email:this.formPOSTRegistroUsuario.value.email,
              password:this.formPOSTRegistroUsuario.value.pass,
              username:this.formPOSTRegistroUsuario.value.username,
            }
                
            )
                .subscribe((respuesta: any) => {
 
            })

            // ACA HAY QUE ESPERAR UNA RESPUESTA 201 SI SE CREO USUARIO, SINO ERROR


                
            // CODIGO QUE VALIDA, ES APARTE AL CONSUMO DEL SERVICIO
            this.router.navigateByUrl("/auth/login")
            this.formPOSTRegistroUsuario.reset(); // SI VALIDA CORRECTAMENTE SE REINICIAN LOS VALORES DE LOS CAMPOS

      } 
      else{
            // SI NO VALIDA TODOS LOS CAMPOS QUEDAN MARCADO EN ROJO
            this.formPOSTRegistroUsuario.markAllAsTouched();
            alert("No se ingresaron correctamente los datos")
          
      }
  }

//////////////////////////////////////////////////////////////

  




}


