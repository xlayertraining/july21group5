import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { NetworkService } from 'src/app/service/network.service';
import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-offer-job',
  templateUrl: './offer-job.component.html',
  styleUrls: ['./offer-job.component.scss'],
  providers: [NetworkService]
})
export class OfferJobComponent implements OnInit {
  designation: String = '';
  companyName: String = '';
  description: String = '';
  minimumQualification: String = '';
  preferredQualification: String = '';
  salary: String = '';
  accountId: String = '';
  location: String = '';
  remoteJob: String = '';

  constructor(private networkService: NetworkService, private router: Router) { }

  ngOnInit(): void {
  }

  onOfferJobPost(): void {

    // validation

    if (this.designation.length == 0) {
      alert('Please enter valid designation.');
      return;
    }

    if (this.companyName.length == 0) {
      alert('Please enter valid companyName.');
      return;
    }
    if (this.description.length == 0) {
      alert('Please enter valid description.');
      return;
    }

    if (this.minimumQualification.length == 0) {
      alert('Please enter valid minimumQualification.');
      return;
    }
    
    if (this.preferredQualification.length == 0) {
      alert('Please enter valid preferredQualification.');
      return;
    }

    if (this.salary.length == 0) {
      alert('Please enter valid salary.');
      return;
    }

    if (this.accountId.length == 0) {
      alert('Please enter valid accountId.');
      return;
    }

    if (this.location.length == 0) {
      alert('Please enter valid location.');
      return;
    }

    if (this.remoteJob.length == 0) {
      alert('Please enter valid option for remoteJob.');
      return;
    }

    const restBody = {
      designation: this.designation,
      companyName: this.companyName,
      description: this.description,
      minimumQualification: this.minimumQualification,
      preferredQualification: this.preferredQualification,
      salary: this.salary,
      accountId: this.accountId,
      location: this.location,
      remoteJob: this.remoteJob
    };

    console.log('main_body', restBody);

    this.networkService.postOfferJob(restBody).subscribe( success => {
      console.log(success);
      if (success.status == true) {
        // Job has been posted
        localStorage.setItem(environment.authKey, success.result[0].Authorization);
        this.router.navigate(['submit_application']);
      } else {
        alert(success.message);
      }

    }, error => {

    });

  }

}
