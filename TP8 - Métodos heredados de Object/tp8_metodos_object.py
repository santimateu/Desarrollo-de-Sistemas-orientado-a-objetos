# =============================================
# TP8 - Métodos heredados de Object
# Clase Persona - Comprobación de métodos
# =============================================

# =============================================
# PARTE 1: Sin sobrescribir métodos
# =============================================

class Persona:
    def __init__(self, nombre, edad, email):
        self.nombre = nombre
        self.edad = edad
        self.email = email


print("=" * 50)
print("   PARTE 1: SIN SOBRESCRIBIR MÉTODOS")
print("=" * 50)

# Crear dos personas con los mismos datos
p1 = Persona("Fede", 25, "fede@mail.com")
p2 = Persona("Fede", 25, "fede@mail.com")

# Imprimir el objeto directamente
print(f"\nprint(p1):        {p1}")
print(f"print(p2):        {p2}")

# Usar str()
print(f"\nstr(p1):          {str(p1)}")

# Usar repr()
print(f"repr(p1):         {repr(p1)}")

# Comparar con ==
print(f"\np1 == p2:         {p1 == p2}")
print(f"p1 is p2:         {p1 is p2}")

# Obtener hash
print(f"\nhash(p1):         {hash(p1)}")
print(f"hash(p2):         {hash(p2)}")

# Mostrar tipo con type()
print(f"\ntype(p1):         {type(p1)}")
print(f"type(p2):         {type(p2)}")

# Mostrar métodos heredados con dir()
print(f"\ndir(p1):")
for metodo in dir(p1):
    if metodo.startswith("__"):
        print(f"  {metodo}")


# =============================================
# PARTE 2: Sobrescribir métodos
# =============================================

class Persona:
    def __init__(self, nombre, edad, email):
        self.nombre = nombre
        self.edad = edad
        self.email = email

    def __str__(self):
        return f"Persona(nombre={self.nombre}, edad={self.edad}, email={self.email})"

    def __repr__(self):
        return f"Persona('{self.nombre}', {self.edad}, '{self.email}')"

    def __eq__(self, otro):
        if not isinstance(otro, Persona):
            return False
        return self.nombre == otro.nombre and self.edad == otro.edad and self.email == otro.email

    def __hash__(self):
        return hash((self.nombre, self.edad, self.email))


print("\n\n" + "=" * 50)
print("   PARTE 2: CON MÉTODOS SOBRESCRITOS")
print("=" * 50)

# Crear dos personas con los mismos datos
p1 = Persona("Fede", 25, "fede@mail.com")
p2 = Persona("Fede", 25, "fede@mail.com")

# Imprimir el objeto directamente
print(f"\nprint(p1):        {p1}")
print(f"print(p2):        {p2}")

# Usar str()
print(f"\nstr(p1):          {str(p1)}")

# Usar repr()
print(f"repr(p1):         {repr(p1)}")

# Comparar con ==
print(f"\np1 == p2:         {p1 == p2}")
print(f"p1 is p2:         {p1 is p2}")

# Obtener hash
print(f"\nhash(p1):         {hash(p1)}")
print(f"hash(p2):         {hash(p2)}")
print(f"hash(p1) == hash(p2): {hash(p1) == hash(p2)}")

# Mostrar tipo con type()
print(f"\ntype(p1):         {type(p1)}")

# Equivalente de getClass() de Java en Python
print(f"type(p1).__name__: {type(p1).__name__}")


# =============================================
# PREGUNTAS Y RESPUESTAS
# =============================================

print("\n\n" + "=" * 50)
print("   PREGUNTAS Y RESPUESTAS")
print("=" * 50)

print("""
1. ¿Qué imprime el objeto antes de sobrescribir __str__()?
   Imprime algo como <__main__.Persona object at 0x...>, que es la
   dirección de memoria del objeto. Es el comportamiento por defecto
   heredado de la clase object.

2. ¿Qué cambia después de implementar __str__()?
   Ahora imprime la representación legible que definimos, por ejemplo:
   Persona(nombre=Fede, edad=25, email=fede@mail.com)

3. ¿Por qué p1 == p2 primero da False?
   Porque por defecto, Python compara por identidad (dirección en memoria).
   Como p1 y p2 son dos objetos distintos en memoria, == da False.

4. ¿Por qué después puede dar True?
   Porque al sobrescribir __eq__() definimos que dos Personas son iguales
   si tienen el mismo nombre, edad y email. Ahora compara por valor.

5. ¿Qué relación tienen __eq__() y __hash__()?
   Si dos objetos son iguales según __eq__(), deben tener el mismo hash.
   Si sobrescribís __eq__() sin __hash__(), Python hace el objeto
   unhashable (no se puede usar en sets o como clave de diccionario).

6. ¿Cuál sería el equivalente de getClass() de Java en Python?
   Es type(objeto) o objeto.__class__. Ambos devuelven la clase del objeto.
   type(p1).__name__ devuelve el nombre como string, igual que
   getClass().getName() en Java.
""")
