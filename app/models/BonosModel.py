from ..database.db import get_db_connection
from .entities.Bonos import Bonos

class BonosModel(): 

    @classmethod
    def create_bono(cls, datos):
        try:
            conn = get_db_connection()
            with conn.cursor() as cursor:
                query = """INSERT INTO bonos
                        (modalidad, duracion, nombre, precio, caducidad, numero_de_clases, nota) 
                        VALUE (%s, %s, %s, %s, %s, %s, %s )"""
                insert = (datos.modalidad, datos.duracion, datos.nombre, datos.precio, 
                            datos.caducidad, datos.numero_de_clases, datos.nota)
                            
                cursor.execute(query, insert)
                affected_rows = cursor.rowcount
                conn.commit()
            conn.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def views_bono(cls):
        try:
            conn = get_db_connection()
            with conn.cursor() as cursor:
                query = """SELECT id, nombre FROM bonos """
                cursor.execute(query)
                datos = cursor.fetchall()
            return datos
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def delete_bono(cls, id):
        try:
            conn = get_db_connection()
            with conn.cursor() as cursor:
                query = """DELETE FROM bonos WHERE id = %s """
                cursor.execute(query, (id,))
                affected_rows = cursor.rowcount
                conn.commit()

            conn.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def view_bono(cls,id):

        
        try:
            conn = get_db_connection()
            with conn.cursor() as cursor:
                query = """SELECT * FROM bonos WHERE id= %s"""
                cursor.execute(query,(id,))
                datos = cursor.fetchone()
                
            conn.close()
            return datos
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def updata_bono(cls, datos, id):
        try:
            conn = get_db_connection()
            with conn.cursor() as cursor:
                query = """UPDATE bonos SET 
                modalidad = %s, duracion = %s, nombre = %s , precio = %s , caducidad = %s , numero_de_clases = %s , nota = %s 
                WHERE id = %s"""
                insert = (datos.modalidad, datos.duracion , datos.nombre, datos.precio,
                            datos.caducidad, datos.numero_de_clases, datos.nota, id,)
                cursor.execute(query, insert)
                affected_rows = cursor.rowcount
                conn.commit()

            conn.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

        