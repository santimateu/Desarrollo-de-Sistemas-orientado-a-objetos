"""
RUTAS - Asocia cada ruta con el método del controlador que la atiende.
"""
from controllers.notificacion_controller import NotificacionController


def notificacion_routes(controller: NotificacionController):
    return {
        "/notificaciones": controller.notificar_canales,
        "/notificaciones/push": controller.notificar_push,
    }
