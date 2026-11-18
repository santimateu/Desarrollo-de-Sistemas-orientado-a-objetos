import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

import index


def ejecutar_main(argv):
    salida = io.StringIO()
    with patch("sys.argv", ["index.py", *argv]), redirect_stdout(salida):
        index.main()
    return salida.getvalue()


class TestIndex(unittest.TestCase):
    def test_sin_argumentos_ejecuta_todas_las_rutas(self):
        salida = ejecutar_main([])
        for canal in ("[EMAIL]", "[WHATSAPP]", "[SMS]", "[PUSH]"):
            self.assertIn(canal, salida)

    def test_con_una_ruta_ejecuta_solo_esa(self):
        salida = ejecutar_main(["/notificaciones/push"])
        self.assertIn("[PUSH]", salida)
        self.assertNotIn("[EMAIL]", salida)


if __name__ == "__main__":
    unittest.main()
