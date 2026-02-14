# Tamanho da matriz
while True:
    tamanho_input = input("Digite o tamanho da matriz (ex: 3 para 3x3): ")
    
    if tamanho_input.isnumeric() and int(tamanho_input) > 0:
        tamanho = int(tamanho_input)
        break
    else:
        print("Digite um número inteiro positivo.")

# Criando matriz vazia
matriz = [[0 for _ in range(tamanho)] for _ in range(tamanho)]

soma_total = 0
soma_terceira_coluna = 0
maior_segunda_linha = None
numeros_impares = 0

# Preenchimento
for linha in range(tamanho):
    for coluna in range(tamanho):
        while True:
            valor = input(f"Digite [{linha}][{coluna}]: ")
            
            if valor == '':
                print("Não é permitido espaço vazio")
            elif not valor.lstrip('-').isnumeric():
                print("É permitido apenas números inteiros")
            else:
                numero = int(valor)
                matriz[linha][coluna] = numero
                soma_total += numero
                
                # Ímpares
                if numero % 2 != 0:
                    numeros_impares += 1
                
                # Terceira coluna (índice 2)
                if coluna == 2:
                    soma_terceira_coluna += numero
                
                # Segunda linha (índice 1)
                if linha == 1:
                    if maior_segunda_linha is None or numero > maior_segunda_linha:
                        maior_segunda_linha = numero
                
                break

print("-" * 40)

# Mostrar matriz formatada
for linha in matriz:
    print("[", end="")
    for numero in linha:
        print(f"{numero:^5}", end="")
    print("]")

print("-" * 40)

print(f"Soma total: {soma_total}")

if tamanho > 2:
    print(f"Soma da terceira coluna: {soma_terceira_coluna}")
else:
    print("Não existe terceira coluna.")

if tamanho > 1:
    print(f"Maior valor da segunda linha: {maior_segunda_linha}")
else:
    print("Não existe segunda linha.")

print(f"Quantidade de números ímpares: {numeros_impares}")
