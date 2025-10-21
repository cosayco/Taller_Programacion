import pandas as pd

#Simulacion de datos tecnicos
datos = {
    "Material":["Cobre", "Plata", "Aluminio", "Hierro", "Oro"],
    "Masa":[270,315,150,250,500],
    "Volumen":[100,90,80,120,50]
}

df=pd.DataFrame(datos)
df["Densidad"]=df["Masa"]/df["Volumen"]

import matplotlib.pyplot as plt

#Grafico de barras
plt.figure(figsize=(8,5))
plt.bar(df["Material"], df["Densidad"], color="red")
plt.title("Densidad por Material") 
plt.xlabel("Material")
plt.ylabel("Densidad (g/cm³)")
plt.grid(True)
plt.tight_layout()
plt.show()

#Grafico circular
plt.figure(figsize=(6,6))
plt.pie(df["Masa"], labels=df["Material"], autopct="%1.1f%%", startangle=90)
plt.title("Distribucion de Masa por Material")
plt.tight_layout()
plt.show()

#Grafico lineas
plt.figure(figsize=(8,5))
plt.plot(df["Material"], df["Masa"], marker="o", label="Masa")
plt.plot(df["Material"], df["Volumen"], marker="s", label="Volumen")
plt.title("Masa y Volumen por Material")
plt.xlabel("Material")
plt.ylabel("Valor")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()