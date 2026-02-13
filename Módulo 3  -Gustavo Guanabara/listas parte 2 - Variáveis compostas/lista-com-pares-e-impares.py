#Crie um programa onde o usuário possa digitar 7 valores númericos e cadastre-as em uma lista única que mantenha separadas os valores pares e ímpares. No final mostre os valores pares e ímpares em ordem crescente

numero = [[], []]
valor = 0

for i in range(1,8):
    valor = int(input(f"Digite {i}º valor: "))
    
    if valor % 2 == 0:
        numero[0].append(valor)
    else:
        numero[1].append(valor)
        
numero[0].sort()
numero[1].sort()
        
print("-"*40)
print(f"Números pares: {numero[0]}")
print(f"Números ìmpares: {numero[1]}")