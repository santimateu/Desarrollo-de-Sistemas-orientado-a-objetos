"""
Punto de entrada de la aplicación.

Uso:
    python src/index.py                          # ejecuta todas las rutas
    python src/index.py /notificaciones/push     # ejecuta una ruta
"""
import sys

from app import App


def main():
    app = App()
    rutas = sys.argv[1:] or app.rutas()
    for ruta in rutas:
        app.atender(ruta)


if __name__ == "__main__":
    main()
