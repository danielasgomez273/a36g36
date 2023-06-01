import { TestBed } from '@angular/core/testing';

import { FormContactoService } from './form-contacto.service';

describe('FormContactoService', () => {
  let service: FormContactoService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(FormContactoService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
