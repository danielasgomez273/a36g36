import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NavComponent } from './nav/nav.component';
import { FooterComponent } from './footer/footer.component';
import { Router, RouterModule } from '@angular/router';
import { PagesModule } from '../pages/pages.module';
import { InicioComponent } from '../pages/inicio/inicio.component';

// Importamos los componentes de pages


//const routes:Router[]



@NgModule({
  declarations: [
    NavComponent,
    FooterComponent
  ],
  imports: [
    CommonModule,
  //  RouterModule.forRoot( routes )
  ],
  exports:[
    NavComponent,
    FooterComponent,
    RouterModule

  ]
})
export class SharedModule { }
