import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class EstadisUsuariosService {
  url:string="http://localhost:3000/";

  constructor(private http:HttpClient) { }


  muestraNotas( ){

    return this.http.get(this.url+"notas_usuarios")
  }







}
