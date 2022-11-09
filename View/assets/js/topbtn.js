// Get the button:
let mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() { scrollFunction() };

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}


//Script para boton de nav "ingresar"
function btningresar() {
  location.href = "login.html"
}
//Script para redireccionar al "dashboard usuario"
function dashboardPaciente() {
  location.href = "dashboardUser.html"
}

//Script para redireccionar al "dashboard paciente"
function dashboardAdmin() {
  location.href = "dashboardAdmin.html"
}