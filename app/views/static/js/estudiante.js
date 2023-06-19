// Obtener los elementos del DOM
const tablaSelect = document.getElementById("selecto-tablas");
const alumnoTabla = document.getElementById("alumno-tabla");
const grupoTabla = document.getElementById("grupo-tabla");
const empresaTabla = document.getElementById("empresa-tabla");

// Obtener el valor seleccionado del localStorage
const selectTablas = localStorage.getItem("selectedFruit");

// Mostrar el formulario correspondiente al valor seleccionado
if (selectTablas === "alumno") {
    alumnoTabla.style.display = "block";
    tablaSelect.value = "alumno";
} else if (selectTablas === "grupo") {
    grupoTabla.style.display = "block";
    tablaSelect.value = "grupo";
}else if (selectTablas === "empresa") {
    empresaTabla.style.display = "block";
    tablaSelect.value = "empresa";
}

// Mostrar u ocultar los formularios al cambiar el valor del select
tablaSelect.addEventListener("change", function() {
    var selectedValue = tablaSelect.value;
    
  // Guardar el valor seleccionado en el localStorage
    localStorage.setItem("selectedFruit", selectedValue);
    
  // Mostrar u ocultar los formularios según el valor seleccionado
    if (selectedValue === "alumno") {
    alumnoTabla.style.display = "block";
    grupoTabla.style.display = "none";
    empresaTabla.style.display = "none";
    } else if (selectedValue === "grupo") {
    grupoTabla.style.display = "block";
    alumnoTabla.style.display = "none";
    empresaTabla.style.display = "none";
    } else if (selectedValue === "empresa") {
    empresaTabla.style.display = "block";
    alumnoTabla.style.display = "none";
    grupoTabla.style.display = "none";
    }
});