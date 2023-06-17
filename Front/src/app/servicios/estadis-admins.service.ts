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
// COMENTE ESTO PARA QUE NO ME SALTEN ERROES EXTENOS
// this.url+"api/admin/servicios/"
    return this.http.get("http://localhost:3000/SERVICIOS" , {withCredentials: true})

  }


  /////////////////////////////////////
  muestraIngresos( ){

    return this.http.get(this.url+"ingresos_admins", {withCredentials: true})
  }

  /////////////////////////////////////
  //          SERVICIO POST          //
  /////////////////////////////////////

  POSTRegistroServicio(urlPOST:string, body: any){
    
      return this.http.post(urlPOST,body)

  }

    // metodo para ELIMINAR la informacion
    DELETE(id:string){
      return this.http.delete("http://localhost:3000/SERVICIOS/"+id)
  
    }

  //// MODIFICAR SERVICIOS
  // metodo para TRAER la informacion
  url_SERVICIOS:string='http://localhost:3000/SERVICIOS/';


  modificar(id:number){
    return this.http.get(this.url_SERVICIOS+id)

  }

  // metodo para MODIFICAR la informacion
  modificar2(datos:any, id:number){
    return this.http.put(this.url_SERVICIOS+id,datos)

  }



}
