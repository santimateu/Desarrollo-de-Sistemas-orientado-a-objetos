"""
DAO - Acceso a datos de los destinatarios.
Simula una base de datos con un diccionario en memoria.
"""


class DestinatarioDao:
    def __init__(self):
        self.__destinatarios = {
            "email": "usuario@empresa.com",
            "whatsapp": "+54 9 11 1234-5678",
            "sms": "+54 9 11 8765-4321",
            "push": "Android-Pixel-8",
        }

    def obtener(self, canal):
        return self.__destinatarios[canal]
