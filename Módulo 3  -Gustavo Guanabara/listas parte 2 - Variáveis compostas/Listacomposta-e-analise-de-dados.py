#Faça um programa que leia nome e peso de várias pessoas guardando tudo em uma lista no final mostre:
#Quantas pessoas foram cadastradas
#Uma listagem com pessoas mais pesadas
#Uma listagem com pessoas mais leves.

temporario = []
principal = []
maior = menor = 0

while True:
    temporario.append(str(input("Digite o seu nome: "))) #[0]
    temporario.append(float(input("Digite o seu peso: "))) #[1]
    if len(principal) == 0:
        maior = menor = temporario[1]
    else:
        if temporario[1] > maior:
            maior = temporario[1]
            
        if temporario[1] < menor:
            menor = temporario[1]
            
    principal.append(temporario[:])
    temporario.clear()
    
    
    continuar = ''
    while continuar not in ('S', 'N'):
        continuar = str(input("Deseja continuar? [sim/Não]: ")).strip().upper()
        if continuar == '':
            print("Espaço está em branco")
        else:
            continuar = continuar[0]
    if continuar == 'N':
        break
    
print("-"*40)
print(f"Ao total você cadastrou {len(principal)} pessoas.")
print(f"O maior peso foi de {maior} kg. Peso de ", end='')

        
for listagem in principal:
    if listagem[1] == maior:
        print(f"{listagem[0]}", end=' ')
print()

print(f"O menor peso foi de {menor} kg. peso de ", end='')

for listagem in principal:
    if listagem[1] == menor:
        print(f"{listagem[0]}", end=' ')
print()
        


