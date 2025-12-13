import random

PALOS = ["Corazones", "Diamantes", "Tréboles", "Picas"]
VALORES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


def crear_baraja():
    """Crea y baraja una baraja estándar de 52 cartas."""
    baraja = []
    for palo in PALOS:
        for valor in VALORES:
            baraja.append((valor, palo))
    random.shuffle(baraja)
    return baraja


def carta_a_texto(carta):
    valor, palo = carta
    return f"{valor} de {palo}"


def valor_mano(mano):
    """Calcula el valor de la mano, ajustando Ases (11 -> 1) si es necesario."""
    total = 0
    ases = 0
    for valor, _ in mano:
        if valor in ["J", "Q", "K"]:
            total += 10
        elif valor == "A":
            total += 11
            ases += 1
        else:
            total += int(valor)

    while total > 21 and ases > 0:
        total -= 10
        ases -= 1

    return total


def es_blackjack(mano):
    """Devuelve True si la mano es un Blackjack (21 con 2 cartas)."""
    return len(mano) == 2 and valor_mano(mano) == 21
