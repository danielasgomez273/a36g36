import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

// Importamos modulos
import { ServiciosCompComponent } from './servicios-comp/servicios-comp.component';

// Iportamos Router Module
import { RouterModule, Routes } from '@angular/router';


const routes:Routes=[
  {path:'',
    children:[
        {path:'servicios', component:ServiciosCompComponent},

        {path:'**', redirectTo:'servicios'}

    ]
}
]


@NgModule({
  declarations: [

  ],
  imports: [
    CommonModule,
    RouterModule.forChild(routes)
  ]
})
export class EcommerceRoutingModule { }

