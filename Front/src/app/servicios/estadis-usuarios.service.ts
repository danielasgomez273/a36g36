import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

// INTERFACE DE NOTAS USUARIO
import { NotasGlucemia } from './interfaces/notas-glucemia';


@Injectable({
  providedIn: 'root'
})
export class EstadisUsuariosService {
  
  // url:string='http://127.0.0.1:8000/api/paciente/registros_glucemia/';
  /////////////////////////////////////////////////
  constructor(
    private http:HttpClient) { }


    
    
  //////////////////////////////////////////////////////

  //// AGREGA NOTAS
    nuevaNota(url:string, datos: any){
      return this.http.post(url,datos);
    }





  //// MUESTRA LAS NOTAS  
  url_NOTAS:string='http://localhost:3000/notas_usuarios';
  muestraNotasUsuario( ){
    return this.http.get(this.url_NOTAS)
  }


  ///////////////////////////////////////////////////////////
  //// MUESTRA LOS SERVICIOS DISPONIBLES A LOS USUARIOS ////
  url_SERVICIOS:string='http://localhost:3000/SERVICIOS';
  muestraServicioAUsuario( ){
    return this.http.get<NotasGlucemia[]>(this.url_SERVICIOS)
  }



}
