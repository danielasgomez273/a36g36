import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LoginComponent } from './login/login.component';
import { RegistroComponent } from './registro/registro.component';
import { RouterModule , Routes} from '@angular/router';
import { DashboardAdminComponent } from './dashboard-admin/dashboard-admin.component';
import { DashboardUsuarioComponent } from './dashboard-usuario/dashboard-usuario.component';
import { Registro2usuarioComponent } from './registro2usuario/registro2usuario.component';
import { Registro3usuarioComponent } from './registro3usuario/registro3usuario.component';


// RUTAS EXPORTADAS AL NAV
const routes:Routes=[
  {path:'',
    children:[
        {path:'login', component:LoginComponent},
        {path:'registrarse', component:RegistroComponent},
        {path:'dash_admin', component:DashboardAdminComponent},
        {path:'dash_user', component:DashboardUsuarioComponent},
        {path:'registro2usuario', component:Registro2usuarioComponent},
        {path:'registro3usuario', component:Registro3usuarioComponent},



        {path:'**', redirectTo:'login'}

    ]
}
]

@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    RouterModule.forChild(routes)
  ]
})
export class AuthRoutingModule { }
