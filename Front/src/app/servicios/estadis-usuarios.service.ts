import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class EstadisUsuariosService {
  
  url:string='http://127.0.0.1:8000/api/paciente/registros_glucemia/';

  constructor(private http:HttpClient) { }


  muestraNotas( ){

    return this.http.get(this.url)
  }

}
