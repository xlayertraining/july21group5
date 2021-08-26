import { Component, OnInit } from '@angular/core'
import { Router } from '@angular/router';
import { LoginService } from './login.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
  providers: [LoginService]
})
export class LoginComponent implements OnInit {
  password: any;
  user_id: any;
  constructor(private service: LoginService, private router: Router) { }

  ngOnInit() {
  }
  onSave(): void {
    const body ={
      'email': this.user_id,
      'password': this.password

    }
    this.service.postSignIn(body).subscribe(sucsess => {
      console.log(sucsess);
      if(sucsess.status){
        alert('login successfull ')
      }
    });
    console.log(this.password, this.user_id, body)
  }
}