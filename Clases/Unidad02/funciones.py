#Repaso de funciones 25-26/09/2025
#Crear una función que calcule el área de un triángulo
def area_triangulo(base, altura):
    area = (base * altura) / 2
    return area
print(area_triangulo(5, 10))

#Definir una función que clasifique materiales por dureza
def clasificar_dureza(dureza):
    if dureza < 2.5:
        return "Material blando"
    elif dureza >= 2.5 and dureza < 5.0:
        return "Material de dureza media"
    else:
        return "Material duro"
    
print(clasificar_dureza(3.5))

#Usar variables locales y globales en un mismo programa
contador_global = 0
def incrementar_contador():
    global contador_global
    contador_global += 1
    return contador_global

print(incrementar_contador())

#Crear funciones que retornen múltiples valores con return a, b
def operaciones_basicas(x, y):
    suma = x + y
    resta = x - y
    multiplicacion = x * y
    division = x / y if y != 0 else None
    return suma, resta, multiplicacion, division

resultados = operaciones_basicas(10, 2)
print(resultados)

