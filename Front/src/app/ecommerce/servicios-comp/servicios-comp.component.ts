import { Component, OnInit } from '@angular/core';
import { EcommerceServiceService } from 'src/app/servicios/ecommerce-service.service';

@Component({
  selector: 'app-servicios-comp',
  templateUrl: './servicios-comp.component.html',
  styleUrls: ['./servicios-comp.component.css']
})
export class ServiciosCompComponent implements OnInit {
  servicios:any


    constructor(private servicio:EcommerceServiceService){
      this.servicio.muestraservicio().subscribe({
        next:(servicios_S)=>{
          this.servicios=servicios_S
        },
        error:(errorData)=>{
          console.error(errorData);
        }
        
      }
         )
    }
    ngOnInit():void{}
}


