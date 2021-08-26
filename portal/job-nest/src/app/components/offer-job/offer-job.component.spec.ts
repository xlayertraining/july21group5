import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OfferJobComponent } from './offer-job.component';

describe('OfferJobComponent', () => {
  let component: OfferJobComponent;
  let fixture: ComponentFixture<OfferJobComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ OfferJobComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(OfferJobComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
