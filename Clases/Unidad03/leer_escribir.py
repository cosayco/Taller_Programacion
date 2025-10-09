#Escritura de archivo
def guardar_muestras(muestras, archivo):
    try:
        with open(archivo, 'w') as f:
            for nombre, masa, volumen in muestras:
                f.write(f"{nombre},{masa},{volumen}\n")
        print("Archivo guardado correctamente.")
    except Exception as e:
        print("Error al guardar:", e)

muestras = [("Cobre", 270, 100), ("Plata", 315, 90)]
guardar_muestras(muestras, "muestras.txt")

#Lectura de archivo
def leer_muestras(archivo):
    muestras = []
    try:
        with open(archivo, 'r') as f:
            for linea in f:
                partes = linea.strip().split(',')
                if len(partes) == 3:
                    nombre = partes[0]
                    masa = float(partes[1])
                    volumen = float(partes[2])
                    muestras.append((nombre, masa, volumen))
        print("Archivo leído correctamente.")
    except FileNotFoundError:
        print("Archivo no encontrado.")
    except ValueError:
        print("Error en el formato de los datos.")
    except Exception as e:
        print("Error inesperado:", e)
    return muestras

datos = leer_muestras("muestras.txt")
for nombre, masa, volumen in datos:
    print(f"{nombre} → Masa: {masa} kg, Volumen: {volumen} m³")
