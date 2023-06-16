import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class EstadisAdminsService {
  url:string="http://localhost:8000/";

  /////////////////////////////////////
  constructor(
    private http:HttpClient
  ) { }
  
  /////////////////////////////////////
  muestraEstadisticas( ){

    // COMENTE ESTO PARA QUE NO ME SALTEN ERROES EXTENOS

   // COMENTE ESTO PARA QUE NO ME SALTEN ERROES EXTENOS 
    return this.http.get(this.url+"estadisticas_admins", {withCredentials: true})
  }

  /////////////////////////////////////
  muestraComorbilidades( ){
// COMENTE ESTO PARA QUE NO ME SALTEN ERROES EXTENOS
   // COMENTE ESTO PARA QUE NO ME SALTEN ERROES EXTENOS 
   return this.http.get(this.url+"estadisticas_comorbilidades_admins", {withCredentials: true})
  }


  /////////////////////////////////////
  muestraServicios( ){
<<<<<<< HEAD
    return this.http.get(this.url+"api/admin/servicios/", {withCredentials: true})
=======
// COMENTE ESTO PARA QUE NO ME SALTEN ERROES EXTENOS
return this.http.get(this.url+"api/admin/servicios/", {withCredentials: true})
>>>>>>> d3173a4957530aed588b65dc37bc924f2e9266d2
  }


  /////////////////////////////////////
  muestraIngresos( ){

    return this.http.get(this.url+"ingresos_admins", {withCredentials: true})
  }

  /////////////////////////////////////
  //          SERVICIO POST          //
  /////////////////////////////////////

  POSTRegistroServicio(urlPOST:string, body: any ){
     return this.http.post(urlPOST,body, {withCredentials: true})
  }


}
