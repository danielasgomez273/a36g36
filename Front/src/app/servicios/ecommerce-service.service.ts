import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class EcommerceServiceService {

  constructor() { }
  muestraservicio( ){

    return[
      {nombre:"Consulta Diabetologo",
      descripcion:"Consulta con profesional en Diabetologia",
      monto:4000},
    
      {nombre:"Consulta Cardiologo",
      descripcion:"Consulta con profesional en Cardiologia",
      monto:4200},
    
      {nombre:"Paquete Completo",
      descripcion:"Contratacion del servicio completo",
      monto:12000},
    
      {nombre:"Analisis Clinico",
      descripcion:"Cita para extraccion de sangre",
      monto:4000}]
  }
}

