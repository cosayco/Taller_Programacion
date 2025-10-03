class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola, soy {self.nombre}")

# Clase hija que hereda de Persona
class Estudiante(Persona):
    def estudiar(self):
        print(f"{self.nombre} está estudiando")

# Uso
e1 = Estudiante("Carlos")
e1.saludar()      # Heredado de Persona
e1.estudiar()     # Propio de Estudiante
