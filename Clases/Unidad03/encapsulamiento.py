class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.__saldo = saldo_inicial  # atributo privado

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto

    def retirar(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
        else:
            print("Fondos insuficientes")

    def mostrar_saldo(self):
        print(f"Saldo actual: ${self.__saldo:.2f}")

#Uso
cuenta = CuentaBancaria("Carlos", 1000)
cuenta.depositar(500)
cuenta.retirar(300)
cuenta.mostrar_saldo()  # Saldo actual: $1200.00

# Intento de acceso directo (no recomendado)
print(cuenta.__saldo)  # Error: atributo privado
