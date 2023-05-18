import { Component } from '@angular/core';
import { EcommerceServiceService } from 'src/app/servicios/ecommerce-service.service';
@Component({
  selector: 'app-soporte',
  templateUrl: './soporte.component.html',
  styleUrls: ['./soporte.component.css']
})
export class SoporteComponent {
servicios: { nombre: string; descripcion: string; monto: number; }[];
constructor (servicio:EcommerceServiceService){
  this.servicios=servicio.muestraservicio()
}
ngOnInit(): void{}

}
