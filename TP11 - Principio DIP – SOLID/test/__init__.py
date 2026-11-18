"""
Paquete de tests. Agrega src/ al path para poder importar los módulos
igual que lo hace la aplicación (from domain..., from services..., etc.).
"""
import os
import sys

SRC = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src")
if SRC not in sys.path:
    sys.path.insert(0, SRC)
