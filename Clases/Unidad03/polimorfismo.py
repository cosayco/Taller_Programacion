class Animal:
    def hablar(self):
        print("El animal hace un sonido")

class Perro(Animal):
    def hablar(self):
        print("El perro ladra")

class Gato(Animal):
    def hablar(self):
        print("El gato maúlla")

animales = [Perro(), Gato(), Animal()]

for a in animales:
    a.hablar()
