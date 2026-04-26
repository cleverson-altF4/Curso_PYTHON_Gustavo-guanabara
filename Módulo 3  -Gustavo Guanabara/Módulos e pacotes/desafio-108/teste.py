import moeda

valor = float(input("Digite um valor: "))
print(f"A metade de {moeda.dinheiro(valor)} é {moeda.dinheiro(moeda.metade(valor))}")
print(f"O dobro de {moeda.dinheiro(valor)} é {moeda.dinheiro(moeda.dobro(valor))}")