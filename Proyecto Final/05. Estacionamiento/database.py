import sqlite3
import os

RUTA_DIRECTORIO = os.path.dirname(os.path.abspath(__file__))
DB_FILE = "parking.db"
RUTA_DB = os.path.join(RUTA_DIRECTORIO,"db",DB_FILE)

def init_db():
    conn = sqlite3.connect(RUTA_DB)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS parked (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ticket TEXT UNIQUE,
        patente TEXT,
        tipo TEXT,
        entrada TEXT,
        salida TEXT,
        total REAL
    )
    """)

    conn.commit()
    conn.close()

def contar_vehiculos_dentro():
    conn = sqlite3.connect(RUTA_DB)
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM parked WHERE salida IS NULL")
    count = cur.fetchone()[0]
    conn.close()
    return count

def insertar_entrada(ticket, patente, tipo, entrada):
    conn = sqlite3.connect(RUTA_DB)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO parked(ticket, patente, tipo, entrada, salida, total)
        VALUES (?, ?, ?, ?, NULL, NULL)
    """, (ticket, patente, tipo, entrada))
    conn.commit()
    conn.close()

def obtener_vehiculos_dentro():
    conn = sqlite3.connect(RUTA_DB)
    cur = conn.cursor()
    cur.execute("""
        SELECT id, ticket, patente, tipo, entrada 
        FROM parked 
        WHERE salida IS NULL 
        ORDER BY entrada
    """)
    rows = cur.fetchall()
    conn.close()
    return rows

def registrar_salida(registro_id, salida_iso, total):
    conn = sqlite3.connect(RUTA_DB)
    cur = conn.cursor()
    cur.execute("""
        UPDATE parked SET salida=?, total=? WHERE id=?
    """, (salida_iso, total, registro_id))
    conn.commit()
    conn.close()

def obtener_historial(limit=500):
    conn = sqlite3.connect(RUTA_DB)
    cur = conn.cursor()
    cur.execute("""
        SELECT ticket, patente, tipo, entrada, salida, total
        FROM parked
        ORDER BY entrada DESC
        LIMIT ?
    """, (limit,))
    rows = cur.fetchall()
    conn.close()
    return rows

#init_db()
