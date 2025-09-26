import numpy as np

def seleccionar_palabra(lista_palabras):
    indice = np.random.randint(0, len(lista_palabras))
    return lista_palabras[indice]

def mostrar_tablero(palabra, letras_adivinadas):
    tablero = [letra if letra in letras_adivinadas else '_' for letra in palabra]
    print(' '.join(tablero))

def obtener_letra():
    letra = input("Adivina una letra: ").lower()
    return letra

def juego_ahorcado():
    palabras = np.array(['python', 'numpy', 'ahorcado', 'programa', 'matriz', 'vector'])
    palabra = seleccionar_palabra(palabras)
    letras_adivinadas = set()
    intentos = 6

    print("¡Bienvenido al juego del ahorcado!")
    while intentos > 0:
        mostrar_tablero(palabra, letras_adivinadas)
        letra = obtener_letra()

        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra.")
            continue

        if letra in palabra:
            letras_adivinadas.add(letra)
            if all(l in letras_adivinadas for l in palabra):
                print(f"¡Felicidades! Has adivinado la palabra: {palabra}")
                break
        else:
            intentos -= 1
            print(f"Letra incorrecta. Te quedan {intentos} intentos.")

    else:
        print(f"Has perdido. La palabra era: {palabra}")

juego_ahorcado() #Para iniciar el Juego.