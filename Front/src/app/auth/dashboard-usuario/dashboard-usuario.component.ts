import { Component } from '@angular/core';
import { EstadisUsuariosService } from 'src/app/servicios/estadis-usuarios.service';
import { LoginService } from 'src/app/servicios/login.service';

@Component({
  selector: 'app-dashboard-usuario',
  templateUrl: './dashboard-usuario.component.html',
  styleUrls: ['./dashboard-usuario.component.css']
})
export class DashboardUsuarioComponent {


  notas_usuarios: any;
  constructor(private notas:EstadisUsuariosService , private log :LoginService){
  this.notas.muestraNotas().subscribe({
    next:(notas_S)=>{
      this.notas_usuarios=notas_S
    },
    error:(errorData)=>{
      console.error(errorData);
    } 
  })

  // una vez que el login.component setea la cookie, deberia poder accederla desde aca y saber que efectivamente el usuario esta logueado...
  console.log("log.getToken()", log.getToken(), "--")
}










}
