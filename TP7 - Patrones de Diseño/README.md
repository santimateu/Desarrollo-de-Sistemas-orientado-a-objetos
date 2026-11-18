# TP7 - Patrones de Diseño: Builder y Singleton

- **Builder**: sistema de generación de cuentas bancarias (`CuentaBancaria` + `CuentaBancariaBuilder`).
- **Singleton**: sistema de logs para una aplicación bancaria (`Logger` compartido por `LoginService`, `TransferService` y `AccountService`).

## Estructura

```
├── src/
│   ├── controllers/
│   ├── domain/
│   │   └── patron_builder.py     # Patrón Builder
│   ├── routes/
│   ├── services/
│   │   └── patron_singleton.py   # Patrón Singleton
│   └── dao/
├── test/                         # Tests (misma estructura que src/)
├── requirements.txt              # Dependencias (ninguna externa)
└── README.md
```

## Cómo ejecutar

Desde esta carpeta (requiere Python 3.8 o superior, sin dependencias externas):

```bash
python src/domain/patron_builder.py
python src/services/patron_singleton.py
```
