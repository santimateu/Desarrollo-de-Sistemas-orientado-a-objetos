import unittest

from dao.destinatario_dao import DestinatarioDao


class TestDestinatarioDao(unittest.TestCase):
    def setUp(self):
        self.dao = DestinatarioDao()

    def test_obtiene_destinatario_de_cada_canal(self):
        self.assertEqual(self.dao.obtener("email"), "usuario@empresa.com")
        self.assertEqual(self.dao.obtener("whatsapp"), "+54 9 11 1234-5678")
        self.assertEqual(self.dao.obtener("sms"), "+54 9 11 8765-4321")
        self.assertEqual(self.dao.obtener("push"), "Android-Pixel-8")

    def test_canal_inexistente_lanza_error(self):
        with self.assertRaises(KeyError):
            self.dao.obtener("fax")


if __name__ == "__main__":
    unittest.main()
