#Clases 25-26/09/2025
#Usar lambda para calcular el área de un círculo
PI=3.1416
area_circulo = lambda r: PI * r**2
print("Área del círculo de radio 5:", area_circulo(5))

#Aplicar map() para convertir temperaturas de °C a °F
temp_celsius = [0, 20, 37, 100]
temp_fahrenheit = list(map(lambda c: (c * 9/5) + 32, temp_celsius))
print("Temperaturas en °C:", temp_celsius)
print("Temperaturas en °F:", temp_fahrenheit)

#Combinar dos listas con map() y lambda para calcular presión = fuerza / área
fuerzas = [100, 250, 400, 600]
areas = [10, 25, 50, 75]
presiones = list(map(lambda f, a: f / a, fuerzas, areas))
print("Presiones:", presiones)

#Reemplazar funciones tradicionales por expresiones lambda
def sumar(x, y):
    return x + y
sumar_lambda = lambda x, y: x + y

def multiplicar(x, y):
    return x * y
multiplicar_lambda = lambda x, y: x * y

def doble(x):
    return x * 2
doble_lambda = lambda x: x * 2

def area_rectangulo(base, altura):
    return base * altura
area_rectangulo_lambda = lambda base, altura: base * altura
