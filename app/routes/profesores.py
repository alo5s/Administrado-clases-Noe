from flask import Blueprint, render_template, request, url_for, redirect, flash

# Models
from ..models.ProfesoresModel import ProfesoresModel

# Entities
from ..models.entities.Profesor import Profesor


views_profesores = Blueprint('views_profesores',__name__)

# Render de templates 
def render_profesores_template():
    profesores = ProfesoresModel().views_profesores()
    return render_template("/profesores.html", profesores = profesores)

def render_add_profesores_template():
    return render_template("/add/add-profesores.html")


# Datos GET o POST para guardas de los form add o update
def process_profesores_form():

    #DATOS PERSONALES
    nombre = request.form ["name"]
    apellido = request.form ["apellido"]
    fecha_nacimiento = request.form ["fecha-nacimiento"]
    telefono = request.form ["teléfono"]
    email = request.form ["e-mail"]
    dni = request.form ["dni"]
    domicilio = request.form ["domicilio"]

    #DATOS PROFEESIONALES
    titulo_estudios = request.form ["titulo-estudios"]
    idiomas = request.form ["idiomas"]
    nivel_academico = request.form ["nivel-academico"]
    observaciones_1 = request.form ["Observaciones-1"]

    #DATOS LABORALES
    modalidad = request.form ["modalidad"]
    turno_disponible = request.form ["turno-disponible"]
    otra_disponibilidad = request.form ["otra-disponibilidad"]
    observaciones_2 = request.form ["Observaciones-2"]

    #TARIFA DEL PROFESO
    tarifa = request.form ["tarifa"]
    datos = Profesor (nombre, apellido, fecha_nacimiento, telefono, email, dni, domicilio,
                titulo_estudios, idiomas, nivel_academico, observaciones_1,
                modalidad, turno_disponible, otra_disponibilidad, observaciones_2,
                tarifa)
    
    return datos


# Views Routes

@views_profesores.route("/Profesores")
def home():
    return render_profesores_template()

@views_profesores.route("/Profesores/add_profesores", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        datos = process_profesores_form()
        affected_rows = ProfesoresModel().create_Profe(datos)
        if affected_rows == 1:
            flash("LISTOS")
        else:
            flash("ERROR")        
        
        return render_add_profesores_template()
    return render_add_profesores_template()

@views_profesores.route("/Profesores/delet/<string:id>")
def dalete(id):
    try:    
        affected_rows = ProfesoresModel().delete_profesor(id)
        if affected_rows == 1:
            return render_profesores_template()
        else:
            return render_profesores_template()        
    except Exception as ex:
        return render_profesores_template()
