"""
CODIGO ORIGINAL (se conserva como referencia, sin ejecutar)

class ProcesadorPago:

    def __init__(self, tipo_pago):
        self.tipo_pago = tipo_pago

    def procesar(self, monto):

        if self.tipo_pago == "efectivo":
            total = monto * 0.90

        elif self.tipo_pago == "tarjeta":
            total = monto * 1.10

        elif self.tipo_pago == "transferencia":
            total = monto

        else:
            raise ValueError("Medio de pago inválido")

        print(f"Total a pagar: ${total}")

        with open("pagos.txt", "a") as archivo:
            archivo.write(
                f"{self.tipo_pago},{total}\\n"
            )

        print("Comprobante generado")
        print(f"Medio de pago: {self.tipo_pago}")
        print(f"Importe: ${total}")

        return total


pago1 = ProcesadorPago("efectivo")
pago1.procesar(1000)

pago2 = ProcesadorPago("tarjeta")
pago2.procesar(2000)

pago3 = ProcesadorPago("transferencia")
pago3.procesar(1500)
"""

# =====================================================
# CODIGO REFACTORIZADO APLICANDO EL PATRON STRATEGY
# (cada estrategia decide si le corresponde: aplica / calcular_total)
# =====================================================

from abc import ABC, abstractmethod


# Estrategia: cada medio de pago dice si aplica y como calcula.
class MedioPago(ABC):

    @abstractmethod
    def aplica(self, tipo):
        pass

    @abstractmethod
    def calcular_total(self, monto):
        pass


class Efectivo(MedioPago):
    def aplica(self, tipo):
        return tipo == "efectivo"

    def calcular_total(self, monto):
        return monto * 0.90


class Tarjeta(MedioPago):
    def aplica(self, tipo):
        return tipo == "tarjeta"

    def calcular_total(self, monto):
        return monto * 1.10


class Transferencia(MedioPago):
    def aplica(self, tipo):
        return tipo == "transferencia"

    def calcular_total(self, monto):
        return monto


# El procesador recorre la lista y usa la primera estrategia
# que aplique. Para agregar un medio nuevo, se crea la clase
# y se suma a la lista (sin if/elif).
def procesar_pago(tipo, monto):
    medios = [Efectivo(), Tarjeta(), Transferencia()]

    for medio in medios:
        if medio.aplica(tipo):
            total = medio.calcular_total(monto)

            print(f"Total a pagar: ${total}")

            with open("pagos.txt", "a") as archivo:
                archivo.write(f"{tipo},{total}\n")

            print("Comprobante generado")
            print(f"Medio de pago: {tipo}")
            print(f"Importe: ${total}")

            return total

    raise ValueError("Medio de pago inválido")


procesar_pago("efectivo", 1000)
procesar_pago("tarjeta", 2000)
procesar_pago("transferencia", 1500)
