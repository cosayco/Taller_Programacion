import numpy as np

def generar_numero_aleatorio(inicio, fin):
    return np.random.randint(inicio, fin + 1)

def pedir_intento():
    while True:
        try:
            intento = int(input("Adivina el número: "))
            return intento
        except ValueError:
            print("Por favor, ingresa un número válido.")

def jugar_adivina_el_numero():
    print("¡Bienvenido al juego de adivina el número!")
    inicio = 1
    fin = 100
    numero_secreto = generar_numero_aleatorio(inicio, fin)
    intentos = 0

    while True:
        intento = pedir_intento()
        intentos += 1

        if intento < numero_secreto:
            print("Demasiado bajo.")
        elif intento > numero_secreto:
            print("Demasiado alto.")
        else:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break

jugar_adivina_el_numero() #Para iniciar el Juego.