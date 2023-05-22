import { Component, OnInit } from '@angular/core';
import { EstadisAdminsService } from 'src/app/servicios/estadis-admins.service';



@Component({
  selector: 'app-dashboard-admin',
  templateUrl: './dashboard-admin.component.html',
  styleUrls: ['./dashboard-admin.component.css']
})
export class DashboardAdminComponent {

  estadisticas_admins:any
  comorbilidades_admins: any;
  servicios_admins:any;
  ingresos_admins: any;


  constructor(private estadistica:EstadisAdminsService){
    this.estadistica.muestraEstadisticas().subscribe({
      next:(estadisticas_S)=>{
        this.estadisticas_admins=estadisticas_S
      },
      error:(errorData)=>{
        console.error(errorData);
      } 
    })

    this.estadistica.muestraComorbilidades().subscribe({
      next:(comorbilidades_S)=>{
        this.comorbilidades_admins=comorbilidades_S
      },
      error:(errorData)=>{
        console.error(errorData);
      } 
    })

    this.estadistica.muestraServicios().subscribe({
      next:(servicio_S)=>{
        this.servicios_admins=servicio_S
      },
      error:(errorData)=>{
        console.error(errorData);
      } 
    })

    this.estadistica.muestraIngresos().subscribe({
      next:(ingresos_S)=>{
        this.ingresos_admins=ingresos_S
      },
      error:(errorData)=>{
        console.error(errorData);
      } 
    })

    



  }
  ngOnInit():void{}




}
