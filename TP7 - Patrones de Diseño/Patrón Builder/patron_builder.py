# =============================================
# TP7 - Patrón Builder
# Sistema de generación de cuentas bancarias
# =============================================

class CuentaBancaria:
    def __init__(self):
        self.__nombre_titular = None
        self.__dni = None
        self.__tipo_cuenta = None
        self.__moneda = None
        self.__tarjeta_debito = False
        self.__chequera = False
        self.__home_banking = False
        self.__limite_extraccion = None

    # --- Setters (usados por el Builder) ---
    def set_nombre_titular(self, nombre):
        self.__nombre_titular = nombre

    def set_dni(self, dni):
        self.__dni = dni

    def set_tipo_cuenta(self, tipo):
        self.__tipo_cuenta = tipo

    def set_moneda(self, moneda):
        self.__moneda = moneda

    def set_tarjeta_debito(self, valor):
        self.__tarjeta_debito = valor

    def set_chequera(self, valor):
        self.__chequera = valor

    def set_home_banking(self, valor):
        self.__home_banking = valor

    def set_limite_extraccion(self, limite):
        self.__limite_extraccion = limite

    # --- Getters ---
    def get_nombre_titular(self):
        return self.__nombre_titular

    def get_dni(self):
        return self.__dni

    def get_tipo_cuenta(self):
        return self.__tipo_cuenta

    def get_moneda(self):
        return self.__moneda

    def get_tarjeta_debito(self):
        return self.__tarjeta_debito

    def get_chequera(self):
        return self.__chequera

    def get_home_banking(self):
        return self.__home_banking

    def get_limite_extraccion(self):
        return self.__limite_extraccion

    def mostrar_info(self):
        print("=" * 40)
        print("       DATOS DE LA CUENTA BANCARIA")
        print("=" * 40)
        print(f"  Titular:            {self.__nombre_titular}")
        print(f"  DNI:                {self.__dni}")
        print(f"  Tipo de cuenta:     {self.__tipo_cuenta}")
        print(f"  Moneda:             {self.__moneda}")
        print(f"  Tarjeta de débito:  {'Sí' if self.__tarjeta_debito else 'No'}")
        print(f"  Chequera:           {'Sí' if self.__chequera else 'No'}")
        print(f"  Home Banking:       {'Sí' if self.__home_banking else 'No'}")
        if self.__limite_extraccion is not None:
            print(f"  Límite extracción:  ${self.__limite_extraccion:,.0f}")
        else:
            print(f"  Límite extracción:  Sin límite definido")
        print("=" * 40)


# =============================================
# Builder
# =============================================
class CuentaBancariaBuilder:
    def __init__(self):
        self.__cuenta = CuentaBancaria()

    def con_nombre_titular(self, nombre):
        self.__cuenta.set_nombre_titular(nombre)
        return self

    def con_dni(self, dni):
        self.__cuenta.set_dni(dni)
        return self

    def con_tipo_cuenta(self, tipo):
        self.__cuenta.set_tipo_cuenta(tipo)
        return self

    def con_moneda(self, moneda):
        self.__cuenta.set_moneda(moneda)
        return self

    def con_tarjeta_debito(self, valor=True):
        self.__cuenta.set_tarjeta_debito(valor)
        return self

    def con_chequera(self, valor=True):
        self.__cuenta.set_chequera(valor)
        return self

    def con_home_banking(self, valor=True):
        self.__cuenta.set_home_banking(valor)
        return self

    def con_limite_extraccion(self, limite):
        self.__cuenta.set_limite_extraccion(limite)
        return self

    def build(self):
        return self.__cuenta


# =============================================
# PROGRAMA PRINCIPAL
# =============================================

# --- Cliente básico ---
print("\n>>> Cliente básico")
cuenta_basica = (
    CuentaBancariaBuilder()
    .con_nombre_titular("Juan Pérez")
    .con_dni("30.456.789")
    .con_tipo_cuenta("Caja de Ahorro")
    .con_moneda("ARS")
    .con_home_banking()
    .con_tarjeta_debito()
    .build()
)
cuenta_basica.mostrar_info()

# --- Cliente premium ---
print("\n>>> Cliente premium")
cuenta_premium = (
    CuentaBancariaBuilder()
    .con_nombre_titular("María García")
    .con_dni("28.123.456")
    .con_tipo_cuenta("Cuenta Corriente")
    .con_moneda("USD")
    .con_home_banking()
    .con_tarjeta_debito()
    .con_chequera()
    .con_limite_extraccion(2000000)
    .build()
)
cuenta_premium.mostrar_info()
