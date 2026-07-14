# TP8 - Métodos heredados de Object

Trabajo práctico sobre los métodos especiales (dunder methods) que toda clase en Python hereda de `object`, y cómo sobrescribirlos para dar un comportamiento propio a nuestras clases.

## Objetivo

Comprender el comportamiento por defecto de los métodos heredados de `object` (`__str__`, `__repr__`, `__eq__`, `__hash__`, etc.) y observar cómo cambia al sobrescribirlos en una clase `Persona`.

## Archivos

- `tp8_metodos_object.py`: script principal con dos partes y una sección de preguntas y respuestas.

## Contenido

### Parte 1: Sin sobrescribir métodos
Se define una clase `Persona` mínima y se prueban:
- `print(obj)` y `str(obj)` → muestran la dirección de memoria.
- `repr(obj)` → representación por defecto.
- `p1 == p2` → compara por identidad (`False` aunque tengan los mismos datos).
- `hash(obj)` → hash basado en la identidad.
- `type(obj)` y `dir(obj)` → tipo y métodos heredados.

### Parte 2: Sobrescribiendo métodos
Se redefinen en `Persona`:
- `__str__`: representación legible para el usuario.
- `__repr__`: representación no ambigua para desarrolladores.
- `__eq__`: igualdad por valor (nombre, edad, email).
- `__hash__`: hash consistente con `__eq__`.

Se muestra que ahora `p1 == p2` da `True` y que `hash(p1) == hash(p2)`.

### Preguntas y respuestas
Incluye respuestas a preguntas conceptuales sobre:
1. Comportamiento por defecto de `__str__`.
2. Cambios al sobrescribir `__str__`.
3. Por qué `==` da `False` por defecto.
4. Por qué luego da `True`.
5. Relación entre `__eq__` y `__hash__`.
6. Equivalente en Python de `getClass()` de Java (`type(obj)` / `obj.__class__`).

## Cómo ejecutar

```bash
python tp8_metodos_object.py
```

Requiere Python 3.x. No usa dependencias externas.
