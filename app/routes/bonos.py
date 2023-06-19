from flask import Blueprint, render_template, request, redirect, url_for
import datetime

# Models
from ..models.BonosModel import BonosModel

# Entities
from ..models.entities.Bonos import Bonos


views_bonos = Blueprint('views_bonos',__name__)

# Render de templates 
def render_bonos_template():
    bonos = BonosModel().views_bono()
    return render_template("bonos.html", bonos = bonos)

def render_add_bono_template():
    return render_template("/add/add-bono-alumno.html")

def render_view_update_bono_template(datos):
    return render_template("/view-update/view-update-bono.html", datos=datos,datetime=datetime)

# Datos GET o POST para guardas de los form add o update
def process_bono_form():
    modalidad = request.form["modalidad"]
    duracion = request.form["duración"]
    nombre = request.form["nombre-bono"]
    precio = request.form["precio"]
    caducidad = request.form["caducidad"]
    numero_de_clases = request.form["numero_de_clases"]
    nota = request.form["nota"]
    datos = Bonos(modalidad, duracion, nombre, precio, caducidad, numero_de_clases, nota)
    return datos


# Views Routes
@views_bonos.route("/Bonos")
def home():
    return render_bonos_template()

@views_bonos.route("/Bono/add-bono-alumno/", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        datos = process_bono_form()
        affected_rows = BonosModel().create_bono(datos)
        
        if affected_rows == 1:
            print("Todo Guardados Bien")
        else:
            print("Algo Salio Mal")

        return redirect(url_for("views_bonos.add"))
    return render_add_bono_template()

@views_bonos.route("/Bonos/delet/<string:id>")
def dalete(id):
    try:    
        affected_rows = BonosModel().delete_bono(id)
        if affected_rows == 1:
            return render_bonos_template()
        else:
            return render_bonos_template()
    except Exception as ex:
        return render_bonos_template()

@views_bonos.route("/Bonos/view/<string:id>")
def view(id):
    try:
        datos = BonosModel().view_bono(id)  
        return render_view_update_bono_template(datos)
        print(datos)
    except Exception as ex:
        print("Algo salio mal",ex)
        return render_bonos_template()

@views_bonos.route("/Bonos/update/<id>",  methods=['GET', 'POST'])
def  update(id):
    if request.method == "POST":
        datos = process_bono_form()
        affected_rows = BonosModel.updata_bono(datos, id)
        if affected_rows == 1:
            print("Todo Guardados Bien")
        else:
            print("Algo Salio Mal")

        return render_bonos_template()
    return render_add_bono_template()



