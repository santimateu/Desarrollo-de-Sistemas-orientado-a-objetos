# =============================================
# TP10 - PARTE 2: Patrón Chain of Responsibility
# El pedido pasa por una cadena de validadores (handlers).
# =============================================

from abc import ABC, abstractmethod

from modelos import formato_dinero


class ResultadoProcesamiento:
    def __init__(self):
        self.pasos = []  # lista de (nombre_validador, ok, mensaje)
        self.aprobado = False
        self.motivo = ""

    def registrar(self, nombre, ok, mensaje):
        self.pasos.append((nombre, ok, mensaje))

    def mostrar(self):
        for nombre, ok, mensaje in self.pasos:
            if ok:
                print(f"  {nombre} -> OK")
            else:
                print(f"  {nombre} -> ERROR ({mensaje})")
        if self.aprobado:
            print("  RESULTADO: Pedido aprobado")
        else:
            print(f"  RESULTADO: Pedido rechazado - {self.motivo}")


# ---------- Interfaz Handler ----------

class Validador(ABC):
    def __init__(self):
        self._siguiente = None

    def set_siguiente(self, siguiente):
        self._siguiente = siguiente
        return siguiente  # permite encadenar: a.set_siguiente(b).set_siguiente(c)

    @abstractmethod
    def get_nombre(self):
        """Nombre del paso, se muestra por consola."""

    @abstractmethod
    def validar(self, pedido):
        """Devuelve (ok, mensaje). Cada handler define su propia responsabilidad."""

    def procesar(self, pedido, resultado=None):
        if resultado is None:
            resultado = ResultadoProcesamiento()

        ok, mensaje = self.validar(pedido)
        resultado.registrar(self.get_nombre(), ok, mensaje)

        if not ok:
            # Se corta la cadena: los siguientes validadores no se ejecutan.
            resultado.aprobado = False
            resultado.motivo = mensaje
            return resultado

        if self._siguiente is not None:
            return self._siguiente.procesar(pedido, resultado)

        resultado.aprobado = True
        return resultado


def armar_cadena(*validadores):
    """Enlaza los validadores en el orden recibido y devuelve el primero."""
    for actual, siguiente in zip(validadores, validadores[1:]):
        actual.set_siguiente(siguiente)
    return validadores[0]


# ---------- Handlers concretos ----------

class ValidarCliente(Validador):
    def get_nombre(self):
        return "Validar Cliente"

    def validar(self, pedido):
        cliente = pedido.get_cliente()
        if not cliente.esta_activo():
            return False, f"El cliente {cliente.get_nombre()} está inactivo o bloqueado"
        return True, ""


class ValidarStock(Validador):
    def get_nombre(self):
        return "Validar Stock"

    def validar(self, pedido):
        inventario = pedido.get_inventario()
        for item in pedido.get_items():
            producto = item.get_producto()
            disponible = inventario.get_stock(producto)
            if disponible < item.get_cantidad():
                return False, (f"Sin stock de {producto.get_nombre()} "
                               f"(pedido: {item.get_cantidad()}, disponible: {disponible})")
        return True, ""


class ValidarPago(Validador):
    def get_nombre(self):
        return "Validar Pago"

    def validar(self, pedido):
        medio = pedido.get_cliente().get_medio_pago()
        total = pedido.get_precio_final()
        if medio.get_fondos_disponibles() < total:
            return False, (f"Fondos insuficientes en {medio.get_tipo()} "
                           f"(total: {formato_dinero(total)}, "
                           f"disponible: {formato_dinero(medio.get_fondos_disponibles())})")
        return True, ""
