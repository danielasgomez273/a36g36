import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { FormPagoService } from 'src/app/servicios/form-pago.service';
import { EstadisUsuariosService } from 'src/app/servicios/estadis-usuarios.service';


@Component({
  selector: 'app-formulario-pago',
  templateUrl: './formulario-pago.component.html',
  styleUrls: ['./formulario-pago.component.css']
})
export class FormularioPagoComponent implements OnInit {
  formPOSTPago!: FormGroup;
  mostrarMensajeExito: boolean = false;
  serviciosCarrito: any;
  items: any;

  constructor(
    private formBuilder: FormBuilder,
    private router: Router,
    private serv_pago: FormPagoService,
    private paciente: EstadisUsuariosService,

  ) {}

  ngOnInit(): void {
    this.formPOSTPago = this.formBuilder.group({
      tarjeta: ['', [Validators.required, Validators.pattern('^[0-9]{16}$')]],
      titular: ['', [Validators.required]],
      vencimiento: ['', [Validators.required, Validators.pattern('^(0[1-9]|1[0-2])\/(20[2-9][0-9])$')]],
      codigoSeguridad: ['', [Validators.required, Validators.pattern('^[0-9]{3}$')]],
      dniTitular: ['', [Validators.required, Validators.pattern('^[0-9]+$')]],
    });



    // Codigo que muestra los servicios (instancia)
    this.paciente.muestraCarritoAUsuario().subscribe({
      next:(item)=>{
        this.items=item
      },
      error:(errorData)=>{
        console.error(errorData);
      } 
    })    



  }

  get tarjeta_GET() {
    return this.formPOSTPago.get('tarjeta');
  }

  get titular_GET() {
    return this.formPOSTPago.get('titular');
  }

  get vencimiento_GET() {
    return this.formPOSTPago.get('vencimiento');
  }

  get codigoSeguridad_GET() {
    return this.formPOSTPago.get('codigoSeguridad');
  }

  get dniTitular_GET() {
    return this.formPOSTPago.get('dniTitular');
  }

  enviarDatosFormPago() {
    if (this.formPOSTPago.valid) {
      alert('Felicitaciones. Tu compra se realizó con éxito.');

      this.mostrarMensajeExito = true;

      setTimeout(() => {
        this.mostrarMensajeExito = false;
        this.router.navigateByUrl('/auth/dash_user');
      }, 3000);
    }
  }

  validarNumeros(event: any) {
    const pattern = /^[0-9]*$/;
    const inputChar = String.fromCharCode(event.charCode);
    if (!pattern.test(inputChar)) {
      event.preventDefault();
    }
  }


////////////  METODOS QUE TRAEN SERVICIOS  ///////////

  getCarrito(){
    this.paciente.muestraCarritoAUsuario().subscribe({
      next: (servicios_C) => {
        this.serviciosCarrito = servicios_C;
      },
      error: (errorData) => {
        console.error(errorData);
      }
    });
    }
}
