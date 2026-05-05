import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from Model.DAO.herramienta_dao import HerramientaDAO
from Model.Services.herramienta_service import HerramientaService


# =====================
# VISTA (frontend)
# =====================
class HerramientaVista:
    def mostrar_herramienta(self, nombre, marca, precio):
        print(f"  - {nombre} | Marca: {marca} | Precio: ${precio}")

    def mostrar_lista(self, herramientas):
        print("=== Lista de herramientas ===")
        for h in herramientas:
            self.mostrar_herramienta(h.get_nombre(), h.get_marca(), h.get_precio())

    def mostrar_mensaje(self, mensaje):
        print(mensaje)


# =====================
# CONTROLADOR (backend)
# =====================
class HerramientaControlador:
    def __init__(self):
        self.__dao = HerramientaDAO()
        self.__service = HerramientaService(self.__dao)
        self.__vista = HerramientaVista()

    def agregar(self, nombre, marca, precio):
        self.__service.agregar(nombre, marca, precio)
        self.__vista.mostrar_mensaje(f"Agregada: '{nombre}'.")

    def mostrar_todas(self):
        herramientas = self.__service.listar()
        self.__vista.mostrar_lista(herramientas)

    def actualizar_precio(self, nombre, nuevo_precio):
        exito = self.__service.actualizar_precio(nombre, nuevo_precio)
        if exito:
            self.__vista.mostrar_mensaje(f"Precio de '{nombre}' actualizado a ${nuevo_precio}.")
        else:
            self.__vista.mostrar_mensaje(f"No se encontro '{nombre}'.")


# =====================
# PROGRAMA PRINCIPAL
# =====================
controlador = HerramientaControlador()

controlador.agregar("Taladro", "Bosch", 15000)
controlador.agregar("Martillo", "Stanley", 3500)
controlador.agregar("Sierra circular", "Dewalt", 22000)

print()
controlador.mostrar_todas()

print()
controlador.actualizar_precio("Martillo", 4000)

print()
controlador.mostrar_todas()