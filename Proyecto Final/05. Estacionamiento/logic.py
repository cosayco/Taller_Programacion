from datetime import datetime
import random
import math
from config import PRECIO_POR_MINUTO, MINIMO_A_COBRAR

def generar_ticket():
    return f"TKT-{random.randint(10000, 99999)}"

def calcular_total_por_minutos(entrada_iso, salida_dt):
    entrada_dt = datetime.fromisoformat(entrada_iso)
    delta = salida_dt - entrada_dt
    minutos = math.ceil(delta.total_seconds() / 60)

    subtotal = minutos * PRECIO_POR_MINUTO
    aplicado_minimo = subtotal < MINIMO_A_COBRAR

    total = max(subtotal, MINIMO_A_COBRAR)

    return round(total, 2), minutos, round(subtotal, 2), aplicado_minimo