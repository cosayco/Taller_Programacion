from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)
ruta_csv = os.path.join("db", "produccion.csv")

@app.route("/")
def index():
    # Leer datos desde CSV
    df = pd.read_csv(ruta_csv)
    
    # Agrupar por día
    resumen = df.groupby("Fecha")["Toneladas"].sum().reset_index()
    
    # Crear gráfico
    plt.figure(figsize=(8,4))
    plt.plot(resumen["Fecha"], resumen["Toneladas"], marker="o")
    plt.title("Producción diaria")
    plt.xlabel("Fecha")
    plt.ylabel("Toneladas")
    plt.grid(True)
    plt.tight_layout()
    
    # Guardar imagen
    if not os.path.exists("static"):
        os.makedirs("static")
    plt.savefig("static/grafico.png")
    plt.close()
    
    return render_template("index.html", tabla=resumen.to_html(classes="table table-striped", index=False))

if __name__ == "__main__":
    app.run(debug=True)