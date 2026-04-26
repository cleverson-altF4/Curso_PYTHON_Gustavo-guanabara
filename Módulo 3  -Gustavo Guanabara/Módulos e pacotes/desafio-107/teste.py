import moeda

preco = float(input("Digite um valor: "))
print(f"O dobro de {preco} é {moeda.dobro(preco)}")
print(f"A medade do {preco} é {moeda.metade(preco)}")
print(f"O aumento de 10% de {preco} é {moeda.aumentar(preco,10)}")
print(f"O preço diminuido de {preco} é {moeda.diminuir(preco,15):.2f}")