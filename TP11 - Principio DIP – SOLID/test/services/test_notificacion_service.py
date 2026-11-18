import unittest

from domain.mensajeria import Mensajeria
from services.notificacion_service import NotificacionService


class MensajeriaFalsa(Mensajeria):
    """Canal falso: gracias a DIP se puede inyectar sin tocar el servicio."""

    def __init__(self):
        self.enviados = []

    def enviar(self, mensaje):
        self.enviados.append(mensaje)


class TestNotificacionService(unittest.TestCase):
    def test_notificar_delega_en_la_mensajeria_inyectada(self):
        canal = MensajeriaFalsa()
        NotificacionService(canal).notificar("Hola")
        self.assertEqual(canal.enviados, ["Hola"])

    def test_cada_notificacion_se_envia_una_vez(self):
        canal = MensajeriaFalsa()
        servicio = NotificacionService(canal)
        servicio.notificar("Uno")
        servicio.notificar("Dos")
        self.assertEqual(canal.enviados, ["Uno", "Dos"])


if __name__ == "__main__":
    unittest.main()
