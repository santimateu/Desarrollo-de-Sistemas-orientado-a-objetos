"""
CONTROLADOR - Recibe las solicitudes (desde las rutas) y coordina la lógica.

Aquí se crean las implementaciones concretas de Mensajeria y se inyectan
en NotificacionService (inyección por constructor). El servicio nunca
instancia ni conoce los canales concretos.
"""
from dao.destinatario_dao import DestinatarioDao
from domain.mensajeria import Email, WhatsApp, SMS
from domain.push import Push
from services.notificacion_service import NotificacionService


class NotificacionController:
    def __init__(self, dao: DestinatarioDao):
        self.__dao = dao

    def notificar_canales(self):
        print("=== PARTE 2: aplicando DIP ===")

        servicio = NotificacionService(Email(self.__dao.obtener("email")))  # inyección por constructor
        servicio.notificar("Tu pedido fue confirmado")

        servicio1 = NotificacionService(WhatsApp(self.__dao.obtener("whatsapp")))  # inyección por constructor
        servicio1.notificar("Tu pedido fue confirmado")

        servicio2 = NotificacionService(SMS(self.__dao.obtener("sms")))  # inyección por constructor
        servicio2.notificar("Tu pedido fue confirmado")

    def notificar_push(self):
        print("\n=== PARTE 3: nuevo canal Push (sin modificar NotificacionService) ===")

        servicio3 = NotificacionService(Push(self.__dao.obtener("push")))  # inyección por constructor
        servicio3.notificar("Tu pedido está en camino")
