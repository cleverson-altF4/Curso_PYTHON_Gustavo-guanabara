#Crie um programa que onde o usuário possa digitar 5 valores númericos e cadastre-os em uma lista.
#Já na posição correta de inserção(sem usar Sort())
#NO final mostre a lista ordenada na tela
lista = []

for contador in range(0, 5):
    numero = int(input("Digite um valor: "))
    
    if contador == 0 or numero > lista[len(lista)-1]:
        lista.append(numero)
        print("Adicionado no final da lista")
    else:
        posicao = 0
        while posicao < len(lista):
            if numero <= lista[posicao]:
                lista.insert(posicao, numero)
                print(f"Adicionado na posição {posicao}")
                break
            posicao += 1
            
        
print(lista)
    
   

   