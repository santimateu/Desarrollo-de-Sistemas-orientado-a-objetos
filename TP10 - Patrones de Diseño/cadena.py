# =============================================
# TP10 - PARTE 2: Patrón Chain of Responsibility
# El pedido pasa por una cadena de validadores. Si uno falla, se corta.
# =============================================

from abc import ABC, abstractmethod


# ---------- Abstracción: el eslabón base de la cadena ----------

class Validador(ABC):
    def __init__(self):
        self._siguiente = None

    def set_siguiente(self, validador):
        self._siguiente = validador
        return validador  # permite escribir a.set_siguiente(b).set_siguiente(c)

    @abstractmethod
    def es_valido(self, compra):
        """Cada validador revisa una sola cosa y devuelve True o False."""

    @abstractmethod
    def get_nombre(self):
        """Nombre que se muestra por consola."""

    def procesar(self, compra):
        if not self.es_valido(compra):
            print(f"  {self.get_nombre()} -> ERROR")
            print("  RESULTADO: Pedido rechazado")
            return False

        print(f"  {self.get_nombre()} -> OK")
        if self._siguiente is None:
            print("  RESULTADO: Pedido aprobado")
            return True
        return self._siguiente.procesar(compra)


# ---------- Herencia + polimorfismo: validadores concretos ----------

class ValidarCliente(Validador):
    def get_nombre(self):
        return "Validar Cliente"

    def es_valido(self, compra):
        return compra.get_cliente().esta_activo()


class ValidarStock(Validador):
    def get_nombre(self):
        return "Validar Stock"

    def es_valido(self, compra):
        return compra.get_producto().get_stock() >= compra.get_cantidad()


class ValidarPago(Validador):
    def get_nombre(self):
        return "Validar Pago"

    def es_valido(self, compra):
        return compra.get_cliente().get_saldo() >= compra.get_precio_final()
