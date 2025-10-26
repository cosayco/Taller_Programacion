def valida_bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return "Es bisiesto"
    else:
        return "No es bisiesto"
    
def precio_descuento(precio, porcentaje):
    return precio * (1 - porcentaje / 100)