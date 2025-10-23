import numpy as np

def redondear_array(array_flotante):
    """Redondea cada elemento del array de NumPy a dos decimales."""
    # Usar np.round()
    return np.round(array_flotante, 2)