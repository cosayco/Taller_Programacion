#Ciclo for
radios = [1, 2, 3, 4, 5]
for radio in radios:
    area = 3.14 * radio ** 2
    print(f"El área del círculo con radio {radio} es {area}")

#Ciclo while
profundidad=0
while profundidad < 50:
    profundidad += 5
    print(f"Profundidad actual: {profundidad} metros")

#Ciclo con break
for numero in range(1, 11):
    if numero == 6:
        break
    print(numero)

#Ciclo con continue
for numero in range(1, 11):
    if numero % 2 == 0:
        continue
    print(numero)

#Recursión
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))
