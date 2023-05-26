import { Injectable, ReflectiveInjector } from '@angular/core';
import { loginInterface } from './interfaces/loginInterface';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

import { userInterface } from './interfaces/userInterface';

// LA IDEA DE ESTE SERVICIO ESTA VERIFICAR QUE EL EMAIL INGRESADO COINCIDA CON ALGUNO DE NUESTRA
// "BASE DE DATOS" Y EN EL CASO DE QUE SI QUE TIRE UN MENSAJE VE VALIDACION CORRERCTA. PERO POR AHORA NO PUDIMOS COMPLETARLO

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  constructor( private http:HttpClient) { 
  }


  email_string:string="asd"
  

  // SE CREA METODO DE LOGUEO QUE CONSUMIRA EL LOGIN COMPONENT
      // credenciales trae los datos del form y es de tipo loginInterface.
  login(credenciales:loginInterface):Observable<userInterface>{

    console.log("el email: "+ credenciales.email);

    // OBTENEMOS EL ATRIBUTO email DEL OBSERVABLE Y SE LO CONVIERTE EN STRING
    this.email_string = this.http.get<userInterface>('././assets/data_usuarios.json').pipe(
      map((usuario: userInterface) =>{
        return usuario.email.toString();
      })).toString()

      console.log("??"+this.email_string)
      
      if(this.email_string=credenciales.email){


      }

          return  this.http.get<userInterface>('././assets/data_usuarios.json')

   
  }
   
    

  }

function str(email: string) {
  throw new Error('Function not implemented.');
}

