def validar_densidad(densidad):
    if densidad is None:
        return "Error: volumen no puede ser cero"
    elif densidad < 2.5:
        return "Muestra liviana"
    elif densidad <= 7.0:
        return "Muestra media"
    else:
        return "Muestra pesada"
