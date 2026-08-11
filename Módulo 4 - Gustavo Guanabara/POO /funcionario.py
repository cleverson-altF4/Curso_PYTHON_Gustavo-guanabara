
class Funcionario:
    empresa = "Academia Novo Eu"

    def __init__(self, nome, salario_base, bonus=0.10):
        self.nome = nome
        self.salario_base = salario_base
        self.bonus = bonus


    def salario_liquido(self):
        return self.salario_base + (self.salario_base * self.bonus)




Fulano = Funcionario("Clevison", 1000)
print(F"Nome: {Fulano.nome} recebe por mês {Fulano.salario_liquido()} na empresa {Fulano.empresa}")