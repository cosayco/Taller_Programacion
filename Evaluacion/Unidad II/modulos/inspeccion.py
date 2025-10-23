def mostrar_lista_inversa(lista):
    """
    Itera sobre la lista usando enumerate() e imprime el valor
    junto con su posición contando desde el final.
    """
    longitud = len(lista)
    print("\n--- Posición desde el Final ---")
    for i, valor in enumerate(lista):
        # La posición desde el final es (longitud - indice actual)
        posicion_final = longitud - i
        print(f"Posición {posicion_final}: {valor}")