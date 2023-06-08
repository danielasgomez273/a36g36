import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { loginInterface } from 'src/app/servicios/interfaces/loginInterface';

import { RegistroService } from 'src/app/servicios/registro.service';

@Component({
  selector: 'app-registro2usuario',
  templateUrl: './registro2usuario.component.html',
  styleUrls: ['./registro2usuario.component.css']
})
export class Registro2usuarioComponent implements OnInit{

  formPOSTRegistro2Usuarios: FormGroup;

  // SE INYECTA FormBuilder               y   EL SERVICIO   LoginService
  constructor(private formBuilder:FormBuilder,private router:Router , private serv_Registro2Datos:RegistroService){;



  // SE CREA OBJETO TIPO formBuilder 
  this.formPOSTRegistro2Usuarios=this.formBuilder.group({

    // DATOS PERSONALES
    id_pacinte:[""],
    name:["",[Validators.required]],
    last_name:["",[Validators.required]],
    birthday:["",[Validators.required]],
    sex:["",[Validators.required]],
    phone:["",[Validators.required]],
    
    // DATOS MEDICOS
    id_fichamedica:[],
    tipo_diabetes:["",[Validators.required]],
    terapia_insulina:["",[Validators.required]],
    terapia_pastillas:["",[Validators.required]],
    tipo_glucometro:["",[Validators.required]],
    tipo_sensor:["",[Validators.required]],
    comorbilidades:["",[Validators.required]],
    objetivo_glucosa:["",[Validators.required]],

  });
}


//////////////////// METODOS GET //////////////////////

    get name_GET(){
      return this.formPOSTRegistro2Usuarios.controls['name'];
    }
    get last_name_GET(){
      return this.formPOSTRegistro2Usuarios.controls['last_name'];
    }
    get birthday_GET(){
      return this.formPOSTRegistro2Usuarios.controls['birthday'];
    }
    get sex_GET(){
      return this.formPOSTRegistro2Usuarios.controls['sex'];
    }
    get phone_GET(){
      return this.formPOSTRegistro2Usuarios.controls['phone'];
    }
    get tipo_diabetes_GET(){
      return this.formPOSTRegistro2Usuarios.controls['tipo_diabetes'];
    }
    get terapia_insulina_GET(){
      return this.formPOSTRegistro2Usuarios.controls['terapia_insulina'];
    }
    get terapia_pastillas_GET(){
    return this.formPOSTRegistro2Usuarios.controls['terapia_pastillas'];
    }
    get tipo_glucometro_GET(){
    return this.formPOSTRegistro2Usuarios.controls['tipo_glucometro'];
    }
    get tipo_sensor_GET(){
    return this.formPOSTRegistro2Usuarios.controls['tipo_sensor'];
    }
    get comorbilidades_GET(){
    return this.formPOSTRegistro2Usuarios.controls['comorbilidades'];
    }
    get objetivo_glucosa_GET(){
      return this.formPOSTRegistro2Usuarios.controls['objetivo_glucosa'];
    }
  

  /////////////////////////////////
  //////////// POST //////////////
  ////////////////////////////////

  // METODO DE VALIDACION Y ENVIO DE DATOS DEL SEGUNDO FORMULARIO DE REGISTRO
  enviarDatosRegistroDOS(){
    // si el formulario es valido
    if(this.formPOSTRegistro2Usuarios.valid){

        // ENVIA LOS DATOS
        this.serv_Registro2Datos.POSTRegistroUsuario('http://localhost:3000/USUARIOSDATOSPERSONALES',
        {
        // INFORMACION QUE VAMOS A PASAR
          name:this.formPOSTRegistro2Usuarios.value.name,
          last_name:this.formPOSTRegistro2Usuarios.value.last_name,
          birthday:this.formPOSTRegistro2Usuarios.value.birthday,
          sex:this.formPOSTRegistro2Usuarios.value.sex,
          phone:this.formPOSTRegistro2Usuarios.value.phone,
          tipo_diabetes:this.formPOSTRegistro2Usuarios.value.tipo_diabetes,
          terapia_insulina:this.formPOSTRegistro2Usuarios.value.terapia_insulina,
          terapia_pastillas:this.formPOSTRegistro2Usuarios.value.terapia_pastillas,
          tipo_glucometro:this.formPOSTRegistro2Usuarios.value.tipo_glucometro,
          tipo_sensor:this.formPOSTRegistro2Usuarios.value.tipo_sensor,
          comorbilidades:this.formPOSTRegistro2Usuarios.value.comorbilidades,
          objetivo_glucosa:this.formPOSTRegistro2Usuarios.value.objetivo_glucosa,

          // VER EL TEMA DE LOS IDS

        }
        )
        .subscribe((respuesta: any) => {

        })

        // CODIGO QUE VALIDA, ES APARTE AL CONSUMO DEL SERVICIO
        this.router.navigateByUrl("/auth/dash_user")
        this.formPOSTRegistro2Usuarios.reset(); // SI VALIDA CORRECTAMENTE SE REINICIAN LOS VALORES DE LOS CAMPOS

        } 
    else{
        // SI NO VALIDA TODOS LOS CAMPOS QUEDAN MARCADO EN ROJO
        this.formPOSTRegistro2Usuarios.markAllAsTouched();
        alert("No se ingresaron correctamente los datos")

    }
  }



      



  ngOnInit(): void {}





















}
