import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/servicios/auth.service';
import { EstadisUsuariosService } from 'src/app/servicios/estadis-usuarios.service';

// INTERFACE
import { NotasGlucemia } from '../../servicios/interfaces/notas-glucemia';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';





@Component({
  selector: 'app-dashboard-usuario',
  templateUrl: './dashboard-usuario.component.html',
  styleUrls: ['./dashboard-usuario.component.css']
})
export class DashboardUsuarioComponent implements OnInit {

  notas_glucemia: any;
  servicios: any;

  formNotasPOST: FormGroup | any;


  ////////////////////////////////////////////////////////////
  constructor(
    private paciente:EstadisUsuariosService,
    private usuario:AuthService,
    private formBuilder:FormBuilder){



    };

  
  ///////////////////////////////////////////////////////////
  ngOnInit(): void {

        // OBJETO FORMBUILDER
        this.formNotasPOST= this.formBuilder.group({

          fecha_registro:["",Validators.required],
          valor_glucemia:["",Validators.required],
          comentario_registro:["",Validators.required],
      
        })
    
    
    /////////// MUESTRA NOTAS A USUARIO /////////////
      this.paciente.muestraNotasUsuario().subscribe({
      next:(notas_S)=>{
        this.notas_glucemia=notas_S
      },
      error:(errorData)=>{
        console.error(errorData);
      } 
    })

    ///////// MUESTRA SERVICIOS A USUARIO ///////////
    this.paciente.muestraServicioAUsuario().subscribe({
      next:(servicios_S)=>{
        this.servicios=servicios_S
      },
      error:(errorData)=>{
        console.error(errorData);
      }
    })
    

  // una vez que el login.component setea la cookie, deberia poder accederla desde aca y saber que efectivamente el usuario esta logueado...
  console.log("log.getToken()", this.usuario.getToken(), "--")

} 
///////////// CIERRA NGONINIT /////////////

/////////// AGREGA NOTAS A USUARIO //////////////
  agregarNota(){
    // SI EL FORMULARIO CUMPLE CON LA VALIDACION
    if(this.formNotasPOST.valid){
      // Envia los datos al post
          this.paciente.nuevaNota('http://localhost:3000/notas_usuarios',
            {

              fecha_registro:this.formNotasPOST.value.fecha_registro,
              valor_glucemia:this.formNotasPOST.value.valor_glucemia,
              comentario_registro:this.formNotasPOST.value.comentario_registro,
            })
            .subscribe((respuesta: any) => {
              alert("Nota registrada")
            })
          }

          else{
            alert("Ingrese los datos correctamente")
        this.formNotasPOST.markAllAsTouched();

          }
    
  }

     ///// METODOS GET /////
  //   get fechaRegistro_GET(){
  //    return this.formNotasPOST.controls['fechaResitro'];
  //  }
  //  get valorGlucemia_GET(){
  //  }
  //  get comentarioRegistro_GET(){
  //    return this.formNotasPOST.controls['comentarioResgistro'];
  //  }





///////  CODIGO PARA AGREGAR AL CARRITO  ////////
Snombre:string=""
agregarNombre(value:string){
  this.Snombre=value

  return this.Snombre
}

Smonto:string=""
agregarMonto(value2:string){
  this.Smonto=value2
  return this.Smonto
}

nuevoPedido:any[]=[]
nuevoServicio:any[]=[]

nuevoCarrito(){
  /* La idea es guardar en un array los servicios que se van selccionando */ 
  this.nuevoServicio.push(this.Snombre)
  this.nuevoServicio.push(this.Smonto)

  this.nuevoPedido.push(this.nuevoServicio)

  return this.nuevoPedido
}



}