# 🔹 POO (Programación Orientada a Objetos)
# 👉 Forma de programar donde organizás el código en objetos que tienen datos y comportamiento.
    # Ejemplo:
    # Un auto que tiene color (dato) y puede arrancar (acción).


# 🔹 Clase
# 👉 “Molde” o “plantilla” para crear objetos.
    # class Auto:
    #     pass


# 🔹 Objeto
# 👉 Resultado de usar una clase.
    # a = Auto()


# 🔹 Instancia
# 👉 Sinónimo de objeto creado desde una clase.
    # a = Auto()  # a es una instancia de Auto


# 🔹 Herencia
# 👉 Una clase puede heredar características de otra.
    # class Animal:
    #     def hablar(self):
    #         print("Sonido")
    # class Perro(Animal):
    #     pass


# 🔹 Abstracción
# 👉 Mostrar solo lo importante y ocultar detalles.
    # class Auto:
    #     def arrancar(self):
    #         print("El auto arranca")  # no importa cómo internamente


# 🔹 Polimorfismo
# 👉 Diferentes objetos responden distinto al mismo método.
    # class Perro:
    #     def hablar(self):
    #         print("Guau")

    # class Gato:
    #     def hablar(self):
    #         print("Miau")


# 🔹 Constructor
# 👉 Método que se ejecuta al crear un objeto (__init__).
    # class Auto:
    #     def __init__(self, color):
    #         self.color = color

    # a = Auto("rojo")


# 🔹 Variable
# 👉 Espacio que guarda un valor.
    # x = 10


# 🔹 Valor primitivo
# 👉 Dato simple (no objeto complejo): int, float, bool, string.
    # edad = 25
    # nombre = "Juan"


# 🔹 Stack (pila)
# 👉 Memoria rápida donde se guardan llamadas a funciones y variables locales.
    # función() → entra al stack
    # termina → se elimina

    # Ejemplo mental:

    # llamar función → se apila
    # termina → se desapila


# 🔹 Heap (montículo)
# 👉 Memoria donde se guardan los objetos.
    # a = Auto()
    # 👉 a apunta a un objeto en el heap.

# 🔹 Resumen ultra corto
# POO → programar con objetos
# Clase → molde
# Objeto/instancia → producto del molde
# Herencia → reutilizar código
# Abstracción → simplificar
# Polimorfismo → misma acción, distinto comportamiento
# Constructor → inicializa objeto
# Variable → guarda datos
# Primitivo → dato simple
# Stack → llamadas/variables temporales
# Heap → objetos en memoria