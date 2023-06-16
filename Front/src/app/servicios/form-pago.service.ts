import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class FormPagoService {
 

  constructor( private http:HttpClient ) { }
  
  
  email_string:string=""

  /////////////////////////////////////
  //          SERVICIO POST          //
  /////////////////////////////////////

  POSTFormularioPago(urlPOST:string, body: any){
    return this.http.post(urlPOST,body)
}










  // CIERRA EXPORT


  }
