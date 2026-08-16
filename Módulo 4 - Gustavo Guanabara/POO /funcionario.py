
class Funcionario:
    empresa = "Academia Novo Eu"

    def __init__(self, nome, salario_base, bonus=0.10):
        self.nome = nome
        self.salario_base = salario_base
        self.bonus = bonus


    def salario_liquido(self):
        return self.salario_base + (self.salario_base * self.bonus)

    def salario_desconto(self):
        return self.salario_base - (self.salario_base * self.bonus)



Fulano = Funcionario("Clevison", 1000)
Fulano2 = Funcionario("Luana", 2000)
print(F"Nome: {Fulano.nome} recebe por mês {Fulano.salario_liquido()} na empresa {Fulano.empresa}")
print(F"Nome: {Fulano2.nome} recebe por mês {Fulano2.salario_base} na empresa {Fulano2.empresa} e terá um desconto de {Fulano.salario_desconto():.2f}")