import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { NetworkService } from 'src/app/service/network.service';

@Component({
  selector: 'app-apply-for-job',
  templateUrl: './apply-for-job.component.html',
  styleUrls: ['./apply-for-job.component.scss']
})
export class ApplyForJobComponent implements OnInit {

  applyJobsList: any[] = [
    {
      value: 1, 
      viewValue: 'Work from home'
    },
    {
      value: 2, 
      viewValue: 'BPO Job'
    }
  ];

  jobListArray: any[] = [];

  constructor(private networkService: NetworkService, private router: Router) { }

  ngOnInit(): void {
    this.getJobsList();
  }

  getJobsList(): void {
    this.networkService.getJobs().subscribe( success => {
      console.log(success);
     if (success.status) {
       this.jobListArray = success.result;
     } 
    }, error => {});
  }

  goHome(): void {
    this.router.navigate(['home']);
  }

}
