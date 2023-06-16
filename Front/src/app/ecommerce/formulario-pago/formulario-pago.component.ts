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
  formPOSTPago: FormGroup | any;

  ////////////////////////////////////////////////////////////
  constructor(
    private formBuilder: FormBuilder,
    private router: Router,
    private serv_pago:FormPagoService
  ) {}

  ngOnInit(): void {
    this.formPOSTPago = this.formBuilder.group({
  
      email: ['', [Validators.required, Validators.email]],
      pass: ['', [Validators.required, Validators.minLength(9)]],
      username: ['', [Validators.required]]
    });
  }

  //////////////////////////////////////////////////////////

  get email_GET() {
    return this.formPOSTPago.get('email');
  }
  
  get pass_GET() {
    return this.formPOSTPago.get('pass');
  }
  
  get username_GET() {
    return this.formPOSTPago.get('username');
  }

  enviarDatosFormPago() {
    if (this.formPOSTPago.valid) {
      this.serv_pago
        .POSTFormularioPago('http://127.0.0.1:8000/api/auth/signup/', {
          email: this.formPOSTPago.value.email,
          password: this.formPOSTPago.value.pass,
          username: this.formPOSTPago.value.username,
        })
        .subscribe((respuesta: any) => {});

      this.router.navigateByUrl('/auth/dash_user');
      this.formPOSTPago.reset();
    } else {
      this.formPOSTPago.markAllAsTouched();
      alert('No se ingresaron correctamente los datos');
    }
  }
}
