# Services - Lógica de negocio
# Se encarga de las operaciones sobre las herramientas usando el DAO y el Domain

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from Model.Domain.herramienta import Herramienta

class HerramientaService:
    def __init__(self, dao):
        self.__dao = dao

    def agregar(self, nombre, marca, precio):
        herramienta = Herramienta(nombre, marca, precio)
        self.__dao.guardar(herramienta)
        return herramienta

    def listar(self):
        return self.__dao.obtener_todas()

    def actualizar_precio(self, nombre, nuevo_precio):
        herramienta = self.__dao.buscar_por_nombre(nombre)
        if herramienta:
            herramienta.set_precio(nuevo_precio)
            return True
        return False
