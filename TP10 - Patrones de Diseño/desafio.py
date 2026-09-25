# =============================================
# TP10 - DESAFÍO
# Se agregan DescuentoBlackFriday y ValidarLimiteCompra sin modificar
# las clases que ya existían: solo se heredan.
# Ejecutar con: python desafio.py
# =============================================

from modelos import Producto, Cliente, Compra
from estrategias import Descuento, ClienteVIP, EnvioNormal
from cadena import Validador, ValidarCliente, ValidarStock, ValidarPago


class DescuentoBlackFriday(Descuento):
    def __init__(self):
        super().__init__("Descuento Black Friday", 30)


class ValidarLimiteCompra(Validador):
    def __init__(self, limite):
        super().__init__()
        self._limite = limite

    def get_nombre(self):
        return "Validar Límite de Compra"

    def es_valido(self, compra):
        return compra.get_precio_final() <= self._limite


def procesar(titulo, compra):
    print("=" * 50)
    print(titulo)
    print("=" * 50)
    print("[Strategy]")
    compra.calcular_precio_final()
    print("[Chain of Responsibility] (límite: $500.000)")
    cadena = ValidarCliente()
    cadena.set_siguiente(ValidarLimiteCompra(500000)) \
          .set_siguiente(ValidarStock()) \
          .set_siguiente(ValidarPago())
    cadena.procesar(compra)
    print()


def main():
    tv = Producto("Smart TV", 400000, stock=10)
    lucia = Cliente("Lucía Fernández", saldo=2000000)

    compra1 = Compra(lucia, tv, 1)
    compra1.agregar_estrategia(ClienteVIP())
    compra1.agregar_estrategia(DescuentoBlackFriday())
    compra1.agregar_estrategia(EnvioNormal())
    procesar("DESAFÍO 1: Black Friday dentro del límite", compra1)

    compra2 = Compra(lucia, tv, 3)
    compra2.agregar_estrategia(ClienteVIP())
    compra2.agregar_estrategia(DescuentoBlackFriday())
    compra2.agregar_estrategia(EnvioNormal())
    procesar("DESAFÍO 2: Rechazado por superar el límite", compra2)


if __name__ == "__main__":
    main()
