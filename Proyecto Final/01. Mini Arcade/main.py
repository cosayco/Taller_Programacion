from config import inicializar_pygame
from menu import menu_principal

def main():
    pantalla, clock = inicializar_pygame()
    menu_principal(pantalla, clock)

if __name__ == "__main__":
    main()