#Objetivo: Criar uma nova lista com os elementos da lista original em ordem inversa, sem usar o método reverse() ou a sintaxe de slicing [::-1].

#Passo a passo:

#Crie uma lista de exemplo (ex: [1, 2, 3, 4, 5]).

#Inicialize uma lista vazia para armazenar o resultado.

#Use um laço for para percorrer a lista original de trás para frente (dica: use range() com índices decrescentes).

#A cada iteração, adicione o elemento atual à nova lista.

#Ao final, a nova lista deve ser [5, 4, 3, 2, 1].

lista = []

for i in range(5):
    numero = int(input("Digite um número: "))
    lista.append(numero)
    
invertida = []

for i in range(len(lista)-3,-1,-1):
    invertida.append(lista[i])
    
print(f"Lista normal = {lista}")
print(f"Lista invertida = {invertida}")