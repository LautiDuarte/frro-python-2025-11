"""Base de Datos SQL - Creación de tablas auxiliares"""

import sqlite3
import datetime
from practico_04.ejercicio_01 import borrar_tabla, crear_tabla


def crear_tabla_peso():
    """Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
        - IdPersona: Int() (Clave Foranea Persona)
        - Fecha: Date()
        - Peso: Int()
    """

    connection = sqlite3.connect("ejercicio_01.db")
    cursor = connection.cursor()

    cursor.execute("""
    DROP TABLE IF EXISTS tabla_peso;""")

    cursor.execute("""
    CREATE TABLE tabla_peso (
        idPersona INTEGER NOT NULL CONSTRAINT fk_persona REFERENCES Persona(IdPersona),
        fecha DATE NOT NULL,
        peso INTEGER NOT NULL,
        PRIMARY KEY (idPersona, fecha)  );
 """)
    
    connection.commit()
    connection.close()

    pass # Completar


def borrar_tabla_peso():
    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""
    connection = sqlite3.connect("ejercicio_01.db")
    cursor = connection.cursor()

    cursor.execute("""
    DROP TABLE IF EXISTS tabla_peso;
    """)

    connection.commit()
    connection.close()

    pass # Completar


# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN
