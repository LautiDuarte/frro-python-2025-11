# Implementar los metodos de la capa de negocio de socios.

from practico_05.ejercicio_01 import Socio
from practico_05.ejercicio_02 import DatosSocio


class DniRepetido(Exception):
    pass


class LongitudInvalida(Exception):
    pass


class MaximoAlcanzado(Exception):
    pass


class NegocioSocio(object):

    MIN_CARACTERES = 3
    MAX_CARACTERES = 15
    MAX_SOCIOS = 200

    def __init__(self):
        self.datos = DatosSocio()

    def buscar(self, id_socio):
        """
        Devuelve la instancia del socio, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        socio = self.datos.buscar(id_socio)
        if socio:
            return socio
        else:
            return None 

    def buscar_dni(self, dni_socio):
        """
        Devuelve la instancia del socio, dado su dni.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        socio = self.datos.buscar_dni(dni_socio)
        if socio:
            return socio
        else:
            return None

    def todos(self):
        """
        Devuelve listado de todos los socios.
        :rtype: list
        """
        socios = self.datos.todos()
        if socios:
            return socios
        else:
            return []

    def alta(self, socio):
        """
        Da de alta un socio.
        Se deben validar las 3 reglas de negocio primero.
        Si no validan, levantar la excepcion correspondiente.
        Devuelve True si el alta fue exitoso.
        :type socio: Socio
        :rtype: bool
        """
        if self.regla_1(socio) and self.regla_2(socio) and self.regla_3():
            self.datos.alta(socio)
            return True
        else:
            if not self.regla_1(socio) or not self.regla_2(socio) or not self.regla_3():
                return False

    def baja(self, id_socio):
        """
        Borra el socio especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        socio = self.buscar(id_socio)
        if socio:
            self.datos.baja(id_socio)
            return True
        else:
            return False

    def modificacion(self, socio):
        """
        Modifica un socio.
        Se debe validar la regla 2 primero.
        Si no valida, levantar la excepcion correspondiente.
        Devuelve True si la modificacion fue exitosa.
        :type socio: Socio
        :rtype: bool
        """
        if self.regla_2(socio):
            self.datos.modificacion(socio)
            return True
        else:
            return False

    def regla_1(self, socio):
        """
        Validar que el DNI del socio es unico (que ya no este usado).
        :type socio: Socio
        :raise: DniRepetido
        :return: bool
        """
        dni = socio.dni
        socios = self.datos.todos()
        for s in socios:
            if s.dni == dni:
                raise DniRepetido("El DNI ya está en uso.")
                return False
        return True

    def regla_2(self, socio):
        """
        Validar que el nombre y el apellido del socio cuenten con mas de 3 caracteres pero menos de 15.
        :type socio: Socio
        :raise: LongitudInvalida
        :return: bool
        """
        nombre = socio.nombre
        apellido = socio.apellido
        if self.MIN_CARACTERES <= len(nombre) <= self.MAX_CARACTERES and \
                self.MIN_CARACTERES <= len(apellido) <= self.MAX_CARACTERES:
            return True
        else:
            raise LongitudInvalida("El nombre y apellido deben tener entre 3 y 15 caracteres.")
        return False

    def regla_3(self):
        """
        Validar que no se esta excediendo la cantidad maxima de socios.
        :raise: MaximoAlcanzado
        :return: bool
        """
        cantidad = len(self.datos.todos())
        if cantidad < self.MAX_SOCIOS:
            return True
        else:
            raise MaximoAlcanzado("Se ha alcanzado el máximo de socios permitidos.")
        return False
