import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class NetworkService {

  constructor(private httpHandler: HttpClient) { }

  postSignIn(body: any): Observable<any> {
    return this.httpHandler.post<any>(environment.serverUrl + '/sign/in', body, {});
  }

  postSignUp(body: any): Observable<any> {
    return this.httpHandler.post<any>(environment.serverUrl + '/sign/up', body, {});
  }

  postOfferJob(body: any): Observable<any> {
    return this.httpHandler.post<any>(environment.serverUrl + '/Offer/jobs', body, {});
  }

}
