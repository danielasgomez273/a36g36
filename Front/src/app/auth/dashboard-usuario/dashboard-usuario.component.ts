import { Component } from '@angular/core';
import { EstadisUsuariosService } from 'src/app/servicios/estadis-usuarios.service';


@Component({
  selector: 'app-dashboard-usuario',
  templateUrl: './dashboard-usuario.component.html',
  styleUrls: ['./dashboard-usuario.component.css']
})
export class DashboardUsuarioComponent {


  notas_usuarios: any;
  constructor(private notas:EstadisUsuariosService){
  this.notas.muestraNotas().subscribe({
    next:(notas_S)=>{
      this.notas_usuarios=notas_S
    },
    error:(errorData)=>{
      console.error(errorData);
    } 
  })

}










}