import { Injectable } from '@angular/core';
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
 

  constructor( private http:HttpClient ) { }


  email_string:string=""
  

  // SE CREA METODO DE LOGUEO Y CONTROL QUE CONSUMIRA EL LOGIN COMPONENT
      // credenciales trae los datos del form y es de tipo loginInterface.
  login(credenciales:loginInterface):Observable<any>{
        //No tiene sentido, pero tomamos los datos
        console.log("Estos son los datos que de ingresaron en el formulario")
        console.log("Fijate como hacer la verificacion despues")
        console.log(credenciales)

        return this.http.get("http://localhost:3000/USUARIOS")
    }
  // CIERRA EXPORT
  }



