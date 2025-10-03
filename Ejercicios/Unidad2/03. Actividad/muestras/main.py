from funciones.calculos import calcular_densidad
from funciones.validaciones import validar_densidad
from funciones.utils import mostrar_resultado

masa = float(input("Ingrese la masa de la muestra (kg): "))
volumen = float(input("Ingrese el volumen de la muestra (m³): "))

densidad = calcular_densidad(masa, volumen)
clasificacion = validar_densidad(densidad)

mostrar_resultado(masa, volumen, densidad, clasificacion)
