class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor
            print(f"O valor sacado foi de R${valor:.2f}")


    def __str__(self):
        return f"O valor Total {self.saldo}"


conta1 = ContaBancaria("Clevison", 1500)
conta1.depositar(200)
conta1.sacar(10000)
print(conta1)