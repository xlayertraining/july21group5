import { NgModule } from '@angular/core';
import { CommonModule, } from '@angular/common';
import { BrowserModule  } from '@angular/platform-browser';
import { RouterModule, Routes } from '@angular/router';

import { LoginComponent } from './login/login.component';
import { SignupComponent } from './signup/signup.component';


 
import { SignInComponent } from './components/sign-in/sign-in.component';
import { SignUpComponent } from './components/sign-up/sign-up.component';
import { UserProfileComponent } from './components/user-profile/user-profile.component';
import { HomeComponent } from './components/home/home.component';
import { ApplyForJobComponent } from './components/apply-for-job/apply-for-job.component';
import { OfferJobComponent } from './components/offer-job/offer-job.component';
import { SettingsComponent } from './components/settings/settings.component';
import { SubmitApplicationComponent } from './components/submit-application/submit-application.component';
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
  },
  {
    path: 'home',
    component: HomeComponent
  },
  {
    path: 'apply_for_job',
    component: ApplyForJobComponent
  },
  {
    path: 'offer_jon',
    component: OfferJobComponent
  },
  {
    path: 'settings',
    component: SettingsComponent
  },
  {
    path: 'submit_application',
    component: SubmitApplicationComponent
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
