from ..database.db import get_db_connection

class CalendarioModel():

    @classmethod
    def create_fecha(cls, datos):
        try:
            conn = get_db_connection()
            with conn.cursor() as cursor:
                query = """INSERT INTO calendario (fecha, razon) VALUE (%s, %s) """
                fecha_datos = (datos.fecha, datos.razon)
                cursor.execute(query, fecha_datos)
                affected_rows = cursor.rowcount
            conn.commit()
            conn.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def views_fechas(cls):
        try:
            conn = get_db_connection()
            with conn.cursor() as cursor:
                query = """SELECT * FROM calendario """
                cursor.execute(query)
                datos = cursor.fetchall()
                conn.close()
            return datos
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def update(cls, fechas_actualizadas):
        try:
            conn = get_db_connection()
            with conn.cursor() as cursor:
                affected_rows = 0
                for fecha_id, fecha, razon in fechas_actualizadas:
                    query = "UPDATE calendario SET fecha = %s, razon = %s WHERE id = %s"
                    fecha_datos = (fecha, razon, fecha_id)
                    cursor.execute(query, fecha_datos)
                    affected_rows += cursor.rowcount
                conn.commit()
                conn.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete(cls, id):
        try:
            conn = get_db_connection()
            with conn.cursor() as cursor:
                query = """DELETE FROM calendario WHERE id = %s"""
                cursor.execute(query, (id,))
                affected_rows = cursor.rowcount
                
                conn.commit()
                conn.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

