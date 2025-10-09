edad=int(input("Ingrese su edad: "))

#Setencias condicionales
if edad >= 18:
    print("Es mayor de edad")
elif edad < 18 and edad >= 12:
    print("Es un adolescente")
else:
    print("Es un niño")

densidad=float(input("Ingrese la densidad del líquido (kg/m³): "))
if densidad < 2.5:
    print("El líquido es menos denso que el agua")
elif densidad == 2.5:
    print("El líquido tiene la misma densidad que el agua")
else:
    print("El líquido es más denso que el agua")

