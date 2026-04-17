# Trabajo Práctico: Uso de Memoria en Objetos e Instancias# 🧠

# ## 🎯 Objetivo
# Que los alumnos entiendan:
# - Cómo se crean objetos en memoria
# - Diferencia entre instancias vs valores primitivos
# - Buenas prácticas para evitar uso innecesario de memoria

# ---

# ## 📝 Parte 1 – Análisis (sin código)

# 1. Explicar con sus palabras:
#    - ¿Qué pasa en memoria cuando hago `new Dog('Rex')`?
#    - ¿Por qué `dog1` y `dog2` ocupan espacios distintos en memoria?
#    - ¿Qué diferencia hay entre:
#      ```js
#      const nombre = "fede";
#      const nombre2 = new String("fede");
#      ```
  # 1.
  # Cuando hacés el new, el código reserva un lugar nuevo en la memoria para crear un objeto basado en la clase Dog. 
  # No es solo un texto (como sería un String), 
  # sino una instancia completa que tiene sus propias propiedades y métodos.

  # Porque cada new crea un objeto desde cero. Aunque los dos se llamen "Rex", 
  # Ocupan lugares diferentes en la memoria. Si los comparás, el código te va a decir que no son el mismo objeto.
  
  # - La diferencia es que la primer constante es un Valor Primitivo, meientras que la segunda constante
  # es un Objeto


# 2. Dibujar (tipo esquema):
#    - Stack vs Heap (simple)
#    - Mostrar dónde viven:
#      - variables
#      - objetos
#      - instancias

# ---

# ## 💻 Parte 2 – Código (detectar problemas)

# Dado este código, identificar malas prácticas:

# ```js
# const nombre = new String("Juan");
# const apellido = new String("Perez");

# const nombreCompleto = nombre + apellido;

# const edad = new Number(30);
# const activo = new Boolean(true);

  # La mala practica en este codigo es la concatenacion entre las constantes nombre + apellido
  # al concatenar de esta manera hace que el codigo genere 2 instancias diferentes
  # ocupando mas espacio en la memoria


# 🔧 Parte 3 – Refactor (mejorar uso de memoria)

# class User {
#   constructor(name) {
#     this.name = new String(name);
#   }
# }

# const user1 = new User("Ana");
# const user2 = new User("Ana");

  # class User {
  #   constructor(name) {
  #     this.name = (name);
  #   }
  # }

  # const user1 = new User("Ana");
  # const user2 = new User("Ana");


# 🚀 Parte 4 – Instancias y duplicación

# const dog1 = new Dog("Rex");
# const dog2 = new Dog("Rex");

  # "Está bien. Aunque las dos instancias tengan el mismo valor ('Rex'), "
  # "el código las considera dos objetos diferentes porque cada new reserva un lugar único en la memoria. "
  # "Son dos objetos distintos nacidos del mismo molde (Dog)."


# Parte 5 – Desafío (nivel pro)

# Crear una clase Config que:

# Solo pueda tener una instancia (Singleton)
# Guarde configuraciones como:
# url
# port
# Todos los objetos deben usar la misma instancia

class Config:
    _instance = None  # variable de clase para guardar la única instancia

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # inicialización de atributos por única vez
            cls._instance.url = None
            cls._instance.port = None
        return cls._instance

    def set_config(self, url, port):
        self.url = url
        self.port = port

    def __str__(self):
        return f"Config(url={self.url}, port={self.port})"
    
c1 = Config()
c2 = Config()


# 🔥 Bonus (opcional)

# Investigar y probar en Node.js:
# console.log(process.memoryUsage());