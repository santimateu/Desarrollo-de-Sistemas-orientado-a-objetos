# =============================================
# TP10 - DESAFÍO
# Se agregan DescuentoBlackFriday y ValidarLimiteCompra SIN modificar
# ninguna estrategia ni validador existente (estrategias.py y cadena.py
# quedan intactos: solo se importan y se extienden).
# Ejecutar con: python desafio.py
# =============================================

from modelos import Producto, ItemCompra, MedioPago, Cliente, Inventario, Compra, Pedido, formato_dinero
from estrategias import DescuentoPorcentual, CalculadoraPrecio, ClienteVIP, EnvioNormal
from cadena import Validador, armar_cadena, ValidarCliente, ValidarStock, ValidarPago


class DescuentoBlackFriday(DescuentoPorcentual):
    def __init__(self, porcentaje=30):
        super().__init__("Descuento Black Friday", porcentaje)


class ValidarLimiteCompra(Validador):
    def __init__(self, limite):
        super().__init__()
        self._limite = limite

    def get_nombre(self):
        return "Validar Límite de Compra"

    def validar(self, pedido):
        if pedido.get_precio_final() > self._limite:
            return False, (f"El total {formato_dinero(pedido.get_precio_final())} supera "
                           f"el límite de compra de {formato_dinero(self._limite)}")
        return True, ""


def procesar(titulo, compra, inventario, limite):
    print("=" * 60)
    print(titulo)
    print("=" * 60)

    print("[Strategy]")
    precio = CalculadoraPrecio().calcular(compra)
    precio.mostrar()

    print(f"[Chain of Responsibility] (límite de compra: {formato_dinero(limite)})")
    pedido = Pedido(compra, precio.precio_final, inventario)
    # Se inserta el nuevo eslabón en la composición de la cadena, sin tocar los otros.
    cadena = armar_cadena(ValidarCliente(), ValidarLimiteCompra(limite),
                          ValidarStock(), ValidarPago())
    cadena.procesar(pedido).mostrar()
    print()


def main():
    tv = Producto("Smart TV", 400000)
    inventario = Inventario({"Smart TV": 10})
    cliente = Cliente("Lucía Fernández", MedioPago("Tarjeta de crédito", 2000000))

    # Black Friday con un total dentro del límite -> aprobado
    compra_ok = (Compra(cliente, [ItemCompra(tv, 1)])
                 .agregar_estrategia(ClienteVIP())
                 .agregar_estrategia(DescuentoBlackFriday(30))
                 .agregar_estrategia(EnvioNormal()))
    procesar("DESAFÍO 1: Black Friday dentro del límite", compra_ok, inventario, 500000)

    # Total por encima del límite -> rechazado por el nuevo validador
    # (Validar Stock y Validar Pago no llegan a ejecutarse)
    compra_limite = (Compra(cliente, [ItemCompra(tv, 3)])
                     .agregar_estrategia(ClienteVIP())
                     .agregar_estrategia(DescuentoBlackFriday(30))
                     .agregar_estrategia(EnvioNormal()))
    procesar("DESAFÍO 2: Rechazado por límite de compra", compra_limite, inventario, 500000)


if __name__ == "__main__":
    main()
