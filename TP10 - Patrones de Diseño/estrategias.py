# =============================================
# TP10 - PARTE 1: Patrón Strategy
# Cada regla de precio es una estrategia independiente.
# =============================================

from abc import ABC, abstractmethod

from modelos import formato_dinero

# Los descuentos se aplican antes que los cargos (envío), así el envío
# nunca queda afectado por un descuento porcentual.
PRIORIDAD_DESCUENTO = 1
PRIORIDAD_CARGO = 2


# ---------- Interfaz Strategy ----------

class EstrategiaPrecio(ABC):
    prioridad = PRIORIDAD_DESCUENTO

    @abstractmethod
    def get_nombre(self):
        """Texto que se muestra por consola (ej: 'Cliente VIP: -15%')."""

    @abstractmethod
    def aplicar(self, precio, compra):
        """Recibe el precio actual y devuelve el precio modificado."""

    def aplica(self, compra):
        """Permite que una estrategia decida si corresponde a la compra."""
        return True


# ---------- Estrategias de descuento porcentual ----------

class DescuentoPorcentual(EstrategiaPrecio):
    prioridad = PRIORIDAD_DESCUENTO

    def __init__(self, nombre, porcentaje):
        self._nombre = nombre
        self._porcentaje = porcentaje

    def get_nombre(self):
        return f"{self._nombre}: -{self._porcentaje}%"

    def aplicar(self, precio, compra):
        return precio * (1 - self._porcentaje / 100)


class ClienteComun(DescuentoPorcentual):
    def __init__(self):
        super().__init__("Cliente común", 0)


class ClientePremium(DescuentoPorcentual):
    def __init__(self):
        super().__init__("Cliente Premium", 10)


class ClienteVIP(DescuentoPorcentual):
    def __init__(self):
        super().__init__("Cliente VIP", 15)


class DescuentoPorCantidad(DescuentoPorcentual):
    """Descuento que solo corresponde si la cantidad de productos está en rango."""

    def __init__(self, nombre, porcentaje, minimo_exclusivo, maximo_inclusivo=None):
        super().__init__(nombre, porcentaje)
        self._minimo = minimo_exclusivo
        self._maximo = maximo_inclusivo

    def aplica(self, compra):
        cantidad = compra.get_cantidad_productos()
        if cantidad <= self._minimo:
            return False
        return self._maximo is None or cantidad <= self._maximo


class DescuentoMasDe5Productos(DescuentoPorCantidad):
    # Rango 6 a 10 unidades, para no acumularse con el de "más de 10".
    def __init__(self):
        super().__init__("Más de 5 productos", 5, minimo_exclusivo=5, maximo_inclusivo=10)


class DescuentoMasDe10Productos(DescuentoPorCantidad):
    def __init__(self):
        super().__init__("Más de 10 productos", 10, minimo_exclusivo=10)


class PromocionEspecial(DescuentoPorcentual):
    def __init__(self, porcentaje=10):
        super().__init__("Promoción especial", porcentaje)


# ---------- Estrategias de envío (cargo fijo) ----------

class CargoFijo(EstrategiaPrecio):
    prioridad = PRIORIDAD_CARGO

    def __init__(self, nombre, monto):
        self._nombre = nombre
        self._monto = monto

    def get_nombre(self):
        return f"{self._nombre}: +{formato_dinero(self._monto)}"

    def aplicar(self, precio, compra):
        return precio + self._monto


class RetiroEnSucursal(CargoFijo):
    def __init__(self):
        super().__init__("Retiro en sucursal", 0)


class EnvioNormal(CargoFijo):
    def __init__(self):
        super().__init__("Envío normal", 5000)


class EnvioExpress(CargoFijo):
    def __init__(self):
        super().__init__("Envío Express", 10000)


# ---------- Contexto: combina las estrategias de una compra ----------

class ResultadoPrecio:
    def __init__(self, precio_inicial, pasos, precio_final):
        self.precio_inicial = precio_inicial
        self.pasos = pasos  # lista de (descripcion, precio_resultante | None)
        self.precio_final = precio_final

    def mostrar(self):
        print(f"  Compra inicial: {formato_dinero(self.precio_inicial)}")
        for descripcion, precio in self.pasos:
            if precio is None:
                print(f"  {descripcion} -> no aplica")
            else:
                print(f"  {descripcion} -> {formato_dinero(precio)}")
        print(f"  PRECIO FINAL: {formato_dinero(self.precio_final)}")


class CalculadoraPrecio:
    """Aplica en cadena todas las estrategias de una compra sobre el precio."""

    def calcular(self, compra):
        precio = compra.get_precio_inicial()
        pasos = []
        # sorted es estable: dentro de cada prioridad se respeta el orden de carga.
        for estrategia in sorted(compra.get_estrategias(), key=lambda e: e.prioridad):
            if estrategia.aplica(compra):
                precio = estrategia.aplicar(precio, compra)
                pasos.append((estrategia.get_nombre(), precio))
            else:
                pasos.append((estrategia.get_nombre(), None))
        return ResultadoPrecio(compra.get_precio_inicial(), pasos, max(precio, 0))
