"""Base de datos SQL - Listar"""

import datetime
import sqlite3

from practico_04.ejercicio_02 import agregar_persona
from practico_04.ejercicio_06 import reset_tabla
from practico_04.ejercicio_07 import agregar_peso


def listar_pesos(id_persona):
    """Implementar la funcion listar_pesos, que devuelva el historial de pesos 
    para una persona dada.

    Debe validar:
    - Que el ID de la persona ingresada existe (reutilizando las funciones ya 
     mplementadas).

    Debe devolver:
    - Lista de (fecha, peso), donde fecha esta representado por el siguiente 
    formato: AAAA-MM-DD.

    Ejemplo:
    [
        ('2018-01-01', 80),
        ('2018-02-01', 85),
        ('2018-03-01', 87),
        ('2018-04-01', 84),
        ('2018-05-01', 82),
    ]

    - False en caso de no cumplir con alguna validacion.
    """

    connection = sqlite3.connect("ejercicio_01.db")
    cursor = connection.cursor()

    cursor.execute(""" 
    SELECT idPersona from Persona where idPersona = ? 
    """, (id_persona,))

    persona = cursor.fetchone()

    if persona:
        cursor.execute("""
        SELECT fecha, peso from tabla_peso WHERE idPersona = ?
        """, (id_persona,))
        
        pesos = cursor.fetchall()
        if pesos:

            pesos_convertidos = []
            for fecha, peso in pesos:

                fecha_convertida = datetime.datetime.strptime(fecha, '%Y-%m-%d %H:%M:%S').date()

                pesos_convertidos.append((fecha_convertida.strftime('%Y-%m-%d'), peso))

            connection.close()
            return pesos_convertidos
    else:
        connection.close() 
        return False



# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    agregar_peso(id_juan, datetime.datetime(2018, 5, 1), 80)
    agregar_peso(id_juan, datetime.datetime(2018, 6, 1), 85)
    pesos_juan = listar_pesos(id_juan)
    pesos_esperados = [
        ('2018-05-01', 80),
        ('2018-06-01', 85),
    ]
    assert pesos_juan == pesos_esperados
    # id incorrecto
    assert listar_pesos(200) == False


if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
