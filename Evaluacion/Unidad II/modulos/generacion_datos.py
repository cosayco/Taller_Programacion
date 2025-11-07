import numpy as np

def serie_temporal(inicio, fin, num_puntos):
    """
    Genera un array con num_puntos espaciados uniformemente entre inicio y fin
    utilizando np.linspace().
    """
    return np.linspace(inicio, fin, num_puntos)