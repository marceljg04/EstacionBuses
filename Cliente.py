"""
Los clientes tienen un objeto billete en sus atributos, este se puede asignar o devolver
"""

from Billete import Billete

class Clientes:
    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__billete =  None
   
    #  Getters 
    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def getBillete(self):
        return self.__billete

    #  Setters 
    def setNombre(self, nombre):
        self.__nombre = nombre

    def setApellido(self, apellido):
        self.__apellido = apellido


    def setBillete(self, billete):
        self.__billete = billete

    #  Metodos
    def asignarBillete(self, billete):
        if self.__billete is not None:
            print(f"El cliente {self.__nombre} ya tiene un billete asignado.")
        self.__billete = billete

    def devolverBillete(self):
        if self.__billete is None:
            print(f"El cliente {self.__nombre} no tiene billete para devolver.")
        self.__billete = None