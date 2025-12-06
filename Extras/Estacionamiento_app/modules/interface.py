import tkinter as tk
from tkinter import messagebox
from modules.estacionamiento import Estacionamiento
import random
import threading
import time
import os

parking = Estacionamiento(capacidad=30)
simulacion_activa = False
hilo_simulacion = None

def iniciar_gui():
    global simulacion_activa, hilo_simulacion

    ventana = tk.Tk()
    ventana.title("Estacionamiento Visual")
    ventana.geometry("700x650")
    ventana.resizable(False, False)
    # Reloj digital en esquina superior derecha
    reloj_label = tk.Label(ventana, font=("Arial", 10), fg="#333", anchor="e")
    reloj_label.place(x=580, y=10)

    def actualizar_reloj():
        hora_actual = time.strftime("%H:%M:%S")
        reloj_label.config(text=f"🕒 {hora_actual}")
        ventana.after(1000, actualizar_reloj)

    actualizar_reloj()
    # Etiqueta de estado
    def estado_texto():
        return f"Ocupados: {parking.ocupados()} / {parking.capacidad} | Libres: {parking.disponibles()}"

    estado_label = tk.Label(ventana, text=estado_texto(), font=("Arial", 12))
    estado_label.pack(pady=10)

    # Entrada de patente
    tk.Label(ventana, text="Ingrese la patente del vehículo:", font=("Arial", 10)).pack()
    entry = tk.Entry(ventana, font=("Arial", 12), justify="center")
    entry.pack(pady=5)
    entry.focus()

    # Grilla de espacios
    grilla_frame = tk.Frame(ventana)
    grilla_frame.pack(pady=10)

    espacios = []
    for fila in range(5):
        fila_espacios = []
        for col in range(6):
            lbl = tk.Label(grilla_frame, text="Libre", width=10, height=2, bg="lightgray", relief="ridge", font=("Arial", 10))
            lbl.grid(row=fila, column=col, padx=5, pady=5)
            fila_espacios.append(lbl)
        espacios.append(fila_espacios)

    def actualizar_grilla():
        ocupados = list(parking.vehiculos.keys())
        total = parking.capacidad
        for i in range(total):
            fila, col = divmod(i, 6)
            lbl = espacios[fila][col]
            if i < len(ocupados):
                lbl.config(text=ocupados[i], bg="#4CAF50", fg="white")
            else:
                lbl.config(text="Libre", bg="lightgray", fg="black")

    def actualizar_estado():
        estado_label.config(text=estado_texto())
        actualizar_grilla()

    def ingresar():
        patente = entry.get().strip()
        if not patente:
            messagebox.showwarning("Atención", "Ingrese una patente válida")
            return
        exito, mensaje = parking.ingresar_auto(patente)
        messagebox.showinfo("Ingreso", mensaje)
        entry.delete(0, tk.END)
        actualizar_estado()

    def salir():
        patente = entry.get().strip()
        if not patente:
            messagebox.showwarning("Atención", "Ingrese una patente válida")
            return
        exito, mensaje = parking.retirar_auto(patente)
        if exito:
            messagebox.showinfo("Salida", mensaje)
        else:
            messagebox.showerror("Error", mensaje)
        entry.delete(0, tk.END)
        actualizar_estado()

    def generar_patente():
        letras = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=3))
        numeros = ''.join(random.choices("0123456789", k=3))
        return f"{letras}-{numeros}"

    def simular_movimiento():
        global hilo_simulacion
        simulacion_activa = True

        def ciclo():
            while simulacion_activa:
                time.sleep(2)
                if random.random() < 0.6 and parking.disponibles() > 0:
                    patente = generar_patente()
                    parking.ingresar_auto(patente)
                elif parking.ocupados() > 0:
                    patente = random.choice(list(parking.vehiculos.keys()))
                    parking.retirar_auto(patente)
                actualizar_estado()
                ventana.update()

        hilo_simulacion = threading.Thread(target=ciclo, daemon=True)
        hilo_simulacion.start()

    def detener_simulacion():
        global simulacion_activa
        simulacion_activa = False
        messagebox.showinfo("Simulación", "Simulación automática detenida")

    def abrir_log():
        ruta_log = os.path.join("db", "log.csv")
        if os.path.exists(ruta_log):
            os.startfile(ruta_log)
        else:
            messagebox.showwarning("Log no encontrado", "El archivo log.csv no existe aún")

    # Frame de ingreso manual
    frame_manual = tk.LabelFrame(ventana, text="Ingreso Manual", padx=10, pady=10, font=("Arial", 10, "bold"))
    frame_manual.pack(pady=5)

    tk.Button(frame_manual, text="Ingresar Vehículo", command=ingresar, width=20, bg="#4CAF50", fg="white").pack(pady=5)
    tk.Button(frame_manual, text="Retirar Vehículo", command=salir, width=20, bg="#F44336", fg="white").pack(pady=5)

    # Frame de simulación automática
    frame_auto = tk.LabelFrame(ventana, text="Simulación Automática", padx=10, pady=10, font=("Arial", 10, "bold"))
    frame_auto.pack(pady=5)

    tk.Button(frame_auto, text="Iniciar Simulación", command=simular_movimiento, width=25, bg="#FF9800", fg="white").pack(pady=5)
    tk.Button(frame_auto, text="Detener Simulación", command=detener_simulacion, width=25, bg="#9E9E9E", fg="white").pack(pady=5)

    # Botón para abrir el log
    tk.Button(ventana, text="Consultar Log de Eventos", command=abrir_log, width=30, bg="#3F51B5", fg="white", font=("Arial", 10)).pack(pady=10)

    actualizar_estado()
    ventana.mainloop()