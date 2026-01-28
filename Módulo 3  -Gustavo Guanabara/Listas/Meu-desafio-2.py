#Crie um programa que onde o usuário possa digitar 5 valores númericos e cadastre-os em uma lista.
#Já na posição correta de inserção(sem usar Sort())
#NO final mostre a lista ordenada na tela
lista = []

for i in range(1, 6):
    numero = int(input("Digite um valor: "))
    
    if len(lista) == 0:
        lista.append(numero)
    else:
        inserido = False

        for posicao in range(len(lista)):
            if numero <= lista[posicao]:
                lista.insert(posicao, numero)
                inserido = True
                break

        if not inserido:
            lista.append(numero)

print(lista)

                
            

   