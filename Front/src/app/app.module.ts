import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';

//Modulo para el ruteo
import { AppRoutingModule } from './app-routing.module';
//Importamos modulos
import { SharedModule } from './shared/shared.module';
import { PagesModule } from './pages/pages.module';
import { EcommerceModule } from './ecommerce/ecommerce.module';




@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    SharedModule,
    PagesModule,
    EcommerceModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }