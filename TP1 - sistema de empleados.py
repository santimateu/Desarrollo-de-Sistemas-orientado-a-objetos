# Consigna

# Crear una clase abstracta Empleado

# Atributos: nombre, salario_base

# Método concreto: mostrar_info()

# Método abstracto: calcular_salario()

# Crear las siguientes clases hijas:

# EmpleadoTiempoCompleto → cobra salario_base fijo

# EmpleadoPorHora → cobra según horas trabajadas

# EmpleadoComision → cobra base + comisión por ventas

# Crear al menos 3 objetos (uno de cada tipo)

# Guardarlos en una lista y recorrerla:

# Mostrar info del empleado

# Mostrar salario calculado

from abc import ABC, abstractmethod

# Clase abstracta
class Empleado(ABC):
    def __init__(self, nombre, apellido, edad, antiguedad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.antiguedad = antiguedad

    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}, Antiguedad: {self.antiguedad}"
    @abstractmethod
    def calcular_salario(self):
        pass

# Clases hijas
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, apellido, edad, antiguedad, salario_fijo):
        super().__init__(nombre, apellido, edad, antiguedad)
        self.salario_fijo = salario_fijo

    def calcular_salario(self):
        return f"Sueldo tiempo completo: {self.salario_fijo}"

class EmpleadoPorHora(Empleado):
    def __init__(self, nombre, apellido, edad, antiguedad, horas, valor_hora):
        super().__init__(nombre, apellido, edad, antiguedad)
        self.horas = horas
        self.valor_hora = valor_hora

    def calcular_salario(self):
        sueldo = self.horas * self.valor_hora
        return f"Sueldo por hora: {sueldo}"

class EmpleadoComision(Empleado):
    def __init__(self, nombre, apellido, edad, antiguedad, ventas, porcentaje):
        super().__init__(nombre, apellido, edad, antiguedad)
        self.ventas = ventas
        self.porcentaje = porcentaje

    def calcular_salario(self):
        sueldo = self.ventas * self.porcentaje / 100
        return f"Sueldo por comisión: {sueldo}"
    
# Programa principal
personas = [
    EmpleadoTiempoCompleto("Alvaro", "Rodriguez", 50, 10, 1200000),
    EmpleadoPorHora("Manuel", "Ruiz", 50, 6, 1, 10000),
    EmpleadoComision("Santi", "Mateu", 26, 3, 50000, 10)
    ]

for persona in personas:
    print(persona.mostrar_info())
    print(persona.calcular_salario())
    print("-" * 30)