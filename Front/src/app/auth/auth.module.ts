import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LoginComponent } from './login/login.component';
import { RegistroComponent } from './registro/registro.component';
import { AuthRoutingModule } from './auth-routing.module';
import { RouterModule } from '@angular/router';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { DashboardUsuarioComponent } from './dashboard-usuario/dashboard-usuario.component';
import { DashboardAdminComponent } from './dashboard-admin/dashboard-admin.component';
import { Registro2usuarioComponent } from './registro2usuario/registro2usuario.component';





@NgModule({
  declarations: [
    LoginComponent,
    RegistroComponent,
    DashboardUsuarioComponent,
    DashboardAdminComponent,
    Registro2usuarioComponent
  ],
  imports: [
    CommonModule,
    AuthRoutingModule,
    ReactiveFormsModule,
    FormsModule,
    RouterModule
  ],
  exports:[
    RouterModule
  ]
})
export class AuthModule { }
