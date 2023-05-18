import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-servicios-comp',
  templateUrl: './servicios-comp.component.html',
  styleUrls: ['./servicios-comp.component.css']
})
export class ServiciosCompComponent implements OnInit {
  servicios_S=[
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

    constructor(){}
    ngOnInit(){}
}


