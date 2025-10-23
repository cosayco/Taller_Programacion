import numpy as np

def aplicar_correccion(vector_np):
    """
    Aplica la corrección vectorizada: (Valor Original + 5) / 2
    y retorna el array corregido.
    """
    # Operación vectorizada
    return (vector_np + 5) / 2