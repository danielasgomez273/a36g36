import { Component, OnInit } from '@angular/core';
import { EstadisUsuariosService } from 'src/app/servicios/estadis-usuarios.service';


@Component({
  selector: 'app-dashboard-usuario',
  templateUrl: './dashboard-usuario.component.html',
  styleUrls: ['./dashboard-usuario.component.css']
})
export class DashboardUsuarioComponent implements OnInit {


  notas_usuarios: any;
  servicios: any;
  constructor(private usuario:EstadisUsuariosService){
  this.usuario.muestraNotas().subscribe({
    next:(notas_S)=>{
      this.notas_usuarios=notas_S
    },
    error:(errorData)=>{
      console.error(errorData);
    } 
  })
  this.usuario.muestraservicioausuario().subscribe({
    next:(servicios_S)=>{
      this.servicios=servicios_S
    },
    error:(errorData)=>{
      console.error(errorData);
    }
    
  }
     )

} 
///////  CODIGO PARA AGREGAR AL CARRITO  ////////
Snombre:string=""
agregarNombre(value:string){
  this.Snombre=value

  return this.Snombre
}

Smonto:string=""
agregarMonto(value2:string){
  this.Smonto=value2
  return this.Smonto
}

nuevoPedido:any[]=[]
nuevoServicio:any[]=[]

nuevoCarrito(){
  /* La idea es guardar en un array los servicios que se van selccionando */ 
  this.nuevoServicio.push(this.Snombre)
  this.nuevoServicio.push(this.Smonto)

  this.nuevoPedido.push(this.nuevoServicio)

  return this.nuevoPedido
}
  ngOnInit(): void {
    throw new Error('Method not implemented.');
  }










}
