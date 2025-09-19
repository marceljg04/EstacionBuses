"""
Los billetes tienen un identificador, la informacion del cliente y la del bus
"""

class Billete:
    def __init__(self, id_billete, cliente, bus):
        self.__id_billete = id_billete
        self.__cliente = cliente
        self.__bus = bus

    # Getters
    def getIdBillete(self):
        return self.__id_billete

    def getCliente(self):
        return self.__cliente

    def getBus(self):
        return self.__bus


    # Setters
    def setIdBillete(self, id_billete):
        self.__id_billete = id_billete

    def setCliente(self, cliente):
        self.__cliente = cliente

    def setBus(self, bus):
        self.__bus = bus


    # Metodos
    def __str__(self):
        return f"Billete #{self.__id_billete} de {self.__cliente.getNombre()} {self.__cliente.getApellido()}"