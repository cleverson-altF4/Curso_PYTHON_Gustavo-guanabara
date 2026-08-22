from rich import print
from rich.panel import Panel

class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self):
        print(f"Olá, eu sou [red]{self.nome}[/] e sou {self.setor} na empresa {self.cargo}")


conta = Funcionario("Clevison", "Educador Físico", "Academia Novo Eu")
conta.apresentar()

conta2 = Funcionario("Luana", "Caixa", "Eletro Móveis")
conta2.apresentar()

