def calcular_densidades(masas, volumenes):
    return list(map(lambda m, v: round(m / v, 2), masas, volumenes))
