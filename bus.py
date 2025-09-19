"""
bus contiene atributos: id_bus (incremental), plazas totales, plazas libres, plazas vendidas, billete(sale de clase billetes,  cantidad)
metodos: getters, setters, venta billete, devolucion billete, estado de las plazas
"""
from Billete import Billete
class Autobuses:
    __cantidad_buses = 0
    
    def __init__(self, plazas_totales):
        self.__id_bus = Autobuses.__cantidad_buses
        self.SetPlazasTotales(plazas_totales)
        self.__plazas_libres = plazas_totales
        self.__plazas_vendidas = 0
        Autobuses.__cantidad_buses += 1
        self.__billetes = []
        self.__id_billete = 0
        
    def set_billetes(self, billetes):
        self.__billetes.append(billetes)
    
    def get_billetes(self):
        return self.__billetes
    
    def set_id_billete(self):
        self.__id_billete += 1
        
    def get_id_billete(self):
        return self.__id_billete
    
    def get_id_bus(self):
        return self.__id_bus
    
    def SetPlazasTotales(self, plazas_totales):
        self.__plazas_totales = plazas_totales
        
    def GetPlazasTotales(self):
        return self.__plazas_totales
    
    def get_plazas_vendidas(self):
        return self.__plazas_vendidas
    
    def set_plazas_vendidas(self, compra):
        if compra == True:
            self.__plazas_vendidas += 1
        else:
            self.__plazas_vendidas -= 1
    
    def set_plazas_libres(self, compra):
        if compra == True:
            self.__plazas_libres -= 1
        else:
            self.__plazas_libres += 1
            
    def get_plazas_libres(self):
        return self.__plazas_libres
    
    def eliminar_billete(self, billete):
        if billete in self.__billetes:
            self.__billetes.remove(billete)
        
    @classmethod
    def get_cantidad_buses(cls):
        return cls.cantidad_buses
    
    @classmethod
    def comprar_billete(cls, bus, cliente):
        billete_comprado = False
        if bus.get_plazas_libres() > 0:
            billete = Billete(bus.get_id_billete(), cliente, bus)
            bus.set_id_billete()
            bus.set_billetes(billete)
            cliente.asignarBillete(billete)
            bus.set_plazas_vendidas(True)
            bus.set_plazas_libres(True)
            billete_comprado = True
        return billete_comprado
    
    @classmethod
    def devolver_billete(cls, billete, bus):
        billete_vendido = False
        if billete in bus.__billetes:
            bus.eliminar_billete(billete)
            bus.set_plazas_vendidas(False)
            bus.set_plazas_libres(False)
            billete_vendido = True
        
        return billete_vendido
    