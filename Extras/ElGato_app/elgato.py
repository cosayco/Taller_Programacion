import numpy as np

def crear_tablero():
    return np.full((3, 3), ' ')

def mostrar_tablero(tablero):
    for fila in tablero:
        print('|'.join(fila))
        print('-' * 5)

def movimiento_valido(tablero, fila, columna):
    return tablero[fila, columna] == ' '

def realizar_movimiento(tablero, fila, columna, jugador):
    if movimiento_valido(tablero, fila, columna):
        tablero[fila, columna] = jugador
        return True
    return False

def verificar_ganador(tablero, jugador):
    for i in range(3):
        if np.all(tablero[i, :] == jugador) or np.all(tablero[:, i] == jugador):
            return True
    if np.all(np.diag(tablero) == jugador) or np.all(np.diag(np.fliplr(tablero)) == jugador):
        return True
    return False

def tablero_lleno(tablero):
    return not np.any(tablero == ' ')

def jugar():
    tablero = crear_tablero()
    jugador = 'X'
    while True:
        mostrar_tablero(tablero)
        print(f"Turno del jugador {jugador}")
        try:
            fila = int(input("Ingrese fila (0-2): "))
            columna = int(input("Ingrese columna (0-2): "))
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")
            continue
        if 0 <= fila <= 2 and 0 <= columna <= 2:
            if realizar_movimiento(tablero, fila, columna, jugador):
                if verificar_ganador(tablero, jugador):
                    mostrar_tablero(tablero)
                    print(f"¡El jugador {jugador} ha ganado!")
                    break
                elif tablero_lleno(tablero):
                    mostrar_tablero(tablero)
                    print("¡Empate!")
                    break
                jugador = 'O' if jugador == 'X' else 'X'
            else:
                print("Movimiento no válido. Intente de nuevo.")
        else:
            print("Posición fuera de rango. Intente de nuevo.")

jugar() #Para iniciar el Juego.