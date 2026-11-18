import io
import unittest
from contextlib import redirect_stdout

from domain.mensajeria import Mensajeria, Email, WhatsApp, SMS


def capturar(funcion, *args):
    salida = io.StringIO()
    with redirect_stdout(salida):
        funcion(*args)
    return salida.getvalue().strip()


class TestMensajeria(unittest.TestCase):
    def test_no_se_puede_instanciar_la_abstraccion(self):
        with self.assertRaises(TypeError):
            Mensajeria()

    def test_subclase_sin_enviar_no_se_puede_instanciar(self):
        class Incompleta(Mensajeria):
            pass

        with self.assertRaises(TypeError):
            Incompleta()


class TestCanales(unittest.TestCase):
    def test_canales_implementan_mensajeria(self):
        for canal in (Email("a@b.com"), WhatsApp("123"), SMS("456")):
            self.assertIsInstance(canal, Mensajeria)

    def test_email_envia(self):
        self.assertEqual(
            capturar(Email("a@b.com").enviar, "Hola"),
            "[EMAIL]    Para a@b.com: Hola",
        )

    def test_whatsapp_envia(self):
        self.assertEqual(
            capturar(WhatsApp("123").enviar, "Hola"),
            "[WHATSAPP] Para 123: Hola",
        )

    def test_sms_envia(self):
        self.assertEqual(
            capturar(SMS("456").enviar, "Hola"),
            "[SMS]      Para 456: Hola",
        )


if __name__ == "__main__":
    unittest.main()
