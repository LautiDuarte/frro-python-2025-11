"""Base de Datos SQL - Crear y Borrar Tablas"""

import sqlite3

def crear_tabla():

    connection = sqlite3.connect("ejercicio_01.db")
    cursor = connection.cursor()


    cursor.execute("DROP TABLE IF EXISTS Persona;")


    cursor.execute("""
        CREATE TABLE Persona (
            IdPersona INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre TEXT NOT NULL,
            FechaNacimiento DATE NOT NULL,
            DNI INTEGER NOT NULL,
            Altura INTEGER NOT NULL
        );
    """)

    cursor.execute('DELETE FROM sqlite_sequence WHERE name="Persona";')


    connection.commit()
    connection.close()

    pass 


def borrar_tabla():
    
    connection = sqlite3.connect("ejercicio_01.db")
    cursor = connection.cursor()

    cursor.execute("""
    DROP TABLE IF EXISTS Persona;
    """)
    connection.commit()
    connection.close()

    pass # Completar


# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN
