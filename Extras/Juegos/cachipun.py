import numpy as np

def obtener_eleccion_usuario():
    opciones = ['piedra', 'papel', 'tijera']
    eleccion = input("Elige piedra, papel o tijera: ").lower()
    while eleccion not in opciones:
        eleccion = input("Opción inválida. Elige piedra, papel o tijera: ").lower()
    return eleccion

def obtener_eleccion_computador():
    opciones = ['piedra', 'papel', 'tijera']
    return np.random.choice(opciones)

def determinar_ganador(usuario, computador):
    if usuario == computador:
        return "Empate"
    elif (usuario == 'piedra' and computador == 'tijera') or \
         (usuario == 'papel' and computador == 'piedra') or \
         (usuario == 'tijera' and computador == 'papel'):
        return "¡Ganaste!"
    else:
        return "Perdiste"

def jugar():
    usuario = obtener_eleccion_usuario()
    computador = obtener_eleccion_computador()
    print(f"Tú elegiste: {usuario}")
    print(f"La computadora eligió: {computador}")
    resultado = determinar_ganador(usuario, computador)
    print(resultado)
    jugar_nuevamente = input("¿Quieres jugar de nuevo? (s/n): ").lower()
    if jugar_nuevamente == 's':
        jugar()

jugar() #Para iniciar el Juego.