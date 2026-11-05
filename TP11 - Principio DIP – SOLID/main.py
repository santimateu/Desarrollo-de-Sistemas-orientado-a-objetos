"""
Demostración: el mismo NotificacionService funciona con 4 canales distintos.
Las implementaciones concretas se crean AQUÍ (afuera del servicio) y se inyectan.
"""
from mensajeria import Email, WhatsApp, SMS
from push import Push
from notificacion_service import NotificacionService


def main():
    print("=== PARTE 2: aplicando DIP ===")
    canales = [
        Email("usuario@empresa.com"),
        WhatsApp("+54 9 11 1234-5678"),
        SMS("+54 9 11 8765-4321"),
    ]
    for canal in canales:
        servicio = NotificacionService(canal)   # inyección por constructor
        servicio.notificar("Tu pedido fue confirmado")

    print("\n=== PARTE 3: nuevo canal Push (sin modificar NotificacionService) ===")
    servicio_push = NotificacionService(Push("Android-Pixel-8"))
    servicio_push.notificar("Tu pedido está en camino")


if __name__ == "__main__":
    main()
