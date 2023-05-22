import { TestBed } from '@angular/core/testing';

import { EstadisAdminsService } from './estadis-admins.service';

describe('EstadisAdminsService', () => {
  let service: EstadisAdminsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(EstadisAdminsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
