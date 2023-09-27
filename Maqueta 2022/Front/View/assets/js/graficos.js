/*
let btnDia = document.getElementById("btnDia");
let btnSemana = document.getElementById("btnSemana");
let btnMes = document.getElementById("btnMes");
let btnAnio = document.getElementById("btnAnio");

btnDia.addEventListener("click");
btnSemana.addEventListener("click");
function actualizarGrafico(e){
   console.log(e)
}
*/

const ctx = document.getElementById('graficoPaciente').getContext('2d');
const myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Domingo', 'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado'],
        datasets: [{
            label: 'Glucosa mg/dl',
            data: [0.7 , 0.9 , 1.2 , 0.8 , 0.9 , 0.8 , 0.9],
            backgroundColor: [
                'rgba(3, 79, 108, 0.225)'
            ],
            borderColor: [
                'rgba(3, 79, 108, 1)'
            ],
            borderWidth: 1,
            borderRadius:8
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});