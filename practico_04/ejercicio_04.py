"""Base de Datos SQL - Búsqueda"""

import datetime 
import sqlite3

from practico_04.ejercicio_01 import reset_tabla
from practico_04.ejercicio_02 import agregar_persona




import sqlite3

def buscar_persona(id_persona):
    """Implementar la funcion buscar_persona, que devuelve el registro de una 
    persona basado en su id. El return es una tupla que contiene sus campos: 
    id, nombre, nacimiento, dni y altura. Si no encuentra ningun registro, 
    devuelve False."""

    connection = sqlite3.connect("ejercicio_01.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM Persona WHERE IdPersona = ?
    """, (id_persona,))

    persona = cursor.fetchone()

    connection.close()


    if persona:

        fecha_nacimiento = datetime.datetime.strptime(persona[2], '%Y-%m-%d %H:%M:%S')  

        return (persona[0], persona[1], fecha_nacimiento, persona[3], persona[4])
    else:
        return False


    pass # Completar


# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))

    assert juan == (1, 'juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
