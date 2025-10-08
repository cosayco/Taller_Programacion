class Rectangulo:
    def __init__(self, base, altura):
        self.__base = base        # atributo privado
        self.__altura = altura    # atributo privado

    def calcular_area(self):
        return self.__base * self.__altura

    def calcular_perimetro(self):
        return 2 * (self.__base + self.__altura)

    def es_cuadrado(self):
        return self.__base == self.__altura

    def mostrar_info(self):
        print(f"Base: {self.__base} cm")
        print(f"Altura: {self.__altura} cm")
        print(f"Área: {self.calcular_area()} cm²")
        print(f"Perímetro: {self.calcular_perimetro()} cm")
        print("¿Es cuadrado?:", "Sí" if self.es_cuadrado() else "No")

r1 = Rectangulo(10, 5)
r2 = Rectangulo(7, 7)

r1.mostrar_info()
print("-----")
r2.mostrar_info()
