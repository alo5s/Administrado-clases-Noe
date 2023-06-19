from ..database.db import get_db_connection

class EmpresaModel():

    @classmethod
    def create_empresa(cls, empresa):
        try:
            conn = get_db_connection()

            with conn.cursor() as cursor:
                contacto_query = """INSERT INTO empresa
                                    (nombre_empresa, cif, direccion, telefono, correo,
                                    nombre_1, departamento_1, correo_1, telefono_1, observaciones_1,
                                    nombre_2, departamento_2, correo_2, telefono_2, observaciones_2,
                                    nombre_3, departamento_3, correo_3, telefono_3, observaciones_3)
                                    VALUES (%s, %s, %s, %s, %s,
                                            %s, %s, %s, %s, %s,
                                            %s, %s, %s, %s, %s,
                                            %s, %s, %s, %s, %s)"""
                contacto_data = (empresa.nombre_empresa, empresa.cif, empresa.direccion, empresa.telefono, empresa.correo,
                                empresa.contactos[0]['nombre'], empresa.contactos[0]['departamento'], empresa.contactos[0]['correo_contacto'], empresa.contactos[0]['telefono_contacto'], empresa.contactos[0]['observaciones'],
                                empresa.contactos[1]['nombre'], empresa.contactos[1]['departamento'], empresa.contactos[1]['correo_contacto'], empresa.contactos[1]['telefono_contacto'], empresa.contactos[1]['observaciones'],
                                empresa.contactos[2]['nombre'], empresa.contactos[2]['departamento'], empresa.contactos[2]['correo_contacto'], empresa.contactos[2]['telefono_contacto'], empresa.contactos[2]['observaciones'])
                cursor.execute(contacto_query, contacto_data)

                
                affected_rows = cursor.rowcount
            conn.commit()
            conn.close()

            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def views_empresa(cls):
        try:
            conn = get_db_connection()
            with conn.cursor() as cursor:
                query = """SELECT id, nombre_empresa FROM empresa"""
                cursor.execute(query)
                datos = cursor.fetchall()
                return datos
            conn.close()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_empresa(cls, id):
        try:
            conn = get_db_connection()
            with conn.cursor() as cursor:
                query = """DELETE FROM empresa WHERE id = %s """
                cursor.execute(query, (id,))
                affected_rows = cursor.rowcount
                
            conn.commit()
            conn.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

class AlumnoModel():

    @classmethod
    def create_alumno_mayor_edad(cls, alumno):
        try:
            conn = get_db_connection()
            with conn.cursor() as cursor:
                query_alumno = """INSERT INTO alumno
                (opcion, nombre, apellido, fecha_nacimiento, email, telefono)
                VALUES (%s, %s, %s, %s, %s, %s)"""
                alumno_dato = (alumno.opcion, alumno.nombre, alumno.apellido, alumno.fecha_nacimiento, alumno.email, alumno.telefono)
                cursor.execute(query_alumno, alumno_dato)
                affected_rows = cursor.rowcount

                # Obtener el ID del alumno recién insertado
                id_alumno = cursor.lastrowid

                query_mayor_edad = """INSERT INTO alumno_mayor_edad
                (id_alumno, dni, domicilio) VALUES (%s, %s, %s)"""
                datos_mayor_edad = (id_alumno, alumno.datos[0]['dni'], alumno.datos[0]['domicilio'])
                cursor.execute(query_mayor_edad, datos_mayor_edad)
                
                affected_rows += cursor.rowcount

            conn.commit()
            conn.close()

            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def create_alumno_menor_edad(cls, alumno):
        try:
            conn = get_db_connection()
            with conn.cursor() as cursor:
                query_alumno = """INSERT INTO alumno
                (opcion, nombre, apellido, fecha_nacimiento, email, telefono)
                VALUES (%s, %s, %s, %s, %s, %s)"""
                alumno_dato = (alumno.opcion, alumno.nombre, alumno.apellido, alumno.fecha_nacimiento, alumno.email, alumno.telefono)
                cursor.execute(query_alumno, alumno_dato)
                affected_rows = cursor.rowcount

                # Obtener el ID del alumno recién insertado
                id_alumno = cursor.lastrowid

                query_menor_edad = """INSERT INTO alumno_menor_edad
                    (id_alumno, nombre_t1, apellido_t1, telefono_t1, dni_t1, domicilio_t1,
                    nombre_t2, apellido_t2, telefono_t2, dni_t2, domicilio_t2)
                    VALUES (%s, %s, %s, %s, %s, %s,
                            %s, %s, %s, %s, %s )"""
                tutores_datos = (id_alumno, alumno.datos[0]['nombre'], alumno.datos[0]['apellido'], alumno.datos[0]['telefono'], alumno.datos[0]['dni'], alumno.datos[0]['domicilio'],
                                            alumno.datos[1]['nombre'], alumno.datos[1]['apellido'], alumno.datos[1]['telefono'], alumno.datos[1]['dni'], alumno.datos[1]['domicilio'])
                cursor.execute(query_menor_edad, tutores_datos)
                
                affected_rows += cursor.rowcount
            conn.commit()
            conn.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    

    @classmethod
    def views_alumnos(cls):
        try:
            conn = get_db_connection()
            with conn.cursor() as cursor:
                query = """SELECT  id_alumno, nombre FROM alumno"""
                cursor.execute(query)
                datos = cursor.fetchall()
                return datos
            conn.close()
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def dalete_alumno(cls,id):
        try:
            conn = get_db_connection()
            with conn.cursor() as cursor:
                query = """DELETE FROM alumno WHERE id_alumno = %s """
                cursor.execute(query, (id,))
                affected_rows = cursor.rowcount
                
            conn.commit()
            conn.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
