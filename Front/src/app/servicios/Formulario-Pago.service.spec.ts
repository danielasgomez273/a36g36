/* tslint:disable:no-unused-variable */

import { TestBed, async, inject } from '@angular/core/testing';
import { FormularioPagoService } from './Formulario-Pago.service';

describe('Service: FormularioPago', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [FormularioPagoService]
    });
  });

  it('should ...', inject([FormularioPagoService], (service: FormularioPagoService) => {
    expect(service).toBeTruthy();
  }));
});
