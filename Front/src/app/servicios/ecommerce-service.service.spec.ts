import { TestBed } from '@angular/core/testing';

import { EcommerceServiceService } from './ecommerce-service.service';

describe('EcommerceServiceService', () => {
  let service: EcommerceServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(EcommerceServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
