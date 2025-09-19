from bus import Autobuses
from Cliente import Clientes
buses = []
clientes = []

#funciones
def validar_input_numerico(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor <= 0:
                print("Por favor, introduce un número positivo.")
                continue  
            return valor
        except ValueError:
            print("Error: Debes introducir un número entero válido.")
            
def validar_input_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto and texto.replace(" ", "").isalpha():
            return texto
        print("Error: Por favor, introduce solo letras (sin números ni caracteres especiales).")
                
def menu():
    print("1. Añadir bus")
    print("2. Comprar billete")
    print("3. Devolución billete")
    print("4. Estado de la venta")
    print("0. Salir")

def añadir_bus():
    plazas = validar_input_numerico("Introduce el número de plazas: ")
    bus = Autobuses(plazas)
    buses.append(bus)

def comprovar_buses():
    existe_bus = True
    if len(buses) == 0:
        existe_bus = False
    return existe_bus

def seleccionar_buses():
    id_bus = validar_input_numerico("Introduce el ID del bus: ")
    bus_seleccionado = None
    for bus in buses:
        if bus.get_id_bus() == id_bus:
            bus_seleccionado = bus
    return bus_seleccionado

def mostrar_buses():
    print("Buses disponibles:")
    for bus in buses:
        print(f"ID Bus: {bus.get_id_bus()}, Plazas Totales: {bus.GetPlazasTotales()}, Plazas Vendidas: {bus.get_plazas_vendidas()}, Plazas Libres: {bus.GetPlazasTotales() - bus.get_plazas_vendidas()}")


def comprovar_cliente(nombre_cliente, apellido_cliente):
    for cliente in clientes:
        if cliente.getNombre().lower()  == nombre_cliente and cliente.getApellido().lower() == apellido_cliente:
            return cliente
        else:
            print("Cliente no encontrado. Por favor, regístrate primero.")
    

#entramos en el menu
opcion = -1
while opcion != 0:
    menu()
    opcion = validar_input_numerico("Elige una opción: ")
    if opcion == 1:
        añadir_bus()
        print("Bus añadido correctamente.")
    elif opcion == 2:         #comprar billete
        if comprovar_buses():
            respuesta = ""
            while respuesta not in ['s', 'n']:
                print("Esta registrado como cliente? (s/n)")
                respuesta = input().lower()
                if respuesta == 's':
                    nombre_cliente = validar_input_texto("Introduce el nombre del cliente: ")
                    apellido_cliente = validar_input_texto("Introduce el apellido del cliente: ")
                    cliente = comprovar_cliente(nombre_cliente.lower(), apellido_cliente.lower())
                    if cliente is None:
                        print ("El cliente introducido es falso")
                        respuesta = None
                elif respuesta == 'n':
                    print("Por favor, regístrate primero.")
                    nombre_cliente = validar_input_texto("Introduce el nombre del cliente: ")
                    apellido_cliente = validar_input_texto("Introduce el apellido del cliente: ")
                    cliente = Clientes(nombre_cliente, apellido_cliente)
                    clientes.append(cliente)
                else:
                    print("Respuesta no válida. Por favor, responde con 's' o 'n'.") 
            mostrar_buses()
            bus = seleccionar_buses()
            if bus is not None:
                if Autobuses.comprar_billete(bus, cliente):
                    print("Billete comprado correctamente.")
                else:
                    print("Ya tienes un ticket comprado o no hay plazas disponibles.")
        else:
            print("No hay buses disponibles. Por favor, añade un bus primero.")  
    elif opcion == 3:        #devolucion billete
        if comprovar_buses():
            print("Introduce el nombre y apellido del cliente para devolver el billete: ")
            nombre_cliente = input("Nombre: ").lower()
            apellido_cliente = input("Apellido: ").lower()
            cliente = comprovar_cliente(nombre_cliente, apellido_cliente)
            if cliente is None:
                print("Cliente no encontrado")
            else:
                if cliente.getBillete():
                    billete = cliente.getBillete()
                    bus = billete.getBus()
                    bus_billetes = bus.get_billetes()

                    if billete in bus_billetes:
                        if bus.devolver_billete(billete, bus):
                            print("Billete devuelto correctamente")
                        else:
                            print("No se ha podido devolver el billete")
                    else:
                        print("No tienes un billete comprado")
                else:
                    print("No hay buses disponibles. Por favor, añade un bus primero.")  
                
        else:
            print("No hay buses disponibles. Por favor, añade un bus primero.")  

            

    elif opcion == 4:        #estado de las plazas
        if comprovar_buses():
            mostrar_buses()
        else:
            print("No hay buses disponibles. Por favor, añade un bus primero.")




