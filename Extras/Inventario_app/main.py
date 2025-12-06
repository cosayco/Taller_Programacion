from login import mostrar_login

def iniciar_aplicacion():
    import tkinter as tk
    from tkinter import ttk
    from db.db import inicializar_csv
    from modules.maestros import agregar_producto
    from modules.ingresos import registrar_ingreso
    from modules.salidas import registrar_salida
    from modules.consulta import obtener_productos

    inicializar_csv()
    root = tk.Tk()
    root.title("Control de Inventario")
    # Tamaño de la ventana
    ancho = 500
    alto = 400

    # Obtener dimensiones de la pantalla
    pantalla_ancho = root.winfo_screenwidth()
    pantalla_alto = root.winfo_screenheight()

    # Calcular posición centrada
    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2) - (alto // 2)

    root.geometry(f"{ancho}x{alto}+{x}+{y}")
    root.resizable(False, False)
    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True)

    # Maestros
    frame_maestros = ttk.Frame(notebook)
    notebook.add(frame_maestros, text="Maestros")
    id_entry = ttk.Entry(frame_maestros)
    nombre_entry = ttk.Entry(frame_maestros)
    categoria_entry = ttk.Entry(frame_maestros)
    #unidad_entry = ttk.Entry(frame_maestros)
    unidades = ["unidad", "kg", "litro", "metro", "paquete"]
    unidad_combo = ttk.Combobox(frame_maestros, values=unidades, state="readonly")
    unidad_combo.set("unidad")  # Valor por defecto
    unidad_combo.grid(row=3, column=1)
    precio_entry = ttk.Entry(frame_maestros)
    for i, label in enumerate(["ID", "Nombre", "Categoría", "Unidad", "Precio"]):
        ttk.Label(frame_maestros, text=label).grid(row=i, column=0)
        [id_entry, nombre_entry, categoria_entry, unidad_combo, precio_entry][i].grid(row=i, column=1)
    #ttk.Button(frame_maestros, text="Agregar", command=lambda: agregar_producto(id_entry.get(), nombre_entry.get(), categoria_entry.get(), unidad_entry.get(), precio_entry.get())).grid(row=5, column=0, columnspan=2)
    def agregar_y_limpiar():
        agregar_producto(
            id_entry.get(),
            nombre_entry.get(),
            categoria_entry.get(),
            unidad_combo.get(),
            precio_entry.get()
        )
        # Limpiar campos
        id_entry.delete(0, tk.END)
        nombre_entry.delete(0, tk.END)
        categoria_entry.delete(0, tk.END)
        unidad_combo.set("unidad")
        precio_entry.delete(0, tk.END)

    ttk.Button(frame_maestros, text="Agregar", command=agregar_y_limpiar).grid(row=5, column=0, columnspan=2)

    # Ingresos
    frame_ingresos = ttk.Frame(notebook)
    notebook.add(frame_ingresos, text="Ingresos")
    id_ing = ttk.Entry(frame_ingresos)
    cant_ing = ttk.Entry(frame_ingresos)
    ttk.Label(frame_ingresos, text="ID").grid(row=0, column=0)
    ttk.Label(frame_ingresos, text="Cantidad").grid(row=1, column=0)
    id_ing.grid(row=0, column=1)
    cant_ing.grid(row=1, column=1)
    ttk.Button(frame_ingresos, text="Registrar", command=lambda: registrar_ingreso(id_ing.get(), cant_ing.get())).grid(row=2, column=0, columnspan=2)

    # Salidas
    frame_salidas = ttk.Frame(notebook)
    notebook.add(frame_salidas, text="Salidas")
    id_sal = ttk.Entry(frame_salidas)
    cant_sal = ttk.Entry(frame_salidas)
    ttk.Label(frame_salidas, text="ID").grid(row=0, column=0)
    ttk.Label(frame_salidas, text="Cantidad").grid(row=1, column=0)
    id_sal.grid(row=0, column=1)
    cant_sal.grid(row=1, column=1)
    ttk.Button(frame_salidas, text="Registrar", command=lambda: registrar_salida(id_sal.get(), cant_sal.get())).grid(row=2, column=0, columnspan=2)

    # Consulta
    frame_consulta = ttk.Frame(notebook)
    notebook.add(frame_consulta, text="Consulta")
    tree = ttk.Treeview(frame_consulta, columns=("ID", "Nombre", "Categoría", "Unidad", "Precio", "Stock"), show="headings")
    for col in tree["columns"]:
        tree.heading(col, text=col)
    tree.pack(fill="both", expand=True)
    ttk.Button(frame_consulta, text="Actualizar", command=lambda: actualizar_tree(tree)).pack()

    def actualizar_tree(treeview):
        treeview.delete(*treeview.get_children())
        df = obtener_productos()
        for _, row in df.iterrows():
            treeview.insert("", "end", values=list(row))

    root.mainloop()

mostrar_login(iniciar_aplicacion)