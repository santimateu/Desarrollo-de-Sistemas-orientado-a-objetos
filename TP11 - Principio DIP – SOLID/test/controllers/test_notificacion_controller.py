import io
import unittest
from contextlib import redirect_stdout

from controllers.notificacion_controller import NotificacionController
from dao.destinatario_dao import DestinatarioDao


def capturar(funcion):
    salida = io.StringIO()
    with redirect_stdout(salida):
        funcion()
    return salida.getvalue()


class TestNotificacionController(unittest.TestCase):
    def setUp(self):
        self.controller = NotificacionController(DestinatarioDao())

    def test_notificar_canales_usa_email_whatsapp_y_sms(self):
        salida = capturar(self.controller.notificar_canales)
        self.assertIn("PARTE 2", salida)
        self.assertIn("[EMAIL]    Para usuario@empresa.com: Tu pedido fue confirmado", salida)
        self.assertIn("[WHATSAPP] Para +54 9 11 1234-5678: Tu pedido fue confirmado", salida)
        self.assertIn("[SMS]      Para +54 9 11 8765-4321: Tu pedido fue confirmado", salida)
        self.assertNotIn("[PUSH]", salida)

    def test_notificar_push(self):
        salida = capturar(self.controller.notificar_push)
        self.assertIn("PARTE 3", salida)
        self.assertIn("[PUSH]     Al dispositivo Android-Pixel-8: Tu pedido está en camino", salida)


if __name__ == "__main__":
    unittest.main()
