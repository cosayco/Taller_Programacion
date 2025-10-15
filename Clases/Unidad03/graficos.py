import pandas as pd
import matplotlib.pyplot as plt
# Leer el DataFrame en un archivo CSV
df = pd.read_csv("reporte_muestras.csv")
print(df.head())
# Grafico circular
plt.figure(figsize=(6,6))
plt.pie(df["Masa"], labels=df["Material"], autopct="%1.1f%%"
        , startangle=90)
plt.title("Distribucion masa por material")
plt.tight_layout()
plt.show()

#Grafico de barras
plt.figure(figsize=(8,5))
plt.bar(df["Material"], df["Densidad"], color="steelblue")
plt.title("Densidad de materiales")
plt.xlabel("Material")
plt.ylabel("Densidad (g/cm³)")
plt.grid(True)
plt.tight_layout()
plt.show()

#Grafico de lineas
plt.figure(figsize=(8,5))
plt.plot(df["Material"], df["Masa"], marker="o", label="Masa")
plt.plot(df["Material"], df["Volumen"], marker="s", label="Volumen")
plt.title("Masa y Volumen por material")
plt.xlabel("Material")
plt.ylabel("Valor")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()



