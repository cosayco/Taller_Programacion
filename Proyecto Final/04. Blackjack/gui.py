import tkinter as tk
from tkinter import messagebox

from auth import cargar_usuarios, guardar_usuarios
from blackjack_logic import crear_baraja, carta_a_texto, valor_mano, es_blackjack


class BlackjackApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack - Login")

        self.usuarios = cargar_usuarios()
        self.usuario_actual = None

        self.baraja = []
        self.mano_jugador = []
        self.mano_dealer = []
        self.ronda_activa = False

        self.crear_pantalla_login()


    def crear_pantalla_login(self):
        self.limpiar_root()

        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack()

        tk.Label(frame, text="Blackjack", font=("Arial", 18, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 10))

        tk.Label(frame, text="Usuario:").grid(row=1, column=0, sticky="e")
        self.entry_usuario = tk.Entry(frame)
        self.entry_usuario.grid(row=1, column=1)

        tk.Label(frame, text="Contraseña:").grid(row=2, column=0, sticky="e")
        self.entry_password = tk.Entry(frame, show="*")
        self.entry_password.grid(row=2, column=1)

        btn_login = tk.Button(frame, text="Iniciar sesión", command=self.login)
        btn_login.grid(row=3, column=0, pady=10, sticky="e")

        btn_registro = tk.Button(frame, text="Registrar usuario", command=self.registrar_usuario)
        btn_registro.grid(row=3, column=1, pady=10, sticky="w")

        btn_reglas = tk.Button(frame, text="Ver reglas básicas", command=self.mostrar_reglas)
        btn_reglas.grid(row=4, column=0, columnspan=2, pady=(5, 0))

    def login(self):
        usuario = self.entry_usuario.get().strip()
        password = self.entry_password.get().strip()

        if not usuario or not password:
            messagebox.showwarning("Error", "Debes ingresar usuario y contraseña.")
            return

        if usuario in self.usuarios and self.usuarios[usuario] == password:
            self.usuario_actual = usuario
            messagebox.showinfo("Bienvenido", f"Bienvenido/a, {usuario}")
            self.crear_pantalla_juego()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

    def registrar_usuario(self):
        usuario = self.entry_usuario.get().strip()
        password = self.entry_password.get().strip()

        if not usuario or not password:
            messagebox.showwarning("Error", "Debes ingresar usuario y contraseña para registrarte.")
            return

        if usuario in self.usuarios:
            messagebox.showerror("Error", "Ese nombre de usuario ya existe. Elige otro.")
            return

        self.usuarios[usuario] = password
        guardar_usuarios(self.usuarios)
        messagebox.showinfo("Registro exitoso", "Usuario creado correctamente. Ahora puedes iniciar sesión.")

    def mostrar_reglas(self):
        texto = (
            "REGLAS BÁSICAS DEL BLACKJACK\n\n"
            "1. El objetivo es acercarse lo más posible a 21 sin pasarse.\n"
            "2. Cartas numéricas valen su número.\n"
            "3. J, Q, K valen 10.\n"
            "4. El As (A) vale 1 u 11 según convenga.\n"
            "5. El jugador puede PEDIR carta o PLANTARSE.\n"
            "6. Si el jugador supera 21, pierde automáticamente.\n"
            "7. El dealer pide cartas hasta tener al menos 17.\n"
            "8. Gana quien tenga el valor más alto sin pasarse de 21.\n"
            "9. Si ambos tienen el mismo valor final, es empate (PUSH).\n"
        )
        messagebox.showinfo("Reglas del Blackjack", texto)


    def crear_pantalla_juego(self):
        self.root.title("Blackjack - Juego")
        self.limpiar_root()

        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack()

        tk.Label(frame, text=f"Jugador: {self.usuario_actual}", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=3, pady=(0, 10))

        tk.Label(frame, text="Dealer", font=("Arial", 12, "bold")).grid(row=1, column=0, sticky="w")
        self.lbl_cartas_dealer = tk.Label(frame, text="", justify="left")
        self.lbl_cartas_dealer.grid(row=2, column=0, columnspan=3, sticky="w")

        tk.Label(frame, text="Tus cartas", font=("Arial", 12, "bold")).grid(row=3, column=0, sticky="w", pady=(10, 0))
        self.lbl_cartas_jugador = tk.Label(frame, text="", justify="left")
        self.lbl_cartas_jugador.grid(row=4, column=0, columnspan=3, sticky="w")

        self.lbl_estado = tk.Label(frame, text="", font=("Arial", 11, "bold"), fg="blue")
        self.lbl_estado.grid(row=5, column=0, columnspan=3, pady=(10, 10))

        btn_nueva = tk.Button(frame, text="Nueva ronda", command=self.nueva_ronda)
        btn_nueva.grid(row=6, column=0, padx=5, pady=5)

        self.btn_pedir = tk.Button(frame, text="Pedir carta", command=self.pedir_carta, state="disabled")
        self.btn_pedir.grid(row=6, column=1, padx=5, pady=5)

        self.btn_plantarse = tk.Button(frame, text="Plantarse", command=self.plantarse, state="disabled")
        self.btn_plantarse.grid(row=6, column=2, padx=5, pady=5)

        btn_salir = tk.Button(frame, text="Cerrar juego", command=self.root.destroy)
        btn_salir.grid(row=7, column=0, columnspan=3, pady=(10, 0))

    def limpiar_root(self):
        for widget in self.root.winfo_children():
            widget.destroy()


    def nueva_ronda(self):
        self.baraja = crear_baraja()
        self.mano_jugador = [self.baraja.pop(), self.baraja.pop()]
        self.mano_dealer = [self.baraja.pop(), self.baraja.pop()]
        self.ronda_activa = True

        self.btn_pedir.config(state="normal")
        self.btn_plantarse.config(state="normal")
        self.lbl_estado.config(text="Ronda en juego...")

        self.actualizar_interfaz(inicio=True)

        if es_blackjack(self.mano_jugador) or es_blackjack(self.mano_dealer):
            self.finalizar_ronda_por_blackjack()

    def actualizar_interfaz(self, inicio=False, revelar_dealer=False):
        if not revelar_dealer and self.ronda_activa:
            primera = "?? (carta oculta)"
            resto = [carta_a_texto(c) for c in self.mano_dealer[1:]]
            texto_dealer = primera + "\n" + "\n".join(resto) if resto else primera
        else:
            texto_dealer = "\n".join(carta_a_texto(c) for c in self.mano_dealer)
            texto_dealer += f"\n\nValor: {valor_mano(self.mano_dealer)}"

        self.lbl_cartas_dealer.config(text=texto_dealer)

        texto_jugador = "\n".join(carta_a_texto(c) for c in self.mano_jugador)
        texto_jugador += f"\n\nValor: {valor_mano(self.mano_jugador)}"
        self.lbl_cartas_jugador.config(text=texto_jugador)

    def finalizar_ronda_por_blackjack(self):
        self.ronda_activa = False
        self.btn_pedir.config(state="disabled")
        self.btn_plantarse.config(state="disabled")

        self.actualizar_interfaz(revelar_dealer=True)

        jugador_bj = es_blackjack(self.mano_jugador)
        dealer_bj = es_blackjack(self.mano_dealer)

        if jugador_bj and dealer_bj:
            self.lbl_estado.config(text="Ambos tienen BLACKJACK. Empate (PUSH).")
        elif jugador_bj:
            self.lbl_estado.config(text="¡Tienes BLACKJACK! Ganaste esta ronda.")
        else:
            self.lbl_estado.config(text="El dealer tiene BLACKJACK. Pierdes esta ronda.")

    def pedir_carta(self):
        if not self.ronda_activa:
            return

        self.mano_jugador.append(self.baraja.pop())
        self.actualizar_interfaz()

        if valor_mano(self.mano_jugador) > 21:
            self.ronda_activa = False
            self.btn_pedir.config(state="disabled")
            self.btn_plantarse.config(state="disabled")
            self.actualizar_interfaz(revelar_dealer=True)
            self.lbl_estado.config(text="Te pasaste de 21. Pierdes esta ronda.")

    def plantarse(self):
        if not self.ronda_activa:
            return

        while valor_mano(self.mano_dealer) < 17:
            self.mano_dealer.append(self.baraja.pop())

        self.ronda_activa = False
        self.btn_pedir.config(state="disabled")
        self.btn_plantarse.config(state="disabled")

        self.actualizar_interfaz(revelar_dealer=True)

        valor_j = valor_mano(self.mano_jugador)
        valor_d = valor_mano(self.mano_dealer)

        if valor_d > 21:
            self.lbl_estado.config(text="El dealer se pasó de 21. ¡Ganaste esta ronda!")
        elif valor_j > valor_d:
            self.lbl_estado.config(text="¡Tu mano es mayor! Ganaste esta ronda.")
        elif valor_j < valor_d:
            self.lbl_estado.config(text="La mano del dealer es mayor. Pierdes esta ronda.")
        else:
            self.lbl_estado.config(text="Empate (PUSH).")
