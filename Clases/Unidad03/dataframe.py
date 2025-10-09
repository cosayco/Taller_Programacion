import pandas as pd

datos = {
    "Material": ["Cobre", "Plata", "Aluminio"],
    "Masa": [270,315,150],
    "Volumen": [100,90,80]
}

df = pd.DataFrame(datos)
print(df)

# Calcular la densidad y agregarla como una nueva columna
df["Densidad"] = df["Masa"] / df["Volumen"]
print(df)

# Clasificar los materiales según su densidad
df["Clasificación"] = df["Densidad"].apply(lambda d: "Liviana" if d < 2.5 else "Media" if d <= 7.0 else "Pesada")
print(df)

# Guardar el DataFrame en un archivo CSV
df.to_csv("reporte_muestras.csv", index=False)


