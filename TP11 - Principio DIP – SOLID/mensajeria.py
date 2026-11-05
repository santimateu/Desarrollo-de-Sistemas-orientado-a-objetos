"""
PARTE 2 - Abstracción Mensajeria y sus implementaciones concretas.
"""
from abc import ABC, abstractmethod


class Mensajeria(ABC):
    """Abstracción de la que depende NotificacionService."""

    @abstractmethod
    def enviar(self, mensaje):
        pass


class Email(Mensajeria):
    def __init__(self, direccion):
        self.direccion = direccion

    def enviar(self, mensaje):
        print(f"[EMAIL]    Para {self.direccion}: {mensaje}")


class WhatsApp(Mensajeria):
    def __init__(self, numero):
        self.numero = numero

    def enviar(self, mensaje):
        print(f"[WHATSAPP] Para {self.numero}: {mensaje}")


class SMS(Mensajeria):
    def __init__(self, numero):
        self.numero = numero

    def enviar(self, mensaje):
        print(f"[SMS]      Para {self.numero}: {mensaje}")
