import { Component, OnInit } from '@angular/core';
import { FormBuilder,Validators } from '@angular/forms';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  constructor(private formBuilder:FormBuilder){};
  profileForm=this.formBuilder.group({
    
    email:["",[Validators.required,Validators.email]],
    pass:["",[Validators.required]]

  });
  verificacionLogin(){
    if(this.profileForm.valid){
      console.log("Llamar al servicio de Login");
      this.profileForm.reset();
    } 
    else{
      this.profileForm.markAllAsTouched();
      alert("NO se ingreso con exito, revise si ingreso bien los datos")
    }
  }
  get email_GET(){
    return this.profileForm.controls.email;
  }
  get pass_GET(){
    return this.profileForm.controls.pass;
  }
  ngOnInit(): void {}
}


