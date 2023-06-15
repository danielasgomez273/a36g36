import { Component, OnInit } from '@angular/core';
import { FormBuilder,FormGroup,Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/servicios/auth.service';

// SE USARAN FORMULARIOS REACTIVOS Y VALIDACIONES SINCRONICAS

@Component({
  selector: 'app-formulario-pago',
  templateUrl: './formulario-pago.component.html',
  styleUrls: ['./formulario-pago.component.css']
})

export class formulariopagoComponent implements OnInit{

////////////////////////////////////////////////////////////////////////
formPOSTFormularioPago: FormGroup | any;

  
//////////////////////////////////////////////////////////////////////
  ngOnInit(): void {
    
    this.formPOSTFormularioPago= this.formBuilder.group({
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
    return this.formPOSTFormularioPago.controls['email'];
  }
  get pass_GET(){
    return this.formPOSTFormularioPago.controls['pass'];
  }
  get username_GET(){
    return this.formPOSTFormularioPago.controls['username'];
  }



  //////////// METODO POST //////////////
  enviarDatosRegistroInicial(){
    // SI EL FORMULARIO CUMPLE CON LA VALIDACION
      if(this.formPOSTFormularioPago.valid){

            // Envia los datos
            this.serv_formulario-pago.formPOSTFormularioPago( 'http://127.0.0.1:8000/api/auth/signup/',
            {
              // INFORMACION QUE VAMOS A PASAR  
              email:this.formPOSTFormularioPago.value.email,
              password:this.formPOSTFormularioPago.value.pass,
              username:this.formPOSTFormularioPago.value.username,
            }
                
            )
                .subscribe((respuesta: any) => {
 
            })

            // ACA HAY QUE ESPERAR UNA RESPUESTA 201 SI SE CREO USUARIO, SINO ERROR


                
            // CODIGO QUE VALIDA, ES APARTE AL CONSUMO DEL SERVICIO
            this.router.navigateByUrl("/auth/registro2usuario")
            this.formPOSTFormularioPago.reset(); // SI VALIDA CORRECTAMENTE SE REINICIAN LOS VALORES DE LOS CAMPOS

      } 
      else{
            // SI NO VALIDA TODOS LOS CAMPOS QUEDAN MARCADO EN ROJO
            this.formPOSTFormularioPago.markAllAsTouched();
            alert("No se ingresaron correctamente los datos")
          
      }
  }

//////////////////////////////////////////////////////////////

  




}