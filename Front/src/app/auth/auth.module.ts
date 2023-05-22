import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LoginComponent } from './login/login.component';
import { RegistroComponent } from './registro/registro.component';
import { AuthRoutingModule } from './auth-routing.module';
import { RouterModule } from '@angular/router';
import { ReactiveFormsModule } from '@angular/forms';
import { DashboardUsuarioComponent } from './dashboard-usuario/dashboard-usuario.component';
import { DashboardAdminComponent } from './dashboard-admin/dashboard-admin.component';




@NgModule({
  declarations: [
    LoginComponent,
    RegistroComponent,
    DashboardUsuarioComponent,
    DashboardAdminComponent
  ],
  imports: [
    CommonModule,
    AuthRoutingModule,
    ReactiveFormsModule
  ],
  exports:[
    RouterModule
  ]
})
export class AuthModule { }
