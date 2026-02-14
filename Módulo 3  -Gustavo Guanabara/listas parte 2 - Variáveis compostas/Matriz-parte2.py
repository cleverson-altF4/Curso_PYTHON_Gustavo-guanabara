#Crie uma programa que leia uma matriz de dimensão 3x3 e preencha os valores lidos pelo teclado.No final mostre a matriz na tela com a formatação correta

#Aprimote os desafio anterior mostrando no final.
#A soma de todos os valores pares digitados
#A soma dos valores da terceira coluna
#O maior valor da segunda linha

matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma_pares = soma_coluna = maior = 0

for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f"Digite: [{linha}][{coluna}]: "))
        
print("-"*30)
print('-'*9,"Matriz 3x3", '-'*9)
print()
print("-"*30)

for linha in range(3):
    for coluna in range(3):
        print(f"[{matriz[linha][coluna]}]", end=' ')
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
    print()
    
print("-"*30)
print('-'*9,"Resultado", '-'*9)
print()     
print(f"Números pares da matriz: {soma_pares}")

for linha in range(3):
   soma_coluna += matriz[linha][2]
   
print(f"A soma dos valores da 3º coluna: {soma_coluna}")

for coluna in range(3):
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
        
print(f"O maior número da 2º coluna: {maior}")
        

print("-"*30)