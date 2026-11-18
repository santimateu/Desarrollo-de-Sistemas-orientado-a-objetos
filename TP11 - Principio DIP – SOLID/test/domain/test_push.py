import io
import unittest
from contextlib import redirect_stdout

from domain.mensajeria import Mensajeria
from domain.push import Push


class TestPush(unittest.TestCase):
    def test_push_implementa_mensajeria(self):
        self.assertIsInstance(Push("Pixel"), Mensajeria)

    def test_push_envia(self):
        salida = io.StringIO()
        with redirect_stdout(salida):
            Push("Pixel").enviar("Hola")
        self.assertEqual(salida.getvalue().strip(), "[PUSH]     Al dispositivo Pixel: Hola")


if __name__ == "__main__":
    unittest.main()
