# =============================================
# TP10 - Patrones de Diseño (Strategy + Chain of Responsibility)
# Clases del dominio de la tienda online
# =============================================


def formato_dinero(monto):
    """Muestra un monto como $100.000"""
    return "$" + f"{monto:,.0f}".replace(",", ".")


class Producto:
    def __init__(self, nombre, precio, stock):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def get_stock(self):
        return self.__stock


class Cliente:
    def __init__(self, nombre, saldo, activo=True):
        self.__nombre = nombre
        self.__saldo = saldo
        self.__activo = activo

    def get_nombre(self):
        return self.__nombre

    def get_saldo(self):
        return self.__saldo

    def esta_activo(self):
        return self.__activo


class Compra:
    """Una compra puede tener varias estrategias de precio (Strategy)."""

    def __init__(self, cliente, producto, cantidad):
        self.__cliente = cliente
        self.__producto = producto
        self.__cantidad = cantidad
        self.__estrategias = []
        self.__precio_final = 0

    def get_cliente(self):
        return self.__cliente

    def get_producto(self):
        return self.__producto

    def get_cantidad(self):
        return self.__cantidad

    def get_precio_inicial(self):
        return self.__producto.get_precio() * self.__cantidad

    def get_precio_final(self):
        return self.__precio_final

    def agregar_estrategia(self, estrategia):
        self.__estrategias.append(estrategia)

    def calcular_precio_final(self):
        precio = self.get_precio_inicial()
        print(f"  Compra inicial: {formato_dinero(precio)}")

        # Polimorfismo: cada estrategia sabe cómo modificar el precio
        for estrategia in self.__estrategias:
            precio = estrategia.aplicar(precio)
            print(f"  {estrategia.get_descripcion()} -> {formato_dinero(precio)}")

        self.__precio_final = precio
        print(f"  PRECIO FINAL: {formato_dinero(precio)}")
