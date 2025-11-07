def normalizar(datos):
    """
    Recibe una lista de números, aplica la función lambda para dividir
    cada uno por 100 usando map() y retorna la lista resultante.
    """
    # Usar map() con una lambda para la división, y convertir a list
    datos_normalizados = list(map(lambda x: x / 100, datos))
    return datos_normalizados