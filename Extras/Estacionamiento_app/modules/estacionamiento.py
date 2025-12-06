from modules.vehiculo import Vehiculo
import csv
from datetime import datetime
import os

class Estacionamiento:
    def __init__(self, capacidad=50):
        self.capacidad = capacidad
        self.vehiculos = {}

        self.log_path = os.path.join("\db", "log.csv")
        if not os.path.exists("data"):
            os.makedirs("data")
        if not os.path.exists(self.log_path):
            with open(self.log_path, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Patente", "Hora Ingreso", "Hora Salida", "Duración"])

    def ingresar_auto(self, patente):
        patente = patente.upper()
        if len(self.vehiculos) >= self.capacidad:
            return False, "Estacionamiento lleno"
        if patente in self.vehiculos:
            return False, "Este vehículo ya está ingresado"
        self.vehiculos[patente] = Vehiculo(patente)
        return True, "Vehículo ingresado"

    def retirar_auto(self, patente):
        patente = patente.upper()
        if patente not in self.vehiculos:
            return False, "Vehículo no encontrado"
        vehiculo = self.vehiculos.pop(patente)
        hora_salida = datetime.now()
        duracion = hora_salida - vehiculo.hora_ingreso
        self._registrar_log(vehiculo.patente, vehiculo.hora_ingreso, hora_salida, duracion)
        return True, f"Vehículo retirado. Tiempo estacionado: {duracion}"

    def ocupados(self):
        return len(self.vehiculos)

    def disponibles(self):
        return self.capacidad - len(self.vehiculos)

    def _registrar_log(self, patente, hora_ingreso, hora_salida, duracion):
        with open(self.log_path, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                patente,
                hora_ingreso.strftime("%Y-%m-%d %H:%M:%S"),
                hora_salida.strftime("%Y-%m-%d %H:%M:%S"),
                str(duracion).split('.')[0]
            ])