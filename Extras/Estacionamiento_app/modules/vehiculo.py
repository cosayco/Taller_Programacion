from datetime import datetime

class Vehiculo:
    def __init__(self, patente):
        self.patente = patente.upper()
        self.hora_ingreso = datetime.now()

    def tiempo_estacionado(self):
        return datetime.now() - self.hora_ingreso