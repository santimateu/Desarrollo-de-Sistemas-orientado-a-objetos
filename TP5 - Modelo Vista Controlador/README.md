# TP5 - Modelo Vista Controlador

Gestión de herramientas (alta, listado y actualización de precio) aplicando el patrón **MVC** con capas de DAO, Domain y Services.

## Estructura

```
├── src/
│   ├── controllers/
│   ├── domain/
│   │   └── herramienta.py           # Entidad Herramienta
│   ├── routes/
│   ├── services/
│   │   └── herramienta_service.py   # Lógica de negocio
│   ├── dao/
│   │   └── herramienta_dao.py       # Acceso a datos (lista en memoria)
│   └── index.py                     # Vista, Controlador y programa principal
├── test/                            # Tests (misma estructura que src/)
├── requirements.txt                 # Dependencias (ninguna externa)
└── README.md
```

## Cómo ejecutar

Desde esta carpeta (requiere Python 3.8 o superior, sin dependencias externas):

```bash
python src/index.py
```
