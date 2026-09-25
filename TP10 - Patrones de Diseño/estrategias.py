# =============================================
# TP10 - PARTE 1: Patrón Strategy
# Cada regla de precio es una clase distinta que hereda de EstrategiaPrecio.
# =============================================

from abc import ABC, abstractmethod

from modelos import formato_dinero


# ---------- Abstracción: la interfaz de todas las estrategias ----------

class EstrategiaPrecio(ABC):
    @abstractmethod
    def aplicar(self, precio):
        """Recibe el precio actual y devuelve el precio nuevo."""

    @abstractmethod
    def get_descripcion(self):
        """Texto que se muestra por consola."""


# ---------- Herencia: descuentos ----------

class Descuento(EstrategiaPrecio):
    def __init__(self, nombre, porcentaje):
        self._nombre = nombre
        self._porcentaje = porcentaje

    def aplicar(self, precio):
        return precio - precio * self._porcentaje / 100

    def get_descripcion(self):
        return f"{self._nombre}: -{self._porcentaje}%"


class ClienteComun(Descuento):
    def __init__(self):
        super().__init__("Cliente común", 0)


class ClientePremium(Descuento):
    def __init__(self):
        super().__init__("Cliente Premium", 10)


class ClienteVIP(Descuento):
    def __init__(self):
        super().__init__("Cliente VIP", 15)


class DescuentoMasDe5Productos(Descuento):
    def __init__(self):
        super().__init__("Más de 5 productos", 5)


class DescuentoMasDe10Productos(Descuento):
    def __init__(self):
        super().__init__("Más de 10 productos", 10)


class PromocionEspecial(Descuento):
    def __init__(self, porcentaje):
        super().__init__("Promoción especial", porcentaje)


# ---------- Herencia: envíos ----------

class Envio(EstrategiaPrecio):
    def __init__(self, nombre, costo):
        self._nombre = nombre
        self._costo = costo

    def aplicar(self, precio):
        return precio + self._costo

    def get_descripcion(self):
        return f"{self._nombre}: +{formato_dinero(self._costo)}"


class RetiroEnSucursal(Envio):
    def __init__(self):
        super().__init__("Retiro en sucursal", 0)


class EnvioNormal(Envio):
    def __init__(self):
        super().__init__("Envío normal", 5000)


class EnvioExpress(Envio):
    def __init__(self):
        super().__init__("Envío Express", 10000)
