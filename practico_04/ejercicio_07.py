"""Base de Datos SQL - Uso de múltiples tablas"""

import datetime
import sqlite3

from practico_04.ejercicio_02 import agregar_persona
from practico_04.ejercicio_06 import reset_tabla


def agregar_peso(id_persona, fecha, peso):
    """Implementar la funcion agregar_peso, que inserte un registro en la tabla 
    PersonaPeso.

    Debe validar:
    - Que el ID de la persona ingresada existe (reutilizando las funciones ya 
        implementadas).
    - Que no existe de esa persona un registro de fecha posterior al que 
        queremos ingresar.

    Debe devolver:
    - ID del peso registrado.
    - False en caso de no cumplir con alguna validacion."""

    connection = sqlite3.connect("ejercicio_01.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT idPersona FROM Persona WHERE IdPersona = ?

 """, (id_persona,))
    persona = cursor.fetchone()

    if persona:
        cursor.execute("""
        select idPersona, fecha from tabla_peso where idPersona = ? and fecha > ?
        """, (id_persona, fecha))
    peso_anterior = cursor.fetchone()

    if peso_anterior is not None or persona is None:
        return False
    if peso_anterior is None and persona is not None:
        cursor.execute("""
            INSERT INTO tabla_peso (idPersona, fecha, peso)
            VALUES (?, ?, ?)
        """, (id_persona, fecha, peso))

        id_nuevo = cursor.lastrowid

        connection.commit()
        connection.close()

        
        return id_nuevo
        




    pass # Completar


# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 26), 80) > 0
    # Test Id incorrecto
    assert agregar_peso(200, datetime.datetime(1988, 5, 15), 80) == False
    # Test Registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 16), 80) == False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
