import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule, NgModel } from '@angular/forms';
import { Router, Routes, RouterModule } from '@angular/router'
import { HttpClientModule } from '@angular/common/http';
import { AppComponent } from './app.component'
import { AppRoutingModule } from './app-routing.module';
import { SignInComponent } from './components/sign-in/sign-in.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { FlexLayoutModule } from '@angular/flex-layout';
import { SignUpComponent } from './components/sign-up/sign-up.component';
import { MatButtonModule } from '@angular/material/button';
import { UserProfileComponent } from './components/user-profile/user-profile.component';
import { HomeComponent } from './components/home/home.component';
import { MatIconModule } from '@angular/material/icon';
import { ApplyForJobComponent } from './components/apply-for-job/apply-for-job.component';
import {MatToolbarModule} from '@angular/material/toolbar';
import { SettingsComponent } from './components/settings/settings.component';
import { SubmitApplicationComponent } from './components/submit-application/submit-application.component';
import { OfferJobComponent } from './components/offer-job/offer-job.component';
import {MatSelectModule} from '@angular/material/select';
import {MatTooltipModule} from '@angular/material/tooltip';

@NgModule({

  declarations: [
    AppComponent,
    HomeComponent,
    SignInComponent,
    SignUpComponent,
    UserProfileComponent,
    ApplyForJobComponent,
    SettingsComponent,
    SubmitApplicationComponent,
    OfferJobComponent,
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule,
    BrowserAnimationsModule,
    FlexLayoutModule,
    AppRoutingModule,
    RouterModule,
    MatIconModule,
    MatToolbarModule,
    MatSelectModule,
    HttpClientModule,
    MatTooltipModule,  
  ],

  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {

  constructor(private router: Router) {

    // this.router.navigate(['sign_in']);

  }

}
