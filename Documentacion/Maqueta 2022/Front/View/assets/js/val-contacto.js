const formularioC = document.getElementById('formularioC');

const inputs = document.querySelectorAll('#formularioC input');

/*Caacteres permitidos para los campos*/
const expresiones = {
  mensaje: /^[a-zA-Z0-9\_\-]{1,200}$/, // Letras, numeros, guion y guion_bajo
  nombre: /^[a-zA-ZÀ-ÿ\s]{1,20}$/, // Letras y espacios, pueden llevar acentos.
  password: /^.{4,12}$/, // 4 a 12 digitos.
  correo: /^(([^<>()\[\]\.,;:\s@\”]+(\.[^<>()\[\]\.,;:\s@\”]+)*)|(\”.+\”))@(([^<>()[\]\.,;:\s@\”]+\.)+[^<>()[\]\.,;:\s@\”]{2,})$/,
  telefono: /^\d{7,14}$/ // 7 a 14 numeros.
}

const campos = {
  nombreFC: false,
  emailFC: false,
  mensajeFC: false

}



const validarFormulario = (e) => {
  switch (e.target.name) {
    case "nombreFC":
      validarCampo(expresiones.nombre, e.target, 'nombreFC');

      break;

    case "emailFC":
      validarCampo(expresiones.correo, e.target, 'emailFC');
      break;

    case "mensajeFC":
      validarCampo(expresiones.mensaje, e.target, 'mensajeFC');

      break;
  }
}

const validarCampo = (expresiones, input, campo) => {
  if (expresiones.test(input.value)) {
    document.getElementById(`grupo-${campo}`).classList.remove('form-grupo-incorrecto');
    document.getElementById(`grupo-${campo}`).classList.add('form-grupo-correcto');
    document.querySelector(`#grupo-${campo} i`).classList.add('fa-circle-check');
    document.querySelector(`#grupo-${campo} i`).classList.remove('fa-circle-xmark');

    document.querySelector(`#grupo-${campo} .form-input-error`).classList.remove('form-input-error-activo');
    campos[campo] = true;
  } else {
    document.getElementById(`grupo-${campo}`).classList.add('form-grupo-incorrecto');
    document.getElementById(`grupo-${campo}`).classList.remove('form-grupo-correcto');
    document.querySelector(`#grupo-${campo} i`).classList.add('fa-circle-xmark');
    document.querySelector(`#grupo-${campo} i`).classList.remove('fa-circle-check');

    document.querySelector(`#grupo-${campo} .form-input-error`).classList.add('form-input-error-activo');
    campos[campo] = false;
  }

}


/* CREAMOS FUNCION QUE VALIDA LUEGO DE CADA TECLA PULSADA Y CADA CLICK FUERA DE LOS CAMPOS*/
inputs.forEach((input) => {
  input.addEventListener('keyup', validarFormulario);
  input.addEventListener('blur', validarFormulario);
});



/* VALIDACION DE TODOS LOS CAMPOS DESDE EL BOTON ENVIAR Y LIMPIEZA LUEGO DEL ENVIO */
formularioC.addEventListener('submit', (e) => {
  e.preventDefault();

  if (campos.nombreFC && campos.emailFC && campos.mensajeFC) {
    formularioC.reset();

    document.getElementById('form-mensaje-enviado').classList.add('form-mensaje-enviado-activo');

    setTimeout(() => {
      document.getElementById('form-mensaje-enviado').classList.remove('form-mensaje-enviado-activo');

    }, 5000);

    document.querySelectorAll('.form-grupo-correcto').forEach((icono) => {
      icono.classList.remove('.form-grupo-correcto');
    });

  } else {
    document.getElementById('form-mensaje').classList.add('form-mensaje-activo');


  }

});