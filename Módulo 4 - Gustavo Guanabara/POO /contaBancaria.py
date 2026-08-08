class contaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0


    def Depositar(self, valor):
        self.saldo = self.saldo + valor
        print(f"Você depositou R$ {valor} reais")


    def sacar(self, valor):
        if valor >= valor:
            self.saldo = self.saldo - valor
            print(f"O valor sacado foi de R$ {valor} reais")
        else:
            print("Saldo insuficiente")


    def MostrarSaldo(self):
        print(f"Titular: {self.titular}  | saldo: {self.saldo} reais")



conta = contaBancaria("Clevison")
conta.Depositar(250)
conta.sacar(50)
conta.Depositar(1500)
conta.MostrarSaldo()
conta2 = contaBancaria("Cleiton")
conta2.Depositar(150)
conta2.MostrarSaldo()
