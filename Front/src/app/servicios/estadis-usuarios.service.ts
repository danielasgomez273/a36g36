import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';


// INTERFACE DE NOTAS USUARIO
import { NotasGlucemia } from './interfaces/notas-glucemia';


@Injectable({
  providedIn: 'root'
})
export class EstadisUsuariosService {
  
  // BACK => 'http://127.0.0.1:8000/api/paciente/registros_glucemia/';
  /////////////////////////////////////////////////
  constructor(
    private http:HttpClient) { }


    
    
  //////////////////////////////////////////////////////


  ///////////////////////////////////////////////////
  ////////////////// CODIGO NOTAS ///////////////////
  ///////////////////////////////////////////////////
  //// MUESTRA LAS NOTAS  
  // BACK => 'http://localhost:8000/api/paciente/registros_glucemia/';
  url_NOTAS:string='http://localhost:8000/api/paciente/registros_glucemia/';

  muestraNotasUsuario( ){
    return this.http.get(this.url_NOTAS, {withCredentials: true})
  }


  //// AGREGA NOTAS
  nuevaNota(url:string, datos: any){
    return this.http.post(url,datos, {withCredentials: true});
  }


  //// MODIFICAR NOTAS
  // metodo para TRAER la informacion
  modificar(id:number){
    return this.http.get(this.url_NOTAS+id , {withCredentials: true})

  }

  // metodo para MODIFICAR la informacion
  modificar2(datos:any, id:number){
    return this.http.put(this.url_NOTAS+id,datos , {withCredentials: true})

  }

  // metodo para ELIMINAR la informacion
  DELETE(id:string){
    return this.http.delete("http://localhost:8000/api/paciente/registros_glucemia/"+id , {withCredentials: true})
  }



 

  /////////////////////////////////////////////////////////
  ////////////////// CODIGO DEL CARRITO ///////////////////
  /////////////////////////////////////////////////////////

  //// MUESTRA LOS SERVICIOS DISPONIBLES A LOS USUARIOS ////

  // BACK => url_SERVICIOS:string='http://localhost:8000/api/paciente/servicios/';
  // FRONT => 
  url_SERVICIOS:string='http://localhost:8000/api/paciente/servicios/';
  muestraServicioAUsuario( ){
    return this.http.get<NotasGlucemia[]>(this.url_SERVICIOS, {withCredentials: true})
  }

  //// MUESTRA CARRITO USUARIOS ////

  // BACK => 'http://localhost:8000/api/paciente/carrito/'
  // FRONT => 'http://localhost:3000/CARRITO/'
  muestraCarritoAUsuario( ){
    return this.http.get('http://localhost:8000/api/paciente/carrito/', {withCredentials: true})
  }

  //// ELIMINAR SERVICIO DE CARRITO USUARIOS ////

  // BACK => 'http://localhost:8000/api/paciente/carrito/'
  // FRONT => 'http://localhost:3000/CARRITO/'
  DELETE_SERV(id:string){
    return this.http.delete('http://localhost:8000/api/paciente/carrito/'+id , {withCredentials: true})
  }


}
