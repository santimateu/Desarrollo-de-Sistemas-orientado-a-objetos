"""
PARTE 2 - NotificacionService depende de la abstracción Mensajeria.

- No conoce ninguna clase concreta (Email, SMS, ...).
- No usa if/switch para elegir el canal.
- Recibe el canal por constructor (inyección de dependencias).

Esta clase NO se modifica en la Parte 3.
"""
from mensajeria import Mensajeria


class NotificacionService:
    def __init__(self, mensajeria: Mensajeria):
        self.__mensajeria = mensajeria

    def notificar(self, mensaje):
        self.__mensajeria.enviar(mensaje)
