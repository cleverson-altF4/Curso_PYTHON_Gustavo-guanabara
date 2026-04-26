import moeda

preco = float(input("Digite um preço: "))
print(f"A medade de {preco} é R${moeda.metade(preco)}")
print(f"O dobro de {preco} é R${moeda.dobro(preco)}")
print(f"Aumentando 10%, R${preco} é {moeda.aumentar(preco,10)} ")