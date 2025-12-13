#Exercício 4 — Pulando letras

#Mostre apenas uma em cada duas letras da frase.

nome = str(input("Digite: "))
print(f"Nome pulando de 2 em 2 {nome[::2]}")
print(f"Nome pulando de 3 em 3 {nome[::3]}")