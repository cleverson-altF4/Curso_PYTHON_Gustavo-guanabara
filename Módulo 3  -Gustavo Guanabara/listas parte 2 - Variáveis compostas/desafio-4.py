#crie um programa que crie uma matriz de uma dimensão 3x3 e preencha com valores lidos pelo teclado, no final mostre a matriz na tela com a formatação correta

#aprimore o desafio anterior mostrando no final: 
#A soma de todos os valores pares digitados
#A soma dos valores da diagonal
#O maior valor digitado
# 0 [ ] [ ] [ ]
# 1 [ ] [ ] [ ]
# 2 [ ] [ ] [ ]
#    0   1   2

matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma_total = 0
numeros_pares = 0
maior = None
soma_diagonal = 0

for linha in range(3):
    for coluna in range(3):
        while True:
            valor = input(f"Digite [{linha}][{coluna}]")
        
            if valor == '':
                print("Não é permitido espaço vazio")
            elif not valor.isnumeric():
                print("Apenas números")
            else:
                numero = int(valor)
                matriz[linha][coluna] = numero
                soma_total += numero

                
                if numero % 2 == 0:
                    numeros_pares += 1
                    
                if linha == coluna:
                    soma_diagonal += numero
                    
                if maior is None or numero > maior:
                    maior = numero
                    
                break
                    
print("-"*30)
print()

for linha in matriz:
    print(linha)
    
print("-"*30)
print()

print(f"Soma total dos números digitados: {soma_total}")
print(f"A soma dos números pares: {numeros_pares}")
print(f"A soma dos números em diagonal: {soma_diagonal}")
print(f"O maior número digitado: {maior}")
    
                
                
        
        
            

    
