import math

class Memoria:
    def __init__(self):
        self.valor = 0

    def limpiar(self):
        self.valor = 0

    def agregar(self, numero):
        self.valor += numero

    def restar(self, numero):
        self.valor -= numero

    def obtener(self):
        return self.valor

def calcular_expresion(expresion):
    try:
        return eval(expresion)
    except:
        return "Error"

def calcular_porcentaje(expresion):
    try:
        return eval(expresion) / 100
    except:
        return "Error"

def calcular_raiz(expresion):
    try:
        return math.sqrt(eval(expresion))
    except:
        return "Error"