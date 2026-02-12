#Crie uma programa que leia uma matriz de dimensão 3x3 e preencha os valores lidos pelo teclado.No final mostre a matriz na tela com a formatação correta

matriz = []

for linha in range(3):
    linha_matriz = []
    
    for coluna in range(3):
        numero = int(input("Digite: "))
        linha_matriz.append(numero)
    matriz.append(linha_matriz)
    
for linha_matriz in matriz:
    print(linha_matriz)
print()

        
        