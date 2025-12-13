#Exercício 3 — Fatiamento simples

#Peça uma palavra e mostre:

#As 3 primeiras letras

#As 3 últimas letras

#As letras do meio (se houver)

nome = str(input("Nome: "))
print(f"As 3 primeiras letras {nome[:3]}")
print(f"As 3 últimas letras {nome[5:]}")
print(f"As letras do meio {nome[4:-3]}")