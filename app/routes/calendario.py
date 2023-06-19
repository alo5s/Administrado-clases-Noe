from flask import Blueprint, render_template, request, url_for, redirect, flash
from datetime import datetime

from ..models.CalendarioModel import CalendarioModel

from ..models.entities.Calendario import Calendario
view_calendarioo = Blueprint('view_calendarioo',__name__)

def render_calendario_template():
    fechas = CalendarioModel().views_fechas()
    return render_template("/calendario.html", fechas = fechas)


def process_fecha_form():
    fecha_str = request.form["fecha"]
    fecha = datetime.strptime(fecha_str, "%d-%m-%Y").strftime("%Y-%m-%d")
    razon = request.form["razon"]
    datos = Calendario (fecha, razon)
    return datos

def calendario_form_update():
    datos_actualizar = []
    for key, value in request.form.items():
        if key.startswith("fecha."):
            fecha_id = key.split("fecha.")[1]
            fecha = value
            razon = request.form.get("razon" + fecha_id, "")
            datos_actualizar.append((fecha_id, fecha, razon))
    return datos_actualizar


@view_calendarioo.route("/calendario")
def view():
    return render_calendario_template()

@view_calendarioo.route("/calendario/add-fecha", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        datos = process_fecha_form()
        affected_rows = CalendarioModel().create_fecha(datos)
        if affected_rows == 1:
            print("Todo Guardados Bien")
        else:
            print("Algo Salio Mal")
        return redirect(url_for("view_calendarioo.add"))
    return render_calendario_template()

@view_calendarioo.route("/calendario/update-fecha", methods=['GET', 'POST'])
def update():
    if request.method == "POST":
        datos_actualizar = calendario_form_update()
        affected_rows = CalendarioModel().update(datos_actualizar)
        if affected_rows == affected_rows:
            print("Todo Guardados Bien")
        else:
            print("Algo Salio Mal")
        return redirect(url_for("view_calendarioo.add"))
    return render_calendario_template()

@view_calendarioo.route("/calendario/delete/<string:id>", methods=['GET', 'POST'])
def delete(id):
    try:
        datos = ("esto para pobrar",id)
        affected_rows = CalendarioModel().delete(id)
        if affected_rows == 1:
            print("dato borrado")
        else:
            print("Algo Salio Mal")
        return redirect(url_for("view_calendarioo.add"))
    except Exception as ex:
        return render_calendario_template()

    