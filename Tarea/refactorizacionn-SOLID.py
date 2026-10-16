"""
CODIGO ORIGINAL (se conserva como referencia, sin ejecutar)

class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def calcular_sueldo(self):
        descuento = self.sueldo * 0.10
        return self.sueldo - descuento

    def guardar_empleado(self):
        with open("empleados.txt", "a") as archivo:
            archivo.write(
                f"{self.nombre},{self.sueldo}\\n"
            )

    def generar_recibo(self):
        print("RECIBO DE SUELDO")
        print(f"Empleado: {self.nombre}")
        print(f"Sueldo neto: {self.calcular_sueldo()}")

    def enviar_notificacion(self):
        print(
            f"Enviando email a {self.nombre}"
        )


empleado = Empleado("Juan", 500000)

empleado.guardar_empleado()
empleado.generar_recibo()
empleado.enviar_notificacion()
"""

# =====================================================
# CODIGO REFACTORIZADO APLICANDO SOLID
# =====================================================

from abc import ABC, abstractmethod


# S - Responsabilidad unica: Empleado solo guarda sus datos.
class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo


# O - Abierto/Cerrado: se pueden agregar nuevos descuentos
# creando otra clase, sin modificar las existentes.
class Descuento(ABC):
    @abstractmethod
    def aplicar(self, sueldo):
        pass


class DescuentoFijo(Descuento):
    def __init__(self, porcentaje):
        self.porcentaje = porcentaje

    def aplicar(self, sueldo):
        return sueldo - sueldo * self.porcentaje


# S - Responsabilidad unica: solo calcula el sueldo neto.
class CalculadoraSueldo:
    def __init__(self, descuento: Descuento):
        self.descuento = descuento

    def calcular(self, empleado):
        return self.descuento.aplicar(empleado.sueldo)


# S - Responsabilidad unica: solo se encarga de guardar.
class RepositorioEmpleados:
    def __init__(self, archivo="empleados.txt"):
        self.archivo = archivo

    def guardar(self, empleado):
        with open(self.archivo, "a") as archivo:
            archivo.write(f"{empleado.nombre},{empleado.sueldo}\n")


# S - Responsabilidad unica: solo genera el recibo.
class GeneradorRecibo:
    def __init__(self, calculadora: CalculadoraSueldo):
        self.calculadora = calculadora

    def generar(self, empleado):
        print("RECIBO DE SUELDO")
        print(f"Empleado: {empleado.nombre}")
        print(f"Sueldo neto: {self.calculadora.calcular(empleado)}")


# I / D - Interfaz chica y especifica; el codigo depende de la
# abstraccion Notificador y no de una implementacion concreta.
class Notificador(ABC):
    @abstractmethod
    def enviar(self, empleado):
        pass


# L - Sustitucion de Liskov: cualquier Notificador puede
# reemplazar a otro sin romper el programa.
class NotificadorEmail(Notificador):
    def enviar(self, empleado):
        print(f"Enviando email a {empleado.nombre}")


class NotificadorSMS(Notificador):
    def enviar(self, empleado):
        print(f"Enviando SMS a {empleado.nombre}")


# Uso
empleado = Empleado("Juan", 500000)

calculadora = CalculadoraSueldo(DescuentoFijo(0.10))
repositorio = RepositorioEmpleados()
recibo = GeneradorRecibo(calculadora)
notificador: Notificador = NotificadorEmail()

repositorio.guardar(empleado)
recibo.generar(empleado)
notificador.enviar(empleado)
