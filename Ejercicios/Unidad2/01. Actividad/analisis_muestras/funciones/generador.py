import numpy as np

def generar_datos(n):
    masas = np.random.uniform(100, 500, n)
    volumenes = np.random.uniform(50, 200, n)
    return masas, volumenes
