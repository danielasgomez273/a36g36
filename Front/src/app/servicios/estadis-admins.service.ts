import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class EstadisAdminsService {
  url:string="http://localhost:3000/";
  constructor(
    private http:HttpClient
  ) { }
  muestraEstadisticas( ){

    return this.http.get(this.url+"estadisticas_admins")
  }

}
