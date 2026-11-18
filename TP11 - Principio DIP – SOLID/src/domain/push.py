"""
PARTE 3 - Extensión: nuevo canal de notificaciones push.

Solo se agrega una clase nueva que implementa Mensajeria.
NotificacionService no se modifica.
"""
from domain.mensajeria import Mensajeria


class Push(Mensajeria):
    def __init__(self, dispositivo):
        self.dispositivo = dispositivo

    def enviar(self, mensaje):
        print(f"[PUSH]     Al dispositivo {self.dispositivo}: {mensaje}")
