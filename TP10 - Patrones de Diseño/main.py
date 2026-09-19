# =============================================
# TP10 - Strategy + Chain of Responsibility
# Tienda online: cálculo del precio final y procesamiento del pedido
# Ejecutar con: python main.py
# =============================================

from modelos import Producto, ItemCompra, MedioPago, Cliente, Inventario, Compra, Pedido
from estrategias import (
    CalculadoraPrecio, ClienteVIP, ClientePremium, ClienteComun,
    DescuentoMasDe5Productos, DescuentoMasDe10Productos, PromocionEspecial,
    EnvioExpress, EnvioNormal, RetiroEnSucursal,
)
from cadena import armar_cadena, ValidarCliente, ValidarStock, ValidarPago


def procesar_compra(titulo, compra, inventario):
    print("=" * 60)
    print(titulo)
    print("=" * 60)

    print("[Parte 1 - Strategy]")
    resultado_precio = CalculadoraPrecio().calcular(compra)
    resultado_precio.mostrar()

    print("[Parte 2 - Chain of Responsibility]")
    pedido = Pedido(compra, resultado_precio.precio_final, inventario)
    cadena = armar_cadena(ValidarCliente(), ValidarStock(), ValidarPago())
    cadena.procesar(pedido).mostrar()
    print()


def main():
    cable = Producto("Cable HDMI", 5000)
    mouse = Producto("Mouse", 10000)

    # Ejemplo del enunciado: $100.000 -> VIP -15% -> cantidad -10% -> promo -5% -> Express +$10.000
    items = [ItemCompra(cable, 10), ItemCompra(mouse, 5)]  # 15 productos, $100.000

    # 1) Pedido aprobado
    cliente_ok = Cliente("Juan Pérez", MedioPago("Tarjeta de crédito", 200000))
    compra_ok = (Compra(cliente_ok, items)
                 .agregar_estrategia(ClienteVIP())
                 .agregar_estrategia(DescuentoMasDe10Productos())
                 .agregar_estrategia(PromocionEspecial(5))
                 .agregar_estrategia(EnvioExpress()))
    procesar_compra("ESCENARIO 1: Pedido aprobado", compra_ok,
                    Inventario({"Cable HDMI": 50, "Mouse": 20}))

    # 2) Pedido rechazado por falta de stock
    cliente_stock = Cliente("María Gómez", MedioPago("Débito", 200000))
    compra_stock = (Compra(cliente_stock, items)
                    .agregar_estrategia(ClientePremium())
                    .agregar_estrategia(DescuentoMasDe10Productos())
                    .agregar_estrategia(EnvioNormal()))
    procesar_compra("ESCENARIO 2: Rechazado por falta de stock", compra_stock,
                    Inventario({"Cable HDMI": 50, "Mouse": 2}))

    # 3) Pedido rechazado por problema en el pago
    cliente_pago = Cliente("Carlos Ruiz", MedioPago("Tarjeta de débito", 30000))
    compra_pago = (Compra(cliente_pago, items[:1] + [ItemCompra(mouse, 2)])  # 12 productos
                   .agregar_estrategia(ClienteComun())
                   .agregar_estrategia(DescuentoMasDe10Productos())
                   .agregar_estrategia(DescuentoMasDe5Productos())  # no aplica: son más de 10
                   .agregar_estrategia(RetiroEnSucursal()))
    procesar_compra("ESCENARIO 3: Rechazado por problema en el pago", compra_pago,
                    Inventario({"Cable HDMI": 50, "Mouse": 20}))


if __name__ == "__main__":
    main()
