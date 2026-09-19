# =============================================
# TP10 - Patrones de Diseño (Strategy + Chain of Responsibility)
# Modelo de dominio de la tienda online
# =============================================


def formato_dinero(monto):
    """Formatea un monto como $100.000 (separador de miles con punto)."""
    return "$" + f"{monto:,.0f}".replace(",", ".")


class Producto:
    def __init__(self, nombre, precio_unitario):
        self.__nombre = nombre
        self.__precio_unitario = precio_unitario

    def get_nombre(self):
        return self.__nombre

    def get_precio_unitario(self):
        return self.__precio_unitario


class ItemCompra:
    def __init__(self, producto, cantidad):
        self.__producto = producto
        self.__cantidad = cantidad

    def get_producto(self):
        return self.__producto

    def get_cantidad(self):
        return self.__cantidad

    def get_subtotal(self):
        return self.__producto.get_precio_unitario() * self.__cantidad


class MedioPago:
    def __init__(self, tipo, fondos_disponibles):
        self.__tipo = tipo
        self.__fondos_disponibles = fondos_disponibles

    def get_tipo(self):
        return self.__tipo

    def get_fondos_disponibles(self):
        return self.__fondos_disponibles


class Cliente:
    def __init__(self, nombre, medio_pago, activo=True):
        self.__nombre = nombre
        self.__medio_pago = medio_pago
        self.__activo = activo

    def get_nombre(self):
        return self.__nombre

    def get_medio_pago(self):
        return self.__medio_pago

    def esta_activo(self):
        return self.__activo


class Inventario:
    def __init__(self, stock_por_producto):
        # {nombre_producto: unidades disponibles}
        self.__stock = dict(stock_por_producto)

    def get_stock(self, producto):
        return self.__stock.get(producto.get_nombre(), 0)


class Compra:
    """Compra a la que se le pueden acoplar varias estrategias de precio."""

    def __init__(self, cliente, items):
        self.__cliente = cliente
        self.__items = list(items)
        self.__estrategias = []

    def get_cliente(self):
        return self.__cliente

    def get_items(self):
        return list(self.__items)

    def get_estrategias(self):
        return list(self.__estrategias)

    def agregar_estrategia(self, estrategia):
        self.__estrategias.append(estrategia)
        return self

    def get_cantidad_productos(self):
        return sum(item.get_cantidad() for item in self.__items)

    def get_precio_inicial(self):
        return sum(item.get_subtotal() for item in self.__items)


class Pedido:
    """Compra ya calculada, lista para pasar por la cadena de validaciones."""

    def __init__(self, compra, precio_final, inventario):
        self.__compra = compra
        self.__precio_final = precio_final
        self.__inventario = inventario

    def get_compra(self):
        return self.__compra

    def get_cliente(self):
        return self.__compra.get_cliente()

    def get_items(self):
        return self.__compra.get_items()

    def get_precio_final(self):
        return self.__precio_final

    def get_inventario(self):
        return self.__inventario
