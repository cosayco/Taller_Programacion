import random

SUITS = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def crear_baraja():
    return [(r, s) for s in SUITS for r in RANKS]

def repartir_cartas(baraja, num_jugadores=2, cartas_por_jugador=5):
    manos = []
    for _ in range(num_jugadores):
        mano = [baraja.pop() for _ in range(cartas_por_jugador)]
        manos.append(mano)
    return manos

def mostrar_mano(mano):
    return ', '.join([f"{r} de {s}" for r, s in mano])

def main():
    baraja = crear_baraja()
    random.shuffle(baraja)
    num_jugadores = int(input("¿Cuántos jugadores? (2-6): "))
    if num_jugadores < 2 or num_jugadores > 6:
        print("Número de jugadores inválido.")
        return
    manos = repartir_cartas(baraja, num_jugadores)
    for i, mano in enumerate(manos, 1):
        print(f"Jugador {i}: {mostrar_mano(mano)}")

if __name__ == "__main__":
    main()