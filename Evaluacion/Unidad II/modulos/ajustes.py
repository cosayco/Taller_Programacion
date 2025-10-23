def modificar_por_indice(lista, indice, nuevo_valor):
    """Modifica un elemento de la lista en la posición dada por el índice."""
    lista[indice] = nuevo_valor
    # No retorna nada (la modificación es in-place)