#Faça um programa que leia 5 valores numericos e guarde-as em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista  

lista = []
maior = 0
menor = 0

for contador in range(0,5): # Esse for ele busca a quantidade de número
    lista.append(int(input("Digite um número: ")))
    if contador == 0: #Conta de 1 à 5 números
        maior = menor = lista[contador]
    else:
        if lista[contador] > maior: #a lista que digito e o contador mostra qual posição ficaria > maior
            maior = lista[contador]
            
        if lista[contador] < menor: #a lista que digito e o contador mostra qual posição ficaria < menor
            menor = lista[contador]
    
print("*"*30)
print(f"Os números são = {lista}")
print(f"O maior número digitado foi {maior} no índice", end= ' ')
for indice, valor in enumerate(lista): #índice indica a posição e o valor refere-se os números da lista 
    if valor == maior:
        print(f"{indice}... ", end= '')
print()

print(f"O menor número digitado foi {menor} no índice", end= ' ')
for indice, valor in enumerate(lista):
    if valor == menor:
        print(f"{indice}... ", end= '')
print()
