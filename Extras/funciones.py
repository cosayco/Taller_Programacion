#DECIMAL A BINARIO
def decimal_a_binario(numero_decimal):
    binario = ""

    while numero_decimal > 0:
        binario = f"{numero_decimal % 2}{binario}"
        numero_decimal //= 2
    
    return "0" if binario == "" else binario

