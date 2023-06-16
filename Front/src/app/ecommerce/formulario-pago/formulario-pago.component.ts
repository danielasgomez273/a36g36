import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { FormularioPagoService } from 'src/app/servicios/Formulario-Pago.service';

@Component({
  selector: 'app-formulario-pago',
  templateUrl: './formulario-pago.component.html',
  styleUrls: ['./formulario-pago.component.css']
})
export class FormularioPagoComponent implements OnInit {
  formPOSTFormularioPago!: FormGroup;

  constructor(
    private formBuilder: FormBuilder,
    private router: Router,
    private serv_registro: FormularioPagoService
  ) {}

  ngOnInit(): void {
    this.formPOSTFormularioPago = this.formBuilder.group({
      id: [],
      email: ['', [Validators.required, Validators.email]],
      pass: ['', [Validators.required, Validators.minLength(9)]],
      username: ['', [Validators.required]]
    });
  }

  get email_GET() {
    return this.formPOSTFormularioPago.get('email');
  }
  
  get pass_GET() {
    return this.formPOSTFormularioPago.get('pass');
  }
  
  get username_GET() {
    return this.formPOSTFormularioPago.get('username');
  }

  enviarDatosRegistroInicial() {
    if (this.formPOSTFormularioPago.valid) {
      this.serv_registro
        .POSTFormularioPago('http://127.0.0.1:8000/api/auth/signup/', {
          email: this.formPOSTFormularioPago.value.email,
          password: this.formPOSTFormularioPago.value.pass,
          username: this.formPOSTFormularioPago.value.username,
        })
        .subscribe((respuesta: any) => {});

      this.router.navigateByUrl('/auth/registro2usuario');
      this.formPOSTFormularioPago.reset();
    } else {
      this.formPOSTFormularioPago.markAllAsTouched();
      alert('No se ingresaron correctamente los datos');
    }
  }
}
