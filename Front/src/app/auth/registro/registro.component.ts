import { Component, OnInit } from '@angular/core';
import { FormBuilder,FormGroup,Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { RegistroService } from 'src/app/servicios/registro.service';


// SE USARAN FORMULARIOS REACTIVOS Y VALIDACIONES SINCRONICAS

@Component({
  selector: 'app-registro',
  templateUrl: './registro.component.html',
  styleUrls: ['./registro.component.css']
})

export class RegistroComponent implements OnInit{


// OBJETO TIPO formBuilder 
  formPOSTRegistroUsuario: FormGroup;

// SE INYECTA FormBuilder               y   EL SERVICIO   LoginService
  constructor(private formBuilder:FormBuilder,private router:Router , private serv_registro:RegistroService){

// OBJETO FORMBUILDER
this.formPOSTRegistroUsuario= this.formBuilder.group({
  id:[],
  email:["",[Validators.required,Validators.email]],
  pass:["",[Validators.required,Validators.minLength(7)]],
  username:["",[Validators.required]]

})
};
  ///// METODOS GET /////
  get email_GET(){
    return this.formPOSTRegistroUsuario.controls['email'];
  }
  get pass_GET(){
    return this.formPOSTRegistroUsuario.controls['pass'];
  }
  get username_GET(){
    return this.formPOSTRegistroUsuario.controls['username'];
  }


  /////////////////////////////////
  //////////// POST //////////////
  ////////////////////////////////

  // METODO DE VALIDACION Y ENVIO DE DATOS DEL PRIMER FORMULARIO DE REGISTRO
  enviarDatosRegistroInicial(){
    // SI EL FORMULARIO CUMPLE CON LA VALIDACION
      if(this.formPOSTRegistroUsuario.valid){

                // Envia los datos
                this.serv_registro.POSTRegistroUsuario('http://localhost:3000/USUARIOS',
                {
                  // INFORMACION QUE VAMOS A PASAR  
                  email:this.formPOSTRegistroUsuario.value.email,
                  pass:this.formPOSTRegistroUsuario.value.pass,
                  username:this.formPOSTRegistroUsuario.value.username,
                }
                
                )
                .subscribe((respuesta: any) => {
 
                })

      // CODIGO QUE VALIDA, ES APARTE AL CONSUMO DEL SERVICIO
      this.router.navigateByUrl("/auth/registro2usuario")
      this.formPOSTRegistroUsuario.reset(); // SI VALIDA CORRECTAMENTE SE REINICIAN LOS VALORES DE LOS CAMPOS

      } 
      else{
            // SI NO VALIDA TODOS LOS CAMPOS QUEDAN MARCADO EN ROJO
            this.formPOSTRegistroUsuario.markAllAsTouched();
            alert("No se ingresaron correctamente los datos")
          
      }
  }



  



  ngOnInit(): void {}
}


