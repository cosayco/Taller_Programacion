#Ejercicios Evaluacion 01 - Unidad 01
#Taller de Programacion
#Autor: Carlos Duran Palape

#Ejercicio 1: SUma de dos numeros
N1=int(input("Ingrese primer numero:"))
N2=int(input("Ingrese segundo numero:"))
suma=N1+N2
print("La suma de los numeros es: ", suma)

#Ejercicio 2: Numero par o impar
numero=int(input("Ingrese un numero:"))
resto=numero%2
if resto==0:
    print("Es par")
else:
    print("Es impar")

#Ejercicio 3: Promedio de tres notas
nota1=float(input("Ingrese Nota 01:"))
nota2=float(input("Ingrese Nota 02:"))
nota3=float(input("Ingrese Nota 03:"))
promedio=(nota1+nota2+nota3)/3
if promedio>=4.0:
    print("Estudiante Aprueba")
else:
    print("Estudiante No Aprueba")

#Ejercicio 4: Conversion de Temperatura
celsius=float(input("Ingrese temperatura en Celsius:"))
fahrenheit=(celsius*9/5)+32
print("La temperatura en Fahrenheit es: ", fahrenheit)

#Ejercicio 5: Clasificacion por densidad
densidad=float(input("Ingrese la densidad: "))
if densidad < 2.5:
    print("Liviano")
elif densidad < 7:
    print("Intermedio")
else:
    print("Pesado")

#Ejercicio 6: Validación de muestra técnica
masa=float(input("Ingrese la masa:"))
volumen=float(input("Ingrese el volumen:"))
densidad=masa/volumen
if densidad>=2.5 and densidad<=8:
    print("Muestra Aceptada")
else:
    print("Muestra Rechazada")

#Ejercicio 7: Tabla de multiplicar
numero=int(input("Ingrese un numero:"))
contador=1
while contador<=12:
    resultado=numero*contador
    print(numero, "x", contador, "=", resultado)
    contador+=1

#Ejercicio 8: Contador de números positivos
positivos=0
for contador in range(5):
    num=int(input(f"Ingrese un numero {contador + 1}:"))
    if num>0:
        positivos+=1
print("Cantidad de numeros positivos: ", positivos)

#Ejercicio 9: Area de un triángulo
base=float(input("Ingrese la base del triángulo:"))
altura=float(input("Ingrese la altura del triángulo:"))
area=(base*altura)/2
print("El área del triángulo es: ", area)

#Ejercicio 10: Validacion Contraseña
contraseña=input("Ingrese contraseña:")
if contraseña=="admin123":
    print("Acceso permitido")
else:
    print("Acceso denegado")

#Ejercicio 11: Cálculo descuento
monto=float(input("Ingrese el monto de la compra:"))
if monto>1000:
    descuento=monto*0.15
    monto_final=monto-descuento
    print("Descuento aplicado: ", descuento)
    print("Monto final a pagar: ", monto_final)

#Ejercicio 12: Contador de pares e impares
pares=0
impares=0
for contador in range(10):
    numero=int(input(f"Ingrese un numero {contador + 1}:"))
    if numero%2==0:
        pares+=1
    else:
        impares+=1

print("Cantidad de numeros pares: ", pares)
print("Cantidad de numeros impares: ", impares)

#Ejercicio 13: Simulacion sensor de temperatura
temperatura=float(input("Ingrese la temperatura:"))
if temperatura<10:
    print("Temperatura baja")
elif temperatura<=25:
    print("Temperatura media")
else:
    print("Temperatura alta")

#Ejercicio 14: Cálculo de nota final
practica=float(input("Ingrese la nota práctica:"))
teorica=float(input("Ingrese la nota teórica:"))
proyecto=float(input("Ingrese la nota proyecto:"))
nota_final=(practica*0.3)+(teorica*0.4)+(proyecto*0.3)
print("La nota final es: ", nota_final)