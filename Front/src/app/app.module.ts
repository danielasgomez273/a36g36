import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';

//Modulo para el ruteo
import { AppRoutingModule } from './app-routing.module';
//Importamos modulos
import { SharedModule } from './shared/shared.module';
import { PagesModule } from './pages/pages.module';
import { EcommerceModule } from './ecommerce/ecommerce.module';
import { HttpClientModule } from '@angular/common/http'
import { ReactiveFormsModule } from '@angular/forms';

import { RouterModule } from '@angular/router';
import { EcommerceServiceService } from './servicios/ecommerce-service.service';
import { LoginComponent } from './auth/login/login.component';
import { RegistroComponent } from './auth/registro/registro.component';
import { FormContactoService } from './servicios/form-contacto.service';





@NgModule({
  declarations: [
    AppComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    SharedModule,
    PagesModule,
    EcommerceModule,
    HttpClientModule,
    ReactiveFormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

