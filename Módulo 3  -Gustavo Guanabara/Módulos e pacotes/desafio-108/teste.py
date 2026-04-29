import moeda

valor = float(input("Digite um valor: "))

valor_metade = moeda.metade(valor)
valor_dobro = moeda.dobro(valor)
valor_aumentado = moeda.aumentar(valor)
valor_diminuido = moeda.diminuir(valor)


print(f"Metade: {valor_metade}")
print(f"Dobro: {valor_dobro}")
print(f"Valor aumentado: {valor_aumentado}")
print(f"Valor diminuido: {valor_diminuido}")

