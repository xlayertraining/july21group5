import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
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
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
