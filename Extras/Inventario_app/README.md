# 📦 Aplicación de Inventario (Ejemplo Proyecto Final)

## 📖 Descripción
La **Aplicación de Inventario** desarrollada en Python permite gestionar productos, ingresos, salidas y consultas de stock de manera sencilla y modular.  
Está construida con **Tkinter** para la interfaz gráfica y utiliza archivos **CSV** como base de datos, lo que elimina la necesidad de servidores o bases de datos externas.

## 🏗️ Arquitectura del Proyecto
```
inventario_app/ 
│ 
├── main.py          # Ventana principal y navegación 
├── login.py         # Autenticación de usuario 
│ 
├── db/ 
│   │   
│   ├── db.py        # Manejo de archivo productos.csv 
│   └── productos.csv # Base de datos en formato CSV 
│ 
└── modules/ 
    ├── maestros.py  # Gestión de productos 
    ├── ingresos.py  # Registro de ingresos 
    ├── salidas.py   # Registro de salidas 
    └── consulta.py  # Visualización de inventario
```

## ⚙️ Funcionalidades Principales

- ### 🔑 Login de Acceso
    - Ventana inicial centrada en pantalla.  
    - Usuario: `Admin`  
    - Contraseña: `1234`  
    - Impide el acceso si las credenciales son incorrectas.

- ### 📋 Módulo Maestros
    - Crear nuevos productos con:
        - ID único
        - Nombre
        - Categoría
        - Unidad (Combobox)
        - Precio
    - Valida que el ID no esté duplicado.  
    - Limpia los campos tras agregar el producto.

- ### 📥 Módulo Ingresos
    - Registra ingresos de stock por ID.  
    - Valida que el ID exista en el archivo CSV.  
    - Actualiza el campo **Stock** en la base de datos.

- ### 📤 Módulo Salidas
    - Registra salidas de productos por ID.  
    - Verifica existencia y disponibilidad de stock.  
    - Actualiza el campo **Stock** en la base de datos.

- ### 🔎 Módulo Consulta
    - Muestra el inventario completo en una tabla (**Treeview**).  
    - Permite actualizar la vista con los datos actuales del archivo CSV.

## 🛠️ Detalles Técnicos
- Interfaz gráfica con **Tkinter** y **ttk**.  
- Persistencia de datos con **pandas** y **csv**.  
- Validaciones de tipo y existencia para evitar errores.  
- Compatible con **pandas 2.0+** (uso de `pd.concat` en lugar de `append`).  
- Ventanas con tamaño fijo y centrado automático.
