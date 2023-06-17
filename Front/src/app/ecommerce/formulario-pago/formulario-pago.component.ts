import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { FormPagoService } from 'src/app/servicios/form-pago.service';

@Component({
  selector: 'app-formulario-pago',
  templateUrl: './formulario-pago.component.html',
  styleUrls: ['./formulario-pago.component.css']
})
export class FormularioPagoComponent implements OnInit {
  formPOSTPago!: FormGroup;

  constructor(
    private formBuilder: FormBuilder,
    private router: Router,
    private serv_pago: FormPagoService
  ) {}

  ngOnInit(): void {
    this.formPOSTPago = this.formBuilder.group({
      tarjeta: ['', [Validators.required, Validators.pattern('^[0-9]{16}$')]],
      titular: ['', [Validators.required]],
      vencimiento: ['', [Validators.required, Validators.pattern('^(0[1-9]|1[0-2])\/(20[2-9][0-9])$')]],
      codigoSeguridad: ['', [Validators.required, Validators.pattern('^[0-9]{3}$')]],
      dniTitular: ['', [Validators.required, Validators.pattern('^[0-9]+$')]],
    });
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
      this.serv_pago
        .POSTFormularioPago('http://127.0.0.1:8000/api/auth/signup/', {
          tarjeta: this.formPOSTPago.value.tarjeta,
          titular: this.formPOSTPago.value.titular,
          vencimiento: this.formPOSTPago.value.vencimiento,
          codigoSeguridad: this.formPOSTPago.value.codigoSeguridad,
          dniTitular: this.formPOSTPago.value.dniTitular,
        })
        .subscribe((respuesta: any) => {});

      // Redireccionar al siguiente componente después de la compra
      this.formPOSTPago.markAllAsTouched();
      alert('Felicitaciones! Tu compra ha sido completada');
    } else {
      this.formPOSTPago.markAllAsTouched();
      alert('No se ingresaron correctamente los datos');
    }
  }
  validarNumeros(event: any) {
    const pattern = /^[0-9]*$/;
    const inputChar = String.fromCharCode(event.charCode);
    if (!pattern.test(inputChar)) {
      event.preventDefault();
    }
  }
}

