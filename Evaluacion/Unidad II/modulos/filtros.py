def filtrar_mayores_a(datos, umbral):
    """
    Filtra y retorna los elementos de una lista que son mayores que el umbral,
    usando filter() y lambda.
    """
    # La lambda verifica si x es mayor que el umbral
    resultado = list(filter(lambda x: x > umbral, datos))
    return resultado