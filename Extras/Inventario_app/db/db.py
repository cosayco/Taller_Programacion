import pandas as pd
import os

DB_FOLDER = os.path.dirname(__file__)
PRODUCTOS_CSV = os.path.join(DB_FOLDER, "productos.csv")

def inicializar_csv():
    os.makedirs(DB_FOLDER, exist_ok=True)
    if not os.path.exists(PRODUCTOS_CSV):
        pd.DataFrame(columns=["ID", "Nombre", "Categoría", "Unidad", "Precio", "Stock"]).to_csv(PRODUCTOS_CSV, index=False)

def cargar_productos():
    return pd.read_csv(PRODUCTOS_CSV)

def guardar_productos(df):
    df.to_csv(PRODUCTOS_CSV, index=False)