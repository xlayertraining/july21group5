import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule, NgModel } from '@angular/forms';
import { Router, Routes, RouterModule } from '@angular/router'
import { HttpClientModule } from '@angular/common/http';
import { AppComponent } from './app.component'
import { LoginComponent } from './login/login.component';
import { SignupComponent } from './signup/signup.component';
import { HomeComponent } from './home/home.component';

const routes: Routes = [
  {
    path: 'sign_in',
    component: LoginComponent,
  },
  // {
    // path: 'table/grievance-info-dialog',
    // component: GrievanceInfoDialogComponent
    // }
];
@NgModule({

  declarations: [
    AppComponent,
    LoginComponent,
    SignupComponent,
    HomeComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    RouterModule.forRoot(routes),
    HttpClientModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
