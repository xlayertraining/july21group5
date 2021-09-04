import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  constructor(private router: Router) { }

  ngOnInit(): void {
  }

  onSignOut(): void {
    localStorage.clear();
    this.router.navigate(['sign_in']);
  }

  onOfferJob(): void {
    this.router.navigate(['offer_job']);
  }

  onApplyJob(): void {
    this.router.navigate(['apply_for_job']);
  }

}
