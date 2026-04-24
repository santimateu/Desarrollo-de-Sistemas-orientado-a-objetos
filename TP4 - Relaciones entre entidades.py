class Usuario:
    def __init__(self, nombre):
        # Inicializamos los atributos del objeto
        self.__nombre = nombre
        self.__herramientas = []

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_herramientas(self):
        return self.__herramientas

    def agregar_herramienta(self, herramienta):
        self.__herramientas.append(herramienta)

class Herramienta:
    def __init__(self, nombre, fabricante):
        # Inicializamos los atributos del objeto
        self.__nombre = nombre
        self.__fabricante = fabricante

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_fabricante(self):
        return self.__fabricante

    def set_fabricante(self, fabricante):
        self.__fabricante = fabricante

class Fabricante:
    def __init__(self, nombre, pais):
        # Inicializamos los atributos del objeto
        self.__nombre = nombre
        self.__pais = pais

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_pais(self):
        return self.__pais

    def set_pais(self, pais):
        self.__pais = pais

class Cliente:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__herramientas_alquiladas = []

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_herramientas_alquiladas(self):
        return self.__herramientas_alquiladas

    def alquilar(self, herramienta):
        self.__herramientas_alquiladas.append(herramienta)

# =============================================
# Tema: Sistema de alquiler de herramientas
# =============================================
# Clases y relaciones:
# - Fabricante: empresa que fabrica herramientas (ej: Bosch, Stanley)
# - Herramienta: herramienta física que pertenece a un Fabricante (Composición)
# - Usuario: persona que posee herramientas (Agregación con Herramienta)
# - Cliente: persona que alquila herramientas (Agregación con Herramienta)
#
# Relaciones:
# - Fabricante → Herramienta: Composición (la herramienta depende del fabricante)
# - Usuario    → Herramienta: Agregación  (el usuario tiene herramientas)
# - Cliente    → Herramienta: Agregación  (el cliente alquila herramientas)
# =============================================

# --- Creación de objetos ---
fab1 = Fabricante("Bosch", "Alemania")
fab2 = Fabricante("Stanley", "Estados Unidos")

herr1 = Herramienta("Taladro", fab1)
herr2 = Herramienta("Martillo", fab2)

user = Usuario("Juan")
user.agregar_herramienta(herr1)
user.agregar_herramienta(herr2)

cliente = Cliente("Pedro")
cliente.alquilar(herr1)

# --- Prueba de uso ---
print("=== Sistema de Alquiler de Herramientas ===")
print()
print(f"Fabricante 1: {fab1.get_nombre()} ({fab1.get_pais()})")
print(f"Fabricante 2: {fab2.get_nombre()} ({fab2.get_pais()})")
print()
print(f"Herramienta 1: {herr1.get_nombre()} | Fabricante: {herr1.get_fabricante().get_nombre()}")
print(f"Herramienta 2: {herr2.get_nombre()} | Fabricante: {herr2.get_fabricante().get_nombre()}")
print()
print(f"Usuario: {user.get_nombre()}")
for h in user.get_herramientas():
    print(f"  - Tiene: {h.get_nombre()} (fabricado por {h.get_fabricante().get_nombre()})")
print()
print(f"Cliente: {cliente.get_nombre()}")
for h in cliente.get_herramientas_alquiladas():
    print(f"  - Alquiló: {h.get_nombre()} (fabricado por {h.get_fabricante().get_nombre()})")







