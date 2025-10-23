def imprimir_datos_iterados(datos):
    """
    Itera sobre la lista de datos usando enumerate() e imprime
    cada valor con su índice comenzando en 1.
    """
    print("\n--- Reporte de Niveles ---")
    for i, valor in enumerate(datos):
        # i + 1 convierte el índice base 0 a conteo base 1
        print(f"Item {i + 1}: {valor}")