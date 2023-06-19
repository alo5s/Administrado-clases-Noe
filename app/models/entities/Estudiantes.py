class Empresa():
    def __init__(self, nombre_empresa=None, cif=None, direccion=None, telefono=None, correo=None):
        self.nombre_empresa = nombre_empresa
        self.cif = cif
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.contactos = []

    def agregar_contacto(self, nombre=None, departamento=None, correo_contacto=None, telefono_contacto=None, observaciones=None):
        contacto = {
            'nombre': nombre,
            'departamento': departamento,
            'correo_contacto': correo_contacto,
            'telefono_contacto': telefono_contacto,
            'observaciones': observaciones
        }
        self.contactos.append(contacto)

class Alumno():
    def __init__(self, opcion=None ,nombre=None, apellido=None, fecha_nacimiento=None, email=None, telefono=None):
        self.opcion = opcion
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.email = email 
        self.telefono = telefono
        self.datos = []

    def agregar_adulto(self, dni=None, domicilio=None):
        dato = {
            'dni': dni,
            'domicilio': domicilio
        }
        self.datos.append(dato)

    def agregar_tutor(self, nombre=None, apellido=None, telefono=None, dni=None, domicilio=None):
        tutor = {
            'nombre': nombre,
            'apellido': apellido,
            'telefono': telefono,
            'dni': dni,
            'domicilio': domicilio
        }   
        self.datos.append(tutor)
















