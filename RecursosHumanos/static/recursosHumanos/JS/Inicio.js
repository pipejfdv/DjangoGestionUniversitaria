const contenedorFormularios = document.getElementsByClassName("contenedor-formulario-registro");
const formularioContrato = document.getElementsByClassName("form-contrato");
const formularioEmpleado = document.getElementsByClassName("form-empleado");
function activarFormulario() {
    if (contenedorFormularios[0].classList.contains("oculto")) {
        contenedorFormularios[0].classList.remove("oculto");
        contenedorFormularios[0].classList.add("visible");
    }
    else {
        contenedorFormularios[0].classList.remove("visible");
        contenedorFormularios[0].classList.add("oculto");
    }
}

function activarFormularioContrato(){
    
    formularioContrato[0].classList.add("visible");
    formularioContrato[0].classList.remove("oculto");
    formularioEmpleado[0].classList.remove("visible");
    formularioEmpleado[0].classList.add("oculto");
}

function activarFormularioEmpleado(){
    
    formularioContrato[0].classList.add("oculto");
    formularioContrato[0].classList.remove("visible");
    formularioEmpleado[0].classList.remove("oculto");
    formularioEmpleado[0].classList.add("visible");
}

function validar(){

const campos = document.querySelectorAll(
        ".contenedor-formularios .campo-requerido"
    );

    for (let campo of campos) {
        if (campo.value.trim() === "") {
            const nombreCampo =
                campo.getAttribute("placeholder") ||
                campo.previousElementSibling?.innerText ||
                campo.name;

            alert("Falta completar el campo: " + nombreCampo);
            campo.focus();
            return false;
        }
    }

    return true;

}