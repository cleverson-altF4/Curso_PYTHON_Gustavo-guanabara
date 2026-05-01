import moeda

numero = float(input("Digite um preço: "))
print(f"A metade de {moeda.dinheiro(numero)} é {moeda.dinheiro(moeda.metade(numero))}")