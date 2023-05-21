import { Component, OnInit } from '@angular/core';
import { EstadisAdminsService } from 'src/app/servicios/estadis-admins.service';



@Component({
  selector: 'app-dashboard-admin',
  templateUrl: './dashboard-admin.component.html',
  styleUrls: ['./dashboard-admin.component.css']
})
export class DashboardAdminComponent {

  estadisticas_admins:any


  constructor(private estadistica:EstadisAdminsService){
    this.estadistica.muestraEstadisticas().subscribe({
      next:(estadisticas_S)=>{
        this.estadisticas_admins=estadisticas_S
      },
      error:(errorData)=>{
        console.error(errorData);
      }
      
    }
       )
  }
  ngOnInit():void{}




}
