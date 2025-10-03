from funciones.generador import generar_datos
from funciones.calculos import calcular_densidades
from funciones.clasificacion import clasificar

n = int(input("Ingrese cantidad de muestras: "))
masas, volumenes = generar_datos(n)

densidades = calcular_densidades(masas, volumenes)
tipos = clasificar(densidades)

for i in range(n):
    print(f"Muestra {i+1}: Masa={masas[i]:.2f} kg, Volumen={volumenes[i]:.2f} m³, Densidad={densidades[i]} → {tipos[i]}")