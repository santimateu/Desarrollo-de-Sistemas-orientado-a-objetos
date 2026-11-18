import unittest

from controllers.notificacion_controller import NotificacionController
from dao.destinatario_dao import DestinatarioDao
from routes.notificacion_routes import notificacion_routes


class TestNotificacionRoutes(unittest.TestCase):
    def setUp(self):
        self.controller = NotificacionController(DestinatarioDao())
        self.rutas = notificacion_routes(self.controller)

    def test_define_las_rutas_esperadas(self):
        self.assertEqual(set(self.rutas), {"/notificaciones", "/notificaciones/push"})

    def test_cada_ruta_apunta_al_metodo_del_controlador(self):
        self.assertEqual(self.rutas["/notificaciones"], self.controller.notificar_canales)
        self.assertEqual(self.rutas["/notificaciones/push"], self.controller.notificar_push)


if __name__ == "__main__":
    unittest.main()
