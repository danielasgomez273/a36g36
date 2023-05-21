import { TestBed } from '@angular/core/testing';

import { EstadisUsuariosService } from './estadis-usuarios.service';

describe('EstadisUsuariosService', () => {
  let service: EstadisUsuariosService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(EstadisUsuariosService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
