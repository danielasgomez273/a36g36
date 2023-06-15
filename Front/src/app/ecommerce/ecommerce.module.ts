import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

// Importamos ls componentes
import { ServiciosCompComponent } from './servicios-comp/servicios-comp.component';

// Importamos el modulo de router module
import { RouterModule } from '@angular/router';
import { EcommerceRoutingModule } from './ecommerce-routing.module';
import { formulariopagoComponent } from './formulario-pago/formulario-pago.component';








@NgModule({
  declarations: [
    ServiciosCompComponent,
    formulariopagoComponent
  ],
  imports: [
    CommonModule,
    EcommerceRoutingModule
    
  ],
  exports:[
    ServiciosCompComponent,
    RouterModule
  ]
})
export class EcommerceModule { }
