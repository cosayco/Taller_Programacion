#Clase 11-12/09/2025
#Ejercicio 1
densidades = [2.4, 2.6, 2.8, 2.3, 2.7]

for d in densidades:
    if d > 2.5:
        print(f"Densidad {d} → Válida")
    else:
        print(f"Densidad {d} → Rechazada")

print(densidades)

#Ejercicio 2
coordenadas = (120, 85, -30)

for eje in coordenadas:
    print(f"Coordenada: {eje}")

#Ejercicio 3
muestra = {
    "material": "Cobre",
    "densidad": 2.7,
    "volumen": 120
}

for clave, valor in muestra.items():
    print(f"{clave}: {valor}")

#Ejercicio 4
materiales = ["Cobre", "Hierro", "Plata", "Oro"]

for i, mat in enumerate(materiales):
    print(f"Muestra {i+1}: {mat}")

#Ejercicio 5
nombres = ["M1", "M2", "M3"]
densidades = [2.7, 7.8, 10.5]

for nombre, densidad in zip(nombres, densidades):
    print(f"{nombre} → Densidad: {densidad} g/cm³")

#Ejercicio 6
muestras = {
    "M1": {"material": "Cobre", "densidad": 2.7},
    "M2": {"material": "Hierro", "densidad": 2.4},
    "M3": {"material": "Plata", "densidad": 10.5}
}

for nombre, datos in muestras.items():
    if datos["densidad"] > 2.5:
        print(f"{nombre} → Válida ({datos['material']})")

