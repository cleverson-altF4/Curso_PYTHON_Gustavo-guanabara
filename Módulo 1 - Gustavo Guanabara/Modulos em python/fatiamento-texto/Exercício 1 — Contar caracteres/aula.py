#Exercício 1 — Contar caracteres

#Peça ao usuário que digite uma frase e mostre:

#Quantos caracteres tem a frase (com espaços);

#Quantos caracteres tem sem os espaços.

frase = str(input("Frase: "))
print(f"Com espaços {len(frase)}")
print("Sem espaços", len(frase.replace(' ', '')))
