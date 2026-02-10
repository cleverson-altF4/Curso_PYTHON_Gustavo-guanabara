#Crie um programa onde o usuário possa digitar 7 valores númericos e cadastre-as em uma lista única que mantenha separadas os valores pares e ímpares. No final mostre os valores pares e ímpares em ordem crescente


lista_pares = []
lista_impares = []

for posicao in range(1,8):
    numero = int(input(f"{posicao} - Digite um valor: "))
    
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)
        
        
lista_pares.sort()
lista_impares.sort()

print(f"Números pares ordenados: {lista_pares}")
print(f"Números ímpares ordenados: {lista_impares}")
    

