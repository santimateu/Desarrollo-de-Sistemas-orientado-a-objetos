## Actividad: Crear una clase a eleccion (por ejemplo, "Animal") 
# con un constructor que reciba el nombre y la especie del animal. 
# Luego, crear dos instancias de la clase "Animal" y modificar sus propiedades utilizando métodos setNombre y setEspecie.

class Animal:
    def __init__(self, nombre, especie, alimentacion, habitat):
        self.nombre = nombre
        self.especie = especie
        self.alimentacion = alimentacion
        self.habitat = habitat

    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Especie: {self.especie}, Alimentacion: {self.alimentacion}, Habitat: {self.habitat}"

    def setNombre(self, nombre):
        self.nombre = nombre

    def setEspecie(self, especie):
        self.especie = especie

    def setAlimentacion(self, alimentacion):
        self.alimentacion = alimentacion

    def setHabitat(self, habitat):
        self.habitat = habitat

animal1 = Animal("Perro", "Canino", "Omnivoro", "Adaptable")
animal2 = Animal("Gato", "Felino", "Omnivoro", "Adaptable")
animal3 = Animal("Tigre", "Panthera tigris", "Carnivoro", "Selvas y bosques")
animal4 = Animal("Elefante africano", "Loxodonta africana", "Herbivoro", "Sabanas africanas")

animal1.setNombre("Lobo")
animal1.setEspecie("Canis lupus")
animal1.setHabitat("Bosques")

animal2.setNombre("Tiburon blanco")
animal2.setEspecie("Carcharodon carcharias)")
animal2.setAlimentacion("Carnivoro")
animal2.setHabitat("Oceano")

animal3.setNombre("Águila real")
animal3.setEspecie("Aquila chrysaetos")
animal3.setHabitat("Montañas")

animal4.setNombre("Pingüino emperador")
animal4.setEspecie("Aptenodytes forsteri")
animal4.setHabitat("Antartida")

print(animal1.mostrar_info())
print(animal2.mostrar_info())
print(animal3.mostrar_info())
print(animal4.mostrar_info())