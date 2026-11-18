import io
import unittest
from contextlib import redirect_stdout

from app import App


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = App()

    def test_registra_las_rutas(self):
        self.assertEqual(self.app.rutas(), ["/notificaciones", "/notificaciones/push"])

    def test_atender_ruta_existente(self):
        salida = io.StringIO()
        with redirect_stdout(salida):
            self.app.atender("/notificaciones/push")
        self.assertIn("[PUSH]", salida.getvalue())

    def test_atender_ruta_inexistente(self):
        salida = io.StringIO()
        with redirect_stdout(salida):
            self.app.atender("/no-existe")
        self.assertEqual(salida.getvalue().strip(), "Ruta no encontrada: /no-existe")


if __name__ == "__main__":
    unittest.main()
