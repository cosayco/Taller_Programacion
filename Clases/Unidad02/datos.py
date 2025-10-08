#Clase 11-12/09/2025
#Ejercicio 1
temperaturas = [18.5, 20.1, 19.8, 21.0, 17.6]
suma = sum(temperaturas)
promedio = suma / len(temperaturas)
print(f"Temperaturas: {temperaturas}")
print(f"Promedio: {promedio:.2f} °C")

#Ejercicio 2
coordenadas = (120, 85, -30)
print(f"X: {coordenadas[0]}")
print(f"Y: {coordenadas[1]}")
print(f"Z: {coordenadas[2]}")

#Ejercicio 3
muestra = {
    "material": "Cobre",
    "densidad": 2.7,
    "volumen": 120
}

muestra["volumen"] = 135
print(muestra)

#Ejercicio 4
muestras = {
    "M1": {"material": "Cobre", "densidad": 2.7},
    "M2": {"material": "Hierro", "densidad": 7.8},
    "M3": {"material": "Plata", "densidad": 10.5}
}

print(f"Densidad de M2: {muestras['M2']['densidad']} g/cm³")

#Ejercicio 5
constantes = (9.81, 3.1416, 343)
print(f"Gravedad: {constantes[0]} m/s²")
print(f"PI: {constantes[1]}")
print(f"Velocidad del sonido: {constantes[2]} m/s")

#Ejercicio 6
import random
materiales = ["Cobre", "Hierro", "Plata", "Oro"]
seleccionado = random.choice(materiales)
print(f"Material seleccionado: {seleccionado}")
