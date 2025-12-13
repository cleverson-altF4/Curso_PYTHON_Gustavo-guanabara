#leia o primeiro nome, e o último e mostre o sobrenome no final 
n = str(input("Digite o seu nome: ")).strip()
nome = n.split()
print(f"Prazer em te conhecer {n}")
print(f"Seu primeiro nome {nome[0]}")
print(f"Seu sobrenome é {nome[len(nome)-1]}") #é como se fosse nome[-1]