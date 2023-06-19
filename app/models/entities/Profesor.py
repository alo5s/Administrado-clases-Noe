class Profesor():
    def __init__(self, nombre=None, apellido=None, fecha_nacimiento=None, telefono=None, email=None, dni=None, domicilio=None, titulo_estudios=None, idiomas=None, nivel_academico=None, observaciones_1=None, modalidad=None, turno_disponible=None, otra_disponibilidad=None, observaciones_2=None, tarifa=None):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.telefono = telefono
        self.email = email
        self.dni = dni
        self.domicilio = domicilio
        self.titulo_estudios = titulo_estudios
        self.idiomas = idiomas
        self.nivel_academico = nivel_academico
        self.observaciones_1 = observaciones_1
        self.modalidad = modalidad
        self.turno_disponible = turno_disponible
        self.otra_disponibilidad = otra_disponibilidad
        self.observaciones_2 = observaciones_2
        self.tarifa = tarifa