"""
Archivo principal de la aplicación: arma las dependencias y registra las rutas.
"""
from dao.destinatario_dao import DestinatarioDao
from controllers.notificacion_controller import NotificacionController
from routes.notificacion_routes import notificacion_routes


class App:
    def __init__(self):
        controller = NotificacionController(DestinatarioDao())
        self.__rutas = notificacion_routes(controller)

    def rutas(self):
        return list(self.__rutas)

    def atender(self, ruta):
        if ruta not in self.__rutas:
            print(f"Ruta no encontrada: {ruta}")
            return
        self.__rutas[ruta]()
