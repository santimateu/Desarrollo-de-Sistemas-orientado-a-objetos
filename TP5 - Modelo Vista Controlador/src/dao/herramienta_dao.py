# DAO - Data Access Object
# Simula el almacenamiento de datos (en una lista, como si fuera una base de datos)

class HerramientaDAO:
    def __init__(self):
        self.__herramientas = []

    def guardar(self, herramienta):
        self.__herramientas.append(herramienta)

    def obtener_todas(self):
        return self.__herramientas

    def buscar_por_nombre(self, nombre):
        for h in self.__herramientas:
            if h.get_nombre() == nombre:
                return h
        return None
