from flask import Blueprint, render_template, request, url_for, redirect, flash

# Entities
from ..models.entities.Estudiantes import Empresa, Alumno
# Model
from ..models.EstudiantesModel import EmpresaModel, AlumnoModel

views_estudiantes = Blueprint('views_estudiantes',__name__)

# Render Templates
def render_estudiantes_template():
    empresas = EmpresaModel().views_empresa()
    alumnos = AlumnoModel().views_alumnos()
    return render_template("/estudiantes.html", empresas = empresas, alumnos = alumnos)

def render_add_alumno_template():
    return render_template("/add/add-alumno.html")

def render_add_grupo_template():
    return render_template("/add/add-grupo.html")

def render_add_empresa_template():
    return render_template("/add/add-empresa.html")



# Procece Alumno-Adulto
def process_alumno_datos_adulto_form_():
    #Datos DeL Alumno
    opcion = request.form["menor_adulto"]
    nombre = request.form["fullname"]
    apellido = request.form["apellido"]
    fecha_nacimiento = request.form["fecha_nacimient"]
    email = request.form["email"]
    telefono = request.form["telefono"]

    #------Datos--------#
    dni = request.form["d.n.i"]
    domicilio = request.form["domicilio"]  

    alumno = Alumno(opcion, nombre, apellido, fecha_nacimiento, email, telefono)

    alumno.agregar_adulto(dni, domicilio)

    return alumno


# Procece Alumno-Menor
def process_alumno_datos_menor_form():
    #Datos DeL Alumno
    opcion = request.form["menor_adulto"]
    nombre = request.form["fullname"]
    apellido = request.form["apellido"]
    fecha_nacimiento = request.form["fecha_nacimient"]
    email = request.form["email"]
    telefono = request.form["telefono"]

    #DATOS DE TUTORES 1
    nombre_t1 = request.form["nombre-1"]
    apellido_t1 = request.form["apellido-1"]
    telefono_t1 = request.form["telefono-1"]
    dni_t1 = request.form["dni-1"]
    domicilio_t1 = request.form["domicilio-1"]
    #DATOS DE TUTORES 2
    nombre_t2 = request.form["nombre-2"]
    apellido_t2 = request.form["apellido-2"]
    telefono_t2 = request.form["telefono-2"]
    dni_t2 = request.form["dni-2"]
    domicilio_t2 = request.form["domicilio-2"]

    alumno = Alumno(opcion, nombre, apellido, fecha_nacimiento, email, telefono)

    alumno.agregar_tutor(nombre_t1, apellido_t1, telefono_t1, dni_t1, domicilio_t1)
    alumno.agregar_tutor(nombre_t2, apellido_t2, telefono_t2, dni_t2, domicilio_t2)

    return alumno

# Procece Grupos
def process_grupo_form():
    #DATOS 
    modalidad = request.form["Modalidad"]
    nama_grupo = request.form["name-grupo"]
    numero_estu = request.form["nuemo-estudiante"]
        


# Procece Empresas 
# # PROCESAS LOS DATOS 'POST' DE EL FORM DE LOS TEMPLATE ADD-EMPRESA

def process_empresas_form():
    #DATOS
    nombre_empresa = request.form["name_empresa"]
    cif  = request.form["cif"]
    dirección = request.form["dirección"]
    telefono  = request.form["teléfono"]
    correo = request.form["e-mail"]

    # CONTACTO 1
    nombre_1 = request.form ["nombre-contacto-1"]
    departamento_1 = request.form ["departamento-1"]
    correo_contacto_1 = request.form["e-mail-contacto-1"]
    telefono_contacto_1 = request.form["telefono-contacto-1"]
    observaciones_1 = request.form["observaciones-1"]

    # CONTACTO 2
    nombre_2 = request.form ["nombre-contacto-2"]
    departamento_2 = request.form ["departamento-2"]
    correo_contacto_2 = request.form["e-mail-contacto-2"]
    telefono_contacto_2 = request.form["telefono-contacto-2"]
    observaciones_2 = request.form["observaciones-2"]

    # CONTACTO 3
    nombre_3 = request.form ["nombre-contacto-3"]
    departamento_3 = request.form ["departamento-3"]
    correo_contacto_3 = request.form["e-mail-contacto-3"]
    telefono_contacto_3 = request.form["telefono-contacto-3"]
    observaciones_3 = request.form["observaciones-3"]

    empresa = Empresa (nombre_empresa, cif, dirección, telefono, correo)    
    empresa.agregar_contacto(nombre_1, departamento_1, correo_contacto_1, telefono_contacto_1, observaciones_1)
    empresa.agregar_contacto(nombre_2, departamento_2, correo_contacto_2, telefono_contacto_2, observaciones_2)
    empresa.agregar_contacto(nombre_3, departamento_3, correo_contacto_3, telefono_contacto_3, observaciones_3)

    return empresa


# CARGAR EL TEMPLATE DE TOdO
@views_estudiantes.route("/Estudiantes")
def view():
    return render_estudiantes_template()

# GUARDAR DATOD DE ALUMNO MENOR/ADULTO EN SUS TABLAS SQL(ALUMNO_MENOR/ALUMNO_ADULTO)
@views_estudiantes.route("/Estudiantes/add-alumno", methods=['GET', 'POST'])
def add_alumno():
    if request.method == "POST":
        opcion = request.form["menor_adulto"]
        if opcion == "adulto":
            alumno = process_alumno_datos_adulto_form_()
            affected_rows = AlumnoModel().create_alumno_mayor_edad(alumno)
            if affected_rows == 2:
                flash("!Datos Guardados!")
            else:
                flash("Algo Salio Mal")
        elif opcion == "menor":
            alumno = process_alumno_datos_menor_form()
            affected_rows = AlumnoModel().create_alumno_menor_edad(alumno)
            if affected_rows == 2:
                flash("!Datos Guardados!")
            else:
                flash("Algo Salio Mal")
                
        else:
            return "Error"
        return render_add_alumno_template()
    return render_add_alumno_template()

@views_estudiantes.route("/Estudiantes/Alumno/dalete/<string:id>")
def delete_alumno(id):
    try:
        affected_rows = AlumnoModel().dalete_alumno(id)
        if affected_rows == 1:
            print("Dato borra ")
            #return redirect(render_add_alumno_template())
            return redirect(url_for('views_estudiantes.render_estudiantes_template')) # Para probar Alago despues borra.

        else:
            return render_estudiantes_template()
    except Exception as ex:
        return render_estudiantes_template()


@views_estudiantes.route("/Estudiantes/add-grupo", methods=['GET', 'POST'])
def add_grupo():
    if request.method == "POST":
        return redirect(url_for("views_estudiantes.add_grupo"))
    return render_add_grupo_template()





# GURARDAR DATOS DE LAS EMPRESA EN SUS TABLAS SQL(EMPRESA)
@views_estudiantes.route("/Estudiantes/add-empresa", methods=['GET', 'POST'])
def add_empresa():
    if request.method == "POST":
        empresa = process_empresas_form()
        affected_rows = EmpresaModel().create_empresa(empresa)
        if affected_rows == 1:
            flash("!Datos Guardados!")
        else:
            flash("Algo Salio Mal")
        return redirect(url_for("views_estudiantes.add_empresa"))
    return render_add_empresa_template()

# BORRAR ROW DE LA TABLA EMPRESA PARA BORRA EMPRESA 
@views_estudiantes.route("/Estudiantes/Empresa/dalete/<string:id>")
def dalete_empresa(id):
    try:
        affected_rows = EmpresaModel().delete_empresa(id)
        if affected_rows == 1:
            return render_estudiantes_template()
        else:
            return render_estudiantes_template()
    except Exception as ex:
        return render_estudiantes_template()
