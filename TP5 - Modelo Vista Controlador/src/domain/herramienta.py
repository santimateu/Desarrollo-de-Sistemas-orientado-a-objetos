# Domain - Entidad Herramienta

class Herramienta:
    def __init__(self, nombre, marca, precio):
        self.__nombre = nombre
        self.__marca = marca
        self.__precio = precio

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio
