const formSelect = document.getElementById("selecto-adulto-menor");
var adultoForm = document.getElementById("colum-adulto");
var menorForm = document.getElementById("colum-menor");
var dniAulto = document.getElementById("d.n.i-adulto");
var domiAdulto = document.getElementById("domicilio-adulto");


var selectForm = localStorage.getItem("selectedForm");

if (selectForm === "adulto") {
    adultoForm.style.display = "block";
    dniAulto.style.display = "flex";
    domiAdulto.style.display = "flex";
    formSelect.value = "adulto";
} else if (selectForm === "menor") {
    menorForm.style.display = "block";
    formSelect.value = "menor";
}  

formSelect.addEventListener("change", function() {
    var selectedValue = formSelect.value;
    
    // Guardar el valor seleccionado en el localStorage
    localStorage.setItem("selectedForm", selectedValue);
    
    // Mostrar u ocultar los formularios según el valor seleccionado
    if (selectedValue === "adulto") {
        adultoForm.style.display = "block";
        dniAulto.style.display = "flex";
        domiAdulto.style.display = "flex";
        menorForm.style.display = "none";
    } else if (selectedValue === "menor") {
        menorForm.style.display = "block";
        dniAulto.style.display = "none";
        domiAdulto.style.display = "none";
    } 
});