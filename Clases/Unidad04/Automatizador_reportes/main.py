import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

# 1. Leer datos
ruta_csv = os.path.join("data", "produccion.csv")
df = pd.read_csv(ruta_csv)

# 2. Convertir fechas y limpiar
df["Fecha"] = pd.to_datetime(df["Fecha"])
df.dropna(inplace=True)

# 3. Agrupar por semana
df["Semana"] = df["Fecha"].dt.isocalendar().week
resumen = df.groupby("Semana")["Toneladas"].sum().reset_index()

# 4. Crear gráfico
plt.figure(figsize=(8,4))
plt.bar(resumen["Semana"], resumen["Toneladas"], color="steelblue")
plt.title("Producción semanal")
plt.xlabel("Semana")
plt.ylabel("Toneladas")
plt.tight_layout()

# Crear carpeta de reportes si no existe
if not os.path.exists("reports"):
    os.makedirs("reports")

# Guardar gráfico
grafico_path = os.path.join("reports", "grafico_produccion.png")
plt.savefig(grafico_path)
plt.close()

# 5. Exportar resumen a Excel
fecha_actual = datetime.now().strftime("%Y-%m-%d")
reporte_path = os.path.join("reports", f"reporte_{fecha_actual}.xlsx")
resumen.to_excel(reporte_path, index=False)

print("✅ Reporte generado en carpeta 'reports'")
