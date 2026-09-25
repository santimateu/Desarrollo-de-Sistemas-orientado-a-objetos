# =============================================
# TP10 - Strategy + Chain of Responsibility
# Ejecutar con: python main.py
# =============================================

from modelos import Producto, Cliente, Compra
from estrategias import (
    ClienteComun, ClientePremium, ClienteVIP,
    DescuentoMasDe10Productos, PromocionEspecial,
    RetiroEnSucursal, EnvioNormal, EnvioExpress,
)
from cadena import ValidarCliente, ValidarStock, ValidarPago


def armar_cadena():
    cadena = ValidarCliente()
    cadena.set_siguiente(ValidarStock()).set_siguiente(ValidarPago())
    return cadena


def procesar(titulo, compra):
    print("=" * 50)
    print(titulo)
    print("=" * 50)
    print("[Strategy]")
    compra.calcular_precio_final()
    print("[Chain of Responsibility]")
    armar_cadena().procesar(compra)
    print()


def main():
    auriculares = Producto("Auriculares", 10000, stock=20)
    teclado = Producto("Teclado", 25000, stock=2)

    # 1) Pedido aprobado (ejemplo del enunciado: $100.000 -> $82.675)
    juan = Cliente("Juan Pérez", saldo=200000)
    compra1 = Compra(juan, auriculares, 10)
    compra1.agregar_estrategia(ClienteVIP())
    compra1.agregar_estrategia(DescuentoMasDe10Productos())
    compra1.agregar_estrategia(PromocionEspecial(5))
    compra1.agregar_estrategia(EnvioExpress())
    procesar("ESCENARIO 1: Pedido aprobado", compra1)

    # 2) Pedido rechazado por falta de stock
    maria = Cliente("María Gómez", saldo=500000)
    compra2 = Compra(maria, teclado, 5)
    compra2.agregar_estrategia(ClientePremium())
    compra2.agregar_estrategia(EnvioNormal())
    procesar("ESCENARIO 2: Rechazado por falta de stock", compra2)

    # 3) Pedido rechazado por problema en el pago
    carlos = Cliente("Carlos Ruiz", saldo=30000)
    compra3 = Compra(carlos, auriculares, 4)
    compra3.agregar_estrategia(ClienteComun())
    compra3.agregar_estrategia(RetiroEnSucursal())
    procesar("ESCENARIO 3: Rechazado por problema en el pago", compra3)


if __name__ == "__main__":
    main()
