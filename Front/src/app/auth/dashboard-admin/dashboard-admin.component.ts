import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { EstadisAdminsService } from 'src/app/servicios/estadis-admins.service';



@Component({
  selector: 'app-dashboard-admin',
  templateUrl: './dashboard-admin.component.html',
  styleUrls: ['./dashboard-admin.component.css']
})
export class DashboardAdminComponent implements OnInit{

  estadisticas_admins:any
  comorbilidades_admins: any;
  servicios_admins:any;
  ingresos_admins: any;

  formPOST: FormGroup;

  //////////////////////////

  constructor(private estadistica:EstadisAdminsService, private formBuilder:FormBuilder){
    this.estadistica.muestraEstadisticas().subscribe({
      next:(estadisticas_S)=>{
        this.estadisticas_admins=estadisticas_S
      },
      error:(errorData)=>{
        console.error(errorData);
      } 
    })


  //////////////////////////

    this.estadistica.muestraComorbilidades().subscribe({
      next:(comorbilidades_S)=>{
        this.comorbilidades_admins=comorbilidades_S
      },
      error:(errorData)=>{
        console.error(errorData);
      } 
    })

  //////////////////////////

    this.estadistica.muestraServicios().subscribe({
      next:(servicio_S)=>{
        this.servicios_admins=servicio_S
      },
      error:(errorData)=>{
        console.error(errorData);
      } 
    })
  //////////////////////////
    this.estadistica.muestraIngresos().subscribe({
      next:(ingresos_S)=>{
        this.ingresos_admins=ingresos_S
      },
      error:(errorData)=>{
        console.error(errorData);
      } 
    })


  //////////////////////////
  //////////////////////////



  this.formPOST= this.formBuilder.group({

    id:["",Validators.required],
    nombre_servicio:["",Validators.required],
    descripcion_servicio:["",Validators.required],
    sede_servicio:["",Validators.required],
    precio_servicio:["",Validators.required],
    comentarios_servicio:["",Validators.required],
    prestador:["",Validators.required],

  })
  }
    ///// METODOS GET /////
    get id_GET(){
      return this.formPOST.controls['id'];
    }
    get nombre_servicio_GET(){
      return this.formPOST.controls['nombre_servicio'];
    }
    get descripcion_servicio_GET(){
      return this.formPOST.controls['descripcion_servicio'];
    }
    get sede_servicio_GET(){
      return this.formPOST.controls['sede_servicio'];
    }
    get precio_servicio_GET(){
      return this.formPOST.controls['precio_servicio'];
    }
    get comentarios_servicio_GET(){
      return this.formPOST.controls['comentarios_servicio'];
    }
    get prestador_GET(){
      return this.formPOST.controls['prestador'];
    }
    

  /////////////////////////////////
  //////////// POST //////////////
  ////////////////////////////////

  enviarDatos(){

    // SI EL FORMULARIO CUMPLE CON LA VALIDACION
    if(this.formPOST.valid){

          this.estadistica.POST('http://localhost:3000/registro_de_servicios',
            {
              id:this.formPOST.value.id,
              nombre_servicio:this.formPOST.value.nombre_servicio,
              descripcion_servicio:this.formPOST.value.descripcion_servicio,
              precio_servicio:this.formPOST.value.precio_servicio,
              comentarios_servicio:this.formPOST.value.comentarios_servicio,
              prestador:this.formPOST.value.prestador,
              sede_servicio:this.formPOST.value.sede_servicio,

            })
            .subscribe((respuesta: any) => {
              alert("Servicio Registrado")
            })
          }

          else{
            alert("Ingrese los datos correctamente")
        this.formPOST.markAllAsTouched();

          }
    
  }


  ///////// ///////////// /////////  
  respuesta:any=[];
  ///////// ///////////// /////////  




  ngOnInit():void{
    



  }




}
