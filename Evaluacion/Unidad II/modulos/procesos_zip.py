def imprimir_pares(nombres, codigos):
    """
    Utiliza zip() para emparejar y desempaquetar nombres y códigos,
    e imprime el resultado.
    """
    print("\n--- Pares de Datos ---")
    # Desempaquetado directo en el bucle for
    for nombre, codigo in zip(nombres, codigos):
        print(f"Código {codigo} -> Nombre: {nombre}")