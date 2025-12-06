import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import os

# 1. Leer datos
df = pd.read_csv("data/produccion.csv")

# 2. Preparar datos
df["Semana"] = pd.to_datetime(df["Fecha"]).dt.isocalendar().week
X = df[["Semana"]]   # Variable independiente
y = df["Toneladas"]  # Variable dependiente

# 3. Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 4. Entrenar modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# 5. Evaluar modelo
y_pred = modelo.predict(X_test)
print("Error cuadrático medio:", mean_squared_error(y_test, y_pred))
print("R²:", r2_score(y_test, y_pred))

# 6. Guardar modelo entrenado
if not os.path.exists("models"):
    os.makedirs("models")
joblib.dump(modelo, "models/modelo.pkl")

# 7. Visualizar resultados
plt.figure(figsize=(8,4))
plt.scatter(X_test, y_test, color="blue", label="Datos reales")
plt.plot(X_test, y_pred, color="red", linewidth=2, label="Predicción")
plt.title("Predicción de Producción Semanal")
plt.xlabel("Semana")
plt.ylabel("Toneladas")
plt.legend()
plt.tight_layout()

if not os.path.exists("reports"):
    os.makedirs("reports")
plt.savefig("reports/grafico.png")
plt.close()

print("✅ Modelo entrenado y gráfico generado en carpeta 'reports'")