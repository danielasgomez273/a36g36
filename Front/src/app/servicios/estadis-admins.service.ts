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

  muestraComorbilidades( ){

    return this.http.get(this.url+"estadisticas_comorbilidades_admins")
  }

  muestraServicios( ){

    return this.http.get(this.url+"serv_disponibles_admins")
  }


  muestraIngresos( ){

    return this.http.get(this.url+"ingresos_admins")
  }

}
