import { NgModule } from '@angular/core';
import { CommonModule, } from '@angular/common';
import { BrowserModule  } from '@angular/platform-browser';
import { RouterModule, Routes } from '@angular/router';

import {HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { SignupComponent } from './signup/signup.component';


 
import { SignInComponent } from './components/sign-in/sign-in.component';
import { SignUpComponent } from './components/sign-up/sign-up.component';
import { UserProfileComponent } from './components/user-profile/user-profile.component';
const routes: Routes = [
  {
    path: '',
    component: SignInComponent
  },
  {
    path: 'sign_in',
    component: SignInComponent
  },
  {
    path: 'sign_up',
    component: SignUpComponent
  },
  {
    path: 'user_profile',
    component: UserProfileComponent
  }
  

];

@NgModule({
  imports: [
    CommonModule,
    BrowserModule,
    RouterModule.forRoot(routes,{
      useHash: true
    })
  ],
  exports: [
    ],
})
export class AppRoutingModule { }
