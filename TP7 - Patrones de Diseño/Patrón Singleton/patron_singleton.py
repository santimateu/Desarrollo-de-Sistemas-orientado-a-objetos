# =============================================
# TP7 - Patrón Singleton
# Sistema de logs para aplicación bancaria
# =============================================

from datetime import datetime


# =============================================
# Singleton - Logger
# =============================================
class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__registros = []
        return cls._instance

    def log(self, mensaje):
        entrada = f"[INFO] {mensaje}"
        self.__registros.append(entrada)
        print(entrada)

    def mostrar_registros(self):
        print("\n" + "=" * 50)
        print("         REGISTRO COMPLETO DE EVENTOS")
        print("=" * 50)
        for registro in self.__registros:
            print(f"  {registro}")
        print("=" * 50)


# =============================================
# Servicios que utilizan el Logger
# =============================================
class LoginService:
    def __init__(self):
        self.__logger = Logger()

    def iniciar_sesion(self, usuario):
        self.__logger.log(f"Usuario {usuario} inició sesión")

    def cerrar_sesion(self, usuario):
        self.__logger.log(f"Usuario {usuario} cerró sesión")


class TransferService:
    def __init__(self):
        self.__logger = Logger()

    def realizar_transferencia(self, monto):
        self.__logger.log(f"Transferencia realizada por ${monto}")


class AccountService:
    def __init__(self):
        self.__logger = Logger()

    def consultar_saldo(self):
        self.__logger.log("Consulta de saldo realizada")


# =============================================
# PROGRAMA PRINCIPAL
# =============================================

login_service = LoginService()
transfer_service = TransferService()
account_service = AccountService()

# Verificar que todos usan la misma instancia
print("¿Misma instancia en todos los servicios?", Logger() is Logger())
print()

# Simulación de eventos bancarios
login_service.iniciar_sesion("fede")
transfer_service.realizar_transferencia(50000)
account_service.consultar_saldo()
login_service.cerrar_sesion("fede")

# Mostrar todos los registros
Logger().mostrar_registros()
