class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            print("Saque realizado com sucesso!")

        if self.saldo <= valor:
            print("Saldo insuficiente")


conta1 = ContaBancaria("Cleviso", 1500)
conta1.depositar(200)
conta1.sacar(1000)
print()