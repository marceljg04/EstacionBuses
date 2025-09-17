from Billete import Billete

class Clientes:
    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__billete =  None
    
    def asignarBillete(self, billete):
        if self.billete is not None:
            raise ValueError(f"El cliente {self.nombre} ya tiene un billete asignado.")
        self.billete = billete

    def devolverBillete(self, billete):
        if self.billete is None:
            raise ValueError(f"El cliente {self.nombre} no tiene billete para devolver.")
        self.billete = None

