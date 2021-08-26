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

import { AppRoutingModule } from './app-routing.module';

import { SignInComponent } from './components/sign-in/sign-in.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatFormFieldModule } from '@angular/material/form-field';

import { MatInputModule } from '@angular/material/input';
import { FlexLayoutModule } from '@angular/flex-layout';
import { SignUpComponent } from './components/sign-up/sign-up.component';
import {MatButtonModule} from '@angular/material/button';
// import { UserProfileComponent } from './components/user-profile/user-profile.component';


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

    SignInComponent,
    SignUpComponent,
    // UserProfileComponent,
  ],
  
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {

  constructor(private router: Router) {

    // this.router.navigate(['sign_in']);

  }

}
