class ContaBancaria:
    """
    Criando uma conta bancária simples usando classes
    """
    def __init__(self, id, titular = "", saldo=0):
        self.id = id
        self.titular = titular
        self.Saldo = saldo
        print(f"Conta {self.id} criada com sucesso! | Saldo da conta: R$: {self.Saldo:.2f}")

    def depositar(self, valor):
        self.Saldo += valor
        return f"Depósito de R$: {valor:.2f} reais concluído"

    def sacar(self, valor):
        if valor >= self.Saldo:
            print(f"Saque negado no ID: {self.id} no valor de R$: {valor:.2f} reais")
        else:
            self.Saldo -= valor
            print(f"Saque AUTORIZADO de R$: {valor:.2f} reais")


    def __str__(self):
        return f"Conta: {self.id} | Nome: {self.titular} | Saldo: {self.Saldo:.2f}"



conta1 = ContaBancaria(1, "Clevison", 3000)
conta1.sacar(4000)
print(conta1.__doc__)