tamanho = int(input("Digite uma Matriz 3x3: "))

matriz = []

for i in range(tamanho):
    linha = []
    for j in range(tamanho):
        linha.append(0)
    matriz.append(linha)
    
soma_total = 0
numeros_impares = 0
soma_terceira_linha = 0
maior_segunda_linha = 0

for linha in range(tamanho):
    for coluna in range(tamanho):
        numero = int(input(f"Digite [{linha}][{coluna}]: "))
        matriz[linha][coluna] = numero
        soma_total += numero
        
        if numero % 2 == 1:
            numeros_impares += 1
            
        if linha == 2:
            soma_terceira_linha += numero
            
        if coluna == 1:
            if linha == 0:
                maior_segunda_linha += numero
            else:
                if numero > maior_segunda_linha:
                    maior_segunda_linha = numero
                    
print("-"*30)
for linha in range(tamanho):
    for coluna in range(tamanho):
        print(matriz[linha][coluna], end=' ')
    print()
    
print("-"*30)
print(f"A soma total = {soma_total}")

if tamanho > 2:
    print(f"A soma da terceira linha: {soma_terceira_linha}")
else:
    print("Não existe")

if tamanho > 1:
    print(f"O maior valor da segunda linha: {maior_segunda_linha}")
else:
    print("Não existe")

if numeros_impares == 0:
    print("Não há números ímpares")
else:
    print(f"Números ímpares = {numeros_impares}")
