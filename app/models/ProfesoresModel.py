from ..database.db import get_db_connection

from .entities.Bonos import Bonos

class ProfesoresModel(): 

    @classmethod
    def create_Profe(self, datos):

        query = """INSERT INTO profesores
        (nombre, apellido, fecha_nacimiento, telefono, email, dni, domicilio, titulo_estudios, idiomas, nivel_academico,
        observaciones_1, modalidad, turno_disponible, otra_disponibilidad, observaciones_2, tarifa)
        VALUE (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        insert = (datos.nombre, datos.apellido, datos.fecha_nacimiento, datos.telefono, datos.email, datos.dni, datos.domicilio,
                datos.titulo_estudios, datos.idiomas, datos.nivel_academico, datos.observaciones_1,
                datos.modalidad, datos.turno_disponible, datos.otra_disponibilidad, datos.observaciones_2,
                datos.tarifa)

        try:
            conn = get_db_connection()

            with conn.cursor() as cursor:
                
                cursor.execute(query, insert)
                affected_rows = cursor.rowcount
                conn.commit()
            
            conn.close()

            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def views_profesores(self):

        query = """SELECT id, nombre FROM profesores"""

        try:
            conn = get_db_connection()
            with conn.cursor() as cursor:
                cursor.execute(query)
                datos = cursor.fetchall()

            return datos
            
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_profesor(self, id):
        
        query = """DELETE FROM profesores WHERE id = %s """
        
        try:
            conn = get_db_connection()
            with conn.cursor() as cursor:
                cursor.execute(query, (id,))
                affected_rows = cursor.rowcount
                conn.commit()

            conn.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)