"""
PARTE 1 - Implementación inicial (diseño ACOPLADO, sin DIP).

NotificacionService crea y usa directamente un EmailService.
Este archivo existe solo para mostrar el problema del diseño.
"""


class EmailService:
    def enviar_email(self, mensaje):
        print(f"[EMAIL] Enviando correo: {mensaje}")


class NotificacionService:
    def __init__(self):
        # Dependencia directa de una clase concreta
        self.email = EmailService()

    def notificar(self, mensaje):
        self.email.enviar_email(mensaje)


if __name__ == "__main__":
    print("=== PARTE 1: diseño acoplado ===")
    servicio = NotificacionService()
    servicio.notificar("Bienvenido al sistema")
