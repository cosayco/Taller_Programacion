import pygame
import sys
import tkinter as tk
from tkinter import messagebox
from constantes import ANCHO, ALTO, TAM_CUADRADO, CREMA, AZUL
from clases.tablero import Tablero

FPS = 60

def preguntar_reiniciar(ganador):
    """
    Muestra una ventana preguntando si quieren jugar de nuevo.
    Retorna True si quieren jugar, False si quieren salir.
    """
    root_preg = tk.Tk()
    root_preg.withdraw() 
    
    respuesta = messagebox.askyesno(
        "Fin del Juego", 
        f"¡Felicidades {ganador}!\nHas ganado la partida.\n\n¿Desean jugar otra vez?"
    )
    
    root_preg.destroy()
    return respuesta

def iniciar_juego_damas(nombre_jugador_1, nombre_jugador_2):
    reiniciar = True
    
    while reiniciar:
        pygame.init()
        VENTANA = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption(f'Damas: {nombre_jugador_1} (Azul) vs {nombre_jugador_2} (Crema)')
        
        def get_fila_col_del_mouse(pos):
            x, y = pos
            fila = y // TAM_CUADRADO
            col = x // TAM_CUADRADO
            return fila, col

        run = True
        clock = pygame.time.Clock()
        tablero = Tablero()
        
        seleccionado = None
        turno = AZUL
        turno_extra = False 
        ganador_nombre = None

        while run:
            clock.tick(FPS)
            
            if tablero.fichas_cremas <= 0:
                ganador_nombre = nombre_jugador_1
                run = False
            elif tablero.fichas_azules <= 0:
                ganador_nombre = nombre_jugador_2
                run = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    reiniciar = False 
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    fila, col = get_fila_col_del_mouse(pos)
                    ficha_clicada = tablero.obtener_ficha(fila, col)

                    if seleccionado:
                        if ficha_clicada == 0: 
                            if tablero.validar_movimiento(seleccionado, fila, col):
                                es_salto = abs(fila - seleccionado.fila) == 2
                                if es_salto:
                                    fila_media = (seleccionado.fila + fila) // 2
                                    col_media = (seleccionado.col + col) // 2
                                    ficha_victima = tablero.obtener_ficha(fila_media, col_media)
                                    tablero.eliminar_ficha(ficha_victima)

                                tablero.mover(seleccionado, fila, col)
                                
                                cambio_turno = True
                                if es_salto:
                                    if tablero.hay_captura_posible(seleccionado):
                                        cambio_turno = False
                                        turno_extra = True
                                    else:
                                        turno_extra = False
                                else:
                                    turno_extra = False

                                if cambio_turno:
                                    seleccionado = None
                                    turno = CREMA if turno == AZUL else AZUL
                                    nombre_actual = nombre_jugador_1 if turno == AZUL else nombre_jugador_2
                                    color_texto = "AZUL" if turno == AZUL else "CREMA"
                                    pygame.display.set_caption(f'Turno de: {nombre_actual} ({color_texto})')
                                else:
                                    print("¡Puedes comer otra vez!")
                            else:
                                if not turno_extra:
                                    seleccionado = None

                        elif ficha_clicada != 0 and ficha_clicada.color == turno:
                            if not turno_extra:
                                seleccionado = ficha_clicada
                    
                    else:
                        if ficha_clicada != 0 and ficha_clicada.color == turno:
                            seleccionado = ficha_clicada

            tablero.dibujar(VENTANA)
            pygame.display.update()

        pygame.quit() 
        
        if ganador_nombre:
            decision = preguntar_reiniciar(ganador_nombre)
            if decision:
                pass 
            else:
                reiniciar = False

    sys.exit()

def pantalla_nombres():
    def guardar_y_jugar():
        j1 = entry_j1.get()
        j2 = entry_j2.get()
        
        if j1 == "" or j2 == "":
            messagebox.showwarning("Faltan datos", "Por favor ingresen sus nombres para empezar.")
        else:
            root_nombres.destroy()
            iniciar_juego_damas(j1, j2)

    root_nombres = tk.Tk()
    root_nombres.title("Registro de Jugadores")
    root_nombres.geometry("400x300")
    root_nombres.eval('tk::PlaceWindow . center')

    tk.Label(root_nombres, text="Configuración de Partida", font=("Arial", 16, "bold")).pack(pady=20)

    tk.Label(root_nombres, text="Nombre Jugador 1 (Fichas Azules):").pack()
    entry_j1 = tk.Entry(root_nombres)
    entry_j1.pack(pady=5)

    tk.Label(root_nombres, text="Nombre Jugador 2 (Fichas Cremas):").pack()
    entry_j2 = tk.Entry(root_nombres)
    entry_j2.pack(pady=5)

    tk.Button(root_nombres, text="¡COMENZAR JUEGO!", command=guardar_y_jugar, bg="green", fg="white", font=("Arial", 10, "bold")).pack(pady=30)
    
    root_nombres.mainloop()

def pantalla_login():
    def verificar_credenciales():
        usuario = entry_user.get()
        clave = entry_pass.get()

        if usuario == "admin" and clave == "1234":
            root_login.destroy()
            pantalla_nombres()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    root_login = tk.Tk()
    root_login.title("Seguridad - Damas")
    root_login.geometry("300x250")
    root_login.eval('tk::PlaceWindow . center')

    tk.Label(root_login, text="Bienvenido", font=("Arial", 14, "bold")).pack(pady=10)

    tk.Label(root_login, text="Usuario:").pack(pady=5)
    entry_user = tk.Entry(root_login)
    entry_user.pack(pady=5)

    tk.Label(root_login, text="Contraseña:").pack(pady=5)
    entry_pass = tk.Entry(root_login, show="*")
    entry_pass.pack(pady=5)

    tk.Button(root_login, text="INGRESAR", command=verificar_credenciales, bg="blue", fg="white", width=15).pack(pady=20)

    root_login.mainloop()

if __name__ == "__main__":
    pantalla_login()