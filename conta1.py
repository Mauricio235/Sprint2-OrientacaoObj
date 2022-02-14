

class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo o objeto ...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

     def  transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular


    @property
    def limite(self):
        return self.__limite
    @limite.setter
    def limite(self):
        self.__limite = limite


conta = Conta(123, "Nico", 55.5, 1000)


print(conta)

