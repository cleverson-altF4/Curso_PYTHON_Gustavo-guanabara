#crie um programa que crie uma matriz de uma dimensão 3x3 e preencha com valores lidos pelo teclado, no final mostre a matriz na tela com a formatação correta

#aprimore o desafio anterior mostrando no final: 
#A soma de todos os valores pares digitados
#A soma dos valores da terceira coluna
#O maior valor da segunda linha
# 0 [ ] [ ] [ ]
# 1 [ ] [ ] [ ]
# 2 [ ] [ ] [ ]
#    0   1   2

matriz = []
soma_pares = 0
soma_colunas = 0

for linha in range(3):
    linha_matriz = []
    
    for coluna in range(3):
        numero = int(input(f"Digite: [{linha}] [{coluna}]: "))
        linha_matriz.append(numero)
        if numero % 2 == 0:
            soma_pares += numero
    matriz.append(linha_matriz)
    
print("\nMatriz 3x3")
for linha_matriz in matriz:
    print(linha_matriz)

print(f"A soma dos números pares digitados: {soma_pares}")
print(f"A soma dos valores da terceira coluna: ")

