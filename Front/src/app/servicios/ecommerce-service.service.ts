import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class EcommerceServiceService {
  url:string="http://localhost:3000/";
  constructor( private http:HttpClient ) { }

  // metodo GET para traer los servicios
  muestraservicio( ){

    return this.http.get(this.url+"SERVICIOS")
  }
}

